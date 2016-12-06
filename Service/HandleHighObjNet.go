package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

// 客体网络组 - 添加 - 请求
type HighObjNetGroupAddRequest struct {
	Tokey string
	Group string
}

// 客体网络组 - 删除 - 请求
type HighObjNetGroupDelRequest struct {
	Tokey string
	Group string
}

// <客体网络 | 客体网络组> <添加 | 删除>- 响应
type HighObjNetResponse struct {
	Status int
	ErrMsg string
}

// 客体网络组 - 查找 - 请求
type HighObjNetGroupSearchRequest struct {
	Tokey string
}

// 客体网络组 - 查找 - 响应
type HighObjNetGroupSearchResponse struct {
	Status int
	ErrMsg string
	Groups []string
}

// 客体网络 - 添加 - 请求
type HighObjNetAddRequest struct {
	Tokey  string
	Group  string
	ObjNet string
}

// 客体网络 - 删除 - 请求
type HighObjNetDelRequest struct {
	Tokey  string
	ObjNet string
}

// 客体网络 - 查找 - 请求
type HighObjNetSearchRequest struct {
	Tokey  string
	Group  string
	Start  int
	Length int
}

// 客体网络 - 查找 - 响应
type HighObjNetSearchResponse struct {
	Status  int
	ErrMsg  string
	ObjNets []string
	Total   int
}

func HighObjNetErrResponse(res *HighObjNetResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjNetGroupSearchErrResponse(res *HighObjNetGroupSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjNetSearchErrResponse(res *HighObjNetSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjNetGroupAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjNetGroupAddRequest
	var res HighObjNetResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjNetErrResponse(&res, -1, "POST /highobjnet/groupadd/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjnet/groupadd {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjnet/groupadd ", &res)
		defer LogInsertSys(uname, "添加网络对象组", getResMsgByStatus(res.Status), jdata)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjNetErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjNetErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjNetGroupAdd(GHandleDBRuleUser, req.Group)
		if err != nil {
			w.Write(HighObjNetErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjNetErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjNetErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjNetGroupDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjNetGroupDelRequest
	var res HighObjNetResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjNetErrResponse(&res, -1, "POST /highobjnet/groupdel/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjnet/groupdel {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjnet/groupdel ", &res)
		defer LogInsertSys(uname, "删除网络对象组", getResMsgByStatus(res.Status), jdata)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjNetErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjNetErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjNetGroupDel(GHandleDBRuleUser, req.Group)
		if err != nil {
			w.Write(HighObjNetErrResponse(&res, -1, err.Error()))
			return
		}
		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjNetErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjNetErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjNetGroupSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjNetGroupSearchRequest
	var res HighObjNetGroupSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjNetGroupSearchErrResponse(&res, -1, "POST /highobjnet/groupsearch/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjnet/groupsearch {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjnet/groupsearch ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjNetGroupSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjNetGroupSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Groups, err = DBHighObjNetGroupSearch(GHandleDBRuleUser)
		if err != nil {
			w.Write(HighObjNetGroupSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjNetGroupSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjNetGroupSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

// 客体网络 添加
func HighObjNetAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjNetAddRequest
	var res HighObjNetResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjNetErrResponse(&res, -1, "POST /highobjnet/add/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjnet/add {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjnet/add ", &res)
		defer LogInsertSys(uname, "添加网络对象", getResMsgByStatus(res.Status), jdata)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjNetErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjNetErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjNetAdd(GHandleDBRuleUser, req.Group, req.ObjNet)
		if err != nil {
			w.Write(HighObjNetErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjNetErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjNetErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjNetDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjNetDelRequest
	var res HighObjNetResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjNetErrResponse(&res, -1, "POST /highobjnet/del/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjnet/del {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjnet/del ", &res)
		defer LogInsertSys(uname, "删除网络对象", getResMsgByStatus(res.Status), jdata)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjNetErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjNetErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjNetDel(GHandleDBRuleUser, req.ObjNet)
		if err != nil {
			w.Write(HighObjNetErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjNetErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjNetErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjNetSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjNetSearchRequest
	var res HighObjNetSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjNetSearchErrResponse(&res, -1, "POST /highobjnet/search/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /highobjnet/search {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /highobjnet/search ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjNetSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjNetSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.ObjNets, res.Total, err = DBHighObjNetSearch(GHandleDBRuleUser, req.Group, req.Start, req.Length)
		if err != nil {
			w.Write(HighObjNetSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjNetSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjNetSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}
