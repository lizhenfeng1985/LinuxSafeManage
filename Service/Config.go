package main

import (
	"database/sql"
	"sync"
)

var (
	DBUserName     string = "./db/user.db"
	DBRuleName     string = "./db/rule.db"
	DBAdminLogName string = "./db/admin.log.db"
	DBAuditLogName string = "./db/audit.log.db"

	GPwdUsedInfo  string  = "作者:李振逢 QQ:24324962"
	GHandleDBUser *sql.DB = nil

	GUserTockey      LoginUserTokey = make(LoginUserTokey)
	rwLockGUserTokey sync.Mutex
)
