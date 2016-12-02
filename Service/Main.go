package main

func InitAllRule() error {
	hlog, err := LogInit(LogRunFile)
	if err != nil {
		return err
	}
	GLogRunHandle = hlog

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
	GLogRunHandle.Println("[INFO]", "HttpWebStart:", GHttpWebAddr)
	HttpInitWeb(false)
}
