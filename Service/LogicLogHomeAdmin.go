package main

import "time"

type LogCountHomeAdmin struct {
	CntSelf int
	CntSafe int
	CntSpec int
	CntUser int
}

func LogicLogCountHomeAdmin() (r LogCountHomeAdmin, err error) {
	time_start := time.Now()
	time_stop := time_start.AddDate(0, 0, -6)

	start_time := time_start.Format("2006-01-02") + " 00:00:00"
	stop_time := time_stop.Format("2006-01-02") + " 23:59:59"

	r.CntSelf, err = getLogEventCount(start_time, stop_time, "自我保护")
	if err != nil {
		return r, err
	}
	r.CntSafe, err = getLogEventCount(start_time, stop_time, "基础安全")
	if err != nil {
		return r, err
	}
	r.CntUser, err = getLogEventCount(start_time, stop_time, "用户策略")
	if err != nil {
		return r, err
	}
	r.CntSpec, err = getLogEventCount(start_time, stop_time, "特殊资源")
	if err != nil {
		return r, err
	}
	/*
		db := GHandleDBLog
		time_start := time.Now().Format("2006-01-02")

		tx, err := db.Begin()
		if err != nil {
			log.Printf("LogCountHomeAdmin: %s\n", err)
			return r, err
		}

		// 统计日志
		sqlstr := "SELECT SUM(modself) as cntself, " +
			"SUM(modsafe) as cntsafe, " +
			"SUM(modspecial) as cntspec, " +
			"SUM(moduser) as cntuser " +
			"FROM log_event_count WHERE " +
			fmt.Sprintf("logdate >= '%s' ;", time_start)

		rows, err := db.Query(sqlstr)
		if err != nil {
			log.Printf("LogCountHomeAdmin(): %s, %s", err, sqlstr)
			return r, err
		}
		defer rows.Close()

		for rows.Next() {
			rows.Scan(&r.CntSelf, &r.CntSafe, &r.CntSpec, &r.CntUser)
			break
		}
		rows.Close()

		// 事务提交
		err = tx.Commit()
		if err != nil {
			log.Printf("LogCountHomeAdmin:tx.Commit: %s\n", err)
			tx.Rollback()
			return r, err
		}
	*/
	return r, nil
}
