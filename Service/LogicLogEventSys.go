package main

import (
	"fmt"
	"log"
)

func LogEventSysQuery(time_start, time_stop, key_word string, start, length int) (rs []LogEventSys, total int, err error) {
	db := GHandleDBLog
	tx, err := db.Begin()
	if err != nil {
		log.Printf("LogEventSysQuery: %s\n", err)
		return rs, total, err
	}

	// 查找数量
	sqlstr := "SELECT COUNT(id) from log_sys WHERE " +
		"logtime >= '" + time_start + "' and " +
		"logtime <= '" + time_stop + "' and " +
		"( login_name like '%" + key_word + "%' or " +
		"op like '%" + key_word + "%' or " +
		"result like '%" + key_word + "%' or " +
		"info like '%" + key_word + "%' ) "

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("LogEventSysQuery(): %s, %s", err, sqlstr)
		return rs, total, err
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&total)
		break
	}
	rows.Close()

	if total == 0 {
		return rs, total, nil
	}

	// 查找日志
	sqlstr = "SELECT login_name, op, result, info, strftime('%Y-%m-%d %H:%M:%S', logtime) from log_sys WHERE " +
		"logtime >= '" + time_start + "' and " +
		"logtime <= '" + time_stop + "' and " +
		"( login_name like '%" + key_word + "%' or " +
		"op like '%" + key_word + "%' or " +
		"result like '%" + key_word + "%' or " +
		"info like '%" + key_word + "%' ) " +
		fmt.Sprintf("ORDER BY id DESC LIMIT %d, %d;", start, length)

	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("LogEventSysQuery(): %s, %s", err, sqlstr)
		return rs, total, err
	}
	defer rows.Close()

	var r LogEventSys
	for rows.Next() {
		rows.Scan(&r.LoginName, &r.Op, &r.Result, &r.Info, &r.LogTime)
		rs = append(rs, r)
	}
	rows.Close()

	//log.Println("LogEventSysQuery:", start, length, rs)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("LogEventSysQuery:tx.Commit: %s\n", err)
		tx.Rollback()
		return rs, total, err
	}
	return rs, total, nil
}
