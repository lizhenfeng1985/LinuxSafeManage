# -*- coding: utf-8 -*-

import urllib
import urllib2
import httplib
import ssl
import socket
import json

'''
 HTTP GET
'''
def HttpGet(url, params, timeout=3):
    data = urllib.urlencode(params)
    try:
        f = urllib2.urlopen("%s?%s" % (url, data), timeout=timeout)
        response = f.read()
        f.close()
        rt = json.loads(response)
        return [0, rt]
    except Exception, e:
        return [-1, str(e)]

'''
 HTTP POST
'''
def HttpPost(url, params, timeout=3):
    data = urllib.urlencode(params)
    try:
        f = urllib2.urlopen(url, data=data, timeout=timeout)
        response = f.read()
        f.close()
        rt = json.loads(response)
        return [0, rt]
    except Exception, e:
        return [-1, str(e)]


'''
 patch for change SSL_VER to PROTOCOL_SSLv3
'''
def connect_patched(self):
    "Connect to a host on a given (SSL) port."
    sock = socket.create_connection((self.host, self.port),self.timeout, self.source_address)
    if self._tunnel_host:
        self.sock = sock
        self._tunnel()
    self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file,ssl_version=ssl.PROTOCOL_SSLv3)

'''
 HTTPS GET
'''
def HttpsGet(url, params, timeout=3):
    httplib.HTTPSConnection.connect = connect_patched   
    data = urllib.urlencode(params)
    try:
        f = urllib2.urlopen("%s?%s" % (url, data), timeout=timeout)
        response = f.read()
        f.close()
        rt = json.loads(response)
        return [0, rt]
    except Exception, e:
        return [-1, str(e)]

'''
 HTTPS POST
'''
def HttpsPost(url, params, timeout=3):
    httplib.HTTPSConnection.connect = connect_patched  
    data = urllib.urlencode(params)
    try:
        f = urllib2.urlopen(url, data=data, timeout=timeout)
        response = f.read()
        f.close()
        rt = json.loads(response)
        return [0, rt]
    except Exception, e:
        return [-1, str(e)]


def print_rt(rt):
    for k, v in rt.items():
        print k, v
        
def testLogin():
    url = 'https://127.0.0.1:9001/login/Admin'
    param = {'Password':'123456'}

    rt = HttpsPost(url, param)
    print_rt(rt[1])

    
if __name__ == '__main__':
    testLogin()
