package main

import (
	"fmt"
	"log"
	"strings"
	"sync"
	"time"
)

var (
	rwLockLog      sync.Mutex                       // 记录系统操作锁
	logWaitGroup   sync.WaitGroup                   // 线程等待组
	logCacheInsert []string                         // 拦截的日志放入这里
	logCacheWrite  []string                         // 写入数据库的实际缓存
	logWriteSpace  time.Duration  = time.Second * 1 // 日志写入间隔
	logStatus      int            = 0               // 线程退出标志
)

// 检测时间格式
func IsTimeRangeRight(timeStart string, timeEnd string) bool {
	var unix_stime int64
	var unix_etime int64

	if strings.EqualFold(timeStart, "") != true {
		s_time, err := time.Parse("2006-01-02 15:04:05", timeStart)
		if err == nil {
			unix_stime = s_time.Unix()
		} else {
			return false
		}
	} else {
		unix_stime = 0
	}
	if strings.EqualFold(timeEnd, "") != true {
		e_time, err1 := time.Parse("2006-01-02 15:04:05", timeEnd)
		if err1 == nil {
			unix_etime = e_time.Unix()
		} else {
			return false
		}
	} else {
		unix_etime = time.Now().Unix()
	}
	if unix_stime > unix_etime {
		return false
	} else {
		return true
	}
}

func LogDBInit() (err error) {
	db, err := ConnectSqlite(DBFileLog)
	if err != nil {
		return err
	}

	GHandleDBLog = db
	logStatus = 0
	logWaitGroup.Add(1)
	go LogWriteCacheToDb()
	return nil
}

func LogFini() {
	rwLockLog.Lock()
	logStatus = 1 // 通知日志写入线程退出
	rwLockLog.Unlock()
	logWaitGroup.Wait()
	CloseSqlite(GHandleDBLog)
}

// 插入系统日志
func LogInsertSys(login_name, op, result, info string) {
	sql := "insert into log_sys (id, login_name, op, result, info, logtime) values " +
		fmt.Sprintf("(null, '%s', '%s', '%s', '%s', datetime())", login_name, op, result, info)

	rwLockLog.Lock()
	logCacheInsert = append(logCacheInsert, sql)
	rwLockLog.Unlock()
}

// 插入拦截事件日志
func LogInsertEvent(module, status, etype, eop, uname, proc, obj, result string) {
	sql := "insert into log_event (id, module, status, etype, eop, uname, proc, obj, result, logtime) values " +
		fmt.Sprintf("(null, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', datetime())",
			module, status, etype, eop, uname, proc, obj, result)

	rwLockLog.Lock()
	logCacheInsert = append(logCacheInsert, sql)
	rwLockLog.Unlock()
}

func LogWriteCacheToDbExe() (err error) {
	db := GHandleDBLog
	tx, err := db.Begin()
	if err != nil {
		GHandleFileRunLog.Println("LogWriteCacheToDbExe:DB.Begin(): %s\n", err)
		return err
	}

	for _, sql := range logCacheWrite {
		//fmt.Println(sql)
		_, err = tx.Exec(sql)
		if err != nil {
			GHandleFileRunLog.Println("LogWriteCacheToDbExe(user): %s, %s\n", err, sql)
			tx.Rollback()
			return err
		}
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		GHandleFileRunLog.Println("LogWriteCacheToDbExe(commit transaction): %s\n", err)
		tx.Rollback()
		return err
	}

	return nil
}

// 线程 - 将缓存中的日志写入数据库文件
func LogWriteCacheToDb() {
	for {
		if logStatus == 1 {
			rwLockLog.Lock()
			logCacheWrite = logCacheInsert
			logCacheInsert = logCacheInsert[0:0]
			rwLockLog.Unlock()
			LogWriteCacheToDbExe()
			break
		}
		rwLockLog.Lock()
		logCacheWrite = logCacheInsert
		logCacheInsert = logCacheInsert[0:0]
		rwLockLog.Unlock()
		LogWriteCacheToDbExe()

		time.Sleep(logWriteSpace)
	}
	logWaitGroup.Done()
	GHandleFileRunLog.Println("Write Process exit")
}

// 日志 - 获取指定模块的时间段内数量
func getLogEventCount(start_time, stop_time, module string) (count int, err error) {
	db := GHandleDBLog

	tx, err := db.Begin()
	if err != nil {
		log.Printf("getLogEventCount: %s\n", err)
		return count, err
	}

	// 统计日志
	sqlstr := "SELECT COUNT(*) as md_count FROM log_event WHERE " +
		"logtime >= '" + start_time + "' and " +
		"logtime <= '" + stop_time + "' and " +
		"module = '" + module + "'"

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("getLogEventCount(): %s, %s", err, sqlstr)
		return count, err
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&count)
		break
	}
	rows.Close()

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("getLogEventCount:tx.Commit: %s\n", err)
		tx.Rollback()
		return count, err
	}
	return count, nil
}

// 日志统计 - 更新
func updateLogEventCount(cnt_self, cnt_safe, cnt_user, cnt_spec int, date string) (err error) {
	db := GHandleDBLog

	tx, err := db.Begin()
	if err != nil {
		log.Printf("updateLogEventCount: %s\n", err)
		return err
	}

	// 统计日志
	sqlstr := "SELECT COUNT(*) as md_count FROM log_event_count " +
		fmt.Sprintf("WHERE logdate = '%s';", date)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("updateLogEventCount(): %s, %s", err, sqlstr)
		return err
	}
	defer rows.Close()

	var count int = 0
	for rows.Next() {
		rows.Scan(&count)
		break
	}
	rows.Close()

	sqlstr = "INSERT INTO log_event_count (logdate, modself, modsafe, modspecial, moduser) VALUES " +
		fmt.Sprintf("('%s', %d, %d, %d, %d);", date, cnt_self, cnt_safe, cnt_spec, cnt_user)

	if count > 0 {
		sqlstr = "UPDATE log_event_count set " +
			fmt.Sprintf("modself = %d, modsafe = %d, modspecial = %d, moduser = %d ", cnt_self, cnt_safe, cnt_spec, cnt_user) +
			fmt.Sprintf("WHERE logdate = '%s';", date)
	}

	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("updateLogEventCount:tx.Exec(): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("updateLogEventCount:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

// 日志统计
func LogEventCountService() {
	var start_time, stop_time string
	var time_now time.Time
	GHandleFileRunLog.Println("LogEventCountService start")
	for {
		time.Sleep(60 * time.Second)
		time_now = time.Now()

		start_time = time_now.Format("2006-01-02") + " 00:00:00"
		stop_time = time_now.Format("2006-01-02") + " 23:59:59"

		cnt_self, _ := getLogEventCount(start_time, stop_time, "自我保护")
		cnt_safe, _ := getLogEventCount(start_time, stop_time, "基础安全")
		cnt_user, _ := getLogEventCount(start_time, stop_time, "用户策略")
		cnt_spec, _ := getLogEventCount(start_time, stop_time, "特殊资源")

		//fmt.Println("LogEventCountService:", cnt_self, cnt_safe, cnt_user, cnt_spec, time_now.Format("2006-01-02"))
		updateLogEventCount(cnt_self, cnt_safe, cnt_user, cnt_spec, time_now.Format("2006-01-02"))

	}
	GHandleFileRunLog.Println("LogEventCountService exit")
}
