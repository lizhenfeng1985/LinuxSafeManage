# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui 
import sys
import os
import re
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
    
class AdminBoardHighObjFile(QtGui.QWidget):
    def __init__(self,parent=None):
        super(AdminBoardHighObjFile,self).__init__(parent)        
        #self.setupUi(self)

    def AddAdminTagHighObjFile(self):
        # 变量
        self.adminTagHighObjFilePageLength = 10
        self.adminTagHighObjFilePage = 0
        self.adminTagHighObjFileTotal = 0
        
        # 画线 左
        self.adminTagHighObjFileSpaceLeft = QtGui.QWidget(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.adminTagHighObjFileSpaceLeft.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjFileSpaceLeft.setObjectName(_fromUtf8('adminTagHighSpaceLeft'))

        # 画线 中
        self.adminTagHighObjFileSpaceMid = QtGui.QWidget(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileSpaceMid.setGeometry(QtCore.QRect(210, 0, 1, 295))
        self.adminTagHighObjFileSpaceMid.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjFileSpaceMid.setObjectName(_fromUtf8('adminTagHighSpaceMid'))

        # 画线 右
        self.adminTagHighObjFileSpaceRight = QtGui.QWidget(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.adminTagHighObjFileSpaceRight.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjFileSpaceRight.setObjectName(_fromUtf8('adminTagHighObjFileSpaceRight'))

        # 画线 底
        self.adminTagHighObjFileSpaceBottom = QtGui.QWidget(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.adminTagHighObjFileSpaceBottom.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjFileSpaceBottom.setObjectName(_fromUtf8('adminTagHighObjFileSpaceBottom'))

        # 组 - 添加
        self.adminTagHighObjFileGroupAdd = QtGui.QPushButton(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileGroupAdd.setGeometry(QtCore.QRect(30, 8, 75, 25))
        self.adminTagHighObjFileGroupAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjFileGroupAdd.setObjectName(_fromUtf8('adminTagHighObjFileGroupAdd'))
        self.adminTagHighObjFileGroupAdd.setText(_translate('adminTagHighObjFileGroupAdd', '添加+', None))

        # 组 - 删除
        self.adminTagHighObjFileGroupDel = QtGui.QPushButton(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileGroupDel.setGeometry(QtCore.QRect(125, 8, 75, 25))
        self.adminTagHighObjFileGroupDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjFileGroupDel.setObjectName(_fromUtf8('adminTagHighObjFileGroupDel'))
        self.adminTagHighObjFileGroupDel.setText(_translate('adminTagHighObjFileGroupDel', '删除+', None))

        # 组 - 列表
        self.adminTagHighObjFileGroupTree = QtGui.QTreeWidget(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileGroupTree.setGeometry(QtCore.QRect(30, 40, 170, 245))
        self.adminTagHighObjFileGroupTree.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjFileGroupTree.setObjectName(_fromUtf8('adminTagHighObjFileGroupTree'))
        self.adminTagHighObjFileGroupTree.setHeaderHidden(True)

        # 组标题显示
        self.adminTagHighObjFileGroupNameLable = QtGui.QLabel(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileGroupNameLable.setGeometry(QtCore.QRect(240, 5, 45, 30))
        self.adminTagHighObjFileGroupNameLable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighObjFileGroupNameLable.setObjectName(_fromUtf8('adminTagHighObjFileGroupNameLable'))
        self.adminTagHighObjFileGroupNameLable.setText(_translate('adminTagHighObjFileGroupNameLable', '当前组：', None))
        
        # 组名称 选择
        self.adminTagHighObjFileGroupName = QtGui.QLabel(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileGroupName.setGeometry(QtCore.QRect(285, 5, 120, 30))
        self.adminTagHighObjFileGroupName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighObjFileGroupName.setObjectName(_fromUtf8('adminTagHighObjFileGroupName'))
        self.adminTagHighObjFileGroupName.setText(_translate('adminTagHighObjFileGroupName', '', None))

        # 上一页
        self.adminTagHighObjFilePrev = QtGui.QPushButton(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFilePrev.setGeometry(QtCore.QRect(440, 8, 70, 25))
        #self.adminTagHighObjFilePrev.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjFilePrev.setObjectName(_fromUtf8('adminTagHighObjFilePrev'))
        self.adminTagHighObjFilePrev.setText(_translate('adminTagHighObjFilePrev', '<<  上一页', None))

        # 下一页
        self.adminTagHighObjFileNext = QtGui.QPushButton(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileNext.setGeometry(QtCore.QRect(520, 8, 70, 25))
        #self.adminTagHighObjFileNext.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjFileNext.setObjectName(_fromUtf8('adminTagHighObjFileNext'))
        self.adminTagHighObjFileNext.setText(_translate('adminTagHighObjFileNext', '下一页  >>', None))

        # 客体文件 - 添加
        self.adminTagHighObjFileAdd = QtGui.QPushButton(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileAdd.setGeometry(QtCore.QRect(720, 8, 70, 25))
        self.adminTagHighObjFileAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjFileAdd.setObjectName(_fromUtf8('adminTagHighObjFileAdd'))
        self.adminTagHighObjFileAdd.setText(_translate('adminTagHighObjFileAdd', '添加文件', None))

        # 客体文件 - 删除
        self.adminTagHighObjFileDel = QtGui.QPushButton(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileDel.setGeometry(QtCore.QRect(800, 8, 70, 25))
        self.adminTagHighObjFileDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjFileDel.setObjectName(_fromUtf8('adminTagHighObjFileDel'))
        self.adminTagHighObjFileDel.setText(_translate('adminTagHighObjFileDel', '删除文件', None))

        # 客体文件 - 全选
        self.adminTagHighObjFileSelect = QtGui.QCheckBox(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileSelect.setGeometry(QtCore.QRect(900, 8, 55, 25))
        self.adminTagHighObjFileSelect.setObjectName(_fromUtf8('adminTagHighObjFileSelect'))
        self.adminTagHighObjFileSelect.setText(_translate('adminTagHighObjFileSelect', '全选', None))

        # 客体文件 - 列表表格
        self.adminTagHighObjFileTable = QtGui.QTableWidget(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileTable.setGeometry(QtCore.QRect(225, 40, 735, 245))
        self.adminTagHighObjFileTable.setObjectName(_fromUtf8('adminTagSpecialTable'))
        self.adminTagHighObjFileTable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.jpg);'))
        self.adminTagHighObjFileTable.verticalHeader().setVisible(False)
        self.adminTagHighObjFileTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagHighObjFileTable.setAlternatingRowColors(True)
        #list_widget.adminTagHighObjFileTable(QtGui.QAbstractItemView.SelectRows)
        self.adminTagHighObjFileTable.setRowCount(self.adminTagHighObjFilePageLength)
        self.adminTagHighObjFileTable.setColumnCount(2)
        self.adminTagHighObjFileTable.setHorizontalHeaderLabels([_fromUtf8('客体文件名'),_fromUtf8('选择')])
        self.adminTagHighObjFileTable.setShowGrid(False)
        self.adminTagHighObjFileTable.setColumnWidth(0,400)
        self.adminTagHighObjFileTable.setColumnWidth(1,330)
        for i in range(0, self.adminTagHighObjFilePageLength):
            self.adminTagHighObjFileTable.setRowHeight(i,21)

        #####################################################
        # 添加客体文件弹出
        self.adminTagHighObjFileAddDlg = QtGui.QWidget(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileAddDlg.setGeometry(QtCore.QRect(300, 0, 457, 300))
        self.adminTagHighObjFileAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighObjFileAddDlg.setObjectName(_fromUtf8('adminTagHighObjFileAddDlg'))
        self.adminTagHighObjFileAddDlg.hide()

        # 添加客体文件弹出 - 请选择客体文件
        self.adminTagHighObjFileAddDlgTextLab = QtGui.QLabel(self.adminTagHighObjFileAddDlg)
        self.adminTagHighObjFileAddDlgTextLab.setGeometry(QtCore.QRect(20, 10, 70, 21))
        self.adminTagHighObjFileAddDlgTextLab.setObjectName(_fromUtf8('adminTagHighObjFileAddDlgText'))
        self.adminTagHighObjFileAddDlgTextLab.setText(_translate('adminTagHighObjFileAddDlgText', '请选择客体文件:', None))

        # 添加客体文件弹出 - 客体文件列表
        self.adminTagHighObjFileAddDlgTree = QtGui.QTreeWidget(self.adminTagHighObjFileAddDlg)
        self.adminTagHighObjFileAddDlgTree.setGeometry(QtCore.QRect(10, 35, 431, 192))
        self.adminTagHighObjFileAddDlgTree.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjFileAddDlgTree.setObjectName(_fromUtf8('adminTagHighObjFileAddDlgTree'))
        self.adminTagHighObjFileAddDlgTree.setHeaderHidden(True)

        # 添加客体文件弹出 - 客体文件名称 - 文字
        self.adminTagHighObjFileAddDlgFNameText = QtGui.QLineEdit(self.adminTagHighObjFileAddDlg)
        self.adminTagHighObjFileAddDlgFNameText.setGeometry(QtCore.QRect(10, 240, 40, 21))
        self.adminTagHighObjFileAddDlgFNameText.setObjectName(_fromUtf8('adminTagHighObjFileAddDlgUNameText'))
        self.adminTagHighObjFileAddDlgFNameText.setText(_translate('adminTagHighObjFileAddDlgUNameText', '路径:', None))
        
        # 添加客体文件弹出 - 客体文件名称
        self.adminTagHighObjFileAddDlgFName = QtGui.QLineEdit(self.adminTagHighObjFileAddDlg)
        self.adminTagHighObjFileAddDlgFName.setGeometry(QtCore.QRect(50, 240, 230, 21))
        self.adminTagHighObjFileAddDlgFName.setObjectName(_fromUtf8('adminTagHighObjFileAddDlgUName'))
        self.adminTagHighObjFileAddDlgFName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white_frame.png);'))
        self.adminTagHighObjFileAddDlgFName.setText(_translate('adminTagHighObjFileAddDlgUName', '', None))

        # 添加客体文件弹出 - 扩展名 - 文字
        self.adminTagHighObjFileAddDlgExtText = QtGui.QLineEdit(self.adminTagHighObjFileAddDlg)
        self.adminTagHighObjFileAddDlgExtText.setGeometry(QtCore.QRect(290, 240, 80, 21))
        self.adminTagHighObjFileAddDlgExtText.setObjectName(_fromUtf8('adminTagHighObjFileAddDlgExtText'))
        self.adminTagHighObjFileAddDlgExtText.setText(_translate('adminTagHighObjFileAddDlgExtText', '扩展名(.XXX):', None))

        # 添加客体文件弹出 - 扩展名
        self.adminTagHighObjFileAddDlgExt = QtGui.QLineEdit(self.adminTagHighObjFileAddDlg)
        self.adminTagHighObjFileAddDlgExt.setGeometry(QtCore.QRect(375, 240, 65, 21))
        self.adminTagHighObjFileAddDlgExt.setObjectName(_fromUtf8('adminTagHighObjFileAddDlgExt'))
        self.adminTagHighObjFileAddDlgExt.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white_frame.png);'))
        self.adminTagHighObjFileAddDlgExt.setText(_translate('adminTagHighObjFileAddDlgExt', '', None))
        
        # 添加客体文件弹出 - 添加
        self.adminTagHighObjFileAddDlgOk = QtGui.QPushButton(self.adminTagHighObjFileAddDlg)
        self.adminTagHighObjFileAddDlgOk.setGeometry(QtCore.QRect(120, 270, 75, 23))
        self.adminTagHighObjFileAddDlgOk.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjFileAddDlgOk.setObjectName(_fromUtf8('adminTagHighObjFileAddDlgOk'))
        self.adminTagHighObjFileAddDlgOk.setText(_translate('adminTagHighObjFileAddDlgOk', '添加', None))

        # 添加客体文件弹出 - 取消
        self.adminTagHighObjFileAddDlgCancel = QtGui.QPushButton(self.adminTagHighObjFileAddDlg)
        self.adminTagHighObjFileAddDlgCancel.setGeometry(QtCore.QRect(250, 270, 75, 23))
        self.adminTagHighObjFileAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjFileAddDlgCancel.setObjectName(_fromUtf8('adminTagHighObjFileAddDlgOk'))
        self.adminTagHighObjFileAddDlgCancel.setText(_translate('adminTagHighObjFileAddDlgCancel', '取消', None))

        ###########################################################
        # 添加组 弹出
        self.adminTagHighObjFileGroupAddDlg = QtGui.QWidget(self.adminTagHighTagObjFileBkg)
        self.adminTagHighObjFileGroupAddDlg.setGeometry(QtCore.QRect(300, 0, 271, 105))
        self.adminTagHighObjFileGroupAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighObjFileGroupAddDlg.setObjectName(_fromUtf8('adminTagHighObjFileGroupAddDlg'))
        self.adminTagHighObjFileGroupAddDlg.hide()

        # 添加组 弹出 - 输入组名称
        self.adminTagHighObjFileGroupAddDlgText = QtGui.QLabel(self.adminTagHighObjFileGroupAddDlg)
        self.adminTagHighObjFileGroupAddDlgText.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.adminTagHighObjFileGroupAddDlgText.setObjectName(_fromUtf8('adminTagHighObjFileGroupAddDlgText'))
        self.adminTagHighObjFileGroupAddDlgText.setText(_translate('adminTagHighObjFileGroupAddDlgText', '请输入组名称:', None))

        # 添加组 弹出 - 组名称
        self.adminTagHighObjFileGroupAddDlgName = QtGui.QLineEdit(self.adminTagHighObjFileGroupAddDlg)
        self.adminTagHighObjFileGroupAddDlgName.setGeometry(QtCore.QRect(20, 30, 231, 31))
        self.adminTagHighObjFileGroupAddDlgName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white.png);'))
        self.adminTagHighObjFileGroupAddDlgName.setObjectName(_fromUtf8('adminTagHighObjFileGroupAddDlgName'))
        self.adminTagHighObjFileGroupAddDlgName.setText(_translate('adminTagHighObjFileGroupAddDlgName', '', None))

        # 添加组 弹出 - 添加
        self.adminTagHighObjFileGroupAddDlgOK = QtGui.QPushButton(self.adminTagHighObjFileGroupAddDlg)
        self.adminTagHighObjFileGroupAddDlgOK.setGeometry(QtCore.QRect(40, 70, 75, 23))
        self.adminTagHighObjFileGroupAddDlgOK.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjFileGroupAddDlgOK.setObjectName(_fromUtf8('adminTagHighObjFileGroupAddDlgOK'))
        self.adminTagHighObjFileGroupAddDlgOK.setText(_translate('adminTagHighObjFileGroupAddDlgOK', '添加', None))

        # 添加组 弹出 - 取消
        self.adminTagHighObjFileGroupAddDlgCancel = QtGui.QPushButton(self.adminTagHighObjFileGroupAddDlg)
        self.adminTagHighObjFileGroupAddDlgCancel.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.adminTagHighObjFileGroupAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjFileGroupAddDlgCancel.setObjectName(_fromUtf8('adminTagHighObjFileGroupAddDlgCancel'))
        self.adminTagHighObjFileGroupAddDlgCancel.setText(_translate('adminTagHighObjFileGroupAddDlgCancel', '取消', None))
        
        ###############################################################
        # 添加组
        self.onAdminTagHighObjFileGroupSet()
        
        # 组列表消息
        self.connect(self.adminTagHighObjFileGroupTree, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onAdminTagHighObjFileGroupClick)
        self.connect(self.adminTagHighObjFileGroupAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFileGroupAdd)
        self.connect(self.adminTagHighObjFileGroupDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFileGroupDel)
        self.connect(self.adminTagHighObjFileGroupAddDlgOK, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFileGroupAddDlgOK)
        self.connect(self.adminTagHighObjFileGroupAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFileGroupAddDlgCancel)
        
        # 添加客体文件消息
        self.connect(self.adminTagHighObjFileAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFileAdd)
        self.connect(self.adminTagHighObjFilePrev, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFilePrev)
        self.connect(self.adminTagHighObjFileNext, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFileNext)
        self.connect(self.adminTagHighObjFileDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFileDel)
        self.connect(self.adminTagHighObjFileSelect, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFileSelect)
        self.connect(self.adminTagHighObjFileAddDlgOk, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFileAddDlgOk)
        self.connect(self.adminTagHighObjFileAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjFileAddDlgCancel)
        self.connect(self.adminTagHighObjFileAddDlgTree, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onAdminTagHighObjFileAddDlgTreeClick)
        

    def AdddminTagHighObjFileGroupTree(self, title, data):
        root = self.adminTagHighObjFileGroupTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)
        #item.setCheckState (0, QtCore.Qt.Unchecked)

    def AdddminTagHighObjFileTree(self, title, data):
        root = self.adminTagHighObjFileAddDlgTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)

    def onAdminTagHighObjFileGroupClick(self, item, column):
        if self.AdminBoardCheckPopUp():
            return
        self.adminTagHighObjFileGroupName.setText(item.text(column))
        self.AdminTagHighObjFileSet(0, self.adminTagHighObjFilePageLength)

    def onAdminTagHighObjFileAddDlgTreeClick(self, item, column):
        self.adminTagHighObjFileAddDlgFName.setText(item.text(column))


    # 客体文件 - 全选
    def onAdminTagHighObjFileSelect(self):
        chk = self.adminTagHighObjFileSelect.checkState()
        if chk == 0: #全不选
            itemcnt = self.adminTagHighObjFileTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighObjFileTable.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(False)
        elif chk == 2: #全选
            itemcnt = self.adminTagHighObjFileTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighObjFileTable.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(2)
        else:
            pass
        
    # 设置客体文件列表
    def AdminTagHighObjFileSet(self, start, length):
        group = unicode(self.adminTagHighObjFileGroupName.text())
        print group, start, length
        # 查找当前组客体文件列表
        url = 'https://%s:%s/highobjfile/search/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.adminTagHighObjFileTotal = res['Total']
                
                # 清空列表
                for i in xrange(0, self.adminTagHighObjFilePageLength):
                    self.adminTagHighObjFileTable.setItem(i, 0, None)
                    self.adminTagHighObjFileTable.setItem(i, 1, None)
                    self.adminTagHighObjFilePage = 0
                if res['ObjFiles'] != None:
                    # 添加列表
                    cnt = len(res['ObjFiles'])
                    for i in xrange(0, cnt):
                        newItem = QtGui.QTableWidgetItem(res['ObjFiles'][i])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighObjFileTable.setItem(i, 0, newItem)
                    
                        newItemChkbox = QtGui.QTableWidgetItem()
                        newItemChkbox.setCheckState(False)
                        newItemChkbox.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighObjFileTable.setItem(i, 1, newItemChkbox)
                    self.adminTagHighObjFilePage = start / self.adminTagHighObjFilePageLength
            else:
                QtGui.QMessageBox.about(self, u'错误提示', res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])
        

    # 上一页
    def onAdminTagHighObjFilePrev(self):
        start = self.adminTagHighObjFilePageLength * (self.adminTagHighObjFilePage - 1)
        if start < 0 :
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是第一页')
        else:
            self.AdminTagHighObjFileSet(start, self.adminTagHighObjFilePageLength)
        

    # 下一页
    def onAdminTagHighObjFileNext(self):
        start = self.adminTagHighObjFilePageLength * (self.adminTagHighObjFilePage + 1)
        if start >= self.adminTagHighObjFileTotal :
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是最后一页')
        else:
            self.AdminTagHighObjFileSet(start, self.adminTagHighObjFilePageLength)

    # 删除客体文件列表
    def onAdminTagHighObjFileDel(self):
        itemcnt = self.adminTagHighObjFileTable.rowCount()
        dellist = []
        
        for i in range(0, itemcnt):
            it = self.adminTagHighObjFileTable.item(i, 1)
            if it == None:
                continue
            chk = it.checkState()
            if chk == 2: # 状态有0和2
                ofile = unicode(self.adminTagHighObjFileTable.item(i, 0).text())
                dellist.append(ofile)

        url = 'https://%s:%s/highobjfile/del/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        print url
        for ofile in dellist:
            data = {
                'Tokey'   : self.Tokey,
                'ObjFile'    : ofile
            }
            print data
            param = {'Data' : json.dumps(data)} 
            rt = HttpsPost(url, param)
            print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:             
                    #QtGui.QMessageBox.about(self, u'提示', u'删除客体文件成功:' + ofile)
                    pass
                else:
                    QtGui.QMessageBox.about(self, u'错误提示', u'删除客体文件失败:' + ofile + ':' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除客体文件失败:' + rt[1])
                
        #刷新列表
        self.AdminTagHighObjFileSet(0, self.adminTagHighObjFilePageLength)
        
    # 设置组列表
    def onAdminTagHighObjFileGroupSet(self):
        url = 'https://%s:%s/highobjfile/groupsearch/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.adminTagHighObjFileGroupTree.clear()
                if res['Groups'] == None:
                    return
                for group in res['Groups']:
                    self.AdddminTagHighObjFileGroupTree(group, group)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])
    
    # 弹出 - 添加组
    def onAdminTagHighObjFileGroupAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighObjFileGroupAddDlg.show()

    # 删除组
    def onAdminTagHighObjFileGroupDel(self):
        group = unicode(self.adminTagHighObjFileGroupName.text())
        if group == '':
            QtGui.QMessageBox.about(self, u'设置', u'请选择一个组')
            return
        url = 'https://%s:%s/highobjfile/groupdel/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                QtGui.QMessageBox.about(self, u'设置', u'删除组成功:')
                self.adminTagHighObjFileGroupName.setText(u'')
                self.onAdminTagHighObjFileGroupSet()
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除组失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'删除组失败:' + rt[1])
    

    # 弹出 - 添加组 - OK
    def onAdminTagHighObjFileGroupAddDlgOK(self):
        self.AdminBoardUnsetPopUp()        
        self.adminTagHighObjFileGroupAddDlg.hide()

        group = unicode(self.adminTagHighObjFileGroupAddDlgName.text())

        if group == '':
            QtGui.QMessageBox.about(self, u'设置', u'组名称不能为空')
            return
        
        url = 'https://%s:%s/highobjfile/groupadd/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.adminTagHighObjFileGroupAddDlgName.setText(_fromUtf8(''))                
                self.onAdminTagHighObjFileGroupSet()
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加组失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加组失败:' + rt[1])

    # 弹出 - 添加组 - Cancel
    def onAdminTagHighObjFileGroupAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighObjFileGroupAddDlg.hide()

    # 弹出 - 添加客体文件
    def onAdminTagHighObjFileAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighObjFileAddDlg.show()
        
        # 获取系统文件列表
        url = 'https://%s:%s/highobjfile/list/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'ObjDir'  : '/'
        }
        print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:             
                self.adminTagHighObjFileAddDlgTree.clear()
                for ofile, t in res['ObjFiles'].items():
                    if t == 1:
                        ofile = ofile + '/'
                    self.AdddminTagHighObjFileTree(ofile, ofile)                
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'获取系统文件列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'获取系统文件列表失败:' + rt[1])
        

    # 弹出 - 客体文件 - OK
    def onAdminTagHighObjFileAddDlgOk(self):
        group = unicode(self.adminTagHighObjFileGroupName.text())
        fname = unicode(self.adminTagHighObjFileAddDlgFName.text())
        ext   = unicode(self.adminTagHighObjFileAddDlgExt.text())

        print '---'
        print fname, ext
        if len(fname) == 0:
            QtGui.QMessageBox.about(self, u'错误提示', u'请先选择目录或文件')
            return
        if len(ext) > 0:
            if fname[-1:] != u'/':
                QtGui.QMessageBox.about(self, u'错误提示', u'扩展名只能添加在目录后面')
                return
            rt = re.match(u'^[.]+[a-zA-Z0-9]+$', ext)
            if rt == None:
                QtGui.QMessageBox.about(self, u'错误提示', u'扩展名格式错误')
                return
            uname = fname + u'*' + ext
        else:
            uname = fname 

        # 添加客体文件
        url = 'https://%s:%s/highobjfile/add/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group,
            'ObjFile'    : uname,
        }
        print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:             
                #QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.AdminTagHighObjFileSet(0, self.adminTagHighObjFilePageLength)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加客体文件失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加客体文件失败:' + rt[1])
        

    # 弹出 - 客体文件 - Cancel
    def onAdminTagHighObjFileAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighObjFileAddDlg.hide()
        self.adminTagHighObjFileAddDlgFName.setText(u'')
        self.adminTagHighObjFileAddDlgExt.setText(u'')
        
import images_rc
