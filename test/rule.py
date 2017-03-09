# -*- coding: utf-8 -*-
import sys
from http import *


URL = 'https://127.0.0.1:9001'
global Tokey

def Login():
    global Tokey
    url = URL + "/login/Admin"
    data = {
        'Password'    : '123456',
        'LocalIPPort' : '127.0.0.1:9001',
        'CenterIPPort': '127.0.0.1:9003',
    }
    param = {'Data' : json.dumps(data)}        
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'Login:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        Tokey = res['Tokey']
        print 'Login:OK', Tokey
        return 0
    else:
        print 'Login:Failed:' + res['ErrMsg']
        return -1

# highuser|highproc|highobjproc|highobjnet|highobjfile
def GroupAdd(g_uri, group):
    global Tokey
    url = URL + "/%s/groupadd/Admin" % g_uri
    data = {
        'Tokey'   : Tokey,
        'Group'   : group
    }
    param = {'Data' : json.dumps(data)}        
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'GroupAdd:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        print 'GroupAdd:OK'
        return 0
    else:
        print 'GroupAdd:Failed:' + res['ErrMsg']
        return -1

def UserAdd(group, uname):
    global Tokey
    url = URL + "/highuser/add/Admin"
    data = {
        'Tokey'   : Tokey,
        'Group'   : group,
        'User'    : uname,
    }
    param = {'Data' : json.dumps(data)}        
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'UserAdd:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        print 'UserAdd:OK'
        return 0
    else:
        print 'UserAdd:Failed:' + res['ErrMsg']
        return -1


def ProcAdd(group, proc):
    global Tokey
    url = URL + "/highproc/add/Admin"
    data = {
        'Tokey'   : Tokey,
        'Group'   : group,
        'Proc'    : proc,
    }
    param = {'Data' : json.dumps(data)}        
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'ProcAdd:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        print 'ProcAdd:OK'
        return 0
    else:
        print 'ProcAdd:Failed:' + res['ErrMsg']
        return -1

def ObjProcAdd(group, proc):
    global Tokey
    url = URL + "/highobjproc/add/Admin"
    data = {
        'Tokey'   : Tokey,
        'Group'   : group,
        'ObjProc'    : proc,
    }
    param = {'Data' : json.dumps(data)}        
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'ObjProcAdd:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        print 'ObjProcAdd:OK'
        return 0
    else:
        print 'ObjProcAdd:Failed:' + res['ErrMsg']
        return -1

def ObjNetAdd(group, obj_net):
    global Tokey
    url = URL + "/highobjnet/add/Admin"
    data = {
        'Tokey'   : Tokey,
        'Group'   : group,
        'ObjNet'    : obj_net,
    }
    param = {'Data' : json.dumps(data)}        
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'ObjNetAdd:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        print 'ObjNetAdd:OK'
        return 0
    else:
        print 'ObjNetAdd:Failed:' + res['ErrMsg']
        return -1

def ObjFileAdd(group, obj_file):
    global Tokey
    url = URL + "/highobjfile/add/Admin"
    data = {
        'Tokey'   : Tokey,
        'Group'   : group,
        'ObjFile'    : obj_file,
    }
    param = {'Data' : json.dumps(data)}        
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'ObjFileAdd:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        print 'ObjFileAdd:OK'
        return 0
    else:
        print 'ObjFileAdd:Failed:' + res['ErrMsg']
        return -1


# obj_type:文件对象|进程对象|网络对象
# perm:只读|读写|进程执行|进程结束|网络监听|网络连接
def AddPerm(g_user, g_proc, g_obj, obj_type, perm):
    global Tokey
    url = URL + "/highperm/add/Admin"
    data = {
        'Tokey'   : Tokey,
        'UserGroup'   : g_user,
        'ProcGroup'    : g_proc,
        'ObjGroup' : g_obj,
        'ObjType' : obj_type,
        'Perm' : perm,
        'Mode' : '启用'
    }
    param = {'Data' : json.dumps(data)}        
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'AddPerm:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        print 'AddPerm:OK'
        return 0
    else:
        print 'AddPerm:Failed:' + res['ErrMsg']
        return -1
    
def DelPerm(g_user, g_proc, g_obj, obj_type, perm):
    global Tokey
    url = URL + "/highperm/del/Admin"
    data = {
        'Tokey'   : Tokey,
        'UserGroup'   : g_user,
        'ProcGroup'    : g_proc,
        'ObjGroup' : g_obj,
        'ObjType' : obj_type,
        'Perm' : perm
    }
    param = {'Data' : json.dumps(data)}
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'DelPerm:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        print 'DelPerm:OK'
        return 0
    else:
        print 'DelPerm:Failed:' + res['ErrMsg']
        return -1


def SetRuleStatusSelf(status):
    global Tokey
    url = URL + "/statself/set/Admin"
    data = {
        'Tokey': Tokey,
        'Mode': status,
    }
    param = {'Data': json.dumps(data)}
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'SetRuleStatus:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        print 'SetRuleStatus:OK'
        return 0
    else:
        print 'SetRuleStatus:Failed:' + res['ErrMsg']
        return -1

def SetRuleStatusUser(status):
    global Tokey
    url = URL + "/statuser/set/Admin"
    data = {
        'Tokey': Tokey,
        'Mode': status,
    }
    param = {'Data': json.dumps(data)}
    rt = HttpsPost(url, param)
    if rt[0] != 0:
        print 'SetRuleStatus:Failed:' + rt[1]
        return -1
    res = rt[1]
    if res['Status'] == 0:
        print 'SetRuleStatus:OK'
        return 0
    else:
        print 'SetRuleStatus:Failed:' + res['ErrMsg']
        return -1