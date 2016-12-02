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
		return false, nil // 客体有组，用户有组，程序有组，无权限 : 拒绝
	}

	return true, nil // 客体有组，用户有组，程序有组，有权限 : 允许
}

// 匹配进程
func MatchProc(user, proc, obj_proc, op string) (perm bool, err error) {
	perm = true
	// 超级进程
	LockGMemRuleSuperHandle.Lock()
	_, ok := GMemRuleSuperHandle[proc]
	if ok {
		return true, nil
	}
	LockGMemRuleSuperHandle.Unlock()

	// cache 检测
	in_cache, perm, err := MatchCacheProc(user, proc, obj_proc, op)
	if err == nil && in_cache == true {
		return perm, nil
	}

	// 自保护策略
	LockGMemRuleSelfrHandle.Lock()
	perm, err = MatchProcPolicy(&GMemRuleSelfHandle, user, proc, obj_proc, op, "自保护")
	LockGMemRuleSelfrHandle.Unlock()
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
		return false, nil // 客体有组，用户有组，程序有组，无权限 : 拒绝
	}

	return true, nil // 客体有组，用户有组，程序有组，有权限 : 允许
}

// 匹配网络
func MatchNet(user, proc, obj_net, op string) (perm bool, err error) {
	perm = true
	// 超级进程
	LockGMemRuleSuperHandle.Lock()
	_, ok := GMemRuleSuperHandle[proc]
	if ok {
		return true, nil
	}
	LockGMemRuleSuperHandle.Unlock()

	// cache 检测
	in_cache, perm, err := MatchCacheNet(user, proc, obj_net, op)
	if err == nil && in_cache == true {
		return perm, nil
	}

	// 自保护策略
	LockGMemRuleSelfrHandle.Lock()
	perm, err = MatchNetPolicy(&GMemRuleSelfHandle, user, proc, obj_net, op, "自保护")
	LockGMemRuleSelfrHandle.Unlock()
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
			return false, nil // 客体有组，用户有组，程序有组，无权限 : 拒绝
		}
	}

	return true, nil // 客体有组，用户有组，程序有组，有权限 : 允许
}

// 匹配文件
func MatchFile(user, proc, obj_file, op string) (perm bool, err error) {
	// 超级进程
	LockGMemRuleSuperHandle.Lock()
	_, ok := GMemRuleSuperHandle[proc]
	if ok {
		return true, nil
	}
	LockGMemRuleSuperHandle.Unlock()

	// cache 检测
	in_cache, perm, err := MatchCacheNet(user, proc, obj_file, op)
	if err == nil && in_cache == true {
		return perm, nil
	}

	// 文件路径拆分
	obj_fs := MatchFileSplitPath(obj_file)

	// 自保护策略
	LockGMemRuleSelfrHandle.Lock()
	perm, err = MatchFilePolicy(&GMemRuleSelfHandle, user, proc, op, "自保护", obj_fs)
	LockGMemRuleSelfrHandle.Unlock()
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

func MatchAll(hook *GoHookInfo) (perm bool, err error) {
	var space [1]byte
	var trim string = string(space[0:1])
	perm = true

	//User, err := user.LookupId(fmt.Sprintf("%d", hook.Uid))
	User, err := user.LookupId("S-1-5-21-4019211918-2684473899-631832799-1000")
	if err != nil {
		return perm, err
	}

	UserName := User.Username
	SubPath := string(bytes.TrimRight(hook.SubPath[0:264], trim))
	ObjSrcPath := string(bytes.TrimRight(hook.ObjSrcPath[0:264], trim))
	ObjDstPath := string(bytes.TrimRight(hook.ObjDstPath[0:264], trim))

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
	case 61:
		fmt.Println("网络_连接：", hook.OpType)
		perm, err = MatchNet(UserName, SubPath, ObjSrcPath, "网络连接")
	case 62:
		fmt.Println("网络_监听：", hook.OpType)
		perm, err = MatchNet(UserName, SubPath, ObjSrcPath, "网络监听")
	default:
		fmt.Println("错误类型：", hook.OpType)

	}
	fmt.Println(perm, hook.OpType, UserName, SubPath, ObjSrcPath, ObjDstPath)

	return perm, nil
}

// 接收新客户端 - 回调
func RuleMatchNewClient(c *TCPClient) {
	c.RecvSize = GRuleMatchTCPMsgRecvSize
	c.SendSize = GRuleMatchTCPMsgSendSize
	GLogRunHandle.Println("[INFO]", "TCPClientNew:", c.Conn.RemoteAddr().String())
}

// 接收客户端消息 - 回调
func RuleMatchNewMessage(c *TCPClient, message []byte, tid int) {
	var perm GoPerm
	var hook GoHookInfo

	sendbuf := new(bytes.Buffer)
	perm.Perm = 0

	buf := bytes.NewReader(message)
	err := binary.Read(buf, binary.LittleEndian, &hook)
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
	}

	binary.Write(sendbuf, binary.LittleEndian, perm)
	c.SendBytes(sendbuf.Bytes())
}

// 客户端关闭 - 回调
func RuleMatchClientClose(c *TCPClient, err error) {
	GLogRunHandle.Println("[INFO]", "TCPClientClose:", c.Conn.RemoteAddr().String(), err)
}

// 启动TCP服务
func RuleMatchInitTCPServer(run_in_thread bool) {
	GLogRunHandle.Println("[INFO]", "TCPServerStart:", GRuleMatchTCPAddr)
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
