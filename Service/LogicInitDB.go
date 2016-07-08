package main

import (
	"database/sql"
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
