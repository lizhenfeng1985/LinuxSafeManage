package main

import (
	"database/sql"
	"errors"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"runtime"
	"strconv"
)

func DBHighObjProcGroupAdd(db *sql.DB, group string) (err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjProcGroupAdd: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("INSERT INTO obj_proc_group (id, groupname, gtype) VALUES (null, '%s', 0);", group)

	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcGroupAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjProcGroupAdd:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjProcGroupAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighObjProcGroupDel(db *sql.DB, group string) (err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjProcGroupAdd: %s\n", err)
		return err
	}

	// 查找组和类型
	sqlstr := fmt.Sprintf("SELECT gtype FROM obj_proc_group WHERE groupname = '%s';", group)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcGroupDel(): %s, %s", err, sqlstr)
		return errors.New("错误:查询客体程序组失败")
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

	// 查找组的客体程序数 如果大于0 不允许删除
	sqlstr = fmt.Sprintf("SELECT count(*) FROM obj_proc u JOIN obj_proc_group g ON u.gid = g.id WHERE g.groupname = '%s';", group)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcGroupDel(): %s, %s", err, sqlstr)
		return errors.New("错误:查询客体程序组失败")
	}
	defer rows.Close()

	var cnt int = 0
	for rows.Next() {
		rows.Scan(&cnt)
	}
	rows.Close()
	if cnt > 0 {
		return errors.New("错误:请先删除当前组中的客体程序")
	}

	// 查找是否关联了权限，如果关联了权限，不允许删除
	sqlstr = fmt.Sprintf("SELECT count(*) FROM perms WHERE obj = '%s' and objtype = '进程对象';", group)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcGroupDel(): %s, %s", err, sqlstr)
		return errors.New("错误:查询关联的权限失败")
	}
	defer rows.Close()

	cnt = 0
	for rows.Next() {
		rows.Scan(&cnt)
	}
	rows.Close()
	if cnt > 0 {
		return errors.New("错误:请先删除关联的权限")
	}

	// 删除
	sqlstr = fmt.Sprintf("DELETE FROM obj_proc_group WHERE groupname = '%s' and gtype != 1;", group)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcGroupDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjProcGroupDel:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjProcGroupDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighObjProcGroupSearch(db *sql.DB) (groups []string, err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjProcGroupSearch: %s\n", err)
		return groups, err
	}

	sqlstr := fmt.Sprintf("SELECT groupname FROM obj_proc_group ORDER BY id;")

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcGroupSearch(): %s, %s", err, sqlstr)
		return groups, errors.New("错误:查询客体程序组失败")
	}
	defer rows.Close()

	for rows.Next() {
		var group string
		rows.Scan(&group)
		groups = append(groups, group)
	}
	rows.Close()

	//log.Println("DBHighObjProcGroupSearch:", groups)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjProcGroupDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return groups, err
	}
	return groups, nil
}

// 获取客体程序列表
func DBHighObjProcList() (obj_procs []string, err error) {
	if runtime.GOOS == "windows" { // for test
		for i := 1; i <= 40; i++ {
			obj_procs = append(obj_procs, fmt.Sprintf("/proc/%d.exe", i))
		}
	} else {
		files, _ := ioutil.ReadDir("/proc")
		for _, fi := range files {
			if fi.IsDir() {
				_, err := strconv.Atoi(fi.Name())
				if err == nil {
					link, err := os.Readlink("/proc/" + fi.Name() + "/exe")
					if err == nil {
						obj_procs = append(obj_procs, link)
					}
				}
			}
		}
		return obj_procs, nil
	}
	return obj_procs, err
}

// 添加客体程序
func DBHighObjProcAdd(db *sql.DB, group, obj_proc string) (err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjProcAdd: %s\n", err)
		return err
	}

	// 查找gid
	sqlstr := fmt.Sprintf("SELECT id FROM obj_proc_group WHERE groupname = '%s';", group)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcAdd(): %s, %s", err, sqlstr)
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
		return errors.New("错误:请先选择客体程序组")
	}

	// 查找客体程序是否已经添加到某个组
	sqlstr = "SELECT g.groupname FROM obj_proc_group g JOIN obj_proc u " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE u.obj_procname = '%s';", obj_proc)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcAdd(): %s, %s", err, sqlstr)
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
		return errors.New("错误:该客体程序已经存在于分组:" + gname)
	}

	sqlstr = fmt.Sprintf("INSERT INTO obj_proc (id, gid, obj_procname) VALUES (null, %d, '%s');", gid, obj_proc)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjProcAdd:", gid, group, obj_proc)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjProcAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}

	// 更新内存
	LockGMemRuleUserHandle.Lock()
	GMemRuleUserHandle.RObjProc[obj_proc] = group
	LockGMemRuleUserHandle.Unlock()

	return nil
}

// 删除客体程序
func DBHighObjProcDel(db *sql.DB, obj_proc string) (err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjProcDel: %s\n", err)
		return err
	}

	// 查找客体程序是否存在
	sqlstr := fmt.Sprintf("SELECT id FROM obj_proc WHERE obj_procname = '%s';", obj_proc)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcDel(): %s, %s", err, sqlstr)
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
		return errors.New("错误:该客体程序不存在")
	}

	sqlstr = fmt.Sprintf("DELETE FROM obj_proc WHERE id = %d;", uid)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjProcDel:", uid, obj_proc)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjProcDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}

	// 更新内存
	LockGMemRuleUserHandle.Lock()
	delete(GMemRuleUserHandle.RObjProc, obj_proc)
	LockGMemRuleUserHandle.Unlock()

	return nil
}

// 查找客体程序
func DBHighObjProcSearch(db *sql.DB, group string, start, length int) (obj_procs []string, total int, err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjProcSearch: %s\n", err)
		return obj_procs, total, err
	}

	// 查找数量
	sqlstr := "SELECT COUNT(*) FROM obj_proc u JOIN obj_proc_group g " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE g.groupname = '%s';", group)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcSearch(): %s, %s", err, sqlstr)
		return obj_procs, total, err
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&total)
		break
	}
	rows.Close()

	if total == 0 {
		return obj_procs, total, nil
	}

	// 查找客体程序
	sqlstr = "SELECT u.obj_procname FROM obj_proc u JOIN obj_proc_group g " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE g.groupname = '%s' ORDER BY u.obj_procname ASC LIMIT %d, %d;", group, start, length)

	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjProcSearch(): %s, %s", err, sqlstr)
		return obj_procs, total, err
	}
	defer rows.Close()

	var obj_proc string
	for rows.Next() {
		rows.Scan(&obj_proc)
		obj_procs = append(obj_procs, obj_proc)
	}
	rows.Close()

	//log.Println("DBHighObjProcSearch:", group, start, length, obj_procs)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjProcSearch:tx.Commit: %s\n", err)
		tx.Rollback()
		return obj_procs, total, err
	}
	return obj_procs, total, nil
}
