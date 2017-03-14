package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

type SafeSetRequest struct {
	Tokey     string
	Mode      int
	FileEtc   int
	FileLib   int
	FileBin   int
	FileBoot  int
	NetFtp    int
	NetTelnet int
	NetMail   int
	NetWeb    int
}

type SafeGetRequest struct {
	Tokey string
}

type SafeResponse struct {
	Status    int
	ErrMsg    string
	Mode      int
	FileEtc   int
	FileLib   int
	FileBin   int
	FileBoot  int
	NetFtp    int
	NetTelnet int
	NetMail   int
	NetWeb    int
}

func SafeErrResponse(res *SafeResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func SafeGetHandler(w http.ResponseWriter, r *http.Request) {
	var res SafeResponse
	var req SafeGetRequest
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(SafeErrResponse(&res, -1, "POST /safeget/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /safeget {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /safeget ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(SafeErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(SafeErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Mode, res.FileEtc, res.FileLib, res.FileBin, res.FileBoot, res.NetFtp, res.NetTelnet, res.NetMail, res.NetWeb, err = DBSafeConfigGet()
		if err != nil {
			w.Write(SafeErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(SafeErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(SafeErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func SafeSetHandler(w http.ResponseWriter, r *http.Request) {
	var res SafeResponse
	var req SafeSetRequest
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(SafeErrResponse(&res, -1, "POST /safeset/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /safeset {User:%s, Data=%s}", uname, jdata)
		//defer //log.Println("RESP /safeset ", &res)
		defer LogInsertSys(uname, "设置基础安全策略状态", getResMsgByStatus(res.Status), jdata)

		// Check User
		if uname != "Admin" && uname != "CenterAdmin" {
			w.Write(SafeErrResponse(&res, -1, "错误:非管理员没有操作权限"))
			return
		}

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(SafeErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(SafeErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// 检测授权
		if CheckSerialAndCloseProtest() != nil {
			w.Write(SafeErrResponse(&res, -3, "错误:软件未注册"))
			return
		}

		// logic
		err := DBSafeConfigSet(req.Mode, req.FileEtc, req.FileLib, req.FileBin, req.FileBoot, req.NetFtp, req.NetTelnet, req.NetMail, req.NetWeb)
		if err != nil {
			w.Write(SafeErrResponse(&res, -1, err.Error()))
			return
		}

		res.Mode = req.Mode
		res.FileEtc = req.FileEtc
		res.FileLib = req.FileLib
		res.FileBin = req.FileBin
		res.FileBoot = req.FileBoot
		res.NetFtp = req.NetFtp
		res.NetTelnet = req.NetTelnet
		res.NetMail = req.NetMail
		res.NetWeb = req.NetWeb

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(SafeErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(SafeErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}
