package main

import (
	"path"
	"strings"
)

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
		// add log
		return false, nil // 客体有组，用户无组 : 拒绝
	}

	proc_group, ok := handle.RProc[proc]
	if ok == false {
		// add log
		return false, nil // 客体有组，用户有组，程序无组 : 拒绝
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
		// add log
		return false, nil // 客体有组，用户无组 : 拒绝
	}

	proc_group, ok := handle.RProc[proc]
	if ok == false {
		// add log
		return false, nil // 客体有组，用户有组，程序无组 : 拒绝
	}

	perm_str := "进程对象_" + user_group + "_" + proc_group + "_" + obj_group + "_" + op
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

func MatchFilePolicy(handle *RuleMemHandle, user, proc, obj_file, op, rule_type string) (perm bool, err error) {
	obj_group, ok := handle.RObjFile[obj_file]
	if ok == false {
		return true, nil // 客体未关联组 : 允许
	}

	user_group, ok := handle.RUser[user]
	if ok == false {
		// add log
		return false, nil // 客体有组，用户无组 : 拒绝
	}

	proc_group, ok := handle.RProc[proc]
	if ok == false {
		// add log
		return false, nil // 客体有组，用户有组，程序无组 : 拒绝
	}

	perm_str := "进程对象_" + user_group + "_" + proc_group + "_" + obj_group + "_" + op
	_, ok = handle.RPerm[perm_str]
	if ok == false {
		// add log
		return false, nil // 客体有组，用户有组，程序有组，无权限 : 拒绝
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

	for _, fs := range obj_fs {
		// 自保护策略
		LockGMemRuleSelfrHandle.Lock()
		perm, err = MatchFilePolicy(&GMemRuleSelfHandle, user, proc, fs, op, "自保护")
		LockGMemRuleSelfrHandle.Unlock()
		if err != nil {
			return perm, err
		}
		if perm == false {
			return perm, nil
		}

		// 用户策略
		LockGMemRuleUserHandle.Lock()
		perm, err = MatchFilePolicy(&GMemRuleUserHandle, user, proc, fs, op, "用户策略")
		LockGMemRuleUserHandle.Unlock()
		if err != nil {
			return perm, err
		}
		if perm == false {
			return perm, nil
		}
	}

	return true, nil
}
