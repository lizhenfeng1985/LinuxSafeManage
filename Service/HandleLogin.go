package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

type LoginResponse struct {
	Status int
	ErrMsg string
	User   string
	Tokey  string
}

type LoginRequest struct {
	Password     string
	LocalIPPort  string
	CenterIPPort string
}

func LoginErrResponse(res *LoginResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func LoginHandler(w http.ResponseWriter, r *http.Request) {
	var req LoginRequest
	var res LoginResponse
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(LoginErrResponse(&res, -1, "POST /login/{UserName} : Miss UserName"))
			return
		}
		jdata := r.PostFormValue("Data")

		//log.Printf("POST /login {User:%s, Data:%s}", uname, jdata)
		//defer log.Println("RESP /login ", &res)
		defer LogInsertSys(uname, "登录", getResMsgByStatus(res.Status), "Passwd:*****")

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			w.Write(LoginErrResponse(&res, -1, "错误:Data参数错误"))
			return
		}

		tokey, err := CheckLogin(uname, req.Password)
		if err != nil {
			w.Write(LoginErrResponse(&res, -1, err.Error()))
			return
		}
		res.User = uname
		res.Tokey = tokey

		// set Center IP Port

		jres, err := json.Marshal(res)
		if err != nil {
			w.Write(LoginErrResponse(&res, -1, err.Error()))
			return
		}
		w.Write(jres)
	} else {
		w.Write(LoginErrResponse(&res, -1, "HTTP.Method:"+r.Method))
	}
}
