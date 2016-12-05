package main

import (
	"log"
	"os"
)

func checkFileIsExist(filename string) bool {
	var exist = true
	if _, err := os.Stat(filename); os.IsNotExist(err) {
		exist = false
	}
	return exist
}

func LogFileInit(log_file string) (hlog *log.Logger, err error) {
	if _, err := os.Stat(log_file); os.IsNotExist(err) {
		// 不存在
		fp, err := os.Create(log_file)
		if err != nil {
			return hlog, err
		}
		hlog = log.New(fp, "", log.Lshortfile|log.LstdFlags)
	} else {
		fp, err := os.OpenFile(log_file, os.O_APPEND, 0666)
		if err != nil {
			return hlog, err
		}
		hlog = log.New(fp, "", log.Lshortfile|log.LstdFlags)
	}

	return hlog, nil
}

func LogInfo(hlog *log.Logger, v ...interface{}) {
	hlog.Println("[INFO]", v)
}

func LogError(hlog *log.Logger, v ...interface{}) {
	hlog.Println("[ERROR]", v)
}

func LogDebug(hlog *log.Logger, v ...interface{}) {
	hlog.Println("[DEBUG]", v)
}

func LogFatal(hlog *log.Logger, v ...interface{}) {
	hlog.Fatalln("[FATAL]", v)
}
