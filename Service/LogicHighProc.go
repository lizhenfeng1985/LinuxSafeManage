package main

import (
	"errors"
	"fmt"
	"log"
)

func DBHighProcGroupAdd(group string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighProcGroupAdd: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("INSERT INTO proc_group (id, groupname, gtype) VALUES (null, '%s', 0);", group)

	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighProcGroupAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighProcGroupAdd:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighProcGroupAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighProcGroupDel(group string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighProcGroupAdd: %s\n", err)
		return err
	}

	// 查找组和类型
	sqlstr := fmt.Sprintf("SELECT gtype FROM proc_group WHERE groupname = '%s';", group)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighProcGroupSearch(): %s, %s", err, sqlstr)
		return errors.New("错误:查询程序组失败")
	}
	defer rows.Close()

	var gtype int = 0
	for rows.Next() {
		rows.Scan(&gtype)
	}
	rows.Close()
	if gtype == 1 {
		return errors.New("错误:默认组不允许删除")
	}

	// 查找组的程序数 如果大于0 不允许删除
	sqlstr = fmt.Sprintf("SELECT count(*) FROM proc u JOIN proc_group g ON u.gid = g.id WHERE g.groupname = '%s';", group)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighProcGroupSearch(): %s, %s", err, sqlstr)
		return errors.New("错误:查询程序组失败")
	}
	defer rows.Close()

	var cnt int = 0
	for rows.Next() {
		rows.Scan(&cnt)
	}
	rows.Close()
	if cnt > 0 {
		return errors.New("错误:请先删除当前组中的程序")
	}

	sqlstr = fmt.Sprintf("DELETE FROM proc_group WHERE groupname = '%s' and gtype != 1;", group)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighProcGroupDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighProcGroupDel:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighProcGroupDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighProcGroupSearch() (groups []string, err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighProcGroupSearch: %s\n", err)
		return groups, err
	}

	sqlstr := fmt.Sprintf("SELECT groupname FROM proc_group ORDER BY id;")

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighProcGroupSearch(): %s, %s", err, sqlstr)
		return groups, errors.New("错误:查询程序组失败")
	}
	defer rows.Close()

	for rows.Next() {
		var group string
		rows.Scan(&group)
		groups = append(groups, group)
	}
	rows.Close()

	//log.Println("DBHighProcGroupSearch:", groups)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighProcGroupDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return groups, err
	}
	return groups, nil
}

// 获取程序列表
func DBHighProcList() (procs []string, err error) {
	for i := 1; i <= 40; i++ {
		procs = append(procs, fmt.Sprintf("/proc/%d.exe", i))
	}
	return procs, err
}

// 添加程序
func DBHighProcAdd(group, proc string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighProcAdd: %s\n", err)
		return err
	}

	// 查找gid
	sqlstr := fmt.Sprintf("SELECT id FROM proc_group WHERE groupname = '%s';", group)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighProcAdd(): %s, %s", err, sqlstr)
		return err
	}
	defer rows.Close()

	var gid int = 0
	for rows.Next() {
		rows.Scan(&gid)
		break
	}
	rows.Close()

	if gid == 0 {
		return errors.New("错误:请先选择程序组")
	}

	// 查找程序是否已经添加到某个组
	sqlstr = "SELECT g.groupname FROM proc_group g JOIN proc u " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE u.procname = '%s';", proc)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighProcAdd(): %s, %s", err, sqlstr)
		return err
	}
	defer rows.Close()

	isAdd := 0
	var gname string
	for rows.Next() {
		rows.Scan(&gname)
		isAdd = 1
		break
	}
	rows.Close()
	if isAdd == 1 {
		return errors.New("错误:该程序已经存在于分组:" + gname)
	}

	sqlstr = fmt.Sprintf("INSERT INTO proc (id, gid, procname) VALUES (null, %d, '%s');", gid, proc)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighProcAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighProcAdd:", gid, group, proc)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighProcAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

// 删除程序
func DBHighProcDel(proc string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighProcDel: %s\n", err)
		return err
	}

	// 查找程序是否存在
	sqlstr := fmt.Sprintf("SELECT id FROM proc WHERE procname = '%s';", proc)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighProcDel(): %s, %s", err, sqlstr)
		return err
	}
	defer rows.Close()

	var uid int = 0
	for rows.Next() {
		rows.Scan(&uid)
		break
	}
	rows.Close()
	if uid == 0 {
		return errors.New("错误:该程序不存在")
	}

	sqlstr = fmt.Sprintf("DELETE FROM proc WHERE id = %d;", uid)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighProcDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighProcDel:", uid, proc)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighProcDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

// 查找程序
func DBHighProcSearch(group string, start, length int) (procs []string, total int, err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighProcSearch: %s\n", err)
		return procs, total, err
	}

	// 查找数量
	sqlstr := "SELECT COUNT(*) FROM proc u JOIN proc_group g " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE g.groupname = '%s';", group)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighProcSearch(): %s, %s", err, sqlstr)
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

	// 查找程序
	sqlstr = "SELECT u.procname FROM proc u JOIN proc_group g " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE g.groupname = '%s' ORDER BY u.procname ASC LIMIT %d, %d;", group, start, length)

	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighProcSearch(): %s, %s", err, sqlstr)
		return procs, total, err
	}
	defer rows.Close()

	var proc string
	for rows.Next() {
		rows.Scan(&proc)
		procs = append(procs, proc)
	}
	rows.Close()

	//log.Println("DBHighProcSearch:", group, start, length, procs)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighProcSearch:tx.Commit: %s\n", err)
		tx.Rollback()
		return procs, total, err
	}
	return procs, total, nil
}
