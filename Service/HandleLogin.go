package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

type LoginResponse struct {
	Status int
	ErrMsg string
	User   string
	Tokey  string
}

func LoginErrResponse(res *LoginResponse, status int, errMsg string) []byte {
	res.Status = status
	res.ErrMsg = errMsg

	jres, _ := json.Marshal(res)
	return jres
}

func LoginHandler(w http.ResponseWriter, r *http.Request) {
	var res LoginResponse
	res.Status = 0
	res.ErrMsg = "OK"

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			w.Write(LoginErrResponse(&res, -1, "POST /Login/{UserName} : Miss UserName"))
			return
		}
		pwd := r.PostFormValue("Password")

		log.Printf("POST /Login {User:%s, Password:%s}", uname, pwd)

		tokey, err := CheckLogin(uname, pwd)
		if err != nil {
			w.Write(LoginErrResponse(&res, -1, err.Error()))
			return
		}
		res.User = uname
		res.Tokey = tokey

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
