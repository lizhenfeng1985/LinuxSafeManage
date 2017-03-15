package main

import (
	"html/template"
	"net/http"

	"github.com/gorilla/mux"
)

type TplData struct {
	Data interface{}
}

func getResMsgByStatus(status int) (msg string) {
	if status == 0 {
		return "成功"
	}
	return "失败"
}

func Render(w http.ResponseWriter, tplName string, tplData TplData) {
	t, err := template.ParseFiles(tplName)
	if err == nil {
		t.Execute(w, tplData)
	}
}

func HttpInitWeb(run_in_thread bool) {
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

	// 自保护状态
	rhttps.HandleFunc("/statself/get/{UserName}", RuleStatSelfGetHandler)
	rhttps.HandleFunc("/statself/set/{UserName}", RuleStatSelfSetHandler)

	// 用户策略保护状态
	rhttps.HandleFunc("/statuser/get/{UserName}", RuleStatUserGetHandler)
	rhttps.HandleFunc("/statuser/set/{UserName}", RuleStatUserSetHandler)

	// 管理员首页
	rhttps.HandleFunc("/home/admin/{UserName}", HomeAdminHandler)

	// 设置 - 授权
	rhttps.HandleFunc("/sysconfig/serial/get/{UserName}", SysConfigSnGetHandler)
	rhttps.HandleFunc("/sysconfig/serial/set/{UserName}", SysConfigSnSetHandler)

	// 设置 - 修改密码
	rhttps.HandleFunc("/sysconfig/passwd/set/{UserName}", SysConfigPasswdSetHandler)

	// 设置 - 进程白名单
	rhttps.HandleFunc("/sysconfig/whiteproc/add/{UserName}", SysConfigWhiteProcAddHandler)
	rhttps.HandleFunc("/sysconfig/whiteproc/del/{UserName}", SysConfigWhiteProcDelHandler)
	rhttps.HandleFunc("/sysconfig/whiteproc/search/{UserName}", SysConfigWhiteProcSearchHandler)

	// rhttps添加
	http.Handle("/", rhttps)

	// 静态文件
	//http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./static"))))

	if run_in_thread == true {
		//go http.ListenAndServe(GHttpWebAddr, nil)
		go http.ListenAndServeTLS(GHttpWebAddr, "server.crt", "server.key", nil)
	} else {
		//http.ListenAndServe(GHttpWebAddr, nil)
		http.ListenAndServeTLS(GHttpWebAddr, "server.crt", "server.key", nil)
	}

}
