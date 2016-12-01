package main

import (
	"errors"
	"fmt"
	"log"
)

func DBSuperProcGet() (procs []string, err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBSuperProcGet: %s\n", err)
		return procs, err
	}

	sqlstr := fmt.Sprintf("SELECT procname FROM super_process")

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBSuperProcGet(): %s, %s", err, sqlstr)
		return procs, errors.New("错误:超级进程失败")
	}
	defer rows.Close()

	for rows.Next() {
		var proc string
		rows.Scan(&proc)
		procs = append(procs, proc)
	}
	rows.Close()

	//log.Println("DBSuperProcGet:", procs)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBSuperProcGet:tx.Commit: %s\n", err)
		tx.Rollback()
		return procs, err
	}
	return procs, nil
}

func DBSuperProcSet(proc string) (err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBSuperProcSet: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("insert into super_process (id, procname) values (null, '%s');", proc)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBSuperProcSet:tx.Exec(): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBSuperProcSet:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	//log.Println("DBSuperProcSet:", proc)
	return nil
}
