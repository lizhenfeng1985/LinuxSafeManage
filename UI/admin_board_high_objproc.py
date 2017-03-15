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
    
class AdminBoardHighObjProc(QtGui.QWidget):
    def __init__(self,parent=None):
        super(AdminBoardHighObjProc,self).__init__(parent)        
        #self.setupUi(self)

    def AddAdminTagHighObjProc(self):
        # 变量
        self.adminTagHighObjProcPageLength = 10
        self.adminTagHighObjProcPage = 0
        self.adminTagHighObjProcTotal = 0
        
        # 画线 左
        self.adminTagHighObjProcSpaceLeft = QtGui.QWidget(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.adminTagHighObjProcSpaceLeft.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjProcSpaceLeft.setObjectName(_fromUtf8('adminTagHighSpaceLeft'))

        # 画线 中
        self.adminTagHighObjProcSpaceMid = QtGui.QWidget(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcSpaceMid.setGeometry(QtCore.QRect(210, 0, 1, 295))
        self.adminTagHighObjProcSpaceMid.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjProcSpaceMid.setObjectName(_fromUtf8('adminTagHighSpaceMid'))

        # 画线 右
        self.adminTagHighObjProcSpaceRight = QtGui.QWidget(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.adminTagHighObjProcSpaceRight.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjProcSpaceRight.setObjectName(_fromUtf8('adminTagHighObjProcSpaceRight'))

        # 画线 底
        self.adminTagHighObjProcSpaceBottom = QtGui.QWidget(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.adminTagHighObjProcSpaceBottom.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjProcSpaceBottom.setObjectName(_fromUtf8('adminTagHighObjProcSpaceBottom'))

        # 组 - 添加
        self.adminTagHighObjProcGroupAdd = QtGui.QPushButton(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcGroupAdd.setGeometry(QtCore.QRect(30, 8, 75, 25))
        self.adminTagHighObjProcGroupAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjProcGroupAdd.setObjectName(_fromUtf8('adminTagHighObjProcGroupAdd'))
        self.adminTagHighObjProcGroupAdd.setText(_translate('adminTagHighObjProcGroupAdd', '添加+', None))

        # 组 - 删除
        self.adminTagHighObjProcGroupDel = QtGui.QPushButton(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcGroupDel.setGeometry(QtCore.QRect(125, 8, 75, 25))
        self.adminTagHighObjProcGroupDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjProcGroupDel.setObjectName(_fromUtf8('adminTagHighObjProcGroupDel'))
        self.adminTagHighObjProcGroupDel.setText(_translate('adminTagHighObjProcGroupDel', '删除+', None))

        # 组 - 列表
        self.adminTagHighObjProcGroupTree = QtGui.QTreeWidget(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcGroupTree.setGeometry(QtCore.QRect(30, 40, 170, 245))
        self.adminTagHighObjProcGroupTree.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjProcGroupTree.setObjectName(_fromUtf8('adminTagHighObjProcGroupTree'))
        self.adminTagHighObjProcGroupTree.setHeaderHidden(True)

        # 组标题显示
        self.adminTagHighObjProcGroupNameLable = QtGui.QLabel(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcGroupNameLable.setGeometry(QtCore.QRect(240, 5, 45, 30))
        self.adminTagHighObjProcGroupNameLable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighObjProcGroupNameLable.setObjectName(_fromUtf8('adminTagHighObjProcGroupNameLable'))
        self.adminTagHighObjProcGroupNameLable.setText(_translate('adminTagHighObjProcGroupNameLable', '当前组：', None))
        
        # 组名称 选择
        self.adminTagHighObjProcGroupName = QtGui.QLabel(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcGroupName.setGeometry(QtCore.QRect(285, 5, 120, 30))
        self.adminTagHighObjProcGroupName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighObjProcGroupName.setObjectName(_fromUtf8('adminTagHighObjProcGroupName'))
        self.adminTagHighObjProcGroupName.setText(_translate('adminTagHighObjProcGroupName', '', None))

        # 上一页
        self.adminTagHighObjProcPrev = QtGui.QPushButton(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcPrev.setGeometry(QtCore.QRect(420, 8, 70, 25))
        #self.adminTagHighObjProcPrev.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjProcPrev.setObjectName(_fromUtf8('adminTagHighObjProcPrev'))
        self.adminTagHighObjProcPrev.setText(_translate('adminTagHighObjProcPrev', '<<  上一页', None))

        # 当前页
        self.adminTagHighObjProcPageText = QtGui.QLabel(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcPageText.setGeometry(QtCore.QRect(490, 8, 30, 25))
        self.adminTagHighObjProcPageText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.adminTagHighObjProcPageText.setObjectName(_fromUtf8('adminTagHighObjProcPageText'))
        self.adminTagHighObjProcPageText.setText(_translate('adminTagHighObjProcPageText', '0/0', None))

        # 下一页
        self.adminTagHighObjProcNext = QtGui.QPushButton(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcNext.setGeometry(QtCore.QRect(530, 8, 70, 25))
        #self.adminTagHighObjProcNext.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjProcNext.setObjectName(_fromUtf8('adminTagHighObjProcNext'))
        self.adminTagHighObjProcNext.setText(_translate('adminTagHighObjProcNext', '下一页  >>', None))

        # 客体程序 - 添加
        self.adminTagHighObjProcAdd = QtGui.QPushButton(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcAdd.setGeometry(QtCore.QRect(720, 8, 70, 25))
        self.adminTagHighObjProcAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjProcAdd.setObjectName(_fromUtf8('adminTagHighObjProcAdd'))
        self.adminTagHighObjProcAdd.setText(_translate('adminTagHighObjProcAdd', '添加程序', None))

        # 客体程序 - 删除
        self.adminTagHighObjProcDel = QtGui.QPushButton(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcDel.setGeometry(QtCore.QRect(800, 8, 70, 25))
        self.adminTagHighObjProcDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighObjProcDel.setObjectName(_fromUtf8('adminTagHighObjProcDel'))
        self.adminTagHighObjProcDel.setText(_translate('adminTagHighObjProcDel', '删除程序', None))

        # 客体程序 - 全选
        self.adminTagHighObjProcSelect = QtGui.QCheckBox(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcSelect.setGeometry(QtCore.QRect(900, 8, 55, 25))
        self.adminTagHighObjProcSelect.setObjectName(_fromUtf8('adminTagHighObjProcSelect'))
        self.adminTagHighObjProcSelect.setText(_translate('adminTagHighObjProcSelect', '全选', None))

        # 客体程序 - 列表表格
        self.adminTagHighObjProcTable = QtGui.QTableWidget(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcTable.setGeometry(QtCore.QRect(225, 40, 735, 245))
        self.adminTagHighObjProcTable.setObjectName(_fromUtf8('adminTagSpecialTable'))
        self.adminTagHighObjProcTable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.jpg);'))
        self.adminTagHighObjProcTable.verticalHeader().setVisible(False)
        self.adminTagHighObjProcTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagHighObjProcTable.setAlternatingRowColors(True)
        #list_widget.adminTagHighObjProcTable(QtGui.QAbstractItemView.SelectRows)
        self.adminTagHighObjProcTable.setRowCount(self.adminTagHighObjProcPageLength)
        self.adminTagHighObjProcTable.setColumnCount(2)
        self.adminTagHighObjProcTable.setHorizontalHeaderLabels([_fromUtf8('客体程序名'),_fromUtf8('选择')])
        self.adminTagHighObjProcTable.setShowGrid(False)
        self.adminTagHighObjProcTable.setColumnWidth(0,400)
        self.adminTagHighObjProcTable.setColumnWidth(1,330)
        for i in range(0, self.adminTagHighObjProcPageLength):
            self.adminTagHighObjProcTable.setRowHeight(i,21)

        #####################################################
        # 添加客体程序弹出
        self.adminTagHighObjProcAddDlg = QtGui.QWidget(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcAddDlg.setGeometry(QtCore.QRect(300, 0, 457, 300))
        self.adminTagHighObjProcAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighObjProcAddDlg.setObjectName(_fromUtf8('adminTagHighObjProcAddDlg'))
        self.adminTagHighObjProcAddDlg.hide()

        # 添加客体程序弹出 - 请选择客体程序
        self.adminTagHighObjProcAddDlgTextLab = QtGui.QLabel(self.adminTagHighObjProcAddDlg)
        self.adminTagHighObjProcAddDlgTextLab.setGeometry(QtCore.QRect(20, 10, 100, 21))
        self.adminTagHighObjProcAddDlgTextLab.setObjectName(_fromUtf8('adminTagHighObjProcAddDlgText'))
        self.adminTagHighObjProcAddDlgTextLab.setText(_translate('adminTagHighObjProcAddDlgText', '请选择客体程序:', None))

        # 添加客体程序弹出 - 客体程序列表
        self.adminTagHighObjProcAddDlgTree = QtGui.QTreeWidget(self.adminTagHighObjProcAddDlg)
        self.adminTagHighObjProcAddDlgTree.setGeometry(QtCore.QRect(10, 35, 431, 192))
        self.adminTagHighObjProcAddDlgTree.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjProcAddDlgTree.setObjectName(_fromUtf8('adminTagHighObjProcAddDlgTree'))
        self.adminTagHighObjProcAddDlgTree.setHeaderHidden(True)

        # 添加客体程序弹出 - 客体程序名称 - 文字
        self.adminTagHighObjProcAddDlgUNameText = QtGui.QLineEdit(self.adminTagHighObjProcAddDlg)
        self.adminTagHighObjProcAddDlgUNameText.setGeometry(QtCore.QRect(10, 240, 40, 21))
        self.adminTagHighObjProcAddDlgUNameText.setObjectName(_fromUtf8('adminTagHighObjProcAddDlgUNameText'))
        self.adminTagHighObjProcAddDlgUNameText.setText(_translate('adminTagHighObjProcAddDlgUNameText', '程序:', None))
        
        # 添加客体程序弹出 - 客体程序名称
        self.adminTagHighObjProcAddDlgUName = QtGui.QLineEdit(self.adminTagHighObjProcAddDlg)
        self.adminTagHighObjProcAddDlgUName.setGeometry(QtCore.QRect(50, 240, 390, 21))
        self.adminTagHighObjProcAddDlgUName.setObjectName(_fromUtf8('adminTagHighObjProcAddDlgUName'))
        self.adminTagHighObjProcAddDlgUName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white_frame.png);'))
        self.adminTagHighObjProcAddDlgUName.setText(_translate('adminTagHighObjProcAddDlgUName', '', None))
        
        # 添加客体程序弹出 - 添加
        self.adminTagHighObjProcAddDlgOk = QtGui.QPushButton(self.adminTagHighObjProcAddDlg)
        self.adminTagHighObjProcAddDlgOk.setGeometry(QtCore.QRect(120, 270, 75, 23))
        self.adminTagHighObjProcAddDlgOk.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjProcAddDlgOk.setObjectName(_fromUtf8('adminTagHighObjProcAddDlgOk'))
        self.adminTagHighObjProcAddDlgOk.setText(_translate('adminTagHighObjProcAddDlgOk', '添加', None))

        # 添加客体程序弹出 - 取消
        self.adminTagHighObjProcAddDlgCancel = QtGui.QPushButton(self.adminTagHighObjProcAddDlg)
        self.adminTagHighObjProcAddDlgCancel.setGeometry(QtCore.QRect(250, 270, 75, 23))
        self.adminTagHighObjProcAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjProcAddDlgCancel.setObjectName(_fromUtf8('adminTagHighObjProcAddDlgOk'))
        self.adminTagHighObjProcAddDlgCancel.setText(_translate('adminTagHighObjProcAddDlgCancel', '取消', None))

        ###########################################################
        # 添加组 弹出
        self.adminTagHighObjProcGroupAddDlg = QtGui.QWidget(self.adminTagHighTagObjProcBkg)
        self.adminTagHighObjProcGroupAddDlg.setGeometry(QtCore.QRect(300, 0, 271, 105))
        self.adminTagHighObjProcGroupAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighObjProcGroupAddDlg.setObjectName(_fromUtf8('adminTagHighObjProcGroupAddDlg'))
        self.adminTagHighObjProcGroupAddDlg.hide()

        # 添加组 弹出 - 输入组名称
        self.adminTagHighObjProcGroupAddDlgText = QtGui.QLabel(self.adminTagHighObjProcGroupAddDlg)
        self.adminTagHighObjProcGroupAddDlgText.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.adminTagHighObjProcGroupAddDlgText.setObjectName(_fromUtf8('adminTagHighObjProcGroupAddDlgText'))
        self.adminTagHighObjProcGroupAddDlgText.setText(_translate('adminTagHighObjProcGroupAddDlgText', '请输入组名称:', None))

        # 添加组 弹出 - 组名称
        self.adminTagHighObjProcGroupAddDlgName = QtGui.QLineEdit(self.adminTagHighObjProcGroupAddDlg)
        self.adminTagHighObjProcGroupAddDlgName.setGeometry(QtCore.QRect(20, 30, 231, 31))
        self.adminTagHighObjProcGroupAddDlgName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white.png);'))
        self.adminTagHighObjProcGroupAddDlgName.setObjectName(_fromUtf8('adminTagHighObjProcGroupAddDlgName'))
        self.adminTagHighObjProcGroupAddDlgName.setText(_translate('adminTagHighObjProcGroupAddDlgName', '', None))

        # 添加组 弹出 - 添加
        self.adminTagHighObjProcGroupAddDlgOK = QtGui.QPushButton(self.adminTagHighObjProcGroupAddDlg)
        self.adminTagHighObjProcGroupAddDlgOK.setGeometry(QtCore.QRect(40, 70, 75, 23))
        self.adminTagHighObjProcGroupAddDlgOK.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjProcGroupAddDlgOK.setObjectName(_fromUtf8('adminTagHighObjProcGroupAddDlgOK'))
        self.adminTagHighObjProcGroupAddDlgOK.setText(_translate('adminTagHighObjProcGroupAddDlgOK', '添加', None))

        # 添加组 弹出 - 取消
        self.adminTagHighObjProcGroupAddDlgCancel = QtGui.QPushButton(self.adminTagHighObjProcGroupAddDlg)
        self.adminTagHighObjProcGroupAddDlgCancel.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.adminTagHighObjProcGroupAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighObjProcGroupAddDlgCancel.setObjectName(_fromUtf8('adminTagHighObjProcGroupAddDlgCancel'))
        self.adminTagHighObjProcGroupAddDlgCancel.setText(_translate('adminTagHighObjProcGroupAddDlgCancel', '取消', None))
        
        ###############################################################
        # 添加组
        self.onAdminTagHighObjProcGroupSet()
        
        # 组列表消息
        self.connect(self.adminTagHighObjProcGroupTree, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onAdminTagHighObjProcGroupClick)
        self.connect(self.adminTagHighObjProcGroupAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcGroupAdd)
        self.connect(self.adminTagHighObjProcGroupDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcGroupDel)
        self.connect(self.adminTagHighObjProcGroupAddDlgOK, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcGroupAddDlgOK)
        self.connect(self.adminTagHighObjProcGroupAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcGroupAddDlgCancel)
        
        # 添加客体程序消息
        self.connect(self.adminTagHighObjProcAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcAdd)
        self.connect(self.adminTagHighObjProcPrev, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcPrev)
        self.connect(self.adminTagHighObjProcNext, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcNext)
        self.connect(self.adminTagHighObjProcDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcDel)
        self.connect(self.adminTagHighObjProcSelect, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcSelect)
        self.connect(self.adminTagHighObjProcAddDlgOk, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcAddDlgOk)
        self.connect(self.adminTagHighObjProcAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighObjProcAddDlgCancel)
        self.connect(self.adminTagHighObjProcAddDlgTree, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onAdminTagHighObjProcAddDlgTreeClick)
        

    def AdddminTagHighObjProcGroupTree(self, title, data):
        root = self.adminTagHighObjProcGroupTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)
        #item.setCheckState (0, QtCore.Qt.Unchecked)

    def AdddminTagHighObjProcTree(self, title, data):
        root = self.adminTagHighObjProcAddDlgTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)

    def onAdminTagHighObjProcGroupClick(self, item, column):
        if self.AdminBoardCheckPopUp():
            return
        self.adminTagHighObjProcGroupName.setText(item.text(column))
        self.AdminTagHighObjProcSet(0, self.adminTagHighObjProcPageLength)

    def onAdminTagHighObjProcAddDlgTreeClick(self, item, column):
        self.adminTagHighObjProcAddDlgUName.setText(item.text(column))


    # 客体程序 - 全选
    def onAdminTagHighObjProcSelect(self):
        chk = self.adminTagHighObjProcSelect.checkState()
        if chk == 0: #全不选
            itemcnt = self.adminTagHighObjProcTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighObjProcTable.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(False)
        elif chk == 2: #全选
            itemcnt = self.adminTagHighObjProcTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighObjProcTable.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(2)
        else:
            pass

    def setAdminTagHighObjProcNowPageText(self):
        tot = self.adminTagHighObjProcTotal
        page = self.adminTagHighObjProcPage
        length = self.adminTagHighObjProcPageLength
        page_str = '0/0'
        if tot > 0:
            if tot % length > 0:
                page_str = '%d/%d' % (page + 1, (tot / length) + 1)
            else:
                page_str = '%d/%d' % (page + 1, tot / length)
        self.adminTagHighObjProcPageText.setText(_translate('adminTagHighObjProcPageText', page_str, None))

    # 设置客体程序列表
    def AdminTagHighObjProcSet(self, start, length):
        group = unicode(self.adminTagHighObjProcGroupName.text())
        #print group, start, length
        # 查找当前组客体程序列表
        url = 'https://%s:%s/highobjproc/search/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.adminTagHighObjProcTotal = res['Total']
                
                # 清空列表
                for i in xrange(0, self.adminTagHighObjProcPageLength):
                    self.adminTagHighObjProcTable.setItem(i, 0, None)
                    self.adminTagHighObjProcTable.setItem(i, 1, None)
                    self.adminTagHighObjProcPage = 0
                if res['ObjProcs'] != None:
                    # 添加列表
                    cnt = len(res['ObjProcs'])
                    for i in xrange(0, cnt):
                        newItem = QtGui.QTableWidgetItem(res['ObjProcs'][i])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighObjProcTable.setItem(i, 0, newItem)
                    
                        newItemChkbox = QtGui.QTableWidgetItem()
                        newItemChkbox.setCheckState(False)
                        newItemChkbox.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighObjProcTable.setItem(i, 1, newItemChkbox)
                    self.adminTagHighObjProcPage = start / self.adminTagHighObjProcPageLength
                self.setAdminTagHighObjProcNowPageText()
            else:
                QtGui.QMessageBox.about(self, u'错误提示', res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])
        

    # 上一页
    def onAdminTagHighObjProcPrev(self):
        start = self.adminTagHighObjProcPageLength * (self.adminTagHighObjProcPage - 1)
        if start < 0 :
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是第一页')
        else:
            self.AdminTagHighObjProcSet(start, self.adminTagHighObjProcPageLength)
        

    # 下一页
    def onAdminTagHighObjProcNext(self):
        start = self.adminTagHighObjProcPageLength * (self.adminTagHighObjProcPage + 1)
        if start >= self.adminTagHighObjProcTotal :
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是最后一页')
        else:
            self.AdminTagHighObjProcSet(start, self.adminTagHighObjProcPageLength)

    # 删除客体程序列表
    def onAdminTagHighObjProcDel(self):
        itemcnt = self.adminTagHighObjProcTable.rowCount()
        dellist = []
        
        for i in range(0, itemcnt):
            it = self.adminTagHighObjProcTable.item(i, 1)
            if it == None:
                continue
            chk = it.checkState()
            if chk == 2: # 状态有0和2
                proc = unicode(self.adminTagHighObjProcTable.item(i, 0).text())
                dellist.append(proc)

        url = 'https://%s:%s/highobjproc/del/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        #print url
        for proc in dellist:
            data = {
                'Tokey'   : self.Tokey,
                'ObjProc'    : proc
            }
            #print data
            param = {'Data' : json.dumps(data)} 
            rt = HttpsPost(url, param)
            #print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:             
                    #QtGui.QMessageBox.about(self, u'提示', u'删除客体程序成功:' + proc)
                    pass
                else:
                    QtGui.QMessageBox.about(self, u'错误提示', u'删除客体程序失败:' + proc + ':' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除客体程序失败:' + rt[1])
                
        #刷新列表
        self.AdminTagHighObjProcSet(0, self.adminTagHighObjProcPageLength)
        
    # 设置组列表
    def onAdminTagHighObjProcGroupSet(self):
        url = 'https://%s:%s/highobjproc/groupsearch/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.adminTagHighObjProcGroupTree.clear()
                if res['Groups'] == None:
                    return
                for group in res['Groups']:                    
                    self.AdddminTagHighObjProcGroupTree(group, group)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])
    
    # 弹出 - 添加组
    def onAdminTagHighObjProcGroupAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighObjProcGroupAddDlg.show()

    # 删除组
    def onAdminTagHighObjProcGroupDel(self):
        group = unicode(self.adminTagHighObjProcGroupName.text())
        if group == '':
            QtGui.QMessageBox.about(self, u'设置', u'请选择一个组')
            return
        url = 'https://%s:%s/highobjproc/groupdel/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.onAdminTagHighObjProcGroupSet()
                QtGui.QMessageBox.about(self, u'设置', u'删除组成功:')
                self.adminTagHighObjProcGroupName.setText(u'')
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除组失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'删除组失败:' + rt[1])
    

    # 弹出 - 添加组 - OK
    def onAdminTagHighObjProcGroupAddDlgOK(self):
        self.AdminBoardUnsetPopUp()        
        self.adminTagHighObjProcGroupAddDlg.hide()

        group = unicode(self.adminTagHighObjProcGroupAddDlgName.text())

        if group == '':
            QtGui.QMessageBox.about(self, u'设置', u'组名称不能为空')
            return
        
        url = 'https://%s:%s/highobjproc/groupadd/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.onAdminTagHighObjProcGroupSet()
                QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.adminTagHighObjProcGroupAddDlgName.setText(_fromUtf8(''))
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加组失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加组失败:' + rt[1])

    # 弹出 - 添加组 - Cancel
    def onAdminTagHighObjProcGroupAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighObjProcGroupAddDlg.hide()

    # 弹出 - 添加客体程序
    def onAdminTagHighObjProcAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighObjProcAddDlg.show()
        
        # 获取系统程序列表
        url = 'https://%s:%s/highobjproc/list/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.adminTagHighObjProcAddDlgTree.clear()
                for proc in res['ObjProcs']:                    
                    self.AdddminTagHighObjProcTree(proc, proc)                
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'获取系统程序列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'获取系统程序列表失败:' + rt[1])
        

    # 弹出 - 客体程序 - OK
    def onAdminTagHighObjProcAddDlgOk(self):
        group = unicode(self.adminTagHighObjProcGroupName.text())
        uname = unicode(self.adminTagHighObjProcAddDlgUName.text())

        # 添加客体程序
        url = 'https://%s:%s/highobjproc/add/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group,
            'ObjProc'    : uname,
        }
        #print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:             
                #QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.AdminTagHighObjProcSet(0, self.adminTagHighObjProcPageLength)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加客体程序失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加客体程序失败:' + rt[1])
        

    # 弹出 - 客体程序 - Cancel
    def onAdminTagHighObjProcAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighObjProcAddDlg.hide()
        self.adminTagHighObjProcAddDlgUName.setText(u'')
        
import images_rc
