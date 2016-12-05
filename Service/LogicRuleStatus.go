package main

import (
	"errors"
	"fmt"
	"log"
)

func DBRuleStatSelfGet() (proc_stat, file_stat, net_stat int, err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBRuleStatSelfGet: %s\n", err)
		return proc_stat, file_stat, net_stat, err
	}

	sqlstr := fmt.Sprintf("SELECT proc, file, net FROM status_self WHERE id = 1")

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBRuleStatSelfGet(): %s, %s", err, sqlstr)
		return proc_stat, file_stat, net_stat, errors.New("错误:超级进程失败")
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&proc_stat, &file_stat, &net_stat)
		break
	}
	rows.Close()

	//log.Println("DBRuleStatSelfGet:", proc_stat, file_stat, net_stat)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBRuleStatSelfGet:tx.Commit: %s\n", err)
		tx.Rollback()
		return proc_stat, file_stat, net_stat, err
	}
	return proc_stat, file_stat, net_stat, nil
}

func DBRuleStatSafeGet() (proc_stat, file_stat, net_stat int, err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBRuleStatSafeGet: %s\n", err)
		return proc_stat, file_stat, net_stat, err
	}

	sqlstr := fmt.Sprintf("SELECT proc, file, net FROM status_safe WHERE id = 1")

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBRuleStatSafeGet(): %s, %s", err, sqlstr)
		return proc_stat, file_stat, net_stat, errors.New("错误:超级进程失败")
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&proc_stat, &file_stat, &net_stat)
		break
	}
	rows.Close()

	//log.Println("DBRuleStatSafeGet:", proc_stat, file_stat, net_stat)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBRuleStatSafeGet:tx.Commit: %s\n", err)
		tx.Rollback()
		return proc_stat, file_stat, net_stat, err
	}
	return proc_stat, file_stat, net_stat, nil
}

func DBRuleStatUserGet() (proc_stat, file_stat, net_stat int, err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBRuleStatUserGet: %s\n", err)
		return proc_stat, file_stat, net_stat, err
	}

	sqlstr := fmt.Sprintf("SELECT proc, file, net FROM status_user WHERE id = 1")

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBRuleStatUserGet(): %s, %s", err, sqlstr)
		return proc_stat, file_stat, net_stat, errors.New("错误:超级进程失败")
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&proc_stat, &file_stat, &net_stat)
		break
	}
	rows.Close()

	//log.Println("DBRuleStatUserGet:", proc_stat, file_stat, net_stat)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBRuleStatUserGet:tx.Commit: %s\n", err)
		tx.Rollback()
		return proc_stat, file_stat, net_stat, err
	}
	return proc_stat, file_stat, net_stat, nil
}

func DBRuleStatSelfSet(proc_stat, file_stat, net_stat int) (err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBRuleStatSelfSet: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("UPDATE status_self SET proc=%d, file=%d, net=%d WHERE id=1;", proc_stat, file_stat, net_stat)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBRuleStatSelfSet:tx.Exec(): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBRuleStatSelfSet:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	//log.Println("DBRuleStatSelfSet:", proc_stat, file_stat, net_stat)

	// 更新内存
	LockGMemRuleSelfHandle.Lock()
	GMemRuleSelfHandle.StatusProc = proc_stat
	GMemRuleSelfHandle.StatusFile = file_stat
	GMemRuleSelfHandle.StatusNet = net_stat
	LockGMemRuleSelfHandle.Unlock()

	return nil
}

func DBRuleStatSafeSet(proc_stat, file_stat, net_stat int) (err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBRuleStatSafeSet: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("UPDATE status_safe SET proc=%d, file=%d, net=%d WHERE id=1;", proc_stat, file_stat, net_stat)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBRuleStatSafeSet:tx.Exec(): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBRuleStatSafeSet:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	//log.Println("DBRuleStatSafeSet:", proc_stat, file_stat, net_stat)

	// 更新内存
	LockGMemRuleSafeHandle.Lock()
	GMemRuleSafeHandle.StatusProc = proc_stat
	GMemRuleSafeHandle.StatusFile = file_stat
	GMemRuleSafeHandle.StatusNet = net_stat
	LockGMemRuleSafeHandle.Unlock()
	return nil
}

func DBRuleStatUserSet(proc_stat, file_stat, net_stat int) (err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBRuleStatUserSet: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("UPDATE status_user SET proc=%d, file=%d, net=%d WHERE id=1;", proc_stat, file_stat, net_stat)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBRuleStatUserSet:tx.Exec(): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBRuleStatUserSet:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	//log.Println("DBRuleStatUserSet:", proc_stat, file_stat, net_stat)
	// 更新内存
	LockGMemRuleUserHandle.Lock()
	GMemRuleUserHandle.StatusProc = proc_stat
	GMemRuleUserHandle.StatusFile = file_stat
	GMemRuleUserHandle.StatusNet = net_stat
	LockGMemRuleUserHandle.Unlock()
	return nil
}
