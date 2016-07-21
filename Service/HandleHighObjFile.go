package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

// 客体文件组 - 添加 - 请求
type HighObjFileGroupAddRequest struct {
	Tokey string
	Group string
}

// 客体文件组 - 删除 - 请求
type HighObjFileGroupDelRequest struct {
	Tokey string
	Group string
}

// <客体文件 | 客体文件组> <添加 | 删除>- 响应
type HighObjFileResponse struct {
	Status int
	ErrMsg string
}

// 客体文件组 - 查找 - 请求
type HighObjFileGroupSearchRequest struct {
	Tokey string
}

// 客体文件组 - 查找 - 响应
type HighObjFileGroupSearchResponse struct {
	Status int
	ErrMsg string
	Groups []string
}

// 客体文件 - 添加 - 请求
type HighObjFileAddRequest struct {
	Tokey   string
	Group   string
	ObjFile string
}

// 客体文件 - 删除 - 请求
type HighObjFileDelRequest struct {
	Tokey   string
	ObjFile string
}

// 客体文件 - 查找 - 请求
type HighObjFileSearchRequest struct {
	Tokey  string
	Group  string
	Start  int
	Length int
}

// 客体文件 - 查找 - 响应
type HighObjFileSearchResponse struct {
	Status   int
	ErrMsg   string
	ObjFiles []string
	Total    int
}

// 客体文件 - 列表 - 请求
type HighObjFileListRequest struct {
	Tokey  string
	ObjDir string
}

// 客体文件 - 列表 - 响应
type HighObjFileListResponse struct {
	Status   int
	ErrMsg   string
	ObjFiles map[string]int
}

func HighObjFileErrResponse(res *HighObjFileResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjFileGroupSearchErrResponse(res *HighObjFileGroupSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjFileSearchErrResponse(res *HighObjFileSearchResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjFileListErrResponse(res *HighObjFileListResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func HighObjFileGroupAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjFileGroupAddRequest
	var res HighObjFileResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjFileErrResponse(&res, -1, "POST /highobjfile/groupadd/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highobjfile/groupadd {ObjFile:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highobjfile/groupadd ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjFileErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjFileErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjFileGroupAdd(req.Group)
		if err != nil {
			w.Write(HighObjFileErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjFileErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjFileErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjFileGroupDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjFileGroupDelRequest
	var res HighObjFileResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjFileErrResponse(&res, -1, "POST /highobjfile/groupdel/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highobjfile/groupdel {ObjFile:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highobjfile/groupdel ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjFileErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjFileErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjFileGroupDel(req.Group)
		if err != nil {
			w.Write(HighObjFileErrResponse(&res, -1, err.Error()))
			return
		}
		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjFileErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjFileErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjFileGroupSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjFileGroupSearchRequest
	var res HighObjFileGroupSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjFileGroupSearchErrResponse(&res, -1, "POST /highobjfile/groupsearch/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highobjfile/groupsearch {ObjFile:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highobjfile/groupsearch ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjFileGroupSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjFileGroupSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Groups, err = DBHighObjFileGroupSearch()
		if err != nil {
			w.Write(HighObjFileGroupSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjFileGroupSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjFileGroupSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

// 客体文件列表
func HighObjFileListHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjFileListRequest
	var res HighObjFileListResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjFileListErrResponse(&res, -1, "POST //highobjfile/list/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highobjfile/list {ObjFile:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highobjfile/list ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjFileListErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjFileListErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.ObjFiles, err = DBHighObjFileList()
		if err != nil {
			w.Write(HighObjFileListErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjFileListErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjFileListErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

// 客体文件 添加
func HighObjFileAddHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjFileAddRequest
	var res HighObjFileResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjFileErrResponse(&res, -1, "POST /highobjfile/add/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highobjfile/add {ObjFile:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highobjfile/add ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjFileErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjFileErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjFileAdd(req.Group, req.ObjFile)
		if err != nil {
			w.Write(HighObjFileErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjFileErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjFileErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjFileDelHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjFileDelRequest
	var res HighObjFileResponse
	//var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjFileErrResponse(&res, -1, "POST /highobjfile/del/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highobjfile/del {ObjFile:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highobjfile/del ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjFileErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjFileErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBHighObjFileDel(req.ObjFile)
		if err != nil {
			w.Write(HighObjFileErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjFileErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjFileErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func HighObjFileSearchHandler(w http.ResponseWriter, r *http.Request) {
	var req HighObjFileSearchRequest
	var res HighObjFileSearchResponse
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(HighObjFileSearchErrResponse(&res, -1, "POST /highobjfile/search/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		log.Printf("POST /highobjfile/search {ObjFile:%s, Data=%s}", uname, jdata)
		defer log.Println("RESP /highobjfile/search ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(HighObjFileSearchErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(HighObjFileSearchErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.ObjFiles, res.Total, err = DBHighObjFileSearch(req.Group, req.Start, req.Length)
		if err != nil {
			w.Write(HighObjFileSearchErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(HighObjFileSearchErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(HighObjFileSearchErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}
