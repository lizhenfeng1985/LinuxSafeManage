package main

import (
	"fmt"
	"log"
)

func LogEventSafeQuery(time_start, time_stop, key_word string, start, length int) (rs []LogEventSafe, total int, err error) {
	db := GHandleDBLog
	tx, err := db.Begin()
	if err != nil {
		log.Printf("LogEventSafeQuery: %s\n", err)
		return rs, total, err
	}

	// 查找数量
	sqlstr := "SELECT COUNT(id) from log_event WHERE " +
		"logtime >= '" + time_start + "' and " +
		"logtime <= '" + time_stop + "' and " +
		"( module like '%" + key_word + "%' or " +
		"status like '%" + key_word + "%' or " +
		"etype like '%" + key_word + "%' or " +
		"eop like '%" + key_word + "%' or " +
		"uname like '%" + key_word + "%' or " +
		"proc like '%" + key_word + "%' or " +
		"obj like '%" + key_word + "%' or " +
		"result like '%" + key_word + "%' ) "

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("LogEventSafeQuery(): %s, %s", err, sqlstr)
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
	sqlstr = "SELECT module, status, etype, eop, uname, proc, obj, result, strftime('%Y-%m-%d %H:%M:%S', logtime) from log_event WHERE " +
		"logtime >= '" + time_start + "' and " +
		"logtime <= '" + time_stop + "' and " +
		"( module like '%" + key_word + "%' or " +
		"status like '%" + key_word + "%' or " +
		"etype like '%" + key_word + "%' or " +
		"eop like '%" + key_word + "%' or " +
		"uname like '%" + key_word + "%' or " +
		"proc like '%" + key_word + "%' or " +
		"obj like '%" + key_word + "%' or " +
		"result like '%" + key_word + "%' ) " +
		fmt.Sprintf("ORDER BY id DESC LIMIT %d, %d;", start, length)

	rows, err = db.Query(sqlstr)
	if err != nil {
		log.Printf("LogEventSafeQuery(): %s, %s", err, sqlstr)
		return rs, total, err
	}
	defer rows.Close()

	var r LogEventSafe
	for rows.Next() {
		rows.Scan(&r.Module, &r.Status, &r.Etype, &r.Eop, &r.Uname, &r.Proc, &r.Obj, &r.Result, &r.LogTime)
		rs = append(rs, r)
	}
	rows.Close()

	//log.Println("LogEventSafeQuery:", start, length, rs)

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("LogEventSafeQuery:tx.Commit: %s\n", err)
		tx.Rollback()
		return rs, total, err
	}
	return rs, total, nil
}
