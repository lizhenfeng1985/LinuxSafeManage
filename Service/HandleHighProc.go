package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

// 程序组 - 添加 - 请求
type HighProcGroupAddRequest struct {
	Tokey string
	Group string
}

// 程序组 - 删除 - 请求
type HighProcGroupDelRequest struct {
	Tokey string
	Group string
}

// <程序 | 程序组> <添加 | 删除>- 响应
type HighProcResponse struct {
	Status int
	ErrMsg string
}

// 程序组 - 查找 - 请求
type HighProcGroupSearchRequest struct {
	Tokey string
}

// 程序组 - 查找 - 响应
type HighProcGroupSearchResponse struct {
	Status int
	ErrMsg string
	Groups []string
}

// 程序 - 添加 - 请求
type HighProcAddRequest struct {
	Tokey string
	Group string
	Proc  string
}

// 程序 - 删除 - 请求
type HighProcDelRequest struct {
	Tokey string
	Proc  string
}

// 程序 - 查找 - 请求
type HighProcSearchRequest struct {
	Tokey  string
	Group  string
	Start  int
	Length int
}

// 程序 - 查找 - 响应
type HighProcSearchResponse struct {
	Status int
	ErrMsg string
	Procs  []string
	Total  int
}

// 程序 - 列表 - 请求
type HighProcListRequest struct {
	Tokey string
}

// 程序 - 列表 - 响应
type HighProcListResponse struct {
	Status int
	ErrMsg string
	Procs  []string
}

func HighProcErrResponse(res *HighProcResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighProcGroupSearchErrResponse(res *HighProcGroupSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighProcSearchErrResponse(res *HighProcSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighProcListErrResponse(res *HighProcListResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighProcGroupAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighProcGroupAddRequest
	var res HighProcResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighProcErrResponse(&res, -1, "POST /highproc/groupadd/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highproc/groupadd {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highproc/groupadd ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighProcErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighProcErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighProcGroupAdd(req.Group)
		if err != nil {
			w.Write(HighProcErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighProcErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighProcErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighProcGroupDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighProcGroupDelRequest
	var res HighProcResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighProcErrResponse(&res, -1, "POST /highproc/groupdel/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highproc/groupdel {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highproc/groupdel ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighProcErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighProcErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighProcGroupDel(req.Group)
		if err != nil {
			w.Write(HighProcErrResponse(&res, -1, err.Error()))
			return
		}
		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighProcErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighProcErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighProcGroupSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighProcGroupSearchRequest
	var res HighProcGroupSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighProcGroupSearchErrResponse(&res, -1, "POST /highproc/groupsearch/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highproc/groupsearch {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highproc/groupsearch ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighProcGroupSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighProcGroupSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Groups, err = DBHighProcGroupSearch()
		if err != nil {
			w.Write(HighProcGroupSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighProcGroupSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighProcGroupSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

// 程序列表
func HighProcListHandler(w http.ResponseWriter, r *http.Request) {
	var req HighProcListRequest
	var res HighProcListResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighProcListErrResponse(&res, -1, "POST //highproc/list/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highproc/list {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highproc/list ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighProcListErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighProcListErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Procs, err = DBHighProcList()
		if err != nil {
			w.Write(HighProcListErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighProcListErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighProcListErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

// 程序 添加
func HighProcAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighProcAddRequest
	var res HighProcResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighProcErrResponse(&res, -1, "POST /highproc/add/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highproc/add {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highproc/add ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighProcErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighProcErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighProcAdd(req.Group, req.Proc)
		if err != nil {
			w.Write(HighProcErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighProcErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighProcErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighProcDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighProcDelRequest
	var res HighProcResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighProcErrResponse(&res, -1, "POST /highproc/del/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highproc/del {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highproc/del ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighProcErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighProcErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighProcDel(req.Proc)
		if err != nil {
			w.Write(HighProcErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighProcErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighProcErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighProcSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighProcSearchRequest
	var res HighProcSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighProcSearchErrResponse(&res, -1, "POST /highproc/search/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highproc/search {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highproc/search ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighProcSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighProcSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Procs, res.Total, err = DBHighProcSearch(req.Group, req.Start, req.Length)
		if err != nil {
			w.Write(HighProcSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighProcSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighProcSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}
