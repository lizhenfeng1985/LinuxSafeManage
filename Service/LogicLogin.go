package main

import (
	"crypto/md5"
	"encoding/hex"
	"errors"
	"fmt"
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
