package main

import (
	"errors"
	"fmt"
	"log"
)

func DBSafeConfigGet() (mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb int, err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBSafeConfigGet: %s\n", err)
		return mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb, err
	}

	sqlstr := fmt.Sprintf("SELECT mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb FROM safe WHERE id = %d", 1)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBSafeConfigGet(): %s, %s", err, sqlstr)
		return mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb, errors.New("错误:查询特殊资源配置失败")
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&mode, &fileetc, &filelib, &filebin, &fileboot, &netftp, &nettelnet, &netmail, &netweb)
		break
	}
	rows.Close()

	//log.Println("DB_GET:", mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBSafeConfigGet:tx.Commit: %s\n", err)
		tx.Rollback()
		return mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb, err
	}
	return mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb, nil
}

func DBSafeConfigSet(mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb int) (err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBSafeConfigSet: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("UPDATE safe set mode = %d, fileetc = %d, filelib = %d, filebin = %d, fileboot = %d, netftp = %d, nettelnet = %d, netmail = %d, netweb = %d WHERE id = 1", mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb)

	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBSafeConfigSet:tx.Exec(): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBSafeConfigSet:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	//log.Println("DB_SET:", mode, settime, shutdown, usb, cdrom)

	// 更新内存
	LockGMemRuleSafeHandle.Lock()
	GMemRuleSafeHandle.StatusFile = mode
	GMemRuleSafeHandle.StatusNet = mode
	GMemRuleSafeHandle.StatusProc = mode
	// 根据每项的结果，添加不同的策略
	LockGMemRuleSafeHandle.Unlock()
	return nil
}
