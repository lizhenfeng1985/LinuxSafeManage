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

func DBSuperProcDel(proc string) (err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBSuperProcDel: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("delete from super_process where procname = '%s';", proc)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBSuperProcDel:tx.Exec(): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBSuperProcDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	//log.Println("DBSuperProcDel:", proc)
	return nil
}

func DBSuperProcSearch(start, length int) (procs []string, total int, err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBSuperProcSearch: %s\n", err)
		return procs, total, err
	}

	// 查找数量
	sqlstr := "SELECT COUNT(procname) FROM super_process;"

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBSuperProcSearch(): %s, %s", err, sqlstr)
		return procs, total, err
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&total)
		break
	}
	rows.Close()

	if total == 0 {
		return procs, total, nil
	}

	// 查找用户
	sqlstr = fmt.Sprintf("SELECT procname FROM super_process ORDER BY procname ASC LIMIT %d, %d;", start, length)

	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBSuperProcSearch(): %s, %s", err, sqlstr)
		return procs, total, err
	}
	defer rows.Close()

	var proc string
	for rows.Next() {
		rows.Scan(&proc)
		procs = append(procs, proc)
	}
	rows.Close()

	//log.Println("DBSuperProcSearch:", start, length, procs)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBSuperProcSearch:tx.Commit: %s\n", err)
		tx.Rollback()
		return procs, total, err
	}
	return procs, total, nil
}
