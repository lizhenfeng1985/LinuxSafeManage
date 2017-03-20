package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

// 自保护策略 | 用户策略 - 状态
type RuleStatSetRequest struct {
	Tokey string
	Mode  int
}

type RuleStatGetRequest struct {
	Tokey string
}

type RuleStatResponse struct {
	Status int
	ErrMsg string
	Mode   int
}

func RuleStatErrResponse(res *RuleStatResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func RuleStatSelfGetHandler(w http.ResponseWriter, r *http.Request) {
	var res RuleStatResponse
	var req RuleStatGetRequest
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(RuleStatErrResponse(&res, -1, "POST /statself/get/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /statself/get {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /statself/get ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(RuleStatErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(RuleStatErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		proc_stat, file_stat, net_stat, err := DBRuleStatSelfGet()
		if err != nil {
			w.Write(RuleStatErrResponse(&res, -1, err.Error()))
			return
		}
		if proc_stat != file_stat || proc_stat != net_stat {
			w.Write(RuleStatErrResponse(&res, -1, "错误:自保护状态不一致"))
			return
		}
		res.Mode = proc_stat

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(RuleStatErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(RuleStatErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func RuleStatSelfSetHandler(w http.ResponseWriter, r *http.Request) {
	var res RuleStatResponse
	var req RuleStatSetRequest
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(RuleStatErrResponse(&res, -1, "POST /statself/set/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /statself/set {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /statself/set ", &res)
		defer LogInsertSys(uname, "设置自我保护策略状态", getResMsgByStatus(res.Status), jdata)

		// Check User
		if uname != "Admin" && uname != "CenterAdmin" {
			w.Write(RuleStatErrResponse(&res, -1, "错误:非管理员没有操作权限"))
			return
		}

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(RuleStatErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(RuleStatErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBRuleStatSelfSet(req.Mode, req.Mode, req.Mode)
		if err != nil {
			w.Write(RuleStatErrResponse(&res, -1, err.Error()))
			return
		}
		res.Mode = req.Mode

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(RuleStatErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(RuleStatErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func RuleStatUserGetHandler(w http.ResponseWriter, r *http.Request) {
	var res RuleStatResponse
	var req RuleStatGetRequest
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(RuleStatErrResponse(&res, -1, "POST /statuser/get/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /statuser/get {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /statuser/get ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(RuleStatErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(RuleStatErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		proc_stat, file_stat, net_stat, err := DBRuleStatUserGet()
		if err != nil {
			w.Write(RuleStatErrResponse(&res, -1, err.Error()))
			return
		}
		if proc_stat != file_stat || proc_stat != net_stat {
			w.Write(RuleStatErrResponse(&res, -1, "错误:自保护状态不一致"))
			return
		}
		res.Mode = proc_stat

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(RuleStatErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(RuleStatErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func RuleStatUserSetHandler(w http.ResponseWriter, r *http.Request) {
	var res RuleStatResponse
	var req RuleStatSetRequest
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(RuleStatErrResponse(&res, -1, "POST /statuser/set/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /statuser/set {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /statuser/set ", &res)
		defer LogInsertSys(uname, "设置用户保护策略状态", getResMsgByStatus(res.Status), jdata)

		// Check User
		if uname != "Admin" && uname != "CenterAdmin" {
			w.Write(RuleStatErrResponse(&res, -1, "错误:非管理员没有操作权限"))
			return
		}

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(RuleStatErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(RuleStatErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// 检测授权
		if CheckSerialAndCloseProtect() != nil {
			w.Write(RuleStatErrResponse(&res, -3, "错误:软件未注册"))
			return
		}

		// logic
		err := DBRuleStatUserSet(req.Mode, req.Mode, req.Mode)
		if err != nil {
			w.Write(RuleStatErrResponse(&res, -1, err.Error()))
			return
		}
		res.Mode = req.Mode

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(RuleStatErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(RuleStatErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}
