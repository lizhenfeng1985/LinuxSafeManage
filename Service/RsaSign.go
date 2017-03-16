package main

import (
	"crypto"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha1"
	"crypto/x509"
	"encoding/pem"
	"errors"
)

const (
	GSerialPubKey   string = "./license/pub.key"
	GSerialLicense  string = "./license/lic"
	GSerialCodeFile string = "/root/.LinuxManageInfo"
	GSerialDateSize int    = 136
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
