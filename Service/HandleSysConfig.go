package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

// 系统设置 - 授权 - 设置 - 请求
type SysConfigSnSetRequest struct {
	Tokey string
	Lic   string
}

// 系统设置 - 授权 - 设置 - 响应
type SysConfigSnSetResponse struct {
	Status int
	ErrMsg string
}

// 系统设置 - 授权 - 获取 - 请求
type SysConfigSnGetRequest struct {
	Tokey string
}

// 系统设置 - 授权 - 获取 - 响应
type SysConfigSnGetResponse struct {
	Status   int
	ErrMsg   string
	IsReg    int
	Code     string
	Lic      string
	Validate string
}

// 系统设置 - 授权 - 设置
func SysConfigSnSetHandler(w http.ResponseWriter, r *http.Request) {
	var req SysConfigSnSetRequest
	var res SysConfigSnSetResponse
	var jdata, uname string
	var ok bool

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok = vars["UserName"]
		if !ok {
			res.Status = -1
			res.ErrMsg = "错误:缺少用户标识"
			goto end
		}
		jdata = r.PostFormValue("Data")

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			res.Status = -1
			res.ErrMsg = "错误:Data参数错误"
			goto end
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			res.Status = -1
			res.ErrMsg = "错误:请退出后重新登录"
			goto end
		}

		// logic
		err := SerialRegister(req.Lic)
		if err != nil {
			res.Status = -1
			res.ErrMsg = err.Error()
			goto end
		}

		// OK
		res.Status = 0
		res.ErrMsg = "OK"
	} else {
		res.Status = -1
		res.ErrMsg = "错误:不支持的数据请求方法"
	}
end:
	LogInsertSys(uname, "设置注册码", getResMsgByStatus(res.Status), jdata)
	jres, _ := json.Marshal(res)
	w.Write(jres)
}

// 系统设置 - 授权 - 获取
func SysConfigSnGetHandler(w http.ResponseWriter, r *http.Request) {
	var req SysConfigSnGetRequest
	var res SysConfigSnGetResponse
	var jdata string
	var err error

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			res.Status = -1
			res.ErrMsg = "错误:缺少用户标识"
			goto end
		}
		jdata = r.PostFormValue("Data")

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			res.Status = -1
			res.ErrMsg = "错误:Data参数错误"
			goto end
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			res.Status = -1
			res.ErrMsg = "错误:请退出后重新登录"
			goto end
		}

		// logic
		res.Code, res.Lic, res.Validate, err = SerialGet()
		if err != nil {
			res.Status = -1
			res.ErrMsg = err.Error()
			goto end
		}

		// OK
		res.IsReg = 1
		res.Status = 0
		res.ErrMsg = "OK"
	} else {
		res.Status = -1
		res.ErrMsg = "错误:不支持的数据请求方法"
	}
end:
	jres, _ := json.Marshal(res)
	//logger.Info(r.URL, jdata, string(jres))
	w.Write(jres)
}

//////////////////////////////////

// 系统设置 - 修改密码 - 设置 - 请求
type SysConfigPasswdSetRequest struct {
	Tokey  string
	OldPwd string
	NewPwd string
}

// 系统设置 - 修改密码 - 设置 - 响应
type SysConfigPasswdSetResponse struct {
	Status int
	ErrMsg string
}

// 系统设置 - 修改密码 - 设置
func SysConfigPasswdSetHandler(w http.ResponseWriter, r *http.Request) {
	var req SysConfigPasswdSetRequest
	var res SysConfigPasswdSetResponse
	var jdata, uname string
	var ok bool

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok = vars["UserName"]
		if !ok {
			res.Status = -1
			res.ErrMsg = "错误:缺少用户标识"
			goto end
		}
		jdata = r.PostFormValue("Data")

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			res.Status = -1
			res.ErrMsg = "错误:Data参数错误"
			goto end
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			res.Status = -1
			res.ErrMsg = "错误:请退出后重新登录"
			goto end
		}

		// logic
		err := SysConfigPasswdSet(uname, req.OldPwd, req.NewPwd)
		if err != nil {
			res.Status = -1
			res.ErrMsg = err.Error()
			goto end
		}

		// OK
		res.Status = 0
		res.ErrMsg = "OK"
	} else {
		res.Status = -1
		res.ErrMsg = "错误:不支持的数据请求方法"
	}
end:
	LogInsertSys(uname, "修改密码", getResMsgByStatus(res.Status), jdata)
	jres, _ := json.Marshal(res)
	//logger.Info(r.URL, jdata, string(jres))
	w.Write(jres)
}

//////////////////////////////////
// 白名单 - 添加 - 请求
type SysConfigWhiteProcAddRequest struct {
	Tokey string
	Proc  string
}

// 白名单 - 添加 - 响应
type SysConfigWhiteProcAddResponse struct {
	Status int
	ErrMsg string
}

// 白名单 - 删除 - 请求
type SysConfigWhiteProcDelRequest struct {
	Tokey string
	Proc  string
}

// 白名单 - 删除 - 响应
type SysConfigWhiteProcDelResponse struct {
	Status int
	ErrMsg string
}

// 白名单 - 查找 - 请求
type SysConfigWhiteProcSearchRequest struct {
	Tokey  string
	Start  int
	Length int
}

// 白名单 - 查找 - 响应
type SysConfigWhiteProcSearchResponse struct {
	Status int
	ErrMsg string
	Total  int
	Procs  []string
}

func SysConfigWhiteProcAddHandler(w http.ResponseWriter, r *http.Request) {
	var req SysConfigWhiteProcAddRequest
	var res SysConfigWhiteProcAddResponse
	var jdata, uname string
	var ok bool
	var err error

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok = vars["UserName"]
		if !ok {
			res.Status = -1
			res.ErrMsg = "错误:缺少用户标识"
			goto end
		}
		jdata = r.PostFormValue("Data")

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			res.Status = -1
			res.ErrMsg = "错误:Data参数错误"
			goto end
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			res.Status = -1
			res.ErrMsg = "错误:请退出后重新登录"
			goto end
		}

		// logic
		err = DBSuperProcSet(req.Proc)
		if err != nil {
			res.Status = -1
			res.ErrMsg = err.Error()
			goto end
		}

		// OK
		res.Status = 0
		res.ErrMsg = "OK"
	} else {
		res.Status = -1
		res.ErrMsg = "错误:不支持的数据请求方法"
	}
end:
	LogInsertSys(uname, "添加进程白名单", getResMsgByStatus(res.Status), jdata)
	jres, _ := json.Marshal(res)
	//logger.Info(r.URL, jdata, string(jres))
	w.Write(jres)
}
func SysConfigWhiteProcDelHandler(w http.ResponseWriter, r *http.Request) {
	var req SysConfigWhiteProcDelRequest
	var res SysConfigWhiteProcDelResponse
	var jdata, uname string
	var ok bool
	var err error

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok = vars["UserName"]
		if !ok {
			res.Status = -1
			res.ErrMsg = "错误:缺少用户标识"
			goto end
		}
		jdata = r.PostFormValue("Data")

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			res.Status = -1
			res.ErrMsg = "错误:Data参数错误"
			goto end
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			res.Status = -1
			res.ErrMsg = "错误:请退出后重新登录"
			goto end
		}

		// logic
		err = DBSuperProcDel(req.Proc)
		if err != nil {
			res.Status = -1
			res.ErrMsg = err.Error()
			goto end
		}

		// OK
		res.Status = 0
		res.ErrMsg = "OK"
	} else {
		res.Status = -1
		res.ErrMsg = "错误:不支持的数据请求方法"
	}
end:
	LogInsertSys(uname, "删除进程白名单", getResMsgByStatus(res.Status), jdata)
	jres, _ := json.Marshal(res)
	//logger.Info(r.URL, jdata, string(jres))
	w.Write(jres)
}
func SysConfigWhiteProcSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req SysConfigWhiteProcSearchRequest
	var res SysConfigWhiteProcSearchResponse
	var jdata string
	var err error

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			res.Status = -1
			res.ErrMsg = "错误:缺少用户标识"
			goto end
		}
		jdata = r.PostFormValue("Data")

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			res.Status = -1
			res.ErrMsg = "错误:Data参数错误"
			goto end
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			res.Status = -1
			res.ErrMsg = "错误:请退出后重新登录"
			goto end
		}

		// logic
		res.Procs, res.Total, err = DBSuperProcSearch(req.Start, req.Length)
		if err != nil {
			res.Status = -1
			res.ErrMsg = err.Error()
			goto end
		}

		// OK
		res.Status = 0
		res.ErrMsg = "OK"
	} else {
		res.Status = -1
		res.ErrMsg = "错误:不支持的数据请求方法"
	}
end:
	jres, _ := json.Marshal(res)
	//logger.Info(r.URL, jdata, string(jres))
	w.Write(jres)
}
