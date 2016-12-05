package main

func InitAllRule() error {
	hlog, err := LogFileInit(LogFileRunLog)
	if err != nil {
		return err
	}
	GHandleFileRunLog = hlog

	hlog.Println("[INFO]", "-------START----------")
	hlog.Println("[INFO]", "Init()...")
	hlog.Println("[INFO]", "CreateDB()...")
	FirstCreateDB()

	// 登录用户DB
	LogInfo(hlog, "ConnectSqlite():", DBFileUserName)
	db, err := ConnectSqlite(DBFileUserName)
	if err != nil {
		hlog.Fatalln("[INFO]", err)
		return err
	}
	GHandleDBUser = db

	// 自保护规则DB
	hlog.Println("[INFO]", "ConnectSqlite():", DBFileRuleSelf)
	db, err = ConnectSqlite(DBFileRuleSelf)
	if err != nil {
		hlog.Fatalln("[INFO]", err)
		return err
	}
	GHandleDBRuleSelf = db

	// 基础保护规则DB
	hlog.Println("[INFO]", "ConnectSqlite():", DBFileRuleSafe)
	db, err = ConnectSqlite(DBFileRuleSafe)
	if err != nil {
		hlog.Fatalln("[INFO]", err)
		return err
	}
	GHandleDBRuleSafe = db

	// 自保护规则DB
	hlog.Println("[INFO]", "ConnectSqlite():", DBFileRuleUser)
	db, err = ConnectSqlite(DBFileRuleUser)
	if err != nil {
		hlog.Fatalln("[INFO]", err)
		return err
	}
	GHandleDBRuleUser = db

	// 配置 Mode, Super procsee DB
	hlog.Println("[INFO]", "ConnectSqlite():", DBFileRuleCfg)
	db, err = ConnectSqlite(DBFileRuleCfg)
	if err != nil {
		hlog.Fatalln("[INFO]", err)
		return err
	}
	GHandleDBRuleCfg = db

	// 配置系统操作日志 和 拦截事件
	hlog.Println("[INFO]", "LogInit()...")
	err = LogDBInit()
	if err != nil {
		hlog.Fatalln("[INFO]", err)
		return err
	}

	// 加载规则到内存DB
	hlog.Println("[INFO]", "MemRuleInit()...")
	err = MemRuleInit()
	if err != nil {
		hlog.Fatalln("[INFO]", err)
		return err
	}

	return nil
}

func main() {
	if InitAllRule() != nil {
		return
	}
	RuleMatchInitTCPServer(true)
	GHandleFileRunLog.Println("[INFO]", "HttpWebStart:", GHttpWebAddr)
	HttpInitWeb(false)
}
