package main

import (
	"net/http"

	"github.com/gorilla/mux"
)

func InitAll() error {
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

	hlog.Println("[INFO]", "Init()...ok")
	return nil
}

func main() {
	if InitAll() != nil {
		return
	}

	// Add Routers
	rhttps := mux.NewRouter()
	// 登录
	rhttps.HandleFunc("/login/{UserName}", LoginHandler)

	// 特殊资源
	rhttps.HandleFunc("/specialget/{UserName}", SpecialGetHandler)
	rhttps.HandleFunc("/specialset/{UserName}", SpecialSetHandler)

	// 基础安全
	rhttps.HandleFunc("/safeget/{UserName}", SafeGetHandler)
	rhttps.HandleFunc("/safeset/{UserName}", SafeSetHandler)

	// 高级安全 - 用户组
	rhttps.HandleFunc("/highuser/groupadd/{UserName}", HighUserGroupAddHandler)
	rhttps.HandleFunc("/highuser/groupdel/{UserName}", HighUserGroupDelHandler)
	rhttps.HandleFunc("/highuser/groupsearch/{UserName}", HighUserGroupSearchHandler)

	// 高级安全 - 用户
	rhttps.HandleFunc("/highuser/list/{UserName}", HighUserListHandler)
	rhttps.HandleFunc("/highuser/add/{UserName}", HighUserAddHandler)
	rhttps.HandleFunc("/highuser/del/{UserName}", HighUserDelHandler)
	rhttps.HandleFunc("/highuser/search/{UserName}", HighUserSearchHandler)

	// 高级安全 - 程序组
	rhttps.HandleFunc("/highproc/groupadd/{UserName}", HighProcGroupAddHandler)
	rhttps.HandleFunc("/highproc/groupdel/{UserName}", HighProcGroupDelHandler)
	rhttps.HandleFunc("/highproc/groupsearch/{UserName}", HighProcGroupSearchHandler)

	// 高级安全 - 程序
	rhttps.HandleFunc("/highproc/list/{UserName}", HighProcListHandler)
	rhttps.HandleFunc("/highproc/add/{UserName}", HighProcAddHandler)
	rhttps.HandleFunc("/highproc/del/{UserName}", HighProcDelHandler)
	rhttps.HandleFunc("/highproc/search/{UserName}", HighProcSearchHandler)

	// 高级安全 - 对象 - 程序组
	rhttps.HandleFunc("/highobjproc/groupadd/{UserName}", HighObjProcGroupAddHandler)
	rhttps.HandleFunc("/highobjproc/groupdel/{UserName}", HighObjProcGroupDelHandler)
	rhttps.HandleFunc("/highobjproc/groupsearch/{UserName}", HighObjProcGroupSearchHandler)

	// 高级安装 - 对象 - 程序
	rhttps.HandleFunc("/highobjproc/list/{UserName}", HighObjProcListHandler)
	rhttps.HandleFunc("/highobjproc/add/{UserName}", HighObjProcAddHandler)
	rhttps.HandleFunc("/highobjproc/del/{UserName}", HighObjProcDelHandler)
	rhttps.HandleFunc("/highobjproc/search/{UserName}", HighObjProcSearchHandler)

	// 高级安全 - 对象 - 文件组
	rhttps.HandleFunc("/highobjfile/groupadd/{UserName}", HighObjFileGroupAddHandler)
	rhttps.HandleFunc("/highobjfile/groupdel/{UserName}", HighObjFileGroupDelHandler)
	rhttps.HandleFunc("/highobjfile/groupsearch/{UserName}", HighObjFileGroupSearchHandler)

	// 高级安装 - 对象 - 文件
	rhttps.HandleFunc("/highobjfile/list/{UserName}", HighObjFileListHandler)
	rhttps.HandleFunc("/highobjfile/add/{UserName}", HighObjFileAddHandler)
	rhttps.HandleFunc("/highobjfile/del/{UserName}", HighObjFileDelHandler)
	rhttps.HandleFunc("/highobjfile/search/{UserName}", HighObjFileSearchHandler)

	// 高级安全 - 对象 - 网络组
	rhttps.HandleFunc("/highobjnet/groupadd/{UserName}", HighObjNetGroupAddHandler)
	rhttps.HandleFunc("/highobjnet/groupdel/{UserName}", HighObjNetGroupDelHandler)
	rhttps.HandleFunc("/highobjnet/groupsearch/{UserName}", HighObjNetGroupSearchHandler)

	// 高级安全 - 对象 - 网络
	rhttps.HandleFunc("/highobjnet/add/{UserName}", HighObjNetAddHandler)
	rhttps.HandleFunc("/highobjnet/del/{UserName}", HighObjNetDelHandler)
	rhttps.HandleFunc("/highobjnet/search/{UserName}", HighObjNetSearchHandler)

	// 高级安全 - 权限
	rhttps.HandleFunc("/highperm/add/{UserName}", HighPermAddHandler)
	rhttps.HandleFunc("/highperm/del/{UserName}", HighPermDelHandler)
	rhttps.HandleFunc("/highperm/search/{UserName}", HighPermSearchHandler)

	/*
		rhttp := mux.NewRouter()
		rhttp.HandleFunc("/test", HandlerTest)

		go http.ListenAndServe(":9000", rhttp)
	*/
	http.ListenAndServeTLS(":9001", "server.crt", "server.key", rhttps)

}
