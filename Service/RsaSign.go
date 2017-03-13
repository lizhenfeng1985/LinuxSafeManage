package main

import (
	"crypto"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha1"
	"crypto/x509"
	"encoding/base64"
	"encoding/pem"
	"errors"
	"io/ioutil"
	"os"
	"runtime"
	"strconv"
	"strings"
	"time"
)

const (
	GSerialPubKey   string = "./license/pub.key"
	GSerialLicense  string = "./license/lic"
	GSerialCodeFile string = "/root/.LinuxManageInfo"
)

func RsaCreateKeys() (priKey, pubKey string, err error) {
	privateKey, err := rsa.GenerateKey(rand.Reader, 1024)
	if err != nil {
		return priKey, pubKey, err
	}

	derStream := x509.MarshalPKCS1PrivateKey(privateKey)
	block := &pem.Block{
		Type:  "RSA PRIVATE KEY",
		Bytes: derStream,
	}

	priKey = string(pem.EncodeToMemory(block))

	publicKey := &privateKey.PublicKey
	derPkix, err := x509.MarshalPKIXPublicKey(publicKey)
	if err != nil {
		return priKey, pubKey, err
	}
	block = &pem.Block{
		Type:  "RSA PUBLIC KEY",
		Bytes: derPkix,
	}

	pubKey = string(pem.EncodeToMemory(block))

	return priKey, pubKey, nil
}

func RsaSign(priKey, message string) (signature []byte, err error) {
	var h crypto.Hash

	block, _ := pem.Decode([]byte(priKey))
	if block == nil {
		return signature, err
	}
	priv, err := x509.ParsePKCS1PrivateKey(block.Bytes)
	if err != nil {
		return signature, err
	}

	hash := sha1.New()
	hash.Write([]byte(message))
	hashed := hash.Sum(nil)

	signature, err = rsa.SignPKCS1v15(rand.Reader, priv, h, hashed)
	if err != nil {
		return signature, err
	}

	return signature, nil
}

func RsaVerify(pubKey, message string, signature []byte) (err error) {
	var h crypto.Hash

	block, _ := pem.Decode([]byte(pubKey))
	if block == nil {
		return err
	}

	pubInterface, _ := x509.ParsePKIXPublicKey(block.Bytes)
	pub := pubInterface.(*rsa.PublicKey)

	hash := sha1.New()
	hash.Write([]byte(message))
	hashed := hash.Sum(nil)

	err = rsa.VerifyPKCS1v15(pub, h, hashed, signature)
	return err
}

func GetMachineCode() (code string, err error) {
	var info_path string
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
		code = string(datastr)
	} else {
		data, _ := ioutil.ReadFile(info_path)
		code = string(data)
	}

	if strings.Index(code, "lzf") < 0 ||
		strings.Index(code, "24324962@qq.com") < 0 ||
		strings.Index(code, "Date :") < 0 ||
		strings.Index(code, "Seq  :") < 0 ||
		strings.Index(code, "Warning") < 0 {
		os.Remove(info_path)
		goto re_create
	}
	return code, nil
}

func SerialCreate(priKey, code, validate string) (b64lic string, err error) {
	_, err = time.Parse("20060102", validate)
	if err != nil {
		return b64lic, errors.New("ValiDate format err.")
	}

	lic, err := RsaSign(priKey, code+validate)
	if err != nil {
		return b64lic, err
	}

	b64 := make([]byte, base64.StdEncoding.EncodedLen(len(lic)))
	base64.StdEncoding.Encode(b64, lic)

	return string(b64), err
}

func SerialRegister(b64_lic string) (err error) {
	lic := make([]byte, base64.StdEncoding.DecodedLen(len(b64_lic)))
	base64.StdEncoding.Decode(lic, []byte(b64_lic))

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
	sig := lic[8:len(lic)]

	if time.Now().Format("20060102") > validate {
		return errors.New("License Expired.")
	}

	err = RsaVerify(string(pubKey), string(code), sig)
	if err != nil {
		return errors.New("Wrong License.")
	}

	return ioutil.WriteFile(GSerialLicense, []byte(b64_lic), 0666)
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

	lic := make([]byte, base64.StdEncoding.DecodedLen(len(b64_lic)))
	base64.StdEncoding.Decode(lic, b64_lic)

	validate := string(lic[0:8])
	sig := lic[8:len(lic)]

	if time.Now().Format("20060102") > validate {
		return errors.New("License Expired.")
	}

	err = RsaVerify(string(pubKey), string(code), sig)
	if err != nil {
		return errors.New("Wrong License.")
	}

	return nil
}

/*
func test() {
	pri, _ := ioutil.ReadFile("./license/pri.key")
	code, _ := GetMachineCode()

	lic, err := SerialCreate(string(pri), string(code), "20170314")
	fmt.Println(err, lic)

	fmt.Println("SerialRegister:", SerialRegister(lic))

	fmt.Println("SerialVerify:", SerialVerify())

}
*/
