package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

type SpecialSetRequest struct {
	Tokey    string
	Mode     int
	SetTime  int
	ShutDown int
	Usb      int
	Cdrom    int
}

type SpecialGetRequest struct {
	Tokey string
}

type SpecialResponse struct {
	Status   int
	ErrMsg   string
	Mode     int
	SetTime  int
	ShutDown int
	Usb      int
	Cdrom    int
}

func SpecialErrResponse(res *SpecialResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func SpecialGetHandler(w http.ResponseWriter, r *http.Request) {
	var res SpecialResponse
	var req SpecialGetRequest
	var err error
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(SpecialErrResponse(&res, -1, "POST /specialget/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /specialget {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /specialget ", &res)

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(SpecialErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(SpecialErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		res.Mode, res.SetTime, res.ShutDown, res.Usb, res.Cdrom, err = DBSpecialConfigGet()
		if err != nil {
			w.Write(SpecialErrResponse(&res, -1, err.Error()))
			return
		}

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(SpecialErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(SpecialErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}

func SpecialSetHandler(w http.ResponseWriter, r *http.Request) {
	var res SpecialResponse
	var req SpecialSetRequest
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(SpecialErrResponse(&res, -1, "POST /specialset/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /specialset {User:%s, Data=%s}", uname, jdata)
		//defer log.Println("RESP /specialset ", &res)
		defer LogInsertSys(uname, "设置特殊资源策略状态", getResMsgByStatus(res.Status), jdata)

		// Check User
		if uname != "Admin" && uname != "CenterAdmin" {
			w.Write(SpecialErrResponse(&res, -1, "错误:非管理员没有操作权限"))
			return
		}

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(SpecialErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			w.Write(SpecialErrResponse(&res, -2, "错误:请重新登录"))
			return
		}

		// logic
		err := DBSpecialConfigSet(req.Mode, req.SetTime, req.ShutDown, req.Usb, req.Cdrom)
		if err != nil {
			w.Write(SpecialErrResponse(&res, -1, err.Error()))
			return
		}
		res.Mode = req.Mode
		res.SetTime = req.SetTime
		res.ShutDown = req.ShutDown
		res.Usb = req.Usb
		res.Cdrom = req.Cdrom

		// Response
		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(SpecialErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(SpecialErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}
