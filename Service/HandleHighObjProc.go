package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

// 客体程序组 - 添加 - 请求
type HighObjProcGroupAddRequest struct {
	Tokey string
	Group string
}

// 客体程序组 - 删除 - 请求
type HighObjProcGroupDelRequest struct {
	Tokey string
	Group string
}

// <客体程序 | 客体程序组> <添加 | 删除>- 响应
type HighObjProcResponse struct {
	Status int
	ErrMsg string
}

// 客体程序组 - 查找 - 请求
type HighObjProcGroupSearchRequest struct {
	Tokey string
}

// 客体程序组 - 查找 - 响应
type HighObjProcGroupSearchResponse struct {
	Status int
	ErrMsg string
	Groups []string
}

// 客体程序 - 添加 - 请求
type HighObjProcAddRequest struct {
	Tokey   string
	Group   string
	ObjProc string
}

// 客体程序 - 删除 - 请求
type HighObjProcDelRequest struct {
	Tokey   string
	ObjProc string
}

// 客体程序 - 查找 - 请求
type HighObjProcSearchRequest struct {
	Tokey  string
	Group  string
	Start  int
	Length int
}

// 客体程序 - 查找 - 响应
type HighObjProcSearchResponse struct {
	Status   int
	ErrMsg   string
	ObjProcs []string
	Total    int
}

// 客体程序 - 列表 - 请求
type HighObjProcListRequest struct {
	Tokey string
}

// 客体程序 - 列表 - 响应
type HighObjProcListResponse struct {
	Status   int
	ErrMsg   string
	ObjProcs []string
}

func HighObjProcErrResponse(res *HighObjProcResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjProcGroupSearchErrResponse(res *HighObjProcGroupSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjProcSearchErrResponse(res *HighObjProcSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjProcListErrResponse(res *HighObjProcListResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjProcGroupAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjProcGroupAddRequest
	var res HighObjProcResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjProcErrResponse(&res, -1, "POST /highobjproc/groupadd/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjproc/groupadd {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjproc/groupadd ", &res)
		defer LogInsertSys(uname, "添加进程对象组", getResMsgByStatus(res.Status), jdata)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjProcErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjProcErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjProcGroupAdd(GHandleDBRuleUser, req.Group)
		if err != nil {
			w.Write(HighObjProcErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjProcErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjProcErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjProcGroupDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjProcGroupDelRequest
	var res HighObjProcResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjProcErrResponse(&res, -1, "POST /highobjproc/groupdel/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjproc/groupdel {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjproc/groupdel ", &res)
		defer LogInsertSys(uname, "删除进程对象组", getResMsgByStatus(res.Status), jdata)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjProcErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjProcErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjProcGroupDel(GHandleDBRuleUser, req.Group)
		if err != nil {
			w.Write(HighObjProcErrResponse(&res, -1, err.Error()))
			return
		}
		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjProcErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjProcErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjProcGroupSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjProcGroupSearchRequest
	var res HighObjProcGroupSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjProcGroupSearchErrResponse(&res, -1, "POST /highobjproc/groupsearch/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjproc/groupsearch {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjproc/groupsearch ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjProcGroupSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjProcGroupSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Groups, err = DBHighObjProcGroupSearch(GHandleDBRuleUser)
		if err != nil {
			w.Write(HighObjProcGroupSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjProcGroupSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjProcGroupSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

// 客体程序列表
func HighObjProcListHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjProcListRequest
	var res HighObjProcListResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjProcListErrResponse(&res, -1, "POST //highobjproc/list/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjproc/list {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjproc/list ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjProcListErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjProcListErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.ObjProcs, err = DBHighObjProcList()
		if err != nil {
			w.Write(HighObjProcListErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjProcListErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjProcListErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

// 客体程序 添加
func HighObjProcAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjProcAddRequest
	var res HighObjProcResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjProcErrResponse(&res, -1, "POST /highobjproc/add/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjproc/add {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjproc/add ", &res)
		defer LogInsertSys(uname, "添加进程对象", getResMsgByStatus(res.Status), jdata)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjProcErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjProcErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjProcAdd(GHandleDBRuleUser, req.Group, req.ObjProc)
		if err != nil {
			w.Write(HighObjProcErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjProcErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjProcErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjProcDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjProcDelRequest
	var res HighObjProcResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjProcErrResponse(&res, -1, "POST /highobjproc/del/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjproc/del {User:%s, Data=%s}", uname, jdata)
		//defer //log.Println("RESP /highobjproc/del ", &res)
		defer LogInsertSys(uname, "删除进程对象", getResMsgByStatus(res.Status), jdata)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjProcErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjProcErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjProcDel(GHandleDBRuleUser, req.ObjProc)
		if err != nil {
			w.Write(HighObjProcErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjProcErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjProcErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjProcSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjProcSearchRequest
	var res HighObjProcSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjProcSearchErrResponse(&res, -1, "POST /highobjproc/search/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjproc/search {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjproc/search ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjProcSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjProcSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.ObjProcs, res.Total, err = DBHighObjProcSearch(GHandleDBRuleUser, req.Group, req.Start, req.Length)
		if err != nil {
			w.Write(HighObjProcSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjProcSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjProcSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}
