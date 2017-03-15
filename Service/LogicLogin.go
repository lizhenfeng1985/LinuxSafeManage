package main

import (
	"crypto/md5"
	"encoding/hex"
	"errors"
	"fmt"
	"log"
	"time"
)

type LoginUsers struct {
	User string
	Pwd  string
}

type LoginUserTokey map[string]string

func GetMd5String(in string) (out string) {
	md5Ctx := md5.New()
	md5Ctx.Write([]byte(GPwdUsedInfo + in))
	cipherStr := md5Ctx.Sum(nil)
	out = hex.EncodeToString(cipherStr)
	return out
}

func UserTokeyUpdate(uname string) (tokey string) {
	s := GetMd5String(fmt.Sprintf(":%d", time.Now().Unix()))
	tokey = s[4:12]
	rwLockGUserTokey.Lock()
	GUserTockey[uname] = tokey
	rwLockGUserTokey.Unlock()
	return tokey
}

func UserTokeyCheck(uname, tokey string) bool {
	rwLockGUserTokey.Lock()
	defer rwLockGUserTokey.Unlock()

	tk, ok := GUserTockey[uname]
	if !ok {
		return false
	} else {
		if tk == tokey {
			return true
		}
	}
	return false
}

func CheckLogin(uname, pwd string) (tokey string, err error) {
	// 登录时候检测注册状态，未注册，关闭保护
	CheckSerialAndCloseProtest()

	user, err := DBUserGet(uname)
	if err != nil {
		return tokey, err
	}

	encodePwd := GetMd5String(pwd)
	if encodePwd != user.Pwd {
		return tokey, errors.New("错误:密码不正确")
	}

	tokey = UserTokeyUpdate(uname)
	return tokey, nil
}

func DBUserGet(uname string) (user LoginUsers, err error) {
	db := GHandleDBUser

	tx, err := db.Begin()
	if err != nil {
		log.Printf("RulesCheckUserPassword: %s\n", err)
		return user, err
	}

	sqlstr := fmt.Sprintf("SELECT uname, password FROM users WHERE uname = \"%s\"", uname)

	rows, err := db.Query(sqlstr)
	if err != nil {
		log.Printf("DBUserGet(): %s", err)
		return user, errors.New("错误:查询用户名密码失败")
	}
	defer rows.Close()

	for rows.Next() {
		rows.Scan(&user.User, &user.Pwd)
		break
	}
	rows.Close()

	if user.User == "" {
		return user, errors.New("错误:用户名错误")
	}

	// 事务提交
	err = tx.Commit()
	if err != nil {
		log.Printf("DBInitUser:tx.Commit: %s\n", err)
		tx.Rollback()
		return user, err
	}
	return user, nil
}
