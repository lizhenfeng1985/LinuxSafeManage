package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

// 权限 - 添加 - 请求
type HighPermAddRequest struct {
	Tokey     string
	UserGroup string
	ProcGroup string
	ObjGroup  string
	ObjType   string
	Perm      string
}

// 权限 - 删除 - 请求
type HighPermDelRequest struct {
	Tokey     string
	UserGroup string
	ProcGroup string
	ObjGroup  string
	ObjType   string
	Perm      string
}

// <权限> <添加 | 删除>- 响应
type HighPermResponse struct {
	Status int
	ErrMsg string
}

// 权限 - 查找 - 请求
type HighPermSearchRequest struct {
	Tokey     string
	UserGroup string
	Start     int
	Length    int
}

type PermItem struct {
	UserGroup string
	ProcGroup string
	ObjGroup  string
	ObjType   string
	Perm      string
}

// 权限组 - 查找 - 响应
type HighPermSearchResponse struct {
	Status    int
	ErrMsg    string
	PermItems []PermItem
	Total     int
}

func HighPermErrResponse(res *HighPermResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighPermSearchErrResponse(res *HighPermSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighPermAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighPermAddRequest
	var res HighPermResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighPermErrResponse(&res, -1, "POST /highperm/add/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highperm/add {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highperm/add ", &res)
		defer LogInsertSys(uname, "添加权限", getResMsgByStatus(res.Status), jdata)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighPermErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighPermErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighPermAdd(GHandleDBRuleUser, req.UserGroup, req.ProcGroup, req.ObjGroup, req.ObjType, req.Perm)
		if err != nil {
			w.Write(HighPermErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighPermErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighPermErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighPermDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighPermDelRequest
	var res HighPermResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighPermErrResponse(&res, -1, "POST /highperm/del/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highperm/del {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highperm/del ", &res)
		defer LogInsertSys(uname, "删除权限", getResMsgByStatus(res.Status), jdata)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighPermErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighPermErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighPermDel(GHandleDBRuleUser, req.UserGroup, req.ProcGroup, req.ObjGroup, req.ObjType, req.Perm)
		if err != nil {
			w.Write(HighPermErrResponse(&res, -1, err.Error()))
			return
		}
		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighPermErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighPermErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighPermSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighPermSearchRequest
	var res HighPermSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighPermSearchErrResponse(&res, -1, "POST /highperm/search/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highperm/search {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highperm/search ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighPermSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighPermSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.PermItems, res.Total, err = DBHighPermSearch(GHandleDBRuleUser, req.UserGroup, req.Start, req.Length)
		if err != nil {
			w.Write(HighPermSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighPermSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighPermSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}
