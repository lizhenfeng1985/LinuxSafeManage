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


class AdminBoardHighPerm(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AdminBoardHighPerm, self).__init__(parent)
        # self.setupUi(self)

    def AddAdminTagHighPerm(self):
        # 变量
        self.adminTagHighPermPageLength = 10
        self.adminTagHighPermPage = 0
        self.adminTagHighPermTotal = 0

        # 画线 左
        self.adminTagHighPermSpaceLeft = QtGui.QWidget(self.adminTagHighTagPermBkg)
        self.adminTagHighPermSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.adminTagHighPermSpaceLeft.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighPermSpaceLeft.setObjectName(_fromUtf8('adminTagHighSpaceLeft'))

        # 画线 中
        self.adminTagHighPermSpaceMid = QtGui.QWidget(self.adminTagHighTagPermBkg)
        self.adminTagHighPermSpaceMid.setGeometry(QtCore.QRect(210, 0, 1, 295))
        self.adminTagHighPermSpaceMid.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighPermSpaceMid.setObjectName(_fromUtf8('adminTagHighSpaceMid'))

        # 画线 右
        self.adminTagHighPermSpaceRight = QtGui.QWidget(self.adminTagHighTagPermBkg)
        self.adminTagHighPermSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.adminTagHighPermSpaceRight.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighPermSpaceRight.setObjectName(_fromUtf8('adminTagHighPermSpaceRight'))

        # 画线 底
        self.adminTagHighPermSpaceBottom = QtGui.QWidget(self.adminTagHighTagPermBkg)
        self.adminTagHighPermSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.adminTagHighPermSpaceBottom.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighPermSpaceBottom.setObjectName(_fromUtf8('adminTagHighPermSpaceBottom'))

        # 组 - 标签
        self.adminTagHighPermGroupLable = QtGui.QLabel(self.adminTagHighTagPermBkg)
        self.adminTagHighPermGroupLable.setGeometry(QtCore.QRect(30, 8, 170, 25))
        self.adminTagHighPermGroupLable.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter)
        self.adminTagHighPermGroupLable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighPermGroupLable.setObjectName(_fromUtf8('adminTagHighPermGroupLable'))
        self.adminTagHighPermGroupLable.setText(_translate('adminTagHighPermGroupLable', '请选择用户组', None))

        # 组 - 列表
        self.adminTagHighPermGroupTree = QtGui.QTreeWidget(self.adminTagHighTagPermBkg)
        self.adminTagHighPermGroupTree.setGeometry(QtCore.QRect(30, 40, 170, 245))
        self.adminTagHighPermGroupTree.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighPermGroupTree.setObjectName(_fromUtf8('adminTagHighPermGroupTree'))
        self.adminTagHighPermGroupTree.setHeaderHidden(True)

        # 组标题显示
        self.adminTagHighPermGroupNameLable = QtGui.QLabel(self.adminTagHighTagPermBkg)
        self.adminTagHighPermGroupNameLable.setGeometry(QtCore.QRect(240, 5, 45, 30))
        self.adminTagHighPermGroupNameLable.setStyleSheet(
            _fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighPermGroupNameLable.setObjectName(_fromUtf8('adminTagHighPermGroupNameLable'))
        self.adminTagHighPermGroupNameLable.setText(_translate('adminTagHighPermGroupNameLable', '当前组：', None))

        # 组名称 选择
        self.adminTagHighPermGroupName = QtGui.QLabel(self.adminTagHighTagPermBkg)
        self.adminTagHighPermGroupName.setGeometry(QtCore.QRect(285, 5, 120, 30))
        self.adminTagHighPermGroupName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighPermGroupName.setObjectName(_fromUtf8('adminTagHighPermGroupName'))
        self.adminTagHighPermGroupName.setText(_translate('adminTagHighPermGroupName', '', None))

        # 上一页
        self.adminTagHighPermPrev = QtGui.QPushButton(self.adminTagHighTagPermBkg)
        self.adminTagHighPermPrev.setGeometry(QtCore.QRect(420, 8, 70, 25))
        # self.adminTagHighPermPrev.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighPermPrev.setObjectName(_fromUtf8('adminTagHighPermPrev'))
        self.adminTagHighPermPrev.setText(_translate('adminTagHighPermPrev', '<<  上一页', None))

        # 当前页
        self.adminTagHighPermPageText = QtGui.QLabel(self.adminTagHighTagPermBkg)
        self.adminTagHighPermPageText.setGeometry(QtCore.QRect(490, 8, 30, 25))
        self.adminTagHighPermPageText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        # self.adminTagHighPermPrev.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighPermPageText.setObjectName(_fromUtf8('adminTagHighPermPageText'))
        self.adminTagHighPermPageText.setText(_translate('adminTagHighPermPageText', '0/0', None))

        # 下一页
        self.adminTagHighPermNext = QtGui.QPushButton(self.adminTagHighTagPermBkg)
        self.adminTagHighPermNext.setGeometry(QtCore.QRect(530, 8, 70, 25))
        # self.adminTagHighPermNext.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighPermNext.setObjectName(_fromUtf8('adminTagHighPermNext'))
        self.adminTagHighPermNext.setText(_translate('adminTagHighPermNext', '下一页  >>', None))

        # 权限 - 添加
        self.adminTagHighPermAdd = QtGui.QPushButton(self.adminTagHighTagPermBkg)
        self.adminTagHighPermAdd.setGeometry(QtCore.QRect(720, 8, 70, 25))
        self.adminTagHighPermAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighPermAdd.setObjectName(_fromUtf8('adminTagHighPermAdd'))
        self.adminTagHighPermAdd.setText(_translate('adminTagHighPermAdd', '添加权限', None))

        # 权限 - 删除
        self.adminTagHighPermDel = QtGui.QPushButton(self.adminTagHighTagPermBkg)
        self.adminTagHighPermDel.setGeometry(QtCore.QRect(800, 8, 70, 25))
        self.adminTagHighPermDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighPermDel.setObjectName(_fromUtf8('adminTagHighPermDel'))
        self.adminTagHighPermDel.setText(_translate('adminTagHighPermDel', '删除权限', None))

        # 权限 - 全选
        self.adminTagHighPermSelect = QtGui.QCheckBox(self.adminTagHighTagPermBkg)
        self.adminTagHighPermSelect.setGeometry(QtCore.QRect(900, 8, 55, 25))
        self.adminTagHighPermSelect.setObjectName(_fromUtf8('adminTagHighPermSelect'))
        self.adminTagHighPermSelect.setText(_translate('adminTagHighPermSelect', '全选', None))

        # 权限 - 列表表格
        self.adminTagHighPermTable = QtGui.QTableWidget(self.adminTagHighTagPermBkg)
        self.adminTagHighPermTable.setGeometry(QtCore.QRect(225, 40, 735, 245))
        self.adminTagHighPermTable.setObjectName(_fromUtf8('adminTagSpecialTable'))
        self.adminTagHighPermTable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.jpg);'))
        self.adminTagHighPermTable.verticalHeader().setVisible(False)
        self.adminTagHighPermTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagHighPermTable.setAlternatingRowColors(True)
        # list_widget.adminTagHighPermTable(QtGui.QAbstractItemView.SelectRows)
        self.adminTagHighPermTable.setRowCount(self.adminTagHighPermPageLength)
        self.adminTagHighPermTable.setColumnCount(5)
        self.adminTagHighPermTable.setHorizontalHeaderLabels([_fromUtf8('进程组'), _fromUtf8('对象组'), _fromUtf8('类型'), _fromUtf8('权限'), _fromUtf8('选择')])
        self.adminTagHighPermTable.setShowGrid(False)
        self.adminTagHighPermTable.setColumnWidth(0, 200)
        self.adminTagHighPermTable.setColumnWidth(1, 200)
        self.adminTagHighPermTable.setColumnWidth(2, 100)
        self.adminTagHighPermTable.setColumnWidth(3, 110)
        self.adminTagHighPermTable.setColumnWidth(4, 100)
        for i in range(0, self.adminTagHighPermPageLength):
            self.adminTagHighPermTable.setRowHeight(i, 21)

        #####################################################
        # 添加权限弹出
        self.adminTagHighPermAddDlg = QtGui.QWidget(self.adminTagHighTagPermBkg)
        #self.adminTagHighPermAddDlg.setGeometry(QtCore.QRect(300, 0, 254, 179))
        self.adminTagHighPermAddDlg.setGeometry(QtCore.QRect(300, 0, 274, 230))
        self.adminTagHighPermAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighPermAddDlg.setObjectName(_fromUtf8('adminTagHighPermAddDlg'))
        self.adminTagHighPermAddDlg.hide()

        # 添加权限弹出 - 用户组 - 文字
        self.adminTagHighPermAddDlgUserGroupText = QtGui.QLabel(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgUserGroupText.setGeometry(QtCore.QRect(20, 30, 70, 21))
        self.adminTagHighPermAddDlgUserGroupText.setObjectName(_fromUtf8('adminTagHighPermAddDlgUserGroupText'))
        self.adminTagHighPermAddDlgUserGroupText.setText(_translate('adminTagHighPermAddDlgUserGroupText', '用 户 组：', None))

        # 添加权限弹出 - 用户组 - 显示
        self.adminTagHighPermAddDlgUserGroup = QtGui.QLineEdit(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgUserGroup.setGeometry(QtCore.QRect(90, 30, 160, 22))
        self.adminTagHighPermAddDlgUserGroup.setReadOnly(True)
        self.adminTagHighPermAddDlgUserGroup.setObjectName(_fromUtf8("adminTagHighPermAddDlgUserGroup"))
        self.adminTagHighPermAddDlgUserGroup.setStyleSheet(_fromUtf8("border-image: url(:/images/bkg_btn2.png);"))
        self.adminTagHighPermAddDlgUserGroup.setText(_translate('adminTagHighPermAddDlgUserGroup', '', None))

        # 添加权限弹出 - 程序组 - 文字
        self.adminTagHighPermAddDlgProcGroupText = QtGui.QLabel(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgProcGroupText.setGeometry(QtCore.QRect(20, 60, 70, 21))
        self.adminTagHighPermAddDlgProcGroupText.setObjectName(_fromUtf8('adminTagHighPermAddDlgProcGroupText'))
        self.adminTagHighPermAddDlgProcGroupText.setText(_translate('adminTagHighPermAddDlgProcGroupText', '程 序 组：', None))

        # 添加权限弹出 - 程序组 - 选择
        self.adminTagHighPermAddDlgProcGroup = QtGui.QComboBox(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgProcGroup.setGeometry(QtCore.QRect(90, 60, 160, 22))
        self.adminTagHighPermAddDlgProcGroup.setObjectName(_fromUtf8("adminTagHighPermAddDlgProcGroup"))
        self.adminTagHighPermAddDlgProcGroup.setStyleSheet(_fromUtf8("border-image: url(:/images/bkg_btn2.png);"))
        #self.adminTagHighPermAddDlgProcGroup.addItem(_fromUtf8(""))
        #self.adminTagHighPermAddDlgProcGroup.setItemText(0, _fromUtf8("组1"))

        # 添加权限弹出 - 对象类型 - 文字
        self.adminTagHighPermAddDlgObjTypeText = QtGui.QLabel(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgObjTypeText.setGeometry(QtCore.QRect(20, 90, 70, 21))
        self.adminTagHighPermAddDlgObjTypeText.setObjectName(_fromUtf8('adminTagHighPermAddDlgObjTypeText'))
        self.adminTagHighPermAddDlgObjTypeText.setText(_translate('adminTagHighPermAddDlgObjTypeText', '对象类型：', None))

        # 添加权限弹出 - 对象类型 - 选择
        self.adminTagHighPermAddDlgObjType = QtGui.QComboBox(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgObjType.setGeometry(QtCore.QRect(90, 90, 160, 22))
        self.adminTagHighPermAddDlgObjType.setObjectName(_fromUtf8("adminTagHighPermAddDlgObjType"))
        self.adminTagHighPermAddDlgObjType.setStyleSheet(_fromUtf8("border-image: url(:/images/bkg_btn2.png);"))
        self.adminTagHighPermAddDlgObjType.addItem(_fromUtf8(""))
        self.adminTagHighPermAddDlgObjType.addItem(_fromUtf8(""))
        self.adminTagHighPermAddDlgObjType.addItem(_fromUtf8(""))
        self.adminTagHighPermAddDlgObjType.setItemText(0, _fromUtf8("进程对象"))
        self.adminTagHighPermAddDlgObjType.setItemText(1, _fromUtf8("网络对象"))
        self.adminTagHighPermAddDlgObjType.setItemText(2, _fromUtf8("文件对象"))

        # 添加权限弹出 - 客体对象 - 文字
        self.adminTagHighPermAddDlgObjGroupText = QtGui.QLabel(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgObjGroupText.setGeometry(QtCore.QRect(20, 120, 70, 21))
        self.adminTagHighPermAddDlgObjGroupText.setObjectName(_fromUtf8('adminTagHighPermAddDlgObjGroupText'))
        self.adminTagHighPermAddDlgObjGroupText.setText(_translate('adminTagHighPermAddDlgObjGroupText', '对 象 组：', None))

        # 添加权限弹出 - 客体对象 - 选择
        self.adminTagHighPermAddDlgObjGroup = QtGui.QComboBox(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgObjGroup.setGeometry(QtCore.QRect(90, 120, 160, 22))
        self.adminTagHighPermAddDlgObjGroup.setObjectName(_fromUtf8("adminTagHighPermAddDlgObjGroup"))
        self.adminTagHighPermAddDlgObjGroup.setStyleSheet(_fromUtf8("border-image: url(:/images/bkg_btn2.png);"))

        # 添加权限弹出 - 权限 - 文字
        self.adminTagHighPermAddDlgPermText = QtGui.QLabel(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgPermText.setGeometry(QtCore.QRect(20, 150, 70, 21))
        self.adminTagHighPermAddDlgPermText.setObjectName(_fromUtf8('adminTagHighPermAddDlgPermText'))
        self.adminTagHighPermAddDlgPermText.setText(_translate('adminTagHighPermAddDlgPermText', '权    限：', None))

        # 添加权限弹出 - 权限 - 选择
        self.adminTagHighPermAddDlgPerm = QtGui.QComboBox(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgPerm.setGeometry(QtCore.QRect(90, 150, 160, 22))
        self.adminTagHighPermAddDlgPerm.setObjectName(_fromUtf8("adminTagHighPermAddDlgPerm"))
        self.adminTagHighPermAddDlgPerm.setStyleSheet(_fromUtf8("border-image: url(:/images/bkg_btn2.png);"))
        self.adminTagHighPermAddDlgPerm.addItem(_fromUtf8(""))
        self.adminTagHighPermAddDlgPerm.addItem(_fromUtf8(""))
        self.adminTagHighPermAddDlgPerm.setItemText(0, _fromUtf8("只读"))
        self.adminTagHighPermAddDlgPerm.setItemText(1, _fromUtf8("读写"))

        # 添加权限弹出 - 添加
        self.adminTagHighPermAddDlgOk = QtGui.QPushButton(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgOk.setGeometry(QtCore.QRect(36, 195, 75, 23))
        self.adminTagHighPermAddDlgOk.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighPermAddDlgOk.setObjectName(_fromUtf8('adminTagHighPermAddDlgOk'))
        self.adminTagHighPermAddDlgOk.setText(_translate('adminTagHighPermAddDlgOk', '添加', None))

        # 添加权限弹出 - 取消
        self.adminTagHighPermAddDlgCancel = QtGui.QPushButton(self.adminTagHighPermAddDlg)
        self.adminTagHighPermAddDlgCancel.setGeometry(QtCore.QRect(160, 195, 75, 23))
        self.adminTagHighPermAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighPermAddDlgCancel.setObjectName(_fromUtf8('adminTagHighPermAddDlgOk'))
        self.adminTagHighPermAddDlgCancel.setText(_translate('adminTagHighPermAddDlgCancel', '取消', None))

        ###############################################################
        # 添加组
        self.onAdminTagHighPermGroupSet()

        # 组列表消息
        self.connect(self.adminTagHighPermGroupTree, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'),
                     self.onAdminTagHighPermGroupClick)

        # 添加权限消息
        self.connect(self.adminTagHighPermAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighPermAdd)
        self.connect(self.adminTagHighPermPrev, QtCore.SIGNAL('clicked()'), self.onAdminTagHighPermPrev)
        self.connect(self.adminTagHighPermNext, QtCore.SIGNAL('clicked()'), self.onAdminTagHighPermNext)
        self.connect(self.adminTagHighPermDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighPermDel)
        self.connect(self.adminTagHighPermSelect, QtCore.SIGNAL('clicked()'), self.onAdminTagHighPermSelect)
        self.connect(self.adminTagHighPermAddDlgOk, QtCore.SIGNAL('clicked()'), self.onAdminTagHighPermAddDlgOk)
        self.connect(self.adminTagHighPermAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighPermAddDlgCancel)

        # 消息 - 权限添加 - 客体类型修改
        self.connect(self.adminTagHighPermAddDlgObjType, QtCore.SIGNAL('activated(int)'),
                     self.adminTagHighPermAddDlgObjTypeClick)

    def adminTagHighPermAddDlgObjTypeClick(self, index):
        if index == 0:  # 进程
            url = 'https://%s:%s/highobjproc/groupsearch/%s' % (
            self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
            data = {
                'Tokey': self.Tokey
            }
            #print url, data
            param = {'Data': json.dumps(data)}
            rt = HttpsPost(url, param)
            #print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:
                    self.adminTagHighPermAddDlgObjGroup.clear()
                    if res['Groups'] == None:
                        return
                    i = 0
                    for group in res['Groups']:
                        self.adminTagHighPermAddDlgObjGroup.addItem(_fromUtf8(""))
                        self.adminTagHighPermAddDlgObjGroup.setItemText(i, group)
                        i += 1
                else:
                    QtGui.QMessageBox.about(self, u'错误提示', u'查找进程对象组列表失败:' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'查找进程对象组列表失败:' + rt[1])

            # 设置权限
            self.adminTagHighPermAddDlgPerm.clear()
            self.adminTagHighPermAddDlgPerm.addItem(_fromUtf8(""))
            self.adminTagHighPermAddDlgPerm.addItem(_fromUtf8(""))
            self.adminTagHighPermAddDlgPerm.setItemText(0, u'进程执行')
            self.adminTagHighPermAddDlgPerm.setItemText(1, u'进程结束')
        elif index == 1:  # 网络
            url = 'https://%s:%s/highobjnet/groupsearch/%s' % (
            self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
            data = {
                'Tokey': self.Tokey
            }
            #print url, data
            param = {'Data': json.dumps(data)}
            rt = HttpsPost(url, param)
            #print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:
                    self.adminTagHighPermAddDlgObjGroup.clear()
                    if res['Groups'] == None:
                        return
                    i = 0
                    for group in res['Groups']:
                        self.adminTagHighPermAddDlgObjGroup.addItem(_fromUtf8(""))
                        self.adminTagHighPermAddDlgObjGroup.setItemText(i, group)
                        i += 1
                else:
                    QtGui.QMessageBox.about(self, u'错误提示', u'查找网络对象组列表失败:' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'查找网络对象组列表失败:' + rt[1])
            # 设置权限
            self.adminTagHighPermAddDlgPerm.clear()
            self.adminTagHighPermAddDlgPerm.addItem(_fromUtf8(""))
            self.adminTagHighPermAddDlgPerm.addItem(_fromUtf8(""))
            self.adminTagHighPermAddDlgPerm.setItemText(0, u'网络监听')
            self.adminTagHighPermAddDlgPerm.setItemText(1, u'网络连接')
        elif index == 2:  # 文件
            url = 'https://%s:%s/highobjfile/groupsearch/%s' % (
            self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
            data = {
                'Tokey': self.Tokey
            }
            #print url, data
            param = {'Data': json.dumps(data)}
            rt = HttpsPost(url, param)
            #print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:
                    self.adminTagHighPermAddDlgObjGroup.clear()
                    if res['Groups'] == None:
                        return
                    i = 0
                    for group in res['Groups']:
                        self.adminTagHighPermAddDlgObjGroup.addItem(_fromUtf8(""))
                        self.adminTagHighPermAddDlgObjGroup.setItemText(i, group)
                        i += 1
                else:
                    QtGui.QMessageBox.about(self, u'错误提示', u'查找文件对象组列表失败:' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'查找文件对象组列表失败:' + rt[1])
            # 设置权限
            self.adminTagHighPermAddDlgPerm.clear()
            self.adminTagHighPermAddDlgPerm.addItem(_fromUtf8(""))
            self.adminTagHighPermAddDlgPerm.addItem(_fromUtf8(""))
            self.adminTagHighPermAddDlgPerm.setItemText(0, u'只读')
            self.adminTagHighPermAddDlgPerm.setItemText(1, u'读写')
        else:
            self.adminTagHighPermAddDlgObjGroup.clear()
            self.adminTagHighPermAddDlgPerm.clear()

    def AdddminTagHighPermGroupTree(self, title, data):
        root = self.adminTagHighPermGroupTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)
        # item.setCheckState (0, QtCore.Qt.Unchecked)

    def AdddminTagHighPermTree(self, title, data):
        root = self.adminTagHighPermAddDlgTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)

    def onAdminTagHighPermGroupClick(self, item, column):
        if self.AdminBoardCheckPopUp():
            return
        self.adminTagHighPermGroupName.setText(item.text(column))
        self.AdminTagHighPermSet(0, self.adminTagHighPermPageLength)

    # 权限 - 全选
    def onAdminTagHighPermSelect(self):
        chk = self.adminTagHighPermSelect.checkState()
        if chk == 0:  # 全不选
            itemcnt = self.adminTagHighPermTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighPermTable.item(i, 4)
                if it == None:
                    continue
                it.setCheckState(False)
        elif chk == 2:  # 全选
            itemcnt = self.adminTagHighPermTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighPermTable.item(i, 4)
                if it == None:
                    continue
                it.setCheckState(2)
        else:
            pass

    def setAdminTagHighPermNowPageText(self):
        tot = self.adminTagHighPermTotal
        page = self.adminTagHighPermPage
        length = self.adminTagHighPermPageLength
        page_str = '0/0'
        if tot > 0:
            if tot % length > 0:
                page_str = '%d/%d' % (page + 1, (tot / length) + 1)
            else:
                page_str = '%d/%d' % (page + 1, tot / length)
        self.adminTagHighPermPageText.setText(_translate('adminTagHighPermPageText', page_str, None))

    # 设置权限列表
    def AdminTagHighPermSet(self, start, length):
        group = unicode(self.adminTagHighPermGroupName.text())
        # 查找当前组权限列表
        url = 'https://%s:%s/highperm/search/%s' % (
        self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey,
            'UserGroup': group,
            'Start': start,
            'Length': length
        }
        #print url, data
        param = {'Data': json.dumps(data)}
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.adminTagHighPermTotal = res['Total']

                # 清空列表
                for i in xrange(0, self.adminTagHighPermPageLength):
                    self.adminTagHighPermTable.setItem(i, 0, None)
                    self.adminTagHighPermTable.setItem(i, 1, None)
                    self.adminTagHighPermTable.setItem(i, 2, None)
                    self.adminTagHighPermTable.setItem(i, 3, None)
                    self.adminTagHighPermTable.setItem(i, 4, None)
                    self.adminTagHighPermPage = 0

                if res['PermItems'] != None:
                    # 添加列表
                    cnt = len(res['PermItems'])
                    for i in xrange(0, cnt):
                        newItem = QtGui.QTableWidgetItem(res['PermItems'][i]['ProcGroup'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighPermTable.setItem(i, 0, newItem)

                        newItem = QtGui.QTableWidgetItem(res['PermItems'][i]['ObjGroup'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighPermTable.setItem(i, 1, newItem)

                        newItem = QtGui.QTableWidgetItem(res['PermItems'][i]['ObjType'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighPermTable.setItem(i, 2, newItem)

                        newItem = QtGui.QTableWidgetItem(res['PermItems'][i]['Perm'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighPermTable.setItem(i, 3, newItem)

                        newItemChkbox = QtGui.QTableWidgetItem()
                        newItemChkbox.setCheckState(False)
                        newItemChkbox.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighPermTable.setItem(i, 4, newItemChkbox)
                    self.adminTagHighPermPage = start / self.adminTagHighPermPageLength
                self.setAdminTagHighPermNowPageText()
            else:
                QtGui.QMessageBox.about(self, u'错误提示', res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])

    # 上一页
    def onAdminTagHighPermPrev(self):
        start = self.adminTagHighPermPageLength * (self.adminTagHighPermPage - 1)
        if start < 0:
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是第一页')
        else:
            self.AdminTagHighPermSet(start, self.adminTagHighPermPageLength)

    # 下一页
    def onAdminTagHighPermNext(self):
        start = self.adminTagHighPermPageLength * (self.adminTagHighPermPage + 1)
        if start >= self.adminTagHighPermTotal:
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是最后一页')
        else:
            self.AdminTagHighPermSet(start, self.adminTagHighPermPageLength)

    # 删除权限列表
    def onAdminTagHighPermDel(self):
        itemcnt = self.adminTagHighPermTable.rowCount()
        dellist = []

        for i in range(0, itemcnt):
            it = self.adminTagHighPermTable.item(i, 4)
            if it == None:
                continue
            chk = it.checkState()
            if chk == 2:  # 状态有0和2
                user_group = unicode(self.adminTagHighPermGroupName.text())
                proc_group = unicode(self.adminTagHighPermTable.item(i, 0).text())
                obj_group = unicode(self.adminTagHighPermTable.item(i, 1).text())
                obj_type = unicode(self.adminTagHighPermTable.item(i, 2).text())
                perm_str = unicode(self.adminTagHighPermTable.item(i, 3).text())
                dellist.append({'user_group':user_group, 'proc_group':proc_group, 'obj_group':obj_group, 'obj_type':obj_type, 'perm_str':perm_str})

        url = 'https://%s:%s/highperm/del/%s' % (
        self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        for d in dellist:
            data = {
                'Tokey': self.Tokey,
                'UserGroup': d['user_group'],
                'ProcGroup': d['proc_group'],
                'ObjGroup': d['obj_group'],
                'ObjType': d['obj_type'],
                'Perm': d['perm_str'],
            }
            #print data
            param = {'Data': json.dumps(data)}
            rt = HttpsPost(url, param)
            #print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:
                    # QtGui.QMessageBox.about(self, u'提示', u'删除权限成功:' + user)
                    pass
                else:
                    QtGui.QMessageBox.about(self, u'错误提示', u'删除权限失败:' + json.dumps(d) + ':' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除权限失败:' + rt[1])

        # 刷新列表
        self.AdminTagHighPermSet(0, self.adminTagHighPermPageLength)


    # 设置组列表
    def onAdminTagHighPermGroupSet(self):
        url = 'https://%s:%s/highuser/groupsearch/%s' % (
        self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey
        }
        #print url, data
        param = {'Data': json.dumps(data)}
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.adminTagHighPermGroupTree.clear()
                if res['Groups'] == None:
                    return
                for group in res['Groups']:
                    self.AdddminTagHighPermGroupTree(group, group)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])

    # 弹出 - 添加权限
    def onAdminTagHighPermAdd(self):
        # 检查是否选择了用户组
        self.adminTagHighPermAddDlgUserGroup.setText(self.adminTagHighPermGroupName.text())
        user_group = unicode(self.adminTagHighPermAddDlgUserGroup.text())
        if user_group == u'':
            QtGui.QMessageBox.about(self, u'错误提示', u'请先选择用户组')
            return

        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighPermAddDlg.show()

        # 获取程序组选择框
        url = 'https://%s:%s/highproc/groupsearch/%s' % (
        self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey
        }
        #print url, data
        param = {'Data': json.dumps(data)}
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.adminTagHighPermAddDlgProcGroup.clear()
                if res['Groups'] == None:
                    return
                i = 0
                for group in res['Groups']:
                    self.adminTagHighPermAddDlgProcGroup.addItem(_fromUtf8(""))
                    self.adminTagHighPermAddDlgProcGroup.setItemText(i, _fromUtf8(group))
                    i += 1
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])

    # 弹出 - 权限 - OK
    def onAdminTagHighPermAddDlgOk(self):
        user_group = unicode(self.adminTagHighPermGroupName.text())
        proc_group = unicode(self.adminTagHighPermAddDlgProcGroup.currentText())
        obj_type = unicode(self.adminTagHighPermAddDlgObjType.currentText())
        obj_group = unicode(self.adminTagHighPermAddDlgObjGroup.currentText())
        perm_str = unicode(self.adminTagHighPermAddDlgPerm.currentText())

        # 添加权限
        url = 'https://%s:%s/highperm/add/%s' % (
        self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey,
            'UserGroup': user_group,
            'ProcGroup': proc_group,
            'ObjGroup': obj_group,
            'ObjType': obj_type,
            'Perm': perm_str,
        }
        #print url, data
        param = {'Data': json.dumps(data)}
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                # QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.AdminTagHighPermSet(0, self.adminTagHighPermPageLength)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加权限失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加权限失败:' + rt[1])


    # 弹出 - 权限 - Cancel
    def onAdminTagHighPermAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighPermAddDlg.hide()
        self.adminTagHighPermAddDlgUserGroup.setText(u'')


import images_rc
