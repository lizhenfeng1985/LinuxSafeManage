package main

import (
	"errors"
	"fmt"
	"log"
)

func DBHighObjFileGroupAdd(group string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjFileGroupAdd: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("INSERT INTO obj_file_group (id, groupname, gtype) VALUES (null, '%s', 0);", group)

	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileGroupAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjFileGroupAdd:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjFileGroupAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighObjFileGroupDel(group string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjFileGroupAdd: %s\n", err)
		return err
	}

	// 查找组和类型
	sqlstr := fmt.Sprintf("SELECT gtype FROM obj_file_group WHERE groupname = '%s';", group)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileGroupSearch(): %s, %s", err, sqlstr)
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
	sqlstr = fmt.Sprintf("SELECT count(*) FROM obj_file u JOIN obj_file_group g ON u.gid = g.id WHERE g.groupname = '%s';", group)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileGroupSearch(): %s, %s", err, sqlstr)
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

	sqlstr = fmt.Sprintf("DELETE FROM obj_file_group WHERE groupname = '%s' and gtype != 1;", group)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileGroupDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjFileGroupDel:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjFileGroupDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighObjFileGroupSearch() (groups []string, err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjFileGroupSearch: %s\n", err)
		return groups, err
	}

	sqlstr := fmt.Sprintf("SELECT groupname FROM obj_file_group ORDER BY id;")

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileGroupSearch(): %s, %s", err, sqlstr)
		return groups, errors.New("错误:查询客体程序组失败")
	}
	defer rows.Close()

	for rows.Next() {
		var group string
		rows.Scan(&group)
		groups = append(groups, group)
	}
	rows.Close()

	//log.Println("DBHighObjFileGroupSearch:", groups)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjFileGroupDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return groups, err
	}
	return groups, nil
}

// 获取客体程序列表
func DBHighObjFileList() (obj_files map[string]int, err error) {
	obj_files = make(map[string]int)
	for i := 1; i <= 4; i++ {
		obj_files[fmt.Sprintf("/FF%d", i)] = i % 2
	}
	return obj_files, err
}

// 添加客体程序
func DBHighObjFileAdd(group, obj_file string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjFileAdd: %s\n", err)
		return err
	}

	// 查找gid
	sqlstr := fmt.Sprintf("SELECT id FROM obj_file_group WHERE groupname = '%s';", group)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileAdd(): %s, %s", err, sqlstr)
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
	sqlstr = "SELECT g.groupname FROM obj_file_group g JOIN obj_file u " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE u.obj_filename = '%s';", obj_file)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileAdd(): %s, %s", err, sqlstr)
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

	sqlstr = fmt.Sprintf("INSERT INTO obj_file (id, gid, obj_filename) VALUES (null, %d, '%s');", gid, obj_file)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjFileAdd:", gid, group, obj_file)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjFileAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

// 删除客体程序
func DBHighObjFileDel(obj_file string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjFileDel: %s\n", err)
		return err
	}

	// 查找客体程序是否存在
	sqlstr := fmt.Sprintf("SELECT id FROM obj_file WHERE obj_filename = '%s';", obj_file)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileDel(): %s, %s", err, sqlstr)
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

	sqlstr = fmt.Sprintf("DELETE FROM obj_file WHERE id = %d;", uid)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighObjFileDel:", uid, obj_file)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjFileDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

// 查找客体程序
func DBHighObjFileSearch(group string, start, length int) (obj_files []string, total int, err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighObjFileSearch: %s\n", err)
		return obj_files, total, err
	}

	// 查找数量
	sqlstr := "SELECT COUNT(*) FROM obj_file u JOIN obj_file_group g " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE g.groupname = '%s';", group)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileSearch(): %s, %s", err, sqlstr)
		return obj_files, total, err
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&total)
		break
	}
	rows.Close()

	if total == 0 {
		return obj_files, total, nil
	}

	// 查找客体程序
	sqlstr = "SELECT u.obj_filename FROM obj_file u JOIN obj_file_group g " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE g.groupname = '%s' ORDER BY u.obj_filename ASC LIMIT %d, %d;", group, start, length)

	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighObjFileSearch(): %s, %s", err, sqlstr)
		return obj_files, total, err
	}
	defer rows.Close()

	var obj_file string
	for rows.Next() {
		rows.Scan(&obj_file)
		obj_files = append(obj_files, obj_file)
	}
	rows.Close()

	//log.Println("DBHighObjFileSearch:", group, start, length, obj_files)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighObjFileSearch:tx.Commit: %s\n", err)
		tx.Rollback()
		return obj_files, total, err
	}
	return obj_files, total, nil
}
