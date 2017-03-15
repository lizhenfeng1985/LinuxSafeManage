# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui 
import sys
import json
from http import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
    
class AdminBoardHighUser(QtGui.QWidget):
    def __init__(self,parent=None):
        super(AdminBoardHighUser,self).__init__(parent)        
        #self.setupUi(self)

    def AddAdminTagHighUser(self):
        # 变量
        self.adminTagHighUserPageLength = 10
        self.adminTagHighUserPage = 0
        self.adminTagHighUserTotal = 0
        
        # 画线 左
        self.adminTagHighUserSpaceLeft = QtGui.QWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.adminTagHighUserSpaceLeft.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighUserSpaceLeft.setObjectName(_fromUtf8('adminTagHighSpaceLeft'))

        # 画线 中
        self.adminTagHighUserSpaceMid = QtGui.QWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserSpaceMid.setGeometry(QtCore.QRect(210, 0, 1, 295))
        self.adminTagHighUserSpaceMid.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighUserSpaceMid.setObjectName(_fromUtf8('adminTagHighSpaceMid'))

        # 画线 右
        self.adminTagHighUserSpaceRight = QtGui.QWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.adminTagHighUserSpaceRight.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighUserSpaceRight.setObjectName(_fromUtf8('adminTagHighUserSpaceRight'))

        # 画线 底
        self.adminTagHighUserSpaceBottom = QtGui.QWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.adminTagHighUserSpaceBottom.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighUserSpaceBottom.setObjectName(_fromUtf8('adminTagHighUserSpaceBottom'))

        # 组 - 添加
        self.adminTagHighUserGroupAdd = QtGui.QPushButton(self.adminTagHighTagUserBkg)
        self.adminTagHighUserGroupAdd.setGeometry(QtCore.QRect(30, 8, 75, 25))
        self.adminTagHighUserGroupAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighUserGroupAdd.setObjectName(_fromUtf8('adminTagHighUserGroupAdd'))
        self.adminTagHighUserGroupAdd.setText(_translate('adminTagHighUserGroupAdd', '添加+', None))

        # 组 - 删除
        self.adminTagHighUserGroupDel = QtGui.QPushButton(self.adminTagHighTagUserBkg)
        self.adminTagHighUserGroupDel.setGeometry(QtCore.QRect(125, 8, 75, 25))
        self.adminTagHighUserGroupDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighUserGroupDel.setObjectName(_fromUtf8('adminTagHighUserGroupDel'))
        self.adminTagHighUserGroupDel.setText(_translate('adminTagHighUserGroupDel', '删除+', None))

        # 组 - 列表
        self.adminTagHighUserGroupTree = QtGui.QTreeWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserGroupTree.setGeometry(QtCore.QRect(30, 40, 170, 245))
        self.adminTagHighUserGroupTree.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighUserGroupTree.setObjectName(_fromUtf8('adminTagHighUserGroupTree'))
        self.adminTagHighUserGroupTree.setHeaderHidden(True)

        # 组标题显示
        self.adminTagHighUserGroupNameLable = QtGui.QLabel(self.adminTagHighTagUserBkg)
        self.adminTagHighUserGroupNameLable.setGeometry(QtCore.QRect(240, 5, 45, 30))
        self.adminTagHighUserGroupNameLable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighUserGroupNameLable.setObjectName(_fromUtf8('adminTagHighUserGroupNameLable'))
        self.adminTagHighUserGroupNameLable.setText(_translate('adminTagHighUserGroupNameLable', '当前组：', None))
        
        # 组名称 选择
        self.adminTagHighUserGroupName = QtGui.QLabel(self.adminTagHighTagUserBkg)
        self.adminTagHighUserGroupName.setGeometry(QtCore.QRect(285, 5, 120, 30))
        self.adminTagHighUserGroupName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighUserGroupName.setObjectName(_fromUtf8('adminTagHighUserGroupName'))
        self.adminTagHighUserGroupName.setText(_translate('adminTagHighUserGroupName', '', None))

        # 上一页
        self.adminTagHighUserPrev = QtGui.QPushButton(self.adminTagHighTagUserBkg)
        self.adminTagHighUserPrev.setGeometry(QtCore.QRect(420, 8, 70, 25))
        #self.adminTagHighUserPrev.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighUserPrev.setObjectName(_fromUtf8('adminTagHighUserPrev'))
        self.adminTagHighUserPrev.setText(_translate('adminTagHighUserPrev', '<<  上一页', None))

        # 当前页
        self.adminTagHighUserPageText = QtGui.QLabel(self.adminTagHighTagUserBkg)
        self.adminTagHighUserPageText.setGeometry(QtCore.QRect(490, 8, 30, 25))
        self.adminTagHighUserPageText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.adminTagHighUserPageText.setObjectName(_fromUtf8('adminTagHighUserPageText'))
        self.adminTagHighUserPageText.setText(_translate('adminTagHighUserPageText', '0/0', None))

        # 下一页
        self.adminTagHighUserNext = QtGui.QPushButton(self.adminTagHighTagUserBkg)
        self.adminTagHighUserNext.setGeometry(QtCore.QRect(530, 8, 70, 25))
        #self.adminTagHighUserNext.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighUserNext.setObjectName(_fromUtf8('adminTagHighUserNext'))
        self.adminTagHighUserNext.setText(_translate('adminTagHighUserNext', '下一页  >>', None))

        # 用户 - 添加
        self.adminTagHighUserAdd = QtGui.QPushButton(self.adminTagHighTagUserBkg)
        self.adminTagHighUserAdd.setGeometry(QtCore.QRect(720, 8, 70, 25))
        self.adminTagHighUserAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighUserAdd.setObjectName(_fromUtf8('adminTagHighUserAdd'))
        self.adminTagHighUserAdd.setText(_translate('adminTagHighUserAdd', '添加用户', None))

        # 用户 - 删除
        self.adminTagHighUserDel = QtGui.QPushButton(self.adminTagHighTagUserBkg)
        self.adminTagHighUserDel.setGeometry(QtCore.QRect(800, 8, 70, 25))
        self.adminTagHighUserDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighUserDel.setObjectName(_fromUtf8('adminTagHighUserDel'))
        self.adminTagHighUserDel.setText(_translate('adminTagHighUserDel', '删除用户', None))

        # 用户 - 全选
        self.adminTagHighUserSelect = QtGui.QCheckBox(self.adminTagHighTagUserBkg)
        self.adminTagHighUserSelect.setGeometry(QtCore.QRect(900, 8, 55, 25))
        self.adminTagHighUserSelect.setObjectName(_fromUtf8('adminTagHighUserSelect'))
        self.adminTagHighUserSelect.setText(_translate('adminTagHighUserSelect', '全选', None))

        # 用户 - 列表表格
        self.adminTagHighUserTable = QtGui.QTableWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserTable.setGeometry(QtCore.QRect(225, 40, 735, 245))
        self.adminTagHighUserTable.setObjectName(_fromUtf8('adminTagSpecialTable'))
        self.adminTagHighUserTable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.jpg);'))
        self.adminTagHighUserTable.verticalHeader().setVisible(False)
        self.adminTagHighUserTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagHighUserTable.setAlternatingRowColors(True)
        #list_widget.adminTagHighUserTable(QtGui.QAbstractItemView.SelectRows)
        self.adminTagHighUserTable.setRowCount(self.adminTagHighUserPageLength)
        self.adminTagHighUserTable.setColumnCount(2)
        self.adminTagHighUserTable.setHorizontalHeaderLabels([_fromUtf8('用户名'),_fromUtf8('选择')])
        self.adminTagHighUserTable.setShowGrid(False)
        self.adminTagHighUserTable.setColumnWidth(0, 600)
        self.adminTagHighUserTable.setColumnWidth(1, 130)
        for i in range(0, self.adminTagHighUserPageLength):
            self.adminTagHighUserTable.setRowHeight(i, 21)

        #####################################################
        # 添加用户弹出
        self.adminTagHighUserAddDlg = QtGui.QWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserAddDlg.setGeometry(QtCore.QRect(300, 0, 257, 282))
        self.adminTagHighUserAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighUserAddDlg.setObjectName(_fromUtf8('adminTagHighUserAddDlg'))
        self.adminTagHighUserAddDlg.hide()

        # 添加用户弹出 - 请选择用户
        self.adminTagHighUserAddDlgTextLab = QtGui.QLabel(self.adminTagHighUserAddDlg)
        self.adminTagHighUserAddDlgTextLab.setGeometry(QtCore.QRect(20, 10, 70, 21))
        self.adminTagHighUserAddDlgTextLab.setObjectName(_fromUtf8('adminTagHighUserAddDlgText'))
        self.adminTagHighUserAddDlgTextLab.setText(_translate('adminTagHighUserAddDlgText', '请选择用户:', None))

        # 添加用户弹出 - 用户名称
        self.adminTagHighUserAddDlgUName = QtGui.QLabel(self.adminTagHighUserAddDlg)
        self.adminTagHighUserAddDlgUName.setGeometry(QtCore.QRect(90, 10, 141, 21))
        self.adminTagHighUserAddDlgUName.setObjectName(_fromUtf8('adminTagHighUserAddDlgUName'))
        self.adminTagHighUserAddDlgUName.setText(_translate('adminTagHighUserAddDlgUName', '', None))

        # 添加用户弹出 - 用户列表
        self.adminTagHighUserAddDlgTree = QtGui.QTreeWidget(self.adminTagHighUserAddDlg)
        self.adminTagHighUserAddDlgTree.setGeometry(QtCore.QRect(10, 40, 231, 192))
        self.adminTagHighUserAddDlgTree.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighUserAddDlgTree.setObjectName(_fromUtf8('adminTagHighUserAddDlgTree'))
        self.adminTagHighUserAddDlgTree.setHeaderHidden(True)

        # 添加用户弹出 - 添加
        self.adminTagHighUserAddDlgOk = QtGui.QPushButton(self.adminTagHighUserAddDlg)
        self.adminTagHighUserAddDlgOk.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.adminTagHighUserAddDlgOk.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighUserAddDlgOk.setObjectName(_fromUtf8('adminTagHighUserAddDlgOk'))
        self.adminTagHighUserAddDlgOk.setText(_translate('adminTagHighUserAddDlgOk', '添加', None))

        # 添加用户弹出 - 取消
        self.adminTagHighUserAddDlgCancel = QtGui.QPushButton(self.adminTagHighUserAddDlg)
        self.adminTagHighUserAddDlgCancel.setGeometry(QtCore.QRect(150, 250, 75, 23))
        self.adminTagHighUserAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighUserAddDlgCancel.setObjectName(_fromUtf8('adminTagHighUserAddDlgOk'))
        self.adminTagHighUserAddDlgCancel.setText(_translate('adminTagHighUserAddDlgCancel', '取消', None))

        ###########################################################
        # 添加组 弹出
        self.adminTagHighUserGroupAddDlg = QtGui.QWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserGroupAddDlg.setGeometry(QtCore.QRect(300, 0, 271, 105))
        self.adminTagHighUserGroupAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighUserGroupAddDlg.setObjectName(_fromUtf8('adminTagHighUserGroupAddDlg'))
        self.adminTagHighUserGroupAddDlg.hide()

        # 添加组 弹出 - 输入组名称
        self.adminTagHighUserGroupAddDlgText = QtGui.QLabel(self.adminTagHighUserGroupAddDlg)
        self.adminTagHighUserGroupAddDlgText.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.adminTagHighUserGroupAddDlgText.setObjectName(_fromUtf8('adminTagHighUserGroupAddDlgText'))
        self.adminTagHighUserGroupAddDlgText.setText(_translate('adminTagHighUserGroupAddDlgText', '请输入组名称:', None))

        # 添加组 弹出 - 组名称
        self.adminTagHighUserGroupAddDlgName = QtGui.QLineEdit(self.adminTagHighUserGroupAddDlg)
        self.adminTagHighUserGroupAddDlgName.setGeometry(QtCore.QRect(20, 30, 231, 31))
        self.adminTagHighUserGroupAddDlgName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white.png);'))
        self.adminTagHighUserGroupAddDlgName.setObjectName(_fromUtf8('adminTagHighUserGroupAddDlgName'))
        self.adminTagHighUserGroupAddDlgName.setText(_translate('adminTagHighUserGroupAddDlgName', '', None))

        # 添加组 弹出 - 添加
        self.adminTagHighUserGroupAddDlgOK = QtGui.QPushButton(self.adminTagHighUserGroupAddDlg)
        self.adminTagHighUserGroupAddDlgOK.setGeometry(QtCore.QRect(40, 70, 75, 23))
        self.adminTagHighUserGroupAddDlgOK.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighUserGroupAddDlgOK.setObjectName(_fromUtf8('adminTagHighUserGroupAddDlgOK'))
        self.adminTagHighUserGroupAddDlgOK.setText(_translate('adminTagHighUserGroupAddDlgOK', '添加', None))

        # 添加组 弹出 - 取消
        self.adminTagHighUserGroupAddDlgCancel = QtGui.QPushButton(self.adminTagHighUserGroupAddDlg)
        self.adminTagHighUserGroupAddDlgCancel.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.adminTagHighUserGroupAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighUserGroupAddDlgCancel.setObjectName(_fromUtf8('adminTagHighUserGroupAddDlgCancel'))
        self.adminTagHighUserGroupAddDlgCancel.setText(_translate('adminTagHighUserGroupAddDlgCancel', '取消', None))
        
        ###############################################################
        # 添加组
        self.onAdminTagHighUserGroupSet()
        
        # 组列表消息
        self.connect(self.adminTagHighUserGroupTree, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onAdminTagHighUserGroupClick)
        self.connect(self.adminTagHighUserGroupAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserGroupAdd)
        self.connect(self.adminTagHighUserGroupDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserGroupDel)
        self.connect(self.adminTagHighUserGroupAddDlgOK, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserGroupAddDlgOK)
        self.connect(self.adminTagHighUserGroupAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserGroupAddDlgCancel)
        
        # 添加用户消息
        self.connect(self.adminTagHighUserAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserAdd)
        self.connect(self.adminTagHighUserPrev, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserPrev)
        self.connect(self.adminTagHighUserNext, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserNext)
        self.connect(self.adminTagHighUserDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserDel)
        self.connect(self.adminTagHighUserSelect, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserSelect)
        self.connect(self.adminTagHighUserAddDlgOk, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserAddDlgOk)
        self.connect(self.adminTagHighUserAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighUserAddDlgCancel)
        self.connect(self.adminTagHighUserAddDlgTree, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onAdminTagHighUserAddDlgTreeClick)
        

    def AdddminTagHighUserGroupTree(self, title, data):
        root = self.adminTagHighUserGroupTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)
        #item.setCheckState (0, QtCore.Qt.Unchecked)

    def AdddminTagHighUserTree(self, title, data):
        root = self.adminTagHighUserAddDlgTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)

    def onAdminTagHighUserGroupClick(self, item, column):
        if self.AdminBoardCheckPopUp():
            return
        self.adminTagHighUserGroupName.setText(item.text(column))
        self.AdminTagHighUserSet(0, self.adminTagHighUserPageLength)

    def onAdminTagHighUserAddDlgTreeClick(self, item, column):
        self.adminTagHighUserAddDlgUName.setText(item.text(column))


    # 用户 - 全选
    def onAdminTagHighUserSelect(self):
        chk = self.adminTagHighUserSelect.checkState()
        if chk == 0: #全不选
            itemcnt = self.adminTagHighUserTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighUserTable.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(False)
        elif chk == 2: #全选
            itemcnt = self.adminTagHighUserTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighUserTable.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(2)
        else:
            pass

    def setAdminTagHighUserNowPageText(self):
        tot = self.adminTagHighUserTotal
        page = self.adminTagHighUserPage
        length = self.adminTagHighUserPageLength
        page_str = '0/0'
        if tot > 0:
            if tot % length > 0:
                page_str = '%d/%d' % (page + 1, (tot / length) + 1)
            else:
                page_str = '%d/%d' % (page + 1, tot / length)
        self.adminTagHighUserPageText.setText(_translate('adminTagHighUserPageText', page_str, None))

    # 设置用户列表
    def AdminTagHighUserSet(self, start, length):
        group = unicode(self.adminTagHighUserGroupName.text())
        #print group, start, length
        # 查找当前组用户列表
        url = 'https://%s:%s/highuser/search/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group,
            'Start'   : start,
            'Length'  : length
        }
        #print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.adminTagHighUserTotal = res['Total']
                
                # 清空列表
                for i in xrange(0, self.adminTagHighUserPageLength):
                    self.adminTagHighUserTable.setItem(i, 0, None)
                    self.adminTagHighUserTable.setItem(i, 1, None)
                    self.adminTagHighUserPage = 0
                if res['Users'] != None:
                    # 添加列表
                    cnt = len(res['Users'])
                    for i in xrange(0, cnt):
                        newItem = QtGui.QTableWidgetItem(res['Users'][i])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighUserTable.setItem(i, 0, newItem)
                    
                        newItemChkbox = QtGui.QTableWidgetItem()
                        newItemChkbox.setCheckState(False)
                        newItemChkbox.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighUserTable.setItem(i, 1, newItemChkbox)
                    self.adminTagHighUserPage = start / self.adminTagHighUserPageLength
                self.setAdminTagHighUserNowPageText()
            else:
                QtGui.QMessageBox.about(self, u'错误提示', res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])
        

    # 上一页
    def onAdminTagHighUserPrev(self):
        start = self.adminTagHighUserPageLength * (self.adminTagHighUserPage - 1)
        if start < 0 :
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是第一页')
        else:
            self.AdminTagHighUserSet(start, self.adminTagHighUserPageLength)
        

    # 下一页
    def onAdminTagHighUserNext(self):
        start = self.adminTagHighUserPageLength * (self.adminTagHighUserPage + 1)
        if start >= self.adminTagHighUserTotal :
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是最后一页')
        else:
            self.AdminTagHighUserSet(start, self.adminTagHighUserPageLength)

    # 删除用户列表
    def onAdminTagHighUserDel(self):
        itemcnt = self.adminTagHighUserTable.rowCount()
        dellist = []
        
        for i in range(0, itemcnt):
            it = self.adminTagHighUserTable.item(i, 1)
            if it == None:
                continue
            chk = it.checkState()
            if chk == 2: # 状态有0和2
                user = unicode(self.adminTagHighUserTable.item(i, 0).text())
                dellist.append(user)

        url = 'https://%s:%s/highuser/del/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        #print url
        for user in dellist:
            data = {
                'Tokey'   : self.Tokey,
                'User'    : user
            }
            #print data
            param = {'Data' : json.dumps(data)} 
            rt = HttpsPost(url, param)
            #print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:             
                    #QtGui.QMessageBox.about(self, u'提示', u'删除用户成功:' + user)
                    pass
                else:
                    QtGui.QMessageBox.about(self, u'错误提示', u'删除用户失败:' + user + ':' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除用户失败:' + rt[1])
                
        #刷新列表
        self.AdminTagHighUserSet(0, self.adminTagHighUserPageLength)
        
    # 设置组列表
    def onAdminTagHighUserGroupSet(self):
        url = 'https://%s:%s/highuser/groupsearch/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey
        }
        #print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:             
                self.adminTagHighUserGroupTree.clear()
                if res['Groups'] == None:
                    return
                for group in res['Groups']:                    
                    self.AdddminTagHighUserGroupTree(group, group)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])
    
    # 弹出 - 添加组
    def onAdminTagHighUserGroupAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighUserGroupAddDlg.show()

    # 删除组
    def onAdminTagHighUserGroupDel(self):
        group = unicode(self.adminTagHighUserGroupName.text())
        if group == '':
            QtGui.QMessageBox.about(self, u'设置', u'请选择一个组')
            return
        url = 'https://%s:%s/highuser/groupdel/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group
        }
        #print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.onAdminTagHighUserGroupSet()
                QtGui.QMessageBox.about(self, u'设置', u'删除组成功:')
                self.adminTagHighUserGroupName.setText(u'')
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除组失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'删除组失败:' + rt[1])
    

    # 弹出 - 添加组 - OK
    def onAdminTagHighUserGroupAddDlgOK(self):
        self.AdminBoardUnsetPopUp()        
        self.adminTagHighUserGroupAddDlg.hide()

        group = unicode(self.adminTagHighUserGroupAddDlgName.text())

        if group == '':
            QtGui.QMessageBox.about(self, u'设置', u'组名称不能为空')
            return
        
        url = 'https://%s:%s/highuser/groupadd/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group
        }
        #print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:               
                self.onAdminTagHighUserGroupSet()
                QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.adminTagHighUserGroupAddDlgName.setText(_fromUtf8('')) 
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加组失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加组失败:' + rt[1])

    # 弹出 - 添加组 - Cancel
    def onAdminTagHighUserGroupAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighUserGroupAddDlg.hide()

    # 弹出 - 添加用户
    def onAdminTagHighUserAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighUserAddDlg.show()
        
        # 获取系统用户列表
        url = 'https://%s:%s/highuser/list/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey
        }
        #print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:             
                self.adminTagHighUserAddDlgTree.clear()
                for user in res['Users']:                    
                    self.AdddminTagHighUserTree(user, user)                
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'获取系统用户列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'获取系统用户列表失败:' + rt[1])
        

    # 弹出 - 用户 - OK
    def onAdminTagHighUserAddDlgOk(self):
        group = unicode(self.adminTagHighUserGroupName.text())
        uname = unicode(self.adminTagHighUserAddDlgUName.text())

        # 添加用户
        url = 'https://%s:%s/highuser/add/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group,
            'User'    : uname,
        }
        #print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:             
                #QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.AdminTagHighUserSet(0, self.adminTagHighUserPageLength)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加用户失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加用户失败:' + rt[1])
        

    # 弹出 - 用户 - Cancel
    def onAdminTagHighUserAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighUserAddDlg.hide()
        self.adminTagHighUserAddDlgUName.setText(u'')
        
import images_rc
