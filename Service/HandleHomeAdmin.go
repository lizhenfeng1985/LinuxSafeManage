package main

import "net/http"

type HomeAdminGetRequest struct {
	Tokey string
}

type LabValue struct {
	Label string
	Value int
}

func HomeAdminHandler(w http.ResponseWriter, r *http.Request) {
	//var req HomeAdminGetRequest

	var tpl TplData
	var data []LabValue
	data = append(data, LabValue{Label: "进程事件", Value: 10})
	data = append(data, LabValue{Label: "文件事件", Value: 25})
	data = append(data, LabValue{Label: "网络事件", Value: 15})
	data = append(data, LabValue{Label: "特殊资源", Value: 8})

	tpl.Data = data

	Render(w, "tpl/admin_board_home.tpl", tpl)
}
