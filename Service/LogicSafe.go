package main

import (
	"errors"
	"fmt"
	"log"
)

func DBSafeConfigGet() (mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb int, err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBSafeConfigGet: %s\n", err)
		return mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb, err
	}

	sqlstr := fmt.Sprintf("SELECT mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb FROM safe WHERE id = %d", 1)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBSafeConfigGet(): %s, %s", err, sqlstr)
		return mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb, errors.New("错误:查询特殊资源配置失败")
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&mode, &fileetc, &filelib, &filebin, &fileboot, &netftp, &nettelnet, &netmail, &netweb)
		break
	}
	rows.Close()

	//log.Println("DB_GET:", mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb)
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBSafeConfigGet:tx.Commit: %s\n", err)
		tx.Rollback()
		return mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb, err
	}
	return mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb, nil
}

func DBSafeConfigSet(mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb int) (err error) {
	db := GHandleDBRuleCfg

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBSafeConfigSet: %s\n", err)
		return err
	}

	sqlstr := fmt.Sprintf("UPDATE safe set mode = %d, fileetc = %d, filelib = %d, filebin = %d, fileboot = %d, netftp = %d, nettelnet = %d, netmail = %d, netweb = %d WHERE id = 1", mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb)

	_, err = tx.Exec(sqlstr)
	if err != nil {
		log.Printf("DBSafeConfigSet:tx.Exec(): %s, %s\n", err, sqlstr)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBSafeConfigSet:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	//log.Println("DB_SET:", mode, settime, shutdown, usb, cdrom)

	// 更新数据库和内存
	if fileetc == 1 {
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/etc/")
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/usr/etc/")
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/usr/local/etc/")
	} else {
		DBHighObjFileDel(GHandleDBRuleSafe, "/etc/")
		DBHighObjFileDel(GHandleDBRuleSafe, "/usr/etc/")
		DBHighObjFileDel(GHandleDBRuleSafe, "/usr/local/etc/")
	}

	if filelib == 1 {
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/lib/")
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/lib64/")
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/usr/lib/")
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/usr/lib64/")
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/usr/local/lib/")
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/usr/local/lib64/")
	} else {
		DBHighObjFileDel(GHandleDBRuleSafe, "/lib/")
		DBHighObjFileDel(GHandleDBRuleSafe, "/lib64/")
		DBHighObjFileDel(GHandleDBRuleSafe, "/usr/lib/")
		DBHighObjFileDel(GHandleDBRuleSafe, "/usr/lib64/")
		DBHighObjFileDel(GHandleDBRuleSafe, "/usr/local/lib/")
		DBHighObjFileDel(GHandleDBRuleSafe, "/usr/local/lib64/")
	}

	if filebin == 1 {
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/bin/")
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/usr/bin/")
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/usr/local/bin/")
	} else {
		DBHighObjFileDel(GHandleDBRuleSafe, "/bin/")
		DBHighObjFileDel(GHandleDBRuleSafe, "/usr/bin/")
		DBHighObjFileDel(GHandleDBRuleSafe, "/usr/local/bin/")
	}

	if fileboot == 1 {
		DBHighObjFileAdd(GHandleDBRuleSafe, "文件只读组", "/boot/")
	} else {
		DBHighObjFileDel(GHandleDBRuleSafe, "/boot/")
	}

	if netftp == 1 {
		DBHighObjNetAdd(GHandleDBRuleSafe, "端口禁止连接组", "0.0.0.0:20")
		DBHighObjNetAdd(GHandleDBRuleSafe, "端口禁止连接组", "0.0.0.0:21")
	} else {
		DBHighObjNetDel(GHandleDBRuleSafe, "0.0.0.0:20")
		DBHighObjNetDel(GHandleDBRuleSafe, "0.0.0.0:21")
	}

	if nettelnet == 1 {
		DBHighObjNetAdd(GHandleDBRuleSafe, "端口禁止连接组", "0.0.0.0:23")
	} else {
		DBHighObjNetDel(GHandleDBRuleSafe, "0.0.0.0:23")
	}

	if netmail == 1 {
		DBHighObjNetAdd(GHandleDBRuleSafe, "端口禁止连接组", "0.0.0.0:25")
		DBHighObjNetAdd(GHandleDBRuleSafe, "端口禁止连接组", "0.0.0.0:465")
		DBHighObjNetAdd(GHandleDBRuleSafe, "端口禁止连接组", "0.0.0.0:587")
	} else {
		DBHighObjNetDel(GHandleDBRuleSafe, "0.0.0.0:25")
		DBHighObjNetDel(GHandleDBRuleSafe, "0.0.0.0:465")
		DBHighObjNetDel(GHandleDBRuleSafe, "0.0.0.0:587")
	}

	if netweb == 1 {
		DBHighObjNetAdd(GHandleDBRuleSafe, "端口禁止连接组", "0.0.0.0:80")
		DBHighObjNetAdd(GHandleDBRuleSafe, "端口禁止连接组", "0.0.0.0:8080")
	} else {
		DBHighObjNetDel(GHandleDBRuleSafe, "0.0.0.0:80")
		DBHighObjNetDel(GHandleDBRuleSafe, "0.0.0.0:8080")
	}

	DBRuleStatSafeSet(mode, mode, mode)

	return nil
}
