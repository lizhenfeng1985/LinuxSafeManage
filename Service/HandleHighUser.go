package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

type HighUserGroupAddRequest struct {
	Tokey string
	Group string
}

type HighUserGroupDelRequest struct {
	Tokey string
	Group string
}

type HighUserResponse struct {
	Status int
	ErrMsg string
}

type HighUserGroupSearchRequest struct {
	Tokey string
}

type HighUserGroupSearchResponse struct {
	Status int
	ErrMsg string
	Groups []string
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
