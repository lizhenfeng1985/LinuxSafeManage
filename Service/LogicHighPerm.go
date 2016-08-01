package main

import (
	"errors"
	"fmt"
	"log"
)

func checkTypePerm(ObjType, Perm string) (err error) {
	switch ObjType {
	case "文件对象":
		switch Perm {
		case "只读":
			return nil
		case "读写":
			return nil
		default:
			return errors.New("错误:权限类型错误:" + Perm)
		}
	case "进程对象":
		switch Perm {
		case "进程执行":
			return nil
		case "进程结束":
			return nil
		default:
			return errors.New("错误:权限类型错误:" + Perm)
		}
	case "网络对象":
		switch Perm {
		case "网络监听":
			return nil
		case "网络连接":
			return nil
		default:
			return errors.New("错误:权限类型错误:" + Perm)
		}
	default:
		return errors.New("错误:客体类型错误:" + ObjType)
	}
}

func checkGroupExists(UserGroup, ProcGroup, ObjGroup, ObjType string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighPermAdd: %s\n", err)
		return err
	}

	// 检查用户组是否存在
	sqlstr := fmt.Sprintf("SELECT id FROM user_group WHERE groupname = '%s';", UserGroup)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighPermAdd(): %s, %s", err, sqlstr)
		return errors.New("错误:查询用户组失败")
	}
	defer rows.Close()

	var cnt int = 0
	for rows.Next() {
		rows.Scan(&cnt)
		break
	}
	rows.Close()
	if cnt <= 0 {
		return errors.New("错误:用户组不存在")
	}

	// 检查进程组是否存在
	sqlstr = fmt.Sprintf("SELECT id FROM proc_group WHERE groupname = '%s';", ProcGroup)
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighPermAdd(): %s, %s", err, sqlstr)
		return errors.New("错误:查询程序组失败")
	}
	defer rows.Close()

	cnt = 0
	for rows.Next() {
		rows.Scan(&cnt)
		break
	}
	rows.Close()
	if cnt <= 0 {
		return errors.New("错误:程序组不存在")
	}

	// 检查客体组是否存在
	switch ObjType {
	case "文件对象":
		sqlstr = fmt.Sprintf("SELECT id FROM obj_file_group WHERE groupname = '%s';", ObjGroup)
	case "进程对象":
		sqlstr = fmt.Sprintf("SELECT id FROM obj_proc_group WHERE groupname = '%s';", ObjGroup)
	case "网络对象":
		sqlstr = fmt.Sprintf("SELECT id FROM obj_net_group WHERE groupname = '%s';", ObjGroup)
	default:
		return errors.New("错误:客体类型错误:" + ObjType)
	}
	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighPermAdd(): %s, %s", err, sqlstr)
		return errors.New("错误:查询客体对象组失败")
	}
	defer rows.Close()

	cnt = 0
	for rows.Next() {
		rows.Scan(&cnt)
		break
	}
	rows.Close()
	if cnt <= 0 {
		return errors.New("错误:客体对象组不存在")
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighPermAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighPermAdd(UserGroup, ProcGroup, ObjGroup, ObjType, Perm string) (err error) {
	db := GHandleDBRule

	err = checkTypePerm(ObjType, Perm)
	if err != nil {
		return err
	}

	err = checkGroupExists(UserGroup, ProcGroup, ObjGroup, ObjType)
	if err != nil {
		return err
	}

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighPermAdd: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("INSERT INTO perms (id, user, proc, obj, objtype, perm) VALUES (null, '%s', '%s', '%s', '%s', '%s', );", UserGroup, ProcGroup, ObjGroup, ObjType, Perm)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighPermAdd:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	//log.Println("DBHighPermAdd:", group)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighPermAdd:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighPermDel(UserGroup, ProcGroup, ObjGroup, ObjType, Perm string) (err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighPermDel: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("SELECT id FROM perms WHERE user = '%s' and proc = '%s' and obj = '%s' and objtype = '%s' and perm = '%s';",
		UserGroup, ProcGroup, ObjGroup, ObjType, Perm)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighPermDel(): %s, %s", err, sqlstr)
		return errors.New("错误:查询权限表失败")
	}
	defer rows.Close()

	var cnt int = 0
	for rows.Next() {
		rows.Scan(&cnt)
		break
	}
	rows.Close()
	if cnt <= 0 {
		return errors.New("错误:权限表记录不存在")
	}

	sqlstr = fmt.Sprintf("DELETE FROM perms WHERE user = '%s' and proc = '%s' and obj = '%s' and objtype = '%s' and perm = '%s';",
		UserGroup, ProcGroup, ObjGroup, ObjType, Perm)
	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBHighPermDel:tx.Exec((): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighPermDel:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBHighPermSearch(UserGroup string, Start, Length int) (PermItems []PermItem, err error) {
	db := GHandleDBRule

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBHighPermSearch: %s\n", err)
		return PermItems, err
	}

	sqlstr := fmt.Sprintf("SELECT user, proc, obj, objtype, perm FROM perms WHERE user = '%s' ;", UserGroup)
	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBHighPermSearch(): %s, %s", err, sqlstr)
		return PermItems, errors.New("错误:查询权限表失败")
	}
	defer rows.Close()

	var item PermItem
	for rows.Next() {
		rows.Scan(&item.UserGroup, &item.ProcGroup, &item.ObjGroup, &item.ObjType, &item.Perm)
		PermItems = append(PermItems, item)
	}
	rows.Close()

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBHighPermSearch:tx.Commit: %s\n", err)
		tx.Rollback()
		return PermItems, err
	}
	return PermItems, nil
}
