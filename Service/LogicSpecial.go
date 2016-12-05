package main

import (
	"errors"
	"fmt"
	"log"
)

func DBSpecialConfigGet() (mode, settime, shutdown, usb, cdrom int, err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBSpecialConfigGet: %s\n", err)
		return mode, settime, shutdown, usb, cdrom, err
	}

	sqlstr := fmt.Sprintf("SELECT mode, settime, shutdown, usb, cdrom FROM special WHERE id = %d", 1)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBSpecialConfigGet(): %s, %s", err, sqlstr)
		return mode, settime, shutdown, usb, cdrom, errors.New("错误:查询特殊资源配置失败")
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&mode, &settime, &shutdown, &usb, &cdrom)
		break
	}
	rows.Close()

	//log.Println("DB_GET:", mode, settime, shutdown, usb, cdrom)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBSpecialConfigGet:tx.Commit: %s\n", err)
		tx.Rollback()
		return mode, settime, shutdown, usb, cdrom, err
	}
	return mode, settime, shutdown, usb, cdrom, nil
}

func DBSpecialConfigSet(mode, settime, shutdown, usb, cdrom int) (err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBSpecialConfigSet: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("UPDATE special set mode = %d, settime = %d, shutdown = %d, usb = %d, cdrom = %d WHERE id = 1", mode, settime, shutdown, usb, cdrom)

	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBSpecialConfigSet:tx.Exec(): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBSpecialConfigSet:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}

	//log.Println("DB_SET:", mode, settime, shutdown, usb, cdrom)
	// 更新内存
	LockGMemRuleSpecialHandle.Lock()
	GMemRuleSpecialHandle.StatusMode = mode
	GMemRuleSpecialHandle.StatusSetTime = settime
	GMemRuleSpecialHandle.StatusShutDown = shutdown
	GMemRuleSpecialHandle.StatusUsb = usb
	GMemRuleSpecialHandle.StatusCdrom = cdrom
	LockGMemRuleSpecialHandle.Unlock()

	return nil
}
