# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui 
import sys
import json
import re
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
    
class AdminBoardHighObjNet(QtGui.QWidget):
    def __init__(self,parent=None):
        super(AdminBoardHighObjNet,self).__init__(parent)        
        #self.setupUi(self)

    def AddAdminTagHighObjNet(self):
        # 变量
        self.adminTagHighObjNetPageLength = 10
        self.adminTagHighObjNetPage = 0
        self.adminTagHighObjNetTotal = 0
        
        # 画线 左
        self.adminTagHighObjNetSpaceLeft = QtGui.QWidget(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.adminTagHighObjNetSpaceLeft.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjNetSpaceLeft.setObjectName(_fromUtf8('adminTagHighSpaceLeft'))

        # 画线 中
        self.adminTagHighObjNetSpaceMid = QtGui.QWidget(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetSpaceMid.setGeometry(QtCore.QRect(210, 0, 1, 295))
        self.adminTagHighObjNetSpaceMid.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjNetSpaceMid.setObjectName(_fromUtf8('adminTagHighSpaceMid'))

        # 画线 右
        self.adminTagHighObjNetSpaceRight = QtGui.QWidget(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.adminTagHighObjNetSpaceRight.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjNetSpaceRight.setObjectName(_fromUtf8('adminTagHighObjNetSpaceRight'))

        # 画线 底
        self.adminTagHighObjNetSpaceBottom = QtGui.QWidget(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.adminTagHighObjNetSpaceBottom.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjNetSpaceBottom.setObjectName(_fromUtf8('adminTagHighObjNetSpaceBottom'))

        # 组 - 添加
        self.adminTagHighObjNetGroupAdd = QtGui.QPushButton(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetGroupAdd.setGeometry(QtCore.QRect(30, 8, 75, 25))
        self.adminTagHighObjNetGroupAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjNetGroupAdd.setObjectName(_fromUtf8('adminTagHighObjNetGroupAdd'))
        self.adminTagHighObjNetGroupAdd.setText(_translate('adminTagHighObjNetGroupAdd', '添加+', None))

        # 组 - 删除
        self.adminTagHighObjNetGroupDel = QtGui.QPushButton(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetGroupDel.setGeometry(QtCore.QRect(125, 8, 75, 25))
        self.adminTagHighObjNetGroupDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjNetGroupDel.setObjectName(_fromUtf8('adminTagHighObjNetGroupDel'))
        self.adminTagHighObjNetGroupDel.setText(_translate('adminTagHighObjNetGroupDel', '删除+', None))

        # 组 - 列表
        self.adminTagHighObjNetGroupTree = QtGui.QTreeWidget(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetGroupTree.setGeometry(QtCore.QRect(30, 40, 170, 245))
        self.adminTagHighObjNetGroupTree.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjNetGroupTree.setObjectName(_fromUtf8('adminTagHighObjNetGroupTree'))
        self.adminTagHighObjNetGroupTree.setHeaderHidden(True)

        # 组标题显示
        self.adminTagHighObjNetGroupNameLable = QtGui.QLabel(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetGroupNameLable.setGeometry(QtCore.QRect(240, 5, 45, 30))
        self.adminTagHighObjNetGroupNameLable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighObjNetGroupNameLable.setObjectName(_fromUtf8('adminTagHighObjNetGroupNameLable'))
        self.adminTagHighObjNetGroupNameLable.setText(_translate('adminTagHighObjNetGroupNameLable', '当前组：', None))
        
        # 组名称 选择
        self.adminTagHighObjNetGroupName = QtGui.QLabel(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetGroupName.setGeometry(QtCore.QRect(285, 5, 120, 30))
        self.adminTagHighObjNetGroupName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighObjNetGroupName.setObjectName(_fromUtf8('adminTagHighObjNetGroupName'))
        self.adminTagHighObjNetGroupName.setText(_translate('adminTagHighObjNetGroupName', '', None))

        # 上一页
        self.adminTagHighObjNetPrev = QtGui.QPushButton(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetPrev.setGeometry(QtCore.QRect(440, 8, 70, 25))
        #self.adminTagHighObjNetPrev.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjNetPrev.setObjectName(_fromUtf8('adminTagHighObjNetPrev'))
        self.adminTagHighObjNetPrev.setText(_translate('adminTagHighObjNetPrev', '<<  上一页', None))

        # 下一页
        self.adminTagHighObjNetNext = QtGui.QPushButton(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetNext.setGeometry(QtCore.QRect(520, 8, 70, 25))
        #self.adminTagHighObjNetNext.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjNetNext.setObjectName(_fromUtf8('adminTagHighObjNetNext'))
        self.adminTagHighObjNetNext.setText(_translate('adminTagHighObjNetNext', '下一页  >>', None))

        # 客体网络 - 添加
        self.adminTagHighObjNetAdd = QtGui.QPushButton(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetAdd.setGeometry(QtCore.QRect(720, 8, 70, 25))
        self.adminTagHighObjNetAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjNetAdd.setObjectName(_fromUtf8('adminTagHighObjNetAdd'))
        self.adminTagHighObjNetAdd.setText(_translate('adminTagHighObjNetAdd', '添加地址', None))

        # 客体网络 - 删除
        self.adminTagHighObjNetDel = QtGui.QPushButton(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetDel.setGeometry(QtCore.QRect(800, 8, 70, 25))
        self.adminTagHighObjNetDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjNetDel.setObjectName(_fromUtf8('adminTagHighObjNetDel'))
        self.adminTagHighObjNetDel.setText(_translate('adminTagHighObjNetDel', '删除地址', None))

        # 客体网络 - 全选
        self.adminTagHighObjNetSelect = QtGui.QCheckBox(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetSelect.setGeometry(QtCore.QRect(900, 8, 55, 25))
        self.adminTagHighObjNetSelect.setObjectName(_fromUtf8('adminTagHighObjNetSelect'))
        self.adminTagHighObjNetSelect.setText(_translate('adminTagHighObjNetSelect', '全选', None))

        # 客体网络 - 列表表格
        self.adminTagHighObjNetTable = QtGui.QTableWidget(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetTable.setGeometry(QtCore.QRect(225, 40, 735, 245))
        self.adminTagHighObjNetTable.setObjectName(_fromUtf8('adminTagSpecialTable'))
        self.adminTagHighObjNetTable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.jpg);'))
        self.adminTagHighObjNetTable.verticalHeader().setVisible(False)
        self.adminTagHighObjNetTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagHighObjNetTable.setAlternatingRowColors(True)
        #list_widget.adminTagHighObjNetTable(QtGui.QAbstractItemView.SelectRows)
        self.adminTagHighObjNetTable.setRowCount(self.adminTagHighObjNetPageLength)
        self.adminTagHighObjNetTable.setColumnCount(2)
        self.adminTagHighObjNetTable.setHorizontalHeaderLabels([_fromUtf8('客体网络地址'),_fromUtf8('选择')])
        self.adminTagHighObjNetTable.setShowGrid(False)
        self.adminTagHighObjNetTable.setColumnWidth(0,400)
        self.adminTagHighObjNetTable.setColumnWidth(1,330)
        for i in range(0, self.adminTagHighObjNetPageLength):
            self.adminTagHighObjNetTable.setRowHeight(i,21)

        #####################################################
        # 添加客体网络弹出
        self.adminTagHighObjNetAddDlg = QtGui.QWidget(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetAddDlg.setGeometry(QtCore.QRect(300, 0, 254, 179))
        self.adminTagHighObjNetAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighObjNetAddDlg.setObjectName(_fromUtf8('adminTagHighObjNetAddDlg'))
        self.adminTagHighObjNetAddDlg.hide()

        # 添加客体网络弹出 - 客体网络类型 - 文字
        self.adminTagHighObjNetAddDlgTypeText = QtGui.QLabel(self.adminTagHighObjNetAddDlg)
        self.adminTagHighObjNetAddDlgTypeText.setGeometry(QtCore.QRect(20, 20, 70, 21))
        self.adminTagHighObjNetAddDlgTypeText.setObjectName(_fromUtf8('adminTagHighObjNetAddDlgTypeText'))
        self.adminTagHighObjNetAddDlgTypeText.setText(_translate('adminTagHighObjNetAddDlgTypeText', '网络类型：', None))

        # 添加客体网络弹出 - 客体网络类型 - 选择
        self.adminTagHighObjNetAddDlgType = QtGui.QComboBox(self.adminTagHighObjNetAddDlg)
        self.adminTagHighObjNetAddDlgType.setGeometry(QtCore.QRect(90, 20, 140, 22))
        self.adminTagHighObjNetAddDlgType.setObjectName(_fromUtf8("adminTagHighObjNetAddDlgType"))
        self.adminTagHighObjNetAddDlgType.setStyleSheet(_fromUtf8("border-image: url(:/images/bkg_btn2.png);"))
        self.adminTagHighObjNetAddDlgType.addItem(_fromUtf8(""))
        self.adminTagHighObjNetAddDlgType.addItem(_fromUtf8(""))        
        self.adminTagHighObjNetAddDlgType.setItemText(0, _fromUtf8("监听本地端口"))
        self.adminTagHighObjNetAddDlgType.setItemText(1, _fromUtf8("外连指定地址"))

        # 添加客体网络弹出 - 客体网络IP地址 - 文字
        self.adminTagHighObjNetAddDlgIPText = QtGui.QLabel(self.adminTagHighObjNetAddDlg)
        self.adminTagHighObjNetAddDlgIPText.setGeometry(QtCore.QRect(20, 60, 70, 21))
        self.adminTagHighObjNetAddDlgIPText.setObjectName(_fromUtf8('adminTagHighObjNetAddDlgIPText'))
        self.adminTagHighObjNetAddDlgIPText.setText(_translate('adminTagHighObjNetAddDlgIPText', 'IP 地址 ：', None))

        # 添加客体网络弹出 - 客体网络IP地址
        self.adminTagHighObjNetAddDlgIP = QtGui.QLineEdit(self.adminTagHighObjNetAddDlg)
        self.adminTagHighObjNetAddDlgIP.setGeometry(QtCore.QRect(90, 60, 140, 20))
        self.adminTagHighObjNetAddDlgIP.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white.png);'))
        self.adminTagHighObjNetAddDlgIP.setObjectName(_fromUtf8('adminTagHighObjNetAddDlgIP'))
        self.adminTagHighObjNetAddDlgIP.setText(_translate('adminTagHighObjNetAddDlgIP', '0.0.0.0', None))
        
        # 添加客体网络弹出 - 客体网络端口号 - 文字
        self.adminTagHighObjNetAddDlgPortText = QtGui.QLabel(self.adminTagHighObjNetAddDlg)
        self.adminTagHighObjNetAddDlgPortText.setGeometry(QtCore.QRect(20, 100, 70, 21))
        self.adminTagHighObjNetAddDlgPortText.setObjectName(_fromUtf8('adminTagHighObjNetAddDlgPortText'))
        self.adminTagHighObjNetAddDlgPortText.setText(_translate('adminTagHighObjNetAddDlgPortText', '端口号  ：', None))

        # 添加客体网络弹出 - 客体网络端口号
        self.adminTagHighObjNetAddDlgPort = QtGui.QLineEdit(self.adminTagHighObjNetAddDlg)
        self.adminTagHighObjNetAddDlgPort.setGeometry(QtCore.QRect(90, 100, 140, 20))
        self.adminTagHighObjNetAddDlgPort.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white.png);'))
        self.adminTagHighObjNetAddDlgPort.setObjectName(_fromUtf8('adminTagHighObjNetAddDlgPort'))
        self.adminTagHighObjNetAddDlgPort.setText(_translate('adminTagHighObjNetAddDlgPort', '0', None))

        # 添加客体网络弹出 - 添加
        self.adminTagHighObjNetAddDlgOk = QtGui.QPushButton(self.adminTagHighObjNetAddDlg)
        self.adminTagHighObjNetAddDlgOk.setGeometry(QtCore.QRect(26, 140, 75, 23))
        self.adminTagHighObjNetAddDlgOk.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjNetAddDlgOk.setObjectName(_fromUtf8('adminTagHighObjNetAddDlgOk'))
        self.adminTagHighObjNetAddDlgOk.setText(_translate('adminTagHighObjNetAddDlgOk', '添加', None))

        # 添加客体网络弹出 - 取消
        self.adminTagHighObjNetAddDlgCancel = QtGui.QPushButton(self.adminTagHighObjNetAddDlg)
        self.adminTagHighObjNetAddDlgCancel.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.adminTagHighObjNetAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjNetAddDlgCancel.setObjectName(_fromUtf8('adminTagHighObjNetAddDlgOk'))
        self.adminTagHighObjNetAddDlgCancel.setText(_translate('adminTagHighObjNetAddDlgCancel', '取消', None))

        ###########################################################
        # 添加组 弹出
        self.adminTagHighObjNetGroupAddDlg = QtGui.QWidget(self.adminTagHighTagObjNetBkg)
        self.adminTagHighObjNetGroupAddDlg.setGeometry(QtCore.QRect(300, 0, 271, 105))
        self.adminTagHighObjNetGroupAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighObjNetGroupAddDlg.setObjectName(_fromUtf8('adminTagHighObjNetGroupAddDlg'))
        self.adminTagHighObjNetGroupAddDlg.hide()

        # 添加组 弹出 - 输入组名称
        self.adminTagHighObjNetGroupAddDlgText = QtGui.QLabel(self.adminTagHighObjNetGroupAddDlg)
        self.adminTagHighObjNetGroupAddDlgText.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.adminTagHighObjNetGroupAddDlgText.setObjectName(_fromUtf8('adminTagHighObjNetGroupAddDlgText'))
        self.adminTagHighObjNetGroupAddDlgText.setText(_translate('adminTagHighObjNetGroupAddDlgText', '请输入组名称:', None))

        # 添加组 弹出 - 组名称
        self.adminTagHighObjNetGroupAddDlgName = QtGui.QLineEdit(self.adminTagHighObjNetGroupAddDlg)
        self.adminTagHighObjNetGroupAddDlgName.setGeometry(QtCore.QRect(20, 30, 231, 31))
        self.adminTagHighObjNetGroupAddDlgName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white.png);'))
        self.adminTagHighObjNetGroupAddDlgName.setObjectName(_fromUtf8('adminTagHighObjNetGroupAddDlgName'))
        self.adminTagHighObjNetGroupAddDlgName.setText(_translate('adminTagHighObjNetGroupAddDlgName', '', None))

        # 添加组 弹出 - 添加
        self.adminTagHighObjNetGroupAddDlgOK = QtGui.QPushButton(self.adminTagHighObjNetGroupAddDlg)
        self.adminTagHighObjNetGroupAddDlgOK.setGeometry(QtCore.QRect(40, 70, 75, 23))
        self.adminTagHighObjNetGroupAddDlgOK.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjNetGroupAddDlgOK.setObjectName(_fromUtf8('adminTagHighObjNetGroupAddDlgOK'))
        self.adminTagHighObjNetGroupAddDlgOK.setText(_translate('adminTagHighObjNetGroupAddDlgOK', '添加', None))

        # 添加组 弹出 - 取消
        self.adminTagHighObjNetGroupAddDlgCancel = QtGui.QPushButton(self.adminTagHighObjNetGroupAddDlg)
        self.adminTagHighObjNetGroupAddDlgCancel.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.adminTagHighObjNetGroupAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjNetGroupAddDlgCancel.setObjectName(_fromUtf8('adminTagHighObjNetGroupAddDlgCancel'))
        self.adminTagHighObjNetGroupAddDlgCancel.setText(_translate('adminTagHighObjNetGroupAddDlgCancel', '取消', None))
        
        ###############################################################
        # 添加组
        self.onAdminTagHighObjNetGroupSet()
        
        # 组列表消息
        self.connect(self.adminTagHighObjNetGroupTree, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onAdminTagHighObjNetGroupClick)
        self.connect(self.adminTagHighObjNetGroupAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetGroupAdd)
        self.connect(self.adminTagHighObjNetGroupDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetGroupDel)
        self.connect(self.adminTagHighObjNetGroupAddDlgOK, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetGroupAddDlgOK)
        self.connect(self.adminTagHighObjNetGroupAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetGroupAddDlgCancel)
        
        # 添加客体网络消息
        self.connect(self.adminTagHighObjNetAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetAdd)
        self.connect(self.adminTagHighObjNetPrev, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetPrev)
        self.connect(self.adminTagHighObjNetNext, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetNext)
        self.connect(self.adminTagHighObjNetDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetDel)
        self.connect(self.adminTagHighObjNetSelect, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetSelect)
        self.connect(self.adminTagHighObjNetAddDlgOk, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetAddDlgOk)
        self.connect(self.adminTagHighObjNetAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjNetAddDlgCancel)
        self.connect(self.adminTagHighObjNetAddDlgType, QtCore.SIGNAL('activated(int)'), self.adminTagHighObjNetAddDlgTypeClick)


    def onAdminTagHighObjNetGroupClick(self, item, column):
        if self.AdminBoardCheckPopUp():
            return
        self.adminTagHighObjNetGroupName.setText(item.text(column))
        self.AdminTagHighObjNetSet(0, self.adminTagHighObjNetPageLength)

    def AdddminTagHighObjNetGroupTree(self, title, data):
        root = self.adminTagHighObjNetGroupTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)

    def adminTagHighObjNetAddDlgTypeClick(self, index):
        if index == 0:
            self.adminTagHighObjNetAddDlgIP.setText(u'0.0.0.0')
        else:
            self.adminTagHighObjNetAddDlgIP.setText(u'')
        
    # 客体网络 - 全选
    def onAdminTagHighObjNetSelect(self):
        chk = self.adminTagHighObjNetSelect.checkState()
        if chk == 0: #全不选
            itemcnt = self.adminTagHighObjNetTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighObjNetTable.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(False)
        elif chk == 2: #全选
            itemcnt = self.adminTagHighObjNetTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighObjNetTable.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(2)
        else:
            pass
        
    # 设置客体网络列表
    def AdminTagHighObjNetSet(self, start, length):
        group = unicode(self.adminTagHighObjNetGroupName.text())
        print group, start, length
        # 查找当前组客体网络列表
        url = 'https://%s:%s/highobjnet/search/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group,
            'Start'   : start,
            'Length'  : length
        }
        print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.adminTagHighObjNetTotal = res['Total']
                
                # 清空列表
                for i in xrange(0, self.adminTagHighObjNetPageLength):
                    self.adminTagHighObjNetTable.setItem(i, 0, None)
                    self.adminTagHighObjNetTable.setItem(i, 1, None)
                    self.adminTagHighObjNetPage = 0
                if res['ObjNets'] != None:
                    # 添加列表
                    cnt = len(res['ObjNets'])
                    for i in xrange(0, cnt):
                        newItem = QtGui.QTableWidgetItem(res['ObjNets'][i])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighObjNetTable.setItem(i, 0, newItem)
                    
                        newItemChkbox = QtGui.QTableWidgetItem()
                        newItemChkbox.setCheckState(False)
                        newItemChkbox.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighObjNetTable.setItem(i, 1, newItemChkbox)
                    self.adminTagHighObjNetPage = start / self.adminTagHighObjNetPageLength
            else:
                QtGui.QMessageBox.about(self, u'错误提示', res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])
        

    # 上一页
    def onAdminTagHighObjNetPrev(self):
        start = self.adminTagHighObjNetPageLength * (self.adminTagHighObjNetPage - 1)
        if start < 0 :
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是第一页')
        else:
            self.AdminTagHighObjNetSet(start, self.adminTagHighObjNetPageLength)
        

    # 下一页
    def onAdminTagHighObjNetNext(self):
        start = self.adminTagHighObjNetPageLength * (self.adminTagHighObjNetPage + 1)
        if start >= self.adminTagHighObjNetTotal :
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是最后一页')
        else:
            self.AdminTagHighObjNetSet(start, self.adminTagHighObjNetPageLength)

    # 删除客体网络列表
    def onAdminTagHighObjNetDel(self):
        itemcnt = self.adminTagHighObjNetTable.rowCount()
        dellist = []
        
        for i in range(0, itemcnt):
            it = self.adminTagHighObjNetTable.item(i, 1)
            if it == None:
                continue
            chk = it.checkState()
            if chk == 2: # 状态有0和2
                net = unicode(self.adminTagHighObjNetTable.item(i, 0).text())
                dellist.append(net)

        url = 'https://%s:%s/highobjnet/del/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        print url
        for net in dellist:
            data = {
                'Tokey'   : self.Tokey,
                'ObjNet'    : net
            }
            print data
            param = {'Data' : json.dumps(data)} 
            rt = HttpsPost(url, param)
            print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:             
                    #QtGui.QMessageBox.about(self, u'提示', u'删除客体网络成功:' + net)
                    pass
                else:
                    QtGui.QMessageBox.about(self, u'错误提示', u'删除客体网络地址失败:' + net + ':' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除客体网络地址失败:' + rt[1])
                
        #刷新列表
        self.AdminTagHighObjNetSet(0, self.adminTagHighObjNetPageLength)
        
    # 设置组列表
    def onAdminTagHighObjNetGroupSet(self):
        url = 'https://%s:%s/highobjnet/groupsearch/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey
        }
        print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:             
                self.adminTagHighObjNetGroupTree.clear()
                if res['Groups'] == None:
                    return
                for group in res['Groups']:                    
                    self.AdddminTagHighObjNetGroupTree(group, group)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])
    
    # 弹出 - 添加组
    def onAdminTagHighObjNetGroupAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighObjNetGroupAddDlg.show()

    # 删除组
    def onAdminTagHighObjNetGroupDel(self):
        group = unicode(self.adminTagHighObjNetGroupName.text())
        if group == '':
            QtGui.QMessageBox.about(self, u'设置', u'请选择一个组')
            return
        url = 'https://%s:%s/highobjnet/groupdel/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group
        }
        print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.onAdminTagHighObjNetGroupSet()
                QtGui.QMessageBox.about(self, u'设置', u'删除组成功:')
                self.adminTagHighObjNetGroupName.setText(u'')
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除组失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'删除组失败:' + rt[1])
    

    # 弹出 - 添加组 - OK
    def onAdminTagHighObjNetGroupAddDlgOK(self):
        self.AdminBoardUnsetPopUp()        
        self.adminTagHighObjNetGroupAddDlg.hide()

        group = unicode(self.adminTagHighObjNetGroupAddDlgName.text())

        if group == '':
            QtGui.QMessageBox.about(self, u'设置', u'组名称不能为空')
            return
        
        url = 'https://%s:%s/highobjnet/groupadd/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group
        }
        print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:            
                self.onAdminTagHighObjNetGroupSet()
                QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.adminTagHighObjNetGroupAddDlgName.setText(_fromUtf8(''))
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加组失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加组失败:' + rt[1])

    # 弹出 - 添加组 - Cancel
    def onAdminTagHighObjNetGroupAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighObjNetGroupAddDlg.hide()

    # 弹出 - 添加客体网络
    def onAdminTagHighObjNetAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighObjNetAddDlg.show()
        self.adminTagHighObjNetAddDlgType.setCurrentIndex(0)
        self.adminTagHighObjNetAddDlgIP.setText(_translate('adminTagHighObjNetAddDlgIP', '0.0.0.0', None))
        self.adminTagHighObjNetAddDlgPort.setText(_translate('adminTagHighObjNetAddDlgPort', '0', None))

    # 弹出 - 客体网络 - OK
    def onAdminTagHighObjNetAddDlgOk(self):
        group = unicode(self.adminTagHighObjNetGroupName.text())
        nettype = unicode(self.adminTagHighObjNetAddDlgType.currentText())
        ip  = unicode(self.adminTagHighObjNetAddDlgIP.text())
        port = unicode(self.adminTagHighObjNetAddDlgPort.text())

        rt = re.match(u'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$', ip)
        if rt == None:
            QtGui.QMessageBox.about(self, u'错误提示', u'IP4地址格式错误')
            return
        try:
            iport = int(port)
            if iport < 1 or iport > 65535:
                QtGui.QMessageBox.about(self, u'错误提示', u'端口格式错误')
                return
        except:
            QtGui.QMessageBox.about(self, u'错误提示', u'端口格式错误')
            return

        addr = u'%s:%s' %(ip, port)

        print nettype, addr

        # 添加客体网络
        url = 'https://%s:%s/highobjnet/add/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group,
            'ObjNet'  : addr,
        }
        print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:             
                #QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.AdminTagHighObjNetSet(0, self.adminTagHighObjNetPageLength)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加客体网络失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加客体网络失败:' + rt[1])
        

    # 弹出 - 客体网络 - Cancel
    def onAdminTagHighObjNetAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighObjNetAddDlg.hide()
        self.adminTagHighObjNetAddDlgIP.setText(u'')
        self.adminTagHighObjNetAddDlgPort.setText(u'')        
        
import images_rc
