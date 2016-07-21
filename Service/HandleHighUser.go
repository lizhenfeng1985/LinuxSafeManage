package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

// 用户组 - 添加 - 请求
type HighUserGroupAddRequest struct {
	Tokey string
	Group string
}

// 用户组 - 删除 - 请求
type HighUserGroupDelRequest struct {
	Tokey string
	Group string
}

// <用户 | 用户组> <添加 | 删除>- 响应
type HighUserResponse struct {
	Status int
	ErrMsg string
}

// 用户组 - 查找 - 请求
type HighUserGroupSearchRequest struct {
	Tokey string
}

// 用户组 - 查找 - 响应
type HighUserGroupSearchResponse struct {
	Status int
	ErrMsg string
	Groups []string
}

// 用户 - 添加 - 请求
type HighUserAddRequest struct {
	Tokey string
	Group string
	User  string
}

// 用户 - 删除 - 请求
type HighUserDelRequest struct {
	Tokey string
	User  string
}

// 用户 - 查找 - 请求
type HighUserSearchRequest struct {
	Tokey  string
	Group  string
	Start  int
	Length int
}

// 用户 - 查找 - 响应
type HighUserSearchResponse struct {
	Status int
	ErrMsg string
	Users  []string
	Total  int
}

// 用户 - 列表 - 请求
type HighUserListRequest struct {
	Tokey string
}

// 用户 - 列表 - 响应
type HighUserListResponse struct {
	Status int
	ErrMsg string
	Users  []string
}

func HighUserErrResponse(res *HighUserResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighUserGroupSearchErrResponse(res *HighUserGroupSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighUserSearchErrResponse(res *HighUserSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighUserListErrResponse(res *HighUserListResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighUserGroupAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighUserGroupAddRequest
	var res HighUserResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighUserErrResponse(&res, -1, "POST /highuser/groupadd/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highuser/groupadd {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highuser/groupadd ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighUserErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighUserErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighUserGroupAdd(req.Group)
		if err != nil {
			w.Write(HighUserErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighUserErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighUserErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighUserGroupDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighUserGroupDelRequest
	var res HighUserResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighUserErrResponse(&res, -1, "POST /highuser/groupdel/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highuser/groupdel {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highuser/groupdel ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighUserErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighUserErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighUserGroupDel(req.Group)
		if err != nil {
			w.Write(HighUserErrResponse(&res, -1, err.Error()))
			return
		}
		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighUserErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighUserErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighUserGroupSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighUserGroupSearchRequest
	var res HighUserGroupSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighUserGroupSearchErrResponse(&res, -1, "POST /highuser/groupsearch/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highuser/groupsearch {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highuser/groupsearch ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighUserGroupSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighUserGroupSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Groups, err = DBHighUserGroupSearch()
		if err != nil {
			w.Write(HighUserGroupSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighUserGroupSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighUserGroupSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

// 用户列表
func HighUserListHandler(w http.ResponseWriter, r *http.Request) {
	var req HighUserListRequest
	var res HighUserListResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighUserListErrResponse(&res, -1, "POST //highuser/list/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highuser/list {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highuser/list ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighUserListErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighUserListErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Users, err = DBHighUserList()
		if err != nil {
			w.Write(HighUserListErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighUserListErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighUserListErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

// 用户 添加
func HighUserAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighUserAddRequest
	var res HighUserResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighUserErrResponse(&res, -1, "POST /highuser/add/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highuser/add {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highuser/add ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighUserErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighUserErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighUserAdd(req.Group, req.User)
		if err != nil {
			w.Write(HighUserErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighUserErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighUserErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighUserDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighUserDelRequest
	var res HighUserResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighUserErrResponse(&res, -1, "POST /highuser/del/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highuser/del {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highuser/del ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighUserErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighUserErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighUserDel(req.User)
		if err != nil {
			w.Write(HighUserErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighUserErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighUserErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighUserSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighUserSearchRequest
	var res HighUserSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighUserSearchErrResponse(&res, -1, "POST /highuser/search/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highuser/search {User:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highuser/search ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighUserSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighUserSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Users, res.Total, err = DBHighUserSearch(req.Group, req.Start, req.Length)
		if err != nil {
			w.Write(HighUserSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighUserSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighUserSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}
