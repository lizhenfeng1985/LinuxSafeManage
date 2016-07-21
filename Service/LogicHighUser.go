package main

import (
	"errors"
	"fmt"
	"log"
)

func DBHighUserGroupAdd(group string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighUserGroupAdd: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("INSERT INTO user_group (id, groupname, gtype) VALUES (null, '%s', 0);", group)

	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighUserGroupAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighUserGroupAdd:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighUserGroupAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighUserGroupDel(group string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighUserGroupAdd: %s\n", err)
		return err
	}

	// 查找组和类型
	sqlstr := fmt.Sprintf("SELECT gtype FROM user_group WHERE groupname = '%s';", group)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighUserGroupSearch(): %s, %s", err, sqlstr)
		return errors.New("错误:查询用户组失败")
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

	// 查找组的用户数 如果大于0 不允许删除
	sqlstr = fmt.Sprintf("SELECT count(*) FROM user u JOIN user_group g ON u.gid = g.id WHERE g.groupname = '%s';", group)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighUserGroupSearch(): %s, %s", err, sqlstr)
		return errors.New("错误:查询用户组失败")
	}
	defer rows.Close()

	var cnt int = 0
	for rows.Next() {
		rows.Scan(&cnt)
	}
	rows.Close()
	if cnt > 0 {
		return errors.New("错误:请先删除当前组中的用户")
	}

	sqlstr = fmt.Sprintf("DELETE FROM user_group WHERE groupname = '%s' and gtype != 1;", group)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighUserGroupDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighUserGroupDel:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighUserGroupDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighUserGroupSearch() (groups []string, err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighUserGroupSearch: %s\n", err)
		return groups, err
	}

	sqlstr := fmt.Sprintf("SELECT groupname FROM user_group ORDER BY id;")

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighUserGroupSearch(): %s, %s", err, sqlstr)
		return groups, errors.New("错误:查询用户组失败")
	}
	defer rows.Close()

	for rows.Next() {
		var group string
		rows.Scan(&group)
		groups = append(groups, group)
	}
	rows.Close()

	//log.Println("DBHighUserGroupSearch:", groups)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighUserGroupDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return groups, err
	}
	return groups, nil
}

// 获取用户列表
func DBHighUserList() (users []string, err error) {
	for i := 1; i <= 40; i++ {
		users = append(users, fmt.Sprintf("user_%d", i))
	}
	return users, err
}

// 添加用户
func DBHighUserAdd(group, user string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighUserAdd: %s\n", err)
		return err
	}

	// 查找gid
	sqlstr := fmt.Sprintf("SELECT id FROM user_group WHERE groupname = '%s';", group)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighUserAdd(): %s, %s", err, sqlstr)
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
		return errors.New("错误:请先选择用户组")
	}

	// 查找用户是否已经添加到某个组
	sqlstr = "SELECT g.groupname FROM user_group g JOIN user u " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE u.username = '%s';", user)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighUserAdd(): %s, %s", err, sqlstr)
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
		return errors.New("错误:该用户已经存在于分组:" + gname)
	}

	sqlstr = fmt.Sprintf("INSERT INTO user (id, gid, username) VALUES (null, %d, '%s');", gid, user)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighUserAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighUserAdd:", gid, group, user)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighUserAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

// 删除用户
func DBHighUserDel(user string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighUserDel: %s\n", err)
		return err
	}

	// 查找用户是否存在
	sqlstr := fmt.Sprintf("SELECT id FROM user WHERE username = '%s';", user)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighUserDel(): %s, %s", err, sqlstr)
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
		return errors.New("错误:该用户不存在")
	}

	sqlstr = fmt.Sprintf("DELETE FROM user WHERE id = %d;", uid)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighUserDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighUserDel:", uid, user)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighUserDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

// 查找用户
func DBHighUserSearch(group string, start, length int) (users []string, total int, err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighUserSearch: %s\n", err)
		return users, total, err
	}

	// 查找数量
	sqlstr := "SELECT COUNT(*) FROM user u JOIN user_group g " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE g.groupname = '%s';", group)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighUserSearch(): %s, %s", err, sqlstr)
		return users, total, err
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&total)
		break
	}
	rows.Close()

	if total == 0 {
		return users, total, nil
	}

	// 查找用户
	sqlstr = "SELECT u.username FROM user u JOIN user_group g " +
		"ON u.gid = g.id " +
		fmt.Sprintf("WHERE g.groupname = '%s' ORDER BY u.username ASC LIMIT %d, %d;", group, start, length)

	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighUserSearch(): %s, %s", err, sqlstr)
		return users, total, err
	}
	defer rows.Close()

	var user string
	for rows.Next() {
		rows.Scan(&user)
		users = append(users, user)
	}
	rows.Close()

	//log.Println("DBHighUserSearch:", group, start, length, users)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighUserSearch:tx.Commit: %s\n", err)
		tx.Rollback()
		return users, total, err
	}
	return users, total, nil
}
