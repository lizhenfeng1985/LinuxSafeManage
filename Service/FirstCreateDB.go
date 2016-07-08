package main

import (
	"database/sql"
	"errors"
	"log"
)

func DBInitUser() (err error) {
	db, _ := sql.Open("sqlite3", DBUserName)
	defer db.Close()

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

func DBInitRuleSpeical() (err error) {
	db, _ := sql.Open("sqlite3", DBRuleName)
	defer db.Close()

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

func FirstCreateDB() (err error) {
	var errcnt int = 0
	err = DBInitUser()
	if err != nil {
		errcnt += 1
	}

	err = DBInitRuleSpeical()
	if err != nil {
		errcnt += 1
	}

	if errcnt > 0 {
		return errors.New("FirstCreateDB")
	}

	return nil
}
