package main

import "database/sql"

type RuleUser map[string]string    // 用户名 - 组名
type RuleProc map[string]string    // 进程名 - 组名
type RuleObjProc map[string]string // 客体进程 - 组名
type RuleObjNet map[string]string  // 客体网络 - 组名
type RuleObjFile map[string]string // 客体文件 - 组名
type RulePerm map[string]int       // string(类型+用户组+主体组+客体组+权限) - 0

type RuleMemHandle struct {
	RUser      RuleUser
	RProc      RuleProc
	RObjProc   RuleObjProc
	RObjNet    RuleObjNet
	RObjFile   RuleObjFile
	RPerm      RulePerm
	StatusProc int
	StatusFile int
	StatusNet  int
}

type RuleSpecialMemHandle struct {
	StatusMode     int
	StatusSetTime  int
	StatusShutDown int
	StatusUsb      int
	StatusCdrom    int
}

func MemRuleInitRuleSuper() (err error) {
	procs, err := DBSuperProcGet()
	if err != nil {
		return err
	}

	handle := make(map[string]int)
	for _, proc := range procs {
		handle[proc] = 0
	}

	LockGMemRuleSuperHandle.Lock()
	GMemRuleSuperHandle = handle
	LockGMemRuleSuperHandle.Unlock()
	return nil
}

func MemRuleInitRule(db *sql.DB) (rh RuleMemHandle, err error) {
	rh.RUser = make(RuleUser)
	rh.RProc = make(RuleProc)
	rh.RObjProc = make(RuleObjProc)
	rh.RObjNet = make(RuleObjNet)
	rh.RObjFile = make(RuleObjFile)
	rh.RPerm = make(RulePerm)

	// 获取用户组 - 用户
	user_groups, err := DBHighUserGroupSearch(db)
	if err != nil {
		return rh, err
	}

	for _, group := range user_groups {
		users, _, err := DBHighUserSearch(db, group, 0, 256)
		if err != nil {
			return rh, err
		}
		for _, user := range users {
			rh.RUser[user] = group
		}
	}

	// 获取进程组 - 进程
	groups, err := DBHighProcGroupSearch(db)
	if err != nil {
		return rh, err
	}

	for _, group := range groups {
		procs, _, err := DBHighProcSearch(db, group, 0, 256)
		if err != nil {
			return rh, err
		}
		for _, proc := range procs {
			rh.RProc[proc] = group
		}
	}

	// 获取客体进程组 - 进程
	groups, err = DBHighObjProcGroupSearch(db)
	if err != nil {
		return rh, err
	}

	for _, group := range groups {
		objprocs, _, err := DBHighObjProcSearch(db, group, 0, 256)
		if err != nil {
			return rh, err
		}
		for _, proc := range objprocs {
			rh.RObjProc[proc] = group
		}
	}

	// 获取客体网络组 - 网络
	groups, err = DBHighObjNetGroupSearch(db)
	if err != nil {
		return rh, err
	}

	for _, group := range groups {
		objnets, _, err := DBHighObjNetSearch(db, group, 0, 256)
		if err != nil {
			return rh, err
		}
		for _, objnet := range objnets {
			rh.RObjNet[objnet] = group
		}
	}

	// 获取客体文件组 - 文件
	groups, err = DBHighObjFileGroupSearch(db)
	if err != nil {
		return rh, err
	}

	for _, group := range groups {
		objfiles, _, err := DBHighObjFileSearch(db, group, 0, 256)
		if err != nil {
			return rh, err
		}
		for _, objfile := range objfiles {
			rh.RObjFile[objfile] = group
		}
	}

	// 获取权限 - 客体
	for _, group := range user_groups {
		perm_items, _, err := DBHighPermSearch(db, group, 0, 256)
		if err != nil {
			return rh, err
		}
		for _, perm := range perm_items {
			perm_str := perm.ObjType + "_" + perm.UserGroup + "_" +
				perm.ProcGroup + "_" + perm.ObjGroup + "_" + perm.Perm
			rh.RPerm[perm_str] = 0
		}
	}

	return rh, nil
}

func MemRuleInit() (err error) {
	// 初始化缓存
	LockCacheRule.Lock()
	GCacheRule = CacheNew(GCacheRuleSize)
	LockCacheRule.Unlock()

	// 初始化 - 超级进程
	err = MemRuleInitRuleSuper()
	if err != nil {
		return err
	}

	// 初始化 - 自保护策略
	rh, err := MemRuleInitRule(GHandleDBRuleSelf)
	if err != nil {
		return err
	}
	rh.StatusProc, rh.StatusFile, rh.StatusNet, err = DBRuleStatSelfGet()
	if err != nil {
		return err
	}

	LockGMemRuleSelfHandle.Lock()
	GMemRuleSelfHandle = rh
	LockGMemRuleSelfHandle.Unlock()

	// 初始化 - 基础安全策略
	rh, err = MemRuleInitRule(GHandleDBRuleSafe)
	if err != nil {
		return err
	}
	rh.StatusProc, rh.StatusFile, rh.StatusNet, err = DBRuleStatSafeGet()
	if err != nil {
		return err
	}
	LockGMemRuleSafeHandle.Lock()
	GMemRuleSafeHandle = rh
	LockGMemRuleSafeHandle.Unlock()

	// 初始化 - 用户策略
	rh, err = MemRuleInitRule(GHandleDBRuleUser)
	if err != nil {
		return err
	}
	rh.StatusProc, rh.StatusFile, rh.StatusNet, err = DBRuleStatUserGet()
	if err != nil {
		return err
	}
	LockGMemRuleUserHandle.Lock()
	GMemRuleUserHandle = rh
	LockGMemRuleUserHandle.Unlock()

	// 初始化 - 特殊资源策略
	mode, settime, shutdown, usb, cdrom, err := DBSpecialConfigGet()
	if err != nil {
		return err
	}
	LockGMemRuleSpecialHandle.Lock()
	GMemRuleSpecialHandle.StatusMode = mode
	GMemRuleSpecialHandle.StatusSetTime = settime
	GMemRuleSpecialHandle.StatusShutDown = shutdown
	GMemRuleSpecialHandle.StatusUsb = usb
	GMemRuleSpecialHandle.StatusCdrom = cdrom
	LockGMemRuleSpecialHandle.Unlock()
	return nil
}
