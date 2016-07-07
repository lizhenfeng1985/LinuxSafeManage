package main

import (
	"database/sql"
	"errors"
	"fmt"
	"log"

	_ "github.com/mattn/go-sqlite3"
)

func ConnectSqlite(dbName string) (db *sql.DB, err error) {
	db, err = sql.Open("sqlite3", dbName)
	if err != nil {
		log.Fatal(dbName, err)
	}

	return db, err
}

func CloseSqlite(db *sql.DB) {
	db.Close()
}

func DBUserGet(uname string) (user LoginUsers, err error) {
	db := GHandleDBUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("RulesCheckUserPassword: %s\n", err)
		return user, err
	}

	sqlstr := fmt.Sprintf("SELECT uname, password FROM users WHERE uname = \"%s\"", uname)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBUserGet(): %s", err)
		return user, errors.New("错误:查询用户名密码失败")
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&user.User, &user.Pwd)
		break
	}
	rows.Close()

	if user.User == "" {
		return user, errors.New("错误:用户名错误")
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitUser:tx.Commit: %s\n", err)
		tx.Rollback()
		return user, err
	}
	return user, nil
}
