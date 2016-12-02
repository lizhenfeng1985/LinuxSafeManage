package main

import (
	"database/sql"
	"errors"
	"fmt"
	"log"
)

func DBHighObjNetGroupAdd(db *sql.DB, group string) (err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjNetGroupAdd: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("INSERT INTO obj_net_group (id, groupname, gtype) VALUES (null, '%s', 0);", group)

	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetGroupAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjNetGroupAdd:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjNetGroupAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighObjNetGroupDel(db *sql.DB, group string) (err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjNetGroupAdd: %s\n", err)
		return err
	}

	// 查找组和类型
	sqlstr := fmt.Sprintf("SELECT gtype FROM obj_net_group WHERE groupname = '%s';", group)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetGroupDel(): %s, %s", err, sqlstr)
		return errors.New("错误:查询客体网络组失败")
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

	// 查找组的客体网络数 如果大于0 不允许删除
	sqlstr = fmt.Sprintf("SELECT count(*) FROM obj_net u JOIN obj_net_group g ON u.gid = g.id WHERE g.groupname = '%s';", group)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetGroupDel(): %s, %s", err, sqlstr)
		return errors.New("错误:查询客体网络组失败")
	}
	defer rows.Close()

	var cnt int = 0
	for rows.Next() {
		rows.Scan(&cnt)
	}
	rows.Close()
	if cnt > 0 {
		return errors.New("错误:请先删除当前组中的客体网络")
	}

	sqlstr = fmt.Sprintf("DELETE FROM obj_net_group WHERE groupname = '%s' and gtype != 1;", group)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetGroupDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjNetGroupDel:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjNetGroupDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighObjNetGroupSearch(db *sql.DB) (groups []string, err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjNetGroupSearch: %s\n", err)
		return groups, err
	}

	sqlstr := fmt.Sprintf("SELECT groupname FROM obj_net_group ORDER BY id;")

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetGroupSearch(): %s, %s", err, sqlstr)
		return groups, errors.New("错误:查询客体网络组失败")
	}
	defer rows.Close()

	for rows.Next() {
		var group string
		rows.Scan(&group)
		groups = append(groups, group)
	}
	rows.Close()

	//log.Println("DBHighObjNetGroupSearch:", groups)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjNetGroupDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return groups, err
	}
	return groups, nil
}

// 添加客体网络
func DBHighObjNetAdd(db *sql.DB, group, obj_net string) (err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjNetAdd: %s\n", err)
		return err
	}

	// 查找gid
	sqlstr := fmt.Sprintf("SELECT id FROM obj_net_group WHERE groupname = '%s';", group)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetAdd(): %s, %s", err, sqlstr)
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
		return errors.New("错误:请先选择客体网络组")
	}

	// 查找客体网络是否已经添加到某个组
	sqlstr = "SELECT g.groupname FROM obj_net_group g JOIN obj_net u " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE u.obj_netname = '%s';", obj_net)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetAdd(): %s, %s", err, sqlstr)
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
		return errors.New("错误:该客体网络已经存在于分组:" + gname)
	}

	sqlstr = fmt.Sprintf("INSERT INTO obj_net (id, gid, obj_netname) VALUES (null, %d, '%s');", gid, obj_net)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjNetAdd:", gid, group, obj_net)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjNetAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}

	// 更新内存
	LockGMemRuleUserHandle.Lock()
	GMemRuleUserHandle.RObjNet[obj_net] = group
	LockGMemRuleUserHandle.Unlock()
	return nil
}

// 删除客体网络
func DBHighObjNetDel(db *sql.DB, obj_net string) (err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjNetDel: %s\n", err)
		return err
	}

	// 查找客体网络是否存在
	sqlstr := fmt.Sprintf("SELECT id FROM obj_net WHERE obj_netname = '%s';", obj_net)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetDel(): %s, %s", err, sqlstr)
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
		return errors.New("错误:该客体网络不存在")
	}

	sqlstr = fmt.Sprintf("DELETE FROM obj_net WHERE id = %d;", uid)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjNetDel:", uid, obj_net)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjNetDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	// 更新内存
	LockGMemRuleUserHandle.Lock()
	delete(GMemRuleUserHandle.RObjNet, obj_net)
	LockGMemRuleUserHandle.Unlock()
	return nil
}

// 查找客体网络
func DBHighObjNetSearch(db *sql.DB, group string, start, length int) (obj_nets []string, total int, err error) {
	//db := GHandleDBRuleUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjNetSearch: %s\n", err)
		return obj_nets, total, err
	}

	// 查找数量
	sqlstr := "SELECT COUNT(*) FROM obj_net u JOIN obj_net_group g " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE g.groupname = '%s';", group)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetSearch(): %s, %s", err, sqlstr)
		return obj_nets, total, err
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&total)
		break
	}
	rows.Close()

	if total == 0 {
		return obj_nets, total, nil
	}

	// 查找客体网络
	sqlstr = "SELECT u.obj_netname FROM obj_net u JOIN obj_net_group g " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE g.groupname = '%s' ORDER BY u.obj_netname ASC LIMIT %d, %d;", group, start, length)

	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjNetSearch(): %s, %s", err, sqlstr)
		return obj_nets, total, err
	}
	defer rows.Close()

	var obj_net string
	for rows.Next() {
		rows.Scan(&obj_net)
		obj_nets = append(obj_nets, obj_net)
	}
	rows.Close()

	//log.Println("DBHighObjNetSearch:", group, start, length, obj_nets)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjNetSearch:tx.Commit: %s\n", err)
		tx.Rollback()
		return obj_nets, total, err
	}
	return obj_nets, total, nil
}
