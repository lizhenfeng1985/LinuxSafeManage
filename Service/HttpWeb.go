package main

import (
	"net/http"

	"github.com/gorilla/mux"
)

func InitAll() error {
	FirstCreateDB()

	db, err := ConnectSqlite(DBUserName)
	if err != nil {
		return err
	}
	GHandleDBUser = db
	return nil
}

func main() {
	if InitAll() != nil {
		return
	}

	// Add Routers
	rhttps := mux.NewRouter()
	rhttps.HandleFunc("/login/{UserName}", LoginHandler)

	/*
		rhttp := mux.NewRouter()
		rhttp.HandleFunc("/test", HandlerTest)

		go http.ListenAndServe(":9000", rhttp)
	*/
	http.ListenAndServeTLS(":9001", "server.crt", "server.key", rhttps)

}
