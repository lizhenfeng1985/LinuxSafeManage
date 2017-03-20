package main

import (
	"crypto"
	"crypto/md5"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha1"
	"crypto/x509"
	"encoding/base64"
	"encoding/hex"
	"encoding/pem"
	"errors"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"runtime"
	"strconv"
	"strings"
	"time"
)

const (
	GSerialPubKey      string = "./license/pub.key"
	GSerialLicense     string = "./license/lic"
	GSerialCodeFile    string = "/root/.LinuxManageInfo"
	GSerialDateSize    int    = 136
	GSerialCodeTest    string = "This is a test data, for sn."
	GSerialTypeDebug   int    = 1
	GSerialTypeRelease int    = 1
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
	block, _ := pem.Decode([]byte(priKey))
	if block == nil {
		return signature, errors.New("pem.Decode err")
	}
	priv, err := x509.ParsePKCS1PrivateKey(block.Bytes)
	if err != nil {
		return signature, err
	}

	hash := sha1.New()
	hash.Write([]byte(message))
	hashed := hash.Sum(nil)

	signature, err = rsa.SignPKCS1v15(rand.Reader, priv, crypto.SHA1, hashed)
	if err != nil {
		return signature, err
	}

	return signature, nil
}

func RsaVerify(pubKey, message string, signature []byte) (err error) {
	block, _ := pem.Decode([]byte(pubKey))
	if block == nil {
		return errors.New("pem.Decode err")
	}

	pubInterface, _ := x509.ParsePKIXPublicKey(block.Bytes)
	pub := pubInterface.(*rsa.PublicKey)

	hash := sha1.New()
	hash.Write([]byte(message))
	hashed := hash.Sum(nil)

	err = rsa.VerifyPKCS1v15(pub, crypto.SHA1, hashed, signature)
	return err
}

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

func SerialCreate(lic_type int, priKey, code, validate string) (b64lic string, err error) {
	var lic []byte
	_, err = time.Parse("20060102", validate)
	if err != nil {
		return b64lic, errors.New("ValiDate format err.")
	}

	if lic_type == GSerialTypeDebug {
		code = GSerialCodeTest
	}

	lic, err = RsaSign(priKey, validate+code)
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
		// try test license
		err = RsaVerify(string(pubKey), validate+string(GSerialCodeTest), sig)
		if err != nil {
			return err
		}
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
		// try test license
		err = RsaVerify(string(pubKey), validate+string(GSerialCodeTest), sig)
		if err != nil {
			return errors.New("Wrong License.")
		}
	}

	return nil
}

func SerialVerifyLic(lic_string string) (err error) {
	pubKey, err := ioutil.ReadFile(GSerialPubKey)
	if err != nil {
		return err
	}

	code, err := GetMachineCode()
	if err != nil {
		return err
	}

	b64_lic := []byte(lic_string)
	lic := make([]byte, base64.RawStdEncoding.DecodedLen(len(b64_lic)))
	base64.RawStdEncoding.Decode(lic, b64_lic)

	validate := string(lic[0:8])
	sig := lic[8:GSerialDateSize]

	if time.Now().Format("20060102") > validate {
		return errors.New("License Expired.")
	}

	err = RsaVerify(string(pubKey), validate+string(code), sig)
	if err != nil {
		// try test license
		err = RsaVerify(string(pubKey), validate+string(GSerialCodeTest), sig)
		if err != nil {
			return errors.New("Wrong License.")
		}
	}

	return nil
}

func usage() {
	name := filepath.Base(os.Args[0])
	fmt.Println("Usage:")
	fmt.Printf("  %s  [debug|release]  [Code]  [ValidDate]\n\n", name)
	fmt.Println("Example:")
	fmt.Printf("  %s  debug   e6cfa33976fe431a90668b6deee48e6f  20171201\n", name)
	fmt.Printf("  %s  release e6cfa33976fe431a90668b6deee48e6f  20171201\n\n", name)
}

func main() {
	/*
		os.Args = append(os.Args, "debug")
		os.Args = append(os.Args, "e6cfa33976fe431a90668b6deee48e6f")
		os.Args = append(os.Args, "20170430")
	*/
	var lic string
	var err error
	if len(os.Args) != 4 {
		usage()
		return
	}

	pri, _ := ioutil.ReadFile("./license/pri.key")
	lic_type := os.Args[1]
	code := os.Args[2]
	validate := os.Args[3]

	if lic_type == "debug" {
		lic, err = SerialCreate(GSerialTypeDebug, string(pri), code, validate)
	} else {
		lic, err = SerialCreate(GSerialTypeRelease, string(pri), code, validate)
	}
	if err != nil {
		fmt.Println("Failed:", err)
		return
	}

	fmt.Println("---------------------------------------")
	fmt.Println("Type     : ", lic_type)
	fmt.Println("Code     : ", code)
	fmt.Println("SN       : ", lic)
	fmt.Println("ValiDate : ", validate)
	fmt.Println("SnVerify : ", SerialVerifyLic(lic))
	fmt.Println("---------------------------------------")
}
