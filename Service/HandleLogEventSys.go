package main

import (
	"encoding/json"
	"net/http"

	"github.com/donnie4w/go-logger/logger"
	"github.com/gorilla/mux"
)

// 安全日志 - 查询 - 请求
type LogEventSysQueryRequest struct {
	Tokey     string
	TimeStart string
	TimeStop  string
	KeyWord   string
	Start     int
	Length    int
}

// 安全日志 - 查询  - 响应
type LogEventSysQueryResponse struct {
	Status  int
	ErrMsg  string
	Total   int
	Results []LogEventSys
}

type LogEventSys struct {
	LoginName string
	Op        string
	Result    string
	Info      string
	LogTime   string
}

func LogEventSysQueryHandler(w http.ResponseWriter, r *http.Request) {
	var req LogEventSysQueryRequest
	var res LogEventSysQueryResponse
	var jdata string
	var err error

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
		res.Results, res.Total, err = LogEventSysQuery(req.TimeStart, req.TimeStop, req.KeyWord, req.Start, req.Length)
		if err != nil {
			res.Status = -1
			res.ErrMsg = err.Error()
			goto end
		}

		// OK
		res.Status = 0
		res.ErrMsg = "OK"
	} else {
		res.Status = -1
		res.ErrMsg = "错误:不支持的数据请求方法"
	}
end:
	jres, _ := json.Marshal(res)
	logger.Info(r.URL, jdata, string(jres))
	w.Write(jres)
}
