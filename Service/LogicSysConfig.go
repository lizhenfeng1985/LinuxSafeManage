package main

import (
	"crypto/md5"
	"encoding/base64"
	"encoding/hex"
	"errors"
	"fmt"
	"io/ioutil"
	"os"
	"runtime"
	"strconv"
	"strings"
	"time"
)

func GetMachineCode() (code string, err error) {
	var info_path string
	var code_hard string
	if runtime.GOOS == "windows" {
		info_path = "C:/.LinuxManageInfo"
	} else {
		info_path = GSerialCodeFile
	}

re_create:
	_, err = os.Stat(info_path)
	if err != nil {
		datastr := "-----LinuxManageInfo-----\n"
		datastr += " By   : lzf\n"
		datastr += " Mail : 24324962@qq.com\n"
		datastr += " Date : " + time.Now().Format("2006-01-02 15:04:05") + "\n"
		datastr += (" Seq  : " + strconv.Itoa(int(time.Now().Unix())) + "\n")
		datastr += " Warning : Don't modify or delete this file.\n"
		datastr += "-----End-----\n"

		ioutil.WriteFile(info_path, []byte(datastr), 0666)
		code_hard = string(datastr)
	} else {
		data, _ := ioutil.ReadFile(info_path)
		code_hard = string(data)
	}

	if strings.Index(code_hard, "lzf") < 0 ||
		strings.Index(code_hard, "24324962@qq.com") < 0 ||
		strings.Index(code_hard, "Date :") < 0 ||
		strings.Index(code_hard, "Seq  :") < 0 ||
		strings.Index(code_hard, "Warning") < 0 {
		os.Remove(info_path)
		goto re_create
	}

	hash := md5.New()
	hash.Write([]byte("24324962@qq.com" + code_hard))
	hashed := hash.Sum(nil)

	return hex.EncodeToString(hashed), nil
}

func SerialCreate(priKey, code, validate string) (b64lic string, err error) {
	_, err = time.Parse("20060102", validate)
	if err != nil {
		return b64lic, errors.New("ValiDate format err.")
	}

	lic, err := RsaSign(priKey, validate+code)
	if err != nil {
		return b64lic, err
	}

	sn := validate + string(lic)
	b64 := make([]byte, base64.RawStdEncoding.EncodedLen(len(sn)))
	base64.RawStdEncoding.Encode(b64, []byte(sn))

	return string(b64), err
}

func SerialRegister(b64_lic string) (err error) {
	lic := make([]byte, base64.RawStdEncoding.DecodedLen(len(b64_lic)))
	_, err = base64.RawStdEncoding.Decode(lic, []byte(b64_lic))
	if err != nil {
		return err
	}

	pubKey, err := ioutil.ReadFile(GSerialPubKey)
	if err != nil {
		return err
	}

	code, err := GetMachineCode()
	if err != nil {
		return err
	}

	if len(lic) < 20 {
		return errors.New("Wrong License.")
	}

	validate := string(lic[0:8])
	sig := lic[8:GSerialDateSize]

	if time.Now().Format("20060102") > validate {
		return errors.New("License Expired.")
	}

	err = RsaVerify(string(pubKey), validate+string(code), sig)
	if err != nil {
		return err
	}

	return ioutil.WriteFile(GSerialLicense, []byte(b64_lic), 0666)
}

func SerialGet() (code, license, validate string, err error) {
	code, err = GetMachineCode()
	if err != nil {
		return code, license, validate, err
	}

	b64_lic, err := ioutil.ReadFile(GSerialLicense)
	if err != nil {
		return code, license, validate, err
	}

	license = string(b64_lic)

	lic := make([]byte, base64.RawStdEncoding.DecodedLen(len(b64_lic)))
	_, err = base64.RawStdEncoding.Decode(lic, b64_lic)
	if err != nil {
		return code, license, validate, err
	}

	validate = string(lic[0:8])
	return code, license, validate, nil
}

func SerialVerify() (err error) {
	pubKey, err := ioutil.ReadFile(GSerialPubKey)
	if err != nil {
		return err
	}

	code, err := GetMachineCode()
	if err != nil {
		return err
	}

	b64_lic, err := ioutil.ReadFile(GSerialLicense)
	if err != nil {
		return err
	}

	lic := make([]byte, base64.RawStdEncoding.DecodedLen(len(b64_lic)))
	base64.RawStdEncoding.Decode(lic, b64_lic)

	validate := string(lic[0:8])
	sig := lic[8:GSerialDateSize]

	if time.Now().Format("20060102") > validate {
		return errors.New("License Expired.")
	}

	err = RsaVerify(string(pubKey), validate+string(code), sig)
	if err != nil {
		return errors.New("Wrong License.")
	}

	return nil
}

func CheckSerialAndCloseProtest() (err error) {
	err = SerialVerify()
	if err != nil {
		// 关闭特殊资源
		_, settime, shutdown, usb, cdrom, e := DBSpecialConfigGet()
		if e == nil {
			DBSpecialConfigSet(0, settime, shutdown, usb, cdrom)
		}

		// 关闭基础安全
		_, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb, e := DBSafeConfigGet()
		if e == nil {
			DBSafeConfigSet(0, fileetc, filelib, filebin, fileboot, netftp, nettelnet, netmail, netweb)
		}

		// 关闭高级安全 - 用户配置
		DBRuleStatUserSet(0, 0, 0)
	}
	return err
}

func SysConfigPasswdSet(uname, oldpwd, newpwd string) (err error) {
	user, err := DBUserGet(uname)
	if err != nil {
		return err
	}

	encodePwd := GetMd5String(oldpwd)
	if encodePwd != user.Pwd {
		return errors.New("错误:旧密码不正确")
	}

	encodePwd = GetMd5String(newpwd)
	db := GHandleDBUser
	sql := fmt.Sprintf("update users set password = \"%s\" where uname = \"%s\";", encodePwd, uname)
	tx, err := db.Begin()
	if err != nil {
		return err
	}

	_, err = tx.Exec(sql)
	if err != nil {
		tx.Rollback()
		return err
	}

	err = tx.Commit()
	if err != nil {
		tx.Rollback()
		return err
	}
	return nil
}
