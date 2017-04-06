package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"os/user"
	"path"
	"strings"
)

type GoHookInfo struct {
	OpType     uint32
	Uid        uint32
	SubPid     uint32
	ObjPid     uint32
	SubPath    [264]byte
	ObjSrcPath [264]byte
	ObjDstPath [264]byte
}

type GoPerm struct {
	Perm uint32
}

type CacheValue struct {
	Perm       int
	StatusMode int
}

var GCacheTestReqAll int64 = 0
var GCacheTestReqFind int64 = 0

func getStatusString(status int) (str_stat string) {
	if status == 1 {
		return "开启"
	}
	return "关闭"
}

func MatchCacheProc(user, proc, obj_proc, op string) (in_cache, perm bool, err error) {
	in_cache = false
	return in_cache, perm, nil
}

func MatchProcPolicy(handle *RuleMemHandle, user, proc, obj_proc, op, rule_type string) (perm bool, err error) {
	obj_group, ok := handle.RObjProc[obj_proc]
	if ok == false {
		return true, nil // 客体未关联组 : 允许
	}

	user_group, ok := handle.RUser[user]
	if ok == false {
		user_group = "所有用户" // 客体有组，用户无组 : 尝试默认组
	}

	proc_group, ok := handle.RProc[proc]
	if ok == false {
		proc_group = "所有进程" // 客体有组，用户有组，程序无组 : 尝试默认组
	}

	perm_str := "进程对象_" + user_group + "_" + proc_group + "_" + obj_group + "_" + op
	_, ok = handle.RPerm[perm_str]
	if ok == false {
		// add log
		LogInsertEvent(rule_type, getStatusString(handle.StatusProc), "进程", op, user, proc, obj_proc, "拦截")

		if handle.StatusProc == 0 {
			return true, nil // 维护模式 : 允许
		}
		return false, nil // 客体有组，用户有组，程序有组，无权限 : 拒绝
	}

	return true, nil // 客体有组，用户有组，程序有组，有权限 : 允许
}

// 匹配进程
func MatchProc(user, proc, obj_proc, op string) (perm bool, err error) {
	perm = true

	// cache 检测
	in_cache, perm, err := MatchCacheProc(user, proc, obj_proc, op)
	if err == nil && in_cache == true {
		return perm, nil
	}

	// 自保护策略
	LockGMemRuleSelfHandle.Lock()
	perm, err = MatchProcPolicy(&GMemRuleSelfHandle, user, proc, obj_proc, op, "自我保护")
	LockGMemRuleSelfHandle.Unlock()
	if err != nil {
		return perm, err
	}
	if perm == false {
		return perm, nil
	}

	// 基础安全保护策略
	LockGMemRuleSafeHandle.Lock()
	perm, err = MatchProcPolicy(&GMemRuleSafeHandle, user, proc, obj_proc, op, "基础安全")
	LockGMemRuleSafeHandle.Unlock()
	if err != nil {
		return perm, err
	}
	if perm == false {
		return perm, nil
	}

	// 用户策略
	LockGMemRuleUserHandle.Lock()
	perm, err = MatchProcPolicy(&GMemRuleUserHandle, user, proc, obj_proc, op, "用户策略")
	LockGMemRuleUserHandle.Unlock()

	return perm, nil
}

func MatchCacheNet(user, proc, obj_net, op string) (in_cache, perm bool, err error) {
	in_cache = false
	return in_cache, perm, nil
}

func MatchNetPolicy(handle *RuleMemHandle, user, proc, obj_net, op, rule_type string) (perm bool, err error) {
	obj_group, ok := handle.RObjNet[obj_net]
	if ok == false {
		return true, nil // 客体未关联组 : 允许
	}

	user_group, ok := handle.RUser[user]
	if ok == false {
		user_group = "所有用户" // 客体有组，用户无组 : 尝试默认组
	}

	proc_group, ok := handle.RProc[proc]
	if ok == false {
		proc_group = "所有进程" // 客体有组，用户有组，程序无组 : 尝试默认组
	}

	perm_str := "网络对象_" + user_group + "_" + proc_group + "_" + obj_group + "_" + op
	_, ok = handle.RPerm[perm_str]
	if ok == false {
		// add log
		LogInsertEvent(rule_type, getStatusString(handle.StatusNet), "网络", op, user, proc, obj_net, "拦截")
		if handle.StatusNet == 0 {
			return true, nil // 维护模式 : 允许
		}
		return false, nil // 客体有组，用户有组，程序有组，无权限 : 拒绝
	}

	return true, nil // 客体有组，用户有组，程序有组，有权限 : 允许
}

// 匹配网络
func MatchNet(user, proc, obj_net, op string) (perm bool, err error) {
	perm = true

	// cache 检测
	in_cache, perm, err := MatchCacheNet(user, proc, obj_net, op)
	if err == nil && in_cache == true {
		return perm, nil
	}

	// 自保护策略
	LockGMemRuleSelfHandle.Lock()
	perm, err = MatchNetPolicy(&GMemRuleSelfHandle, user, proc, obj_net, op, "自保护")
	LockGMemRuleSelfHandle.Unlock()
	if err != nil {
		return perm, err
	}
	if perm == false {
		return perm, nil
	}

	// 基础安全保护策略
	LockGMemRuleSafeHandle.Lock()
	perm, err = MatchNetPolicy(&GMemRuleSafeHandle, user, proc, obj_net, op, "基础安全")
	LockGMemRuleSafeHandle.Unlock()
	if err != nil {
		return perm, err
	}
	if perm == false {
		return perm, nil
	}

	// 用户策略
	LockGMemRuleUserHandle.Lock()
	perm, err = MatchNetPolicy(&GMemRuleUserHandle, user, proc, obj_net, op, "用户策略")
	LockGMemRuleUserHandle.Unlock()

	return perm, nil
}

func MatchCacheFile(user, proc, obj_file, op string) (in_cache, perm bool, err error) {
	in_cache = false
	return in_cache, perm, nil
}

func MatchFileSplitPath(obj_file string) (fs []string) {
	// 路径自己
	fs = append(fs, obj_file)

	base := path.Base(obj_file)
	dir := path.Dir(obj_file)

	// 跳过已经是根目录或者异常
	if dir == "/" || dir == "." {
		return fs
	}

	exts := strings.Split(base, ".")
	if len(exts) > 1 {
		ext := exts[len(exts)-1]
		if ext != "" {
			// 扩展名
			fs = append(fs, dir+"/*."+ext)
		}
	}

	// 上层目录
	fs = append(fs, dir)
	for i := 0; i < 32; i++ {
		new_dir := path.Dir(dir)
		if new_dir == "/" || new_dir == "." {
			return fs
		} else {
			fs = append(fs, new_dir)
			dir = new_dir
		}
	}
	return fs
}

func MatchFilePolicy(handle *RuleMemHandle, user, proc, op, rule_type string, obj_files []string) (perm bool, err error) {
	user_group, ok := handle.RUser[user]
	if ok == false {
		user_group = "所有用户" // 客体有组，用户无组 : 尝试默认组
	}

	proc_group, ok := handle.RProc[proc]
	if ok == false {
		proc_group = "所有进程" // 客体有组，用户有组，程序无组 : 尝试默认组
	}

	for _, obj_file := range obj_files {
		obj_group, ok := handle.RObjFile[obj_file]
		if ok == false {
			continue // 客体未关联组 : 允许
		}

		perm_str := "文件对象_" + user_group + "_" + proc_group + "_" + obj_group + "_" + op
		_, ok = handle.RPerm[perm_str]
		if ok == false {
			// add log
			LogInsertEvent(rule_type, getStatusString(handle.StatusFile), "文件", op, user, proc, obj_file, "拦截")

			if handle.StatusFile == 0 {
				//return true, nil // 维护模式 : 允许
				continue
			}
			return false, nil // 客体有组，用户有组，程序有组，无权限 : 拒绝
		}
	}

	return true, nil // 客体有组，用户有组，程序有组，有权限 : 允许
}

// 匹配文件
func MatchFile(user, proc, obj_file, op string) (perm bool, err error) {
	// cache 检测
	in_cache, perm, err := MatchCacheNet(user, proc, obj_file, op)
	if err == nil && in_cache == true {
		return perm, nil
	}

	// 文件路径拆分
	obj_fs := MatchFileSplitPath(obj_file)

	// 自保护策略
	LockGMemRuleSelfHandle.Lock()
	perm, err = MatchFilePolicy(&GMemRuleSelfHandle, user, proc, op, "自保护", obj_fs)
	LockGMemRuleSelfHandle.Unlock()
	if err != nil {
		return perm, err
	}
	if perm == false {
		return perm, nil
	}

	// 基础安全保护策略
	LockGMemRuleSafeHandle.Lock()
	perm, err = MatchFilePolicy(&GMemRuleSafeHandle, user, proc, op, "基础安全", obj_fs)
	LockGMemRuleSafeHandle.Unlock()
	if err != nil {
		return perm, err
	}
	if perm == false {
		return perm, nil
	}

	// 用户策略
	LockGMemRuleUserHandle.Lock()
	perm, err = MatchFilePolicy(&GMemRuleUserHandle, user, proc, op, "用户策略", obj_fs)
	LockGMemRuleUserHandle.Unlock()

	return perm, nil
}

// 匹配 设置时间
func MatchSetTime(user, proc, obj_src, obj_dst, op string) (perm bool, err error) {
	LockGMemRuleSpecialHandle.Lock()
	if GMemRuleSpecialHandle.StatusSetTime == 1 {
		perm = false
		// add log
		LogInsertEvent("特殊资源", getStatusString(GMemRuleSpecialHandle.StatusMode), "设置时间", op, user, proc, obj_src, "拦截")
		if GMemRuleSpecialHandle.StatusMode == 0 {
			perm = true // 维护模式 : 允许
		}
	} else {
		perm = true
	}
	LockGMemRuleSpecialHandle.Unlock()

	return perm, nil
}

// 匹配 关机
func MatchShutDown(user, proc, obj_src, op string) (perm bool, err error) {
	LockGMemRuleSpecialHandle.Lock()
	if GMemRuleSpecialHandle.StatusShutDown == 1 {
		perm = false
		// add log
		LogInsertEvent("特殊资源", getStatusString(GMemRuleSpecialHandle.StatusMode), "关机", op, user, proc, obj_src, "拦截")
		if GMemRuleSpecialHandle.StatusMode == 0 {
			perm = true // 维护模式 : 允许
		}
	} else {
		perm = true
	}
	LockGMemRuleSpecialHandle.Unlock()
	return perm, nil
}

// 匹配 USB
func MatchUSB(user, proc, obj_src, op string) (perm bool, err error) {
	LockGMemRuleSpecialHandle.Lock()
	if GMemRuleSpecialHandle.StatusUsb == 1 {
		perm = false
		// add log
		LogInsertEvent("特殊资源", getStatusString(GMemRuleSpecialHandle.StatusMode), "USB", op, user, proc, obj_src, "拦截")
		if GMemRuleSpecialHandle.StatusMode == 0 {
			perm = true // 维护模式 : 允许
		}
	} else {
		perm = true
	}
	LockGMemRuleSpecialHandle.Unlock()

	return perm, nil
}

// 匹配 CDROM
func MatchCdRom(user, proc, obj_src, op string) (perm bool, err error) {
	LockGMemRuleSpecialHandle.Lock()
	if GMemRuleSpecialHandle.StatusCdrom == 1 {
		perm = false
		// add log
		LogInsertEvent("特殊资源", getStatusString(GMemRuleSpecialHandle.StatusMode), "CDROM", op, user, proc, obj_src, "拦截")
		if GMemRuleSpecialHandle.StatusMode == 0 {
			perm = true // 维护模式 : 允许
		}
	} else {
		perm = true
	}
	LockGMemRuleSpecialHandle.Unlock()

	return perm, nil
}

func MatchAll(hook *GoHookInfo) (perm bool, err error) {
	var space [1]byte
	var trim string = string(space[0:1])
	perm = true

	SubPath := string(bytes.TrimRight(hook.SubPath[0:264], trim))

	// 超级进程
	LockGMemRuleSuperHandle.Lock()
	_, ok := GMemRuleSuperHandle[SubPath]
	if ok {
		LockGMemRuleSuperHandle.Unlock()
		return true, nil
	}
	LockGMemRuleSuperHandle.Unlock()

	User, err := user.LookupId(fmt.Sprintf("%d", hook.Uid))
	if err != nil {
		return perm, err
	}

	UserName := User.Username
	ObjSrcPath := string(bytes.TrimRight(hook.ObjSrcPath[0:264], trim))
	ObjDstPath := string(bytes.TrimRight(hook.ObjDstPath[0:264], trim))

	/*
		// 测试cache效果
		key := "PolicyModule" + "_" + UserName + "_" + SubPath + "_" + ObjSrcPath + "_" + "eType" + "_" + "OP"
		LockCacheRule.Lock()
		GCacheTestReqAll += 1
		_, ok = GCacheRule.CacheGet(key)
		if ok {
			// 找到
			GCacheTestReqFind += 1
		} else {
			GCacheRule.CacheAdd(key, &CacheValue{Perm: 1, StatusMode: 1})
		}

		if GCacheTestReqAll%20 == 0 {
			fmt.Println("ReqAll=", GCacheTestReqAll, "CacheFind=", GCacheTestReqFind, "CacheSize=", GCacheRule.CacheLen())
		}
		LockCacheRule.Unlock()
		fmt.Println("-------------------------")
		fmt.Printf("[%s], Sub=%s, ObjSrc=%s, ObjDst=%s, User=%s, Op=%d, Perm=%d\n", time.Now().Format("2006-01-02 15:04:05"), SubPath, ObjSrcPath, ObjDstPath, UserName, hook.OpType, perm)
		return perm, nil
		// 测试结束
	*/
	switch hook.OpType {
	case 1, 2:
		fmt.Println("文件_读：", hook.OpType)
		perm, err = MatchFile(UserName, SubPath, ObjSrcPath, "只读")
	case 8: // rename
		fmt.Println("文件_移动：", hook.OpType)
		perm, err = MatchFile(UserName, SubPath, ObjSrcPath, "读写")
		if err == nil && perm == false {
			break
		}
		perm, err = MatchFile(UserName, SubPath, ObjDstPath, "读写")

	case 3, 4, 5, 6, 7, 9, 10, 11:
		fmt.Println("文件_写：", hook.OpType)
		perm, err = MatchFile(UserName, SubPath, ObjSrcPath, "读写")
	case 42:
		fmt.Println("进程_结束：", hook.OpType)
		perm, err = MatchProc(UserName, SubPath, ObjSrcPath, "进程结束")
	case 45:
		fmt.Println("进程_执行：", hook.OpType)
		perm, err = MatchProc(UserName, SubPath, ObjSrcPath, "进程执行")
	case 51:
		fmt.Println("时间_设置：", hook.OpType)
		perm, err = MatchSetTime(UserName, SubPath, ObjSrcPath, ObjDstPath, "设置时间")
	case 61:
		fmt.Println("网络_连接：", hook.OpType)
		perm, err = MatchNet(UserName, SubPath, ObjSrcPath, "网络连接")
	case 62:
		fmt.Println("网络_监听：", hook.OpType)
		perm, err = MatchNet(UserName, SubPath, ObjSrcPath, "网络监听")
	default:
		fmt.Println("错误类型：", hook.OpType)

	}

	fmt.Printf("Sub=%s, ObjSrc=%s, ObjDst=%s, User=%s, Op=%d, Perm=%d\n", SubPath, ObjSrcPath, ObjDstPath, UserName, hook.OpType, perm)

	return perm, nil
}

// 接收新客户端 - 回调
func RuleMatchNewClient(c *TCPClient) {
	c.RecvSize = GRuleMatchTCPMsgRecvSize
	c.SendSize = GRuleMatchTCPMsgSendSize
	GHandleFileRunLog.Println("[INFO]", "TCPClientNew:", c.Conn.RemoteAddr().String())
}

// 接收客户端消息 - 回调
func RuleMatchNewMessage(c *TCPClient, message []byte, tid int) (ifClose bool, err error) {
	var perm GoPerm
	var hook GoHookInfo

	ifClose = false
	sendbuf := new(bytes.Buffer)
	perm.Perm = 0

	buf := bytes.NewReader(message)
	err = binary.Read(buf, binary.LittleEndian, &hook)
	if err == nil {
		// match
		b_perm, err := MatchAll(&hook)
		if err == nil {
			if b_perm == true {
				perm.Perm = 0 // allow
			} else {
				perm.Perm = 1 // forbid
			}
		}
	} else {
		return true, err
	}

	err = binary.Write(sendbuf, binary.LittleEndian, perm)
	if err != nil {
		return true, err
	}

	err = c.SendBytes(sendbuf.Bytes())
	if err != nil {
		return true, err
	}

	return ifClose, nil
}

// 客户端关闭 - 回调
func RuleMatchClientClose(c *TCPClient, err error) {
	GHandleFileRunLog.Println("[INFO]", "TCPClientClose:", c.Conn.RemoteAddr().String(), err)
}

// 启动TCP服务
func RuleMatchInitTCPServer(run_in_thread bool) {
	GHandleFileRunLog.Println("[INFO]", "TCPServerStart:", GRuleMatchTCPAddr)
	server := TCPServerNew(GRuleMatchTCPAddr)
	server.OnNewClient(RuleMatchNewClient)
	server.OnNewMessage(RuleMatchNewMessage)
	server.OnClientConnectionClosed(RuleMatchClientClose)
	if run_in_thread == true {
		go server.Listen()
	} else {
		server.Listen()
	}
}
