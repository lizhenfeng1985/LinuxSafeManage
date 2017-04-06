package main

import (
	"database/sql"
	"log"
	"sync"
)

var (
	GPwdUsedInfo string = "作者:李振逢 QQ:24324962"

	DBFileUserName string = "./db/user.db"      // 登录用户DB文件
	DBFileRuleSelf string = "./db/rule_self.db" // 自保护策略DB文件
	DBFileRuleSafe string = "./db/rule_safe.db" // 基础保护策略DB文件
	DBFileRuleUser string = "./db/rule_user.db" // 用户保护策略DB文件
	DBFileRuleCfg  string = "./db/rule_cfg.db"  // 开关配置和超级进程配置DB文件

	LogFileRunLog string = "./log/run.log"      // 程序运行日志文件
	DBFileLog     string = "./log/event_log.db" // 系统运行|拦截事件 日志文件

	GHandleFileRunLog *log.Logger = nil // 运行日志句柄
	GHandleDBUser     *sql.DB     = nil // 登录用户DB句柄
	GHandleDBRuleSelf *sql.DB     = nil // 自保护策略DB句柄
	GHandleDBRuleSafe *sql.DB     = nil // 基础保护策略DB句柄
	GHandleDBRuleUser *sql.DB     = nil // 用户保护策略DB句柄
	GHandleDBRuleCfg  *sql.DB     = nil // 开关配置和超级进程DB句柄
	GHandleDBLog      *sql.DB     = nil // 日志DB句柄

	GUserTockey      LoginUserTokey = make(LoginUserTokey) // 用户登录内存句柄
	rwLockGUserTokey sync.Mutex

	GMemRuleSelfHandle     RuleMemHandle // 自保护策略内存句柄
	LockGMemRuleSelfHandle sync.Mutex    // 自保护策略锁内存句柄

	GMemRuleSafeHandle     RuleMemHandle // 基础安全保护策略内存句柄
	LockGMemRuleSafeHandle sync.Mutex    // 基础安全保护策略内存句柄锁

	GMemRuleUserHandle     RuleMemHandle // 用户保护策略内存句柄
	LockGMemRuleUserHandle sync.Mutex    // 用户保护策略内存句柄锁

	GMemRuleSpecialHandle     RuleSpecialMemHandle // 特殊资源开关内存句柄
	LockGMemRuleSpecialHandle sync.Mutex           // 特殊资源开关内存句柄锁

	GMemRuleSuperHandle     map[string]int // 超级进程策略内存句柄
	LockGMemRuleSuperHandle sync.Mutex     // 超级进程策略内存句柄锁

	GCacheRuleSize int        = 5000 // 缓存记录数量
	GCacheRule     *Cache     = nil  // 缓存句柄
	LockCacheRule  sync.Mutex        // 缓存锁

	GRuleMatchTCPMsgRecvSize int    = 808     // TCP每个消息请求的大小
	GRuleMatchTCPMsgSendSize int    = 4       // TCP每个消息返回的大小
	GRuleMatchTCPAddr        string = ":9002" // 接收内核消息的TCL服务地址
	GHttpWebAddr             string = ":9001" // 接收界面消息的HTTP服务地址
)
