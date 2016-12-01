package main

import (
	"database/sql"
	"log"
	"sync"
)

var (
	DBFileUserName string = "./db/user.db"      // 登录用户DB文件
	DBFileRuleSelf string = "./db/rule_self.db" // 自保护策略DB文件
	DBFileRuleUser string = "./db/rule_user.db" // 用户保护策略DB文件
	DBFileRuleCfg  string = "./db/rule_cfg.db"  // 开关配置和超级进程配置DB文件

	LogRunFile   string = "./log/run.log"   // 程序运行日志文件
	DBFileSystem string = "./log/system.db" // 系统运行日志文件
	DBFileEvent  string = "./log/event.db"  // 事件日志文件

	GPwdUsedInfo string = "作者:李振逢 QQ:24324962"

	GHandleDBUser     *sql.DB = nil // 登录用户DB句柄
	GHandleDBRuleSelf *sql.DB = nil // 自保护策略DB句柄
	GHandleDBRuleUser *sql.DB = nil // 用户保护策略DB句柄
	GHandleDBRuleCfg  *sql.DB = nil // 开关配置和超级进程DB句柄

	GLogRunHandle    *log.Logger    = nil                  // 运行日志句柄
	GUserTockey      LoginUserTokey = make(LoginUserTokey) // 用户登录内存句柄
	rwLockGUserTokey sync.Mutex

	GMemRuleSelfHandle      RuleMemHandle // 自保护策略内存句柄
	LockGMemRuleSelfrHandle sync.Mutex    // 自保护策略锁内存句柄

	GMemRuleUserHandle     RuleMemHandle // 用户保护策略内存句柄
	LockGMemRuleUserHandle sync.Mutex    // 用户保护策略内存句柄锁

	GMemRuleSuperHandle     map[string]int // 超级进程策略内存句柄
	LockGMemRuleSuperHandle sync.Mutex     // 超级进程策略内存句柄锁
)
