# -*- coding: utf-8 -*-
import sys
from http import *
from rule import *
from sendtcp import *

UID = 0
SUB_PID = 0
OBJ_PID = 0
OP_FILE_READ = 1
OP_FILE_SYMLINK = 2
OP_FILE_MKDIR = 3
OP_FILE_RMDIR = 4
OP_FILE_CREATE = 5
OP_FILE_TRUNCATE = 6
OP_FILE_UNLINK = 7
OP_FILE_RENAME = 8
OP_FILE_LINK = 9
OP_FILE_WRITE = 10
OP_FILE_RDWR = 11
OP_PROC_KILL = 42
OP_PROC_EXECUTE = 45
OP_TIME_SET = 51
OP_NET_CONNECT = 61
OP_NET_LISTEN = 62


def test_match_proc():
    SetRuleStatusUser(1)

    # op_type 42:kill  45:exe
    GroupAdd('highobjproc', 'obj_group_1')
    ObjProcAdd('obj_group_1', '/proc/obj_proc_1')

    r = TCPGetMesg(OP_PROC_EXECUTE, UID, SUB_PID, OBJ_PID, '/proc/sub.exe', '/proc/obj_proc_1', '')
    if r != 1:
        print "--Test:Failed:OP_PROC_EXECUTE Forbid", r
        return
    print "--Test:OK:OP_PROC_EXECUTE Forbid", r

    AddPerm('所有用户', '所有进程', 'obj_group_1', '进程对象', '进程执行')
    r = TCPGetMesg(OP_PROC_EXECUTE, UID, SUB_PID, OBJ_PID, '/proc/sub.exe', '/proc/obj_proc_1', '')
    if r != 0:
        print "--Test:Failed:OP_PROC_EXECUTE Allow", r
        return
    print "--Test:OK:OP_PROC_EXECUTE Allow", r

    #######
    r = TCPGetMesg(OP_PROC_KILL, UID, SUB_PID, OBJ_PID, '/proc/sub.exe', '/proc/obj_proc_1', '')
    if r != 1:
        print "--Test:Failed:OP_PROC_KILL Forbid", r
        return
    print "--Test:OK:OP_PROC_KILL Forbid", r

    AddPerm('所有用户', '所有进程', 'obj_group_1', '进程对象', '进程结束')
    r = TCPGetMesg(OP_PROC_KILL, UID, SUB_PID, OBJ_PID, '/proc/sub.exe', '/proc/obj_proc_1', '')
    if r != 0:
        print "--Test:Failed:OP_PROC_KILL Allow", r
        return
    print "--Test:OK:OP_PROC_KILL Allow", r

    ###
    GroupAdd('highproc', 'sub_group_1')
    ProcAdd('sub_group_1', '/proc/sub.exe')
    AddPerm('所有用户', 'sub_group_1', 'obj_group_1', '进程对象', '进程执行')
    r = TCPGetMesg(OP_PROC_KILL, UID, SUB_PID, OBJ_PID, '/proc/sub.exe', '/proc/obj_proc_1', '')
    if r != 1:
        print "--Test:Failed:OP_PROC_KILL Forbid", r
        return
    print "--Test:OK:OP_PROC_KILL Forbid", r

    AddPerm('所有用户', 'sub_group_1', 'obj_group_1', '进程对象', '进程结束')
    r = TCPGetMesg(OP_PROC_KILL, UID, SUB_PID, OBJ_PID, '/proc/sub.exe', '/proc/obj_proc_1', '')
    if r != 0:
        print "--Test:Failed:OP_PROC_KILL Allow", r
        return
    print "--Test:OK:OP_PROC_KILL Allow", r

    DelPerm('所有用户', '所有进程', 'obj_group_1', '进程对象', '进程执行')
    DelPerm('所有用户', 'sub_group_1', 'obj_group_1', '进程对象', '进程执行')
    DelPerm('所有用户', '所有进程', 'obj_group_1', '进程对象', '进程结束')
    return


if __name__ == '__main__':
    r = Login()
    if r != 0:
        sys.exit(0)
    test_match_proc()
