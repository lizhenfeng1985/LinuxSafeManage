package main

import (
	"database/sql"
	"errors"
	"log"
)

func DBInitUser(db *sql.DB) (err error) {
	// Create Table users
	sql := `create table if not exists users (
			uid integer not null primary key, 
			uname char(128) unique,
			password   char(128) not null
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitUser:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitUser:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	sql = `insert into users (uid, uname, password) values 
		(1, 'CenterAdmin', 'bb149ef481514784aa75833d76be7b39'),
		(2, 'CenterAudit', 'bb149ef481514784aa75833d76be7b39'),
		(3, 'Admin', 'b40fdc1791396dc11b4ad54b5744bcd6'),
		(4, 'Audit', 'b40fdc1791396dc11b4ad54b5744bcd6');
	`

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitUser:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitUser:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleSpeical(db *sql.DB) (err error) {
	// Create Table special
	sql := `create table if not exists special (
			id integer not null primary key, 
			mode int default 0,
			settime int default 0,
			shutdown int default 0,
			usb int default 0,
			cdrom int default 0
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleSpeical:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleSpeical:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	sql = `insert into special (id, mode, settime, shutdown, usb, cdrom) values 
		(1, 0, 0, 0, 0, 0);`

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleSpeical:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleSpeical:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleSafe(db *sql.DB) (err error) {
	// Create Table special
	sql := `create table if not exists safe (
			id integer not null primary key, 
			mode int default 0,
			fileetc int default 0,
			filelib int default 0,
			filebin int default 0,
			fileboot int default 0,
			netftp int default 0,
			nettelnet int default 0,
			netmail int default 0,
			netweb int default 0
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleSafe:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleSafe:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	sql = `insert into safe (id, mode, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb) values 
		(1, 0, 0, 0, 0, 0, 0, 0, 0, 0);`

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleSafe:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleSafe:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleSuper(db *sql.DB) (err error) {
	// Create Table super_process
	sql := `create table if not exists super_process (
			id integer not null primary key, 
			procname char(128) not null unique
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleSuper:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleSuper:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}
	/*
		sql = `insert into super_process (id, procname) values
			(1, '/test');`

		_, err = tx.Exec(sql)
		if err != nil {
			log.Printf("DBInitRuleSuper:tx.Exec((): %s, %s\n", err, sql)
			tx.Rollback()
			return err
		}
	*/
	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleSuper:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleUserGroup(db *sql.DB) (err error) {
	// Create Table UserGroup
	sql := `create table if not exists user_group (
			id integer not null primary key, 
			groupname char(128) not null unique,
			gtype int default 0
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleUserGroup:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleUserGroup:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	sql = `insert into user_group (id, groupname, gtype) values 
		(1, '所有用户',1);`

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleUserGroup:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleUserGroup:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleUser(db *sql.DB) (err error) {
	// Create Table User
	sql := `create table if not exists user (
			id integer not null primary key,
			gid int not null default 0,
			username char(128) not null unique
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleUser:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleUser:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleUser:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleProcGroup(db *sql.DB) (err error) {
	// Create Table ProcGroup
	sql := `create table if not exists proc_group (
			id integer not null primary key, 
			groupname char(128) not null unique,
			gtype int default 0
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleProcGroup:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleProcGroup:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	sql = `insert into proc_group (id, groupname, gtype) values 
		(1, '所有进程',1);`

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleProcGroup:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleProcGroup:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleProc(db *sql.DB) (err error) {
	// Create Table Proc
	sql := `create table if not exists proc (
			id integer not null primary key,
			gid int not null default 0,
			procname char(128) not null unique
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleProc:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleProc:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleProc:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleObjProcGroup(db *sql.DB) (err error) {
	// Create Table ObjProcGroup
	sql := `create table if not exists obj_proc_group (
			id integer not null primary key, 
			groupname char(128) not null unique,
			gtype int default 0
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleObjProcGroup:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleObjProcGroup:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleObjProcGroup:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleObjProc(db *sql.DB) (err error) {
	// Create Table ObjProc
	sql := `create table if not exists obj_proc (
			id integer not null primary key,
			gid int not null default 0,
			obj_procname char(128) not null unique
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleObjProc:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleObjProc:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleObjProc:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleObjFileGroup(db *sql.DB) (err error) {
	// Create Table ObjFileGroup
	sql := `create table if not exists obj_file_group (
			id integer not null primary key, 
			groupname char(128) not null unique,
			gtype int default 0
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleObjFileGroup:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleObjFileGroup:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleObjFileGroup:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleObjFile(db *sql.DB) (err error) {
	// Create Table ObjFile
	sql := `create table if not exists obj_file (
			id integer not null primary key,
			gid int not null default 0,
			obj_filename char(128) not null unique
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleObjFile:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleObjFile:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleObjFile:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleObjNetGroup(db *sql.DB) (err error) {
	// Create Table ObjNetGroup
	sql := `create table if not exists obj_net_group (
			id integer not null primary key, 
			groupname char(128) not null unique,
			gtype int default 0
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleObjNetGroup:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleObjNetGroup:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleObjNetGroup:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRuleObjNet(db *sql.DB) (err error) {
	// Create Table ObjFile
	sql := `create table if not exists obj_net (
			id integer not null primary key,
			gid int not null default 0,
			obj_netname char(128) not null unique
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRuleObjNet:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRuleObjNet:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRuleObjNet:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRulePerms(db *sql.DB) (err error) {
	// Create Table ObjFile
	sql := `create table if not exists perms (
			id integer not null primary key,
			user char(128) not null,
			proc char(128) not null,
			obj char(128) not null,
			objtype char(64) not null,
			perm char(64) not null
		);`

	tx, err := db.Begin()
	if err != nil {
		log.Printf("DBInitRulePerms:DB.Begin(): %s\n", err)
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		log.Printf("DBInitRulePerms:tx.Exec((): %s, %s\n", err, sql)
		tx.Rollback()
		return err
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitRulePerms:tx.Commit: %s\n", err)
		tx.Rollback()
		return err
	}
	return nil
}

func DBInitRulePolicy(db *sql.DB) (errcnt int) {
	errcnt = 0

	// 初始化配置 - 用户组
	err := DBInitRuleUserGroup(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 用户
	err = DBInitRuleUser(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 进程组
	err = DBInitRuleProcGroup(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 进程
	err = DBInitRuleProc(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 客体进程组
	err = DBInitRuleObjProcGroup(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 客体进程
	err = DBInitRuleObjProc(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 客体文件组
	err = DBInitRuleObjFileGroup(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 客体文件
	err = DBInitRuleObjFile(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 客体网络组
	err = DBInitRuleObjNetGroup(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 客体网络
	err = DBInitRuleObjNet(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 权限表
	err = DBInitRulePerms(db)
	if err != nil {
		errcnt += 1
	}

	return errcnt
}

func FirstCreateDB() (err error) {
	var errcnt int = 0

	// 初始化用户表
	db, err := ConnectSqlite(DBFileUserName)
	if err != nil {
		return err
	}

	err = DBInitUser(db)
	if err != nil {
		errcnt += 1
	}
	CloseSqlite(db)

	// 初始化配置 - 特殊资源表
	db, err = ConnectSqlite(DBFileRuleCfg)
	if err != nil {
		return err
	}

	err = DBInitRuleSpeical(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 安全项表
	err = DBInitRuleSafe(db)
	if err != nil {
		errcnt += 1
	}

	// 初始化配置 - 超级进程表
	err = DBInitRuleSuper(db)
	if err != nil {
		errcnt += 1
	}
	CloseSqlite(db)

	// 初始化自保护规则
	db, err = ConnectSqlite(DBFileRuleSelf)
	if err != nil {
		return err
	}

	errcnt += DBInitRulePolicy(db)
	CloseSqlite(db)

	// 初始化用户保护规则
	db, err = ConnectSqlite(DBFileRuleUser)
	if err != nil {
		return err
	}

	errcnt += DBInitRulePolicy(db)
	CloseSqlite(db)

	if errcnt > 0 {
		return errors.New("FirstCreateDB")
	}

	return nil
}
