package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

type HomeAdminGetRequest struct {
	Tokey string
}

type LabValue struct {
	Label string
	Value int
}

type HomeAdminGetResponse struct {
	Status    int
	ErrMsg    string
	LabValues []LabValue
}

func HomeAdminHandler(w http.ResponseWriter, r *http.Request) {
	var req HomeAdminGetRequest
	var res HomeAdminGetResponse
	var jdata string

	if r.Method == "POST" {
		r.ParseForm()

		vars := mux.Vars(r)
		uname, ok := vars["UserName"]
		if !ok {
			res.Status = -1
			res.ErrMsg = "错误:缺少用户标识"
			goto end
		}
		jdata = r.PostFormValue("Data")

		// check data
		if json.Unmarshal([]byte(jdata), &req) != nil {
			res.Status = -1
			res.ErrMsg = "错误:Data参数错误"
			goto end
		}

		// Check tokey
		if UserTokeyCheck(uname, req.Tokey) == false {
			res.Status = -1
			res.ErrMsg = "错误:请退出后重新登录"
			goto end
		}

		// logic
		rcnt, err := LogicLogCountHomeAdmin()
		if err != nil {
			res.Status = -1
			res.ErrMsg = err.Error()
			goto end
		}

		res.LabValues = append(res.LabValues, LabValue{Label: "自我保护", Value: rcnt.CntSelf})
		res.LabValues = append(res.LabValues, LabValue{Label: "基础安全", Value: rcnt.CntSafe})
		res.LabValues = append(res.LabValues, LabValue{Label: "用户策略", Value: rcnt.CntSpec})
		res.LabValues = append(res.LabValues, LabValue{Label: "特殊资源", Value: rcnt.CntUser})

		// OK
		res.Status = 0
		res.ErrMsg = "OK"
	} else {
		res.Status = -1
		res.ErrMsg = "错误:不支持的数据请求方法"
	}
end:
	jres, _ := json.Marshal(res)
	//logger.Info(r.URL, jdata, string(jres))
	w.Write(jres)
}
