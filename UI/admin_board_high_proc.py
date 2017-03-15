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
    
class AdminBoardHighProc(QtGui.QWidget):
    def __init__(self,parent=None):
        super(AdminBoardHighProc,self).__init__(parent)        
        #self.setupUi(self)

    def AddAdminTagHighProc(self):
        # 变量
        self.adminTagHighProcPageLength = 10
        self.adminTagHighProcPage = 0
        self.adminTagHighProcTotal = 0
        
        # 画线 左
        self.adminTagHighProcSpaceLeft = QtGui.QWidget(self.adminTagHighTagProcBkg)
        self.adminTagHighProcSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.adminTagHighProcSpaceLeft.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighProcSpaceLeft.setObjectName(_fromUtf8('adminTagHighSpaceLeft'))

        # 画线 中
        self.adminTagHighProcSpaceMid = QtGui.QWidget(self.adminTagHighTagProcBkg)
        self.adminTagHighProcSpaceMid.setGeometry(QtCore.QRect(210, 0, 1, 295))
        self.adminTagHighProcSpaceMid.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighProcSpaceMid.setObjectName(_fromUtf8('adminTagHighSpaceMid'))

        # 画线 右
        self.adminTagHighProcSpaceRight = QtGui.QWidget(self.adminTagHighTagProcBkg)
        self.adminTagHighProcSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.adminTagHighProcSpaceRight.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighProcSpaceRight.setObjectName(_fromUtf8('adminTagHighProcSpaceRight'))

        # 画线 底
        self.adminTagHighProcSpaceBottom = QtGui.QWidget(self.adminTagHighTagProcBkg)
        self.adminTagHighProcSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.adminTagHighProcSpaceBottom.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighProcSpaceBottom.setObjectName(_fromUtf8('adminTagHighProcSpaceBottom'))

        # 组 - 添加
        self.adminTagHighProcGroupAdd = QtGui.QPushButton(self.adminTagHighTagProcBkg)
        self.adminTagHighProcGroupAdd.setGeometry(QtCore.QRect(30, 8, 75, 25))
        self.adminTagHighProcGroupAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighProcGroupAdd.setObjectName(_fromUtf8('adminTagHighProcGroupAdd'))
        self.adminTagHighProcGroupAdd.setText(_translate('adminTagHighProcGroupAdd', '添加+', None))

        # 组 - 删除
        self.adminTagHighProcGroupDel = QtGui.QPushButton(self.adminTagHighTagProcBkg)
        self.adminTagHighProcGroupDel.setGeometry(QtCore.QRect(125, 8, 75, 25))
        self.adminTagHighProcGroupDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighProcGroupDel.setObjectName(_fromUtf8('adminTagHighProcGroupDel'))
        self.adminTagHighProcGroupDel.setText(_translate('adminTagHighProcGroupDel', '删除+', None))

        # 组 - 列表
        self.adminTagHighProcGroupTree = QtGui.QTreeWidget(self.adminTagHighTagProcBkg)
        self.adminTagHighProcGroupTree.setGeometry(QtCore.QRect(30, 40, 170, 245))
        self.adminTagHighProcGroupTree.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighProcGroupTree.setObjectName(_fromUtf8('adminTagHighProcGroupTree'))
        self.adminTagHighProcGroupTree.setHeaderHidden(True)

        # 组标题显示
        self.adminTagHighProcGroupNameLable = QtGui.QLabel(self.adminTagHighTagProcBkg)
        self.adminTagHighProcGroupNameLable.setGeometry(QtCore.QRect(240, 5, 45, 30))
        self.adminTagHighProcGroupNameLable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighProcGroupNameLable.setObjectName(_fromUtf8('adminTagHighProcGroupNameLable'))
        self.adminTagHighProcGroupNameLable.setText(_translate('adminTagHighProcGroupNameLable', '当前组：', None))
        
        # 组名称 选择
        self.adminTagHighProcGroupName = QtGui.QLabel(self.adminTagHighTagProcBkg)
        self.adminTagHighProcGroupName.setGeometry(QtCore.QRect(285, 5, 120, 30))
        self.adminTagHighProcGroupName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_no_frame.png.png);'))
        self.adminTagHighProcGroupName.setObjectName(_fromUtf8('adminTagHighProcGroupName'))
        self.adminTagHighProcGroupName.setText(_translate('adminTagHighProcGroupName', '', None))

        # 上一页
        self.adminTagHighProcPrev = QtGui.QPushButton(self.adminTagHighTagProcBkg)
        self.adminTagHighProcPrev.setGeometry(QtCore.QRect(420, 8, 70, 25))
        #self.adminTagHighProcPrev.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighProcPrev.setObjectName(_fromUtf8('adminTagHighProcPrev'))
        self.adminTagHighProcPrev.setText(_translate('adminTagHighProcPrev', '<<  上一页', None))

        # 当前页
        self.adminTagHighProcPageText = QtGui.QLabel(self.adminTagHighTagProcBkg)
        self.adminTagHighProcPageText.setGeometry(QtCore.QRect(490, 8, 30, 25))
        self.adminTagHighProcPageText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.adminTagHighProcPageText.setObjectName(_fromUtf8('adminTagHighProcPageText'))
        self.adminTagHighProcPageText.setText(_translate('adminTagHighProcPageText', '0/0', None))

        # 下一页
        self.adminTagHighProcNext = QtGui.QPushButton(self.adminTagHighTagProcBkg)
        self.adminTagHighProcNext.setGeometry(QtCore.QRect(530, 8, 70, 25))
        #self.adminTagHighProcNext.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighProcNext.setObjectName(_fromUtf8('adminTagHighProcNext'))
        self.adminTagHighProcNext.setText(_translate('adminTagHighProcNext', '下一页  >>', None))

        # 程序 - 添加
        self.adminTagHighProcAdd = QtGui.QPushButton(self.adminTagHighTagProcBkg)
        self.adminTagHighProcAdd.setGeometry(QtCore.QRect(720, 8, 70, 25))
        self.adminTagHighProcAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighProcAdd.setObjectName(_fromUtf8('adminTagHighProcAdd'))
        self.adminTagHighProcAdd.setText(_translate('adminTagHighProcAdd', '添加程序', None))

        # 程序 - 删除
        self.adminTagHighProcDel = QtGui.QPushButton(self.adminTagHighTagProcBkg)
        self.adminTagHighProcDel.setGeometry(QtCore.QRect(800, 8, 70, 25))
        self.adminTagHighProcDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagHighProcDel.setObjectName(_fromUtf8('adminTagHighProcDel'))
        self.adminTagHighProcDel.setText(_translate('adminTagHighProcDel', '删除程序', None))

        # 程序 - 全选
        self.adminTagHighProcSelect = QtGui.QCheckBox(self.adminTagHighTagProcBkg)
        self.adminTagHighProcSelect.setGeometry(QtCore.QRect(900, 8, 55, 25))
        self.adminTagHighProcSelect.setObjectName(_fromUtf8('adminTagHighProcSelect'))
        self.adminTagHighProcSelect.setText(_translate('adminTagHighProcSelect', '全选', None))

        # 程序 - 列表表格
        self.adminTagHighProcTable = QtGui.QTableWidget(self.adminTagHighTagProcBkg)
        self.adminTagHighProcTable.setGeometry(QtCore.QRect(225, 40, 735, 245))
        self.adminTagHighProcTable.setObjectName(_fromUtf8('adminTagSpecialTable'))
        self.adminTagHighProcTable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.jpg);'))
        self.adminTagHighProcTable.verticalHeader().setVisible(False)
        self.adminTagHighProcTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagHighProcTable.setAlternatingRowColors(True)
        #list_widget.adminTagHighProcTable(QtGui.QAbstractItemView.SelectRows)
        self.adminTagHighProcTable.setRowCount(self.adminTagHighProcPageLength)
        self.adminTagHighProcTable.setColumnCount(2)
        self.adminTagHighProcTable.setHorizontalHeaderLabels([_fromUtf8('程序名'),_fromUtf8('选择')])
        self.adminTagHighProcTable.setShowGrid(False)
        self.adminTagHighProcTable.setColumnWidth(0,400)
        self.adminTagHighProcTable.setColumnWidth(1,330)
        for i in range(0, self.adminTagHighProcPageLength):
            self.adminTagHighProcTable.setRowHeight(i,21)

        #####################################################
        # 添加程序弹出
        self.adminTagHighProcAddDlg = QtGui.QWidget(self.adminTagHighTagProcBkg)
        self.adminTagHighProcAddDlg.setGeometry(QtCore.QRect(300, 0, 457, 300))
        self.adminTagHighProcAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighProcAddDlg.setObjectName(_fromUtf8('adminTagHighProcAddDlg'))
        self.adminTagHighProcAddDlg.hide()

        # 添加程序弹出 - 请选择程序
        self.adminTagHighProcAddDlgTextLab = QtGui.QLabel(self.adminTagHighProcAddDlg)
        self.adminTagHighProcAddDlgTextLab.setGeometry(QtCore.QRect(20, 10, 70, 21))
        self.adminTagHighProcAddDlgTextLab.setObjectName(_fromUtf8('adminTagHighProcAddDlgText'))
        self.adminTagHighProcAddDlgTextLab.setText(_translate('adminTagHighProcAddDlgText', '请选择程序:', None))

        # 添加程序弹出 - 程序列表
        self.adminTagHighProcAddDlgTree = QtGui.QTreeWidget(self.adminTagHighProcAddDlg)
        self.adminTagHighProcAddDlgTree.setGeometry(QtCore.QRect(10, 35, 431, 192))
        self.adminTagHighProcAddDlgTree.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighProcAddDlgTree.setObjectName(_fromUtf8('adminTagHighProcAddDlgTree'))
        self.adminTagHighProcAddDlgTree.setHeaderHidden(True)

        # 添加程序弹出 - 程序名称 - 文字
        self.adminTagHighProcAddDlgUNameText = QtGui.QLineEdit(self.adminTagHighProcAddDlg)
        self.adminTagHighProcAddDlgUNameText.setGeometry(QtCore.QRect(10, 240, 40, 21))
        self.adminTagHighProcAddDlgUNameText.setObjectName(_fromUtf8('adminTagHighProcAddDlgUNameText'))
        self.adminTagHighProcAddDlgUNameText.setText(_translate('adminTagHighProcAddDlgUNameText', '程序:', None))
        
        # 添加程序弹出 - 程序名称
        self.adminTagHighProcAddDlgUName = QtGui.QLineEdit(self.adminTagHighProcAddDlg)
        self.adminTagHighProcAddDlgUName.setGeometry(QtCore.QRect(50, 240, 390, 21))
        self.adminTagHighProcAddDlgUName.setObjectName(_fromUtf8('adminTagHighProcAddDlgUName'))
        self.adminTagHighProcAddDlgUName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white_frame.png);'))
        self.adminTagHighProcAddDlgUName.setText(_translate('adminTagHighProcAddDlgUName', '', None))
        
        # 添加程序弹出 - 添加
        self.adminTagHighProcAddDlgOk = QtGui.QPushButton(self.adminTagHighProcAddDlg)
        self.adminTagHighProcAddDlgOk.setGeometry(QtCore.QRect(120, 270, 75, 23))
        self.adminTagHighProcAddDlgOk.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighProcAddDlgOk.setObjectName(_fromUtf8('adminTagHighProcAddDlgOk'))
        self.adminTagHighProcAddDlgOk.setText(_translate('adminTagHighProcAddDlgOk', '添加', None))

        # 添加程序弹出 - 取消
        self.adminTagHighProcAddDlgCancel = QtGui.QPushButton(self.adminTagHighProcAddDlg)
        self.adminTagHighProcAddDlgCancel.setGeometry(QtCore.QRect(250, 270, 75, 23))
        self.adminTagHighProcAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighProcAddDlgCancel.setObjectName(_fromUtf8('adminTagHighProcAddDlgOk'))
        self.adminTagHighProcAddDlgCancel.setText(_translate('adminTagHighProcAddDlgCancel', '取消', None))

        ###########################################################
        # 添加组 弹出
        self.adminTagHighProcGroupAddDlg = QtGui.QWidget(self.adminTagHighTagProcBkg)
        self.adminTagHighProcGroupAddDlg.setGeometry(QtCore.QRect(300, 0, 271, 105))
        self.adminTagHighProcGroupAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagHighProcGroupAddDlg.setObjectName(_fromUtf8('adminTagHighProcGroupAddDlg'))
        self.adminTagHighProcGroupAddDlg.hide()

        # 添加组 弹出 - 输入组名称
        self.adminTagHighProcGroupAddDlgText = QtGui.QLabel(self.adminTagHighProcGroupAddDlg)
        self.adminTagHighProcGroupAddDlgText.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.adminTagHighProcGroupAddDlgText.setObjectName(_fromUtf8('adminTagHighProcGroupAddDlgText'))
        self.adminTagHighProcGroupAddDlgText.setText(_translate('adminTagHighProcGroupAddDlgText', '请输入组名称:', None))

        # 添加组 弹出 - 组名称
        self.adminTagHighProcGroupAddDlgName = QtGui.QLineEdit(self.adminTagHighProcGroupAddDlg)
        self.adminTagHighProcGroupAddDlgName.setGeometry(QtCore.QRect(20, 30, 231, 31))
        self.adminTagHighProcGroupAddDlgName.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white.png);'))
        self.adminTagHighProcGroupAddDlgName.setObjectName(_fromUtf8('adminTagHighProcGroupAddDlgName'))
        self.adminTagHighProcGroupAddDlgName.setText(_translate('adminTagHighProcGroupAddDlgName', '', None))

        # 添加组 弹出 - 添加
        self.adminTagHighProcGroupAddDlgOK = QtGui.QPushButton(self.adminTagHighProcGroupAddDlg)
        self.adminTagHighProcGroupAddDlgOK.setGeometry(QtCore.QRect(40, 70, 75, 23))
        self.adminTagHighProcGroupAddDlgOK.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighProcGroupAddDlgOK.setObjectName(_fromUtf8('adminTagHighProcGroupAddDlgOK'))
        self.adminTagHighProcGroupAddDlgOK.setText(_translate('adminTagHighProcGroupAddDlgOK', '添加', None))

        # 添加组 弹出 - 取消
        self.adminTagHighProcGroupAddDlgCancel = QtGui.QPushButton(self.adminTagHighProcGroupAddDlg)
        self.adminTagHighProcGroupAddDlgCancel.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.adminTagHighProcGroupAddDlgCancel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagHighProcGroupAddDlgCancel.setObjectName(_fromUtf8('adminTagHighProcGroupAddDlgCancel'))
        self.adminTagHighProcGroupAddDlgCancel.setText(_translate('adminTagHighProcGroupAddDlgCancel', '取消', None))
        
        ###############################################################
        # 添加组
        self.onAdminTagHighProcGroupSet()
        
        # 组列表消息
        self.connect(self.adminTagHighProcGroupTree, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onAdminTagHighProcGroupClick)
        self.connect(self.adminTagHighProcGroupAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcGroupAdd)
        self.connect(self.adminTagHighProcGroupDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcGroupDel)
        self.connect(self.adminTagHighProcGroupAddDlgOK, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcGroupAddDlgOK)
        self.connect(self.adminTagHighProcGroupAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcGroupAddDlgCancel)
        
        # 添加程序消息
        self.connect(self.adminTagHighProcAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcAdd)
        self.connect(self.adminTagHighProcPrev, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcPrev)
        self.connect(self.adminTagHighProcNext, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcNext)
        self.connect(self.adminTagHighProcDel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcDel)
        self.connect(self.adminTagHighProcSelect, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcSelect)
        self.connect(self.adminTagHighProcAddDlgOk, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcAddDlgOk)
        self.connect(self.adminTagHighProcAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagHighProcAddDlgCancel)
        self.connect(self.adminTagHighProcAddDlgTree, QtCore.SIGNAL('itemClicked(QTreeWidgetItem*, int)'), self.onAdminTagHighProcAddDlgTreeClick)
        

    def AdddminTagHighProcGroupTree(self, title, data):
        root = self.adminTagHighProcGroupTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)
        #item.setCheckState (0, QtCore.Qt.Unchecked)

    def AdddminTagHighProcTree(self, title, data):
        root = self.adminTagHighProcAddDlgTree.invisibleRootItem()
        item = QtGui.QTreeWidgetItem(root, [title])
        item.setData(0, QtCore.Qt.UserRole, data)

    def onAdminTagHighProcGroupClick(self, item, column):
        if self.AdminBoardCheckPopUp():
            return
        self.adminTagHighProcGroupName.setText(item.text(column))
        self.AdminTagHighProcSet(0, self.adminTagHighProcPageLength)

    def onAdminTagHighProcAddDlgTreeClick(self, item, column):
        self.adminTagHighProcAddDlgUName.setText(item.text(column))


    # 程序 - 全选
    def onAdminTagHighProcSelect(self):
        chk = self.adminTagHighProcSelect.checkState()
        if chk == 0: #全不选
            itemcnt = self.adminTagHighProcTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighProcTable.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(False)
        elif chk == 2: #全选
            itemcnt = self.adminTagHighProcTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagHighProcTable.item(i, 1)
                if it == None:
                    continue
                it.setCheckState(2)
        else:
            pass

    def setAdminTagHighProcNowPageText(self):
        tot = self.adminTagHighProcTotal
        page = self.adminTagHighProcPage
        length = self.adminTagHighProcPageLength
        page_str = '0/0'
        if tot > 0:
            if tot % length > 0:
                page_str = '%d/%d' % (page + 1, (tot / length) + 1)
            else:
                page_str = '%d/%d' % (page + 1, tot / length)
        self.adminTagHighProcPageText.setText(_translate('adminTagHighProcPageText', page_str, None))

    # 设置程序列表
    def AdminTagHighProcSet(self, start, length):
        group = unicode(self.adminTagHighProcGroupName.text())
        #print group, start, length
        # 查找当前组程序列表
        url = 'https://%s:%s/highproc/search/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.adminTagHighProcTotal = res['Total']
                
                # 清空列表
                for i in xrange(0, self.adminTagHighProcPageLength):
                    self.adminTagHighProcTable.setItem(i, 0, None)
                    self.adminTagHighProcTable.setItem(i, 1, None)
                    self.adminTagHighProcPage = 0
                if res['Procs'] != None:
                    # 添加列表
                    cnt = len(res['Procs'])
                    for i in xrange(0, cnt):
                        newItem = QtGui.QTableWidgetItem(res['Procs'][i])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighProcTable.setItem(i, 0, newItem)
                    
                        newItemChkbox = QtGui.QTableWidgetItem()
                        newItemChkbox.setCheckState(False)
                        newItemChkbox.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagHighProcTable.setItem(i, 1, newItemChkbox)
                    self.adminTagHighProcPage = start / self.adminTagHighProcPageLength
                self.setAdminTagHighProcNowPageText()
            else:
                QtGui.QMessageBox.about(self, u'错误提示', res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])
        

    # 上一页
    def onAdminTagHighProcPrev(self):
        start = self.adminTagHighProcPageLength * (self.adminTagHighProcPage - 1)
        if start < 0 :
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是第一页')
        else:
            self.AdminTagHighProcSet(start, self.adminTagHighProcPageLength)
        

    # 下一页
    def onAdminTagHighProcNext(self):
        start = self.adminTagHighProcPageLength * (self.adminTagHighProcPage + 1)
        if start >= self.adminTagHighProcTotal :
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是最后一页')
        else:
            self.AdminTagHighProcSet(start, self.adminTagHighProcPageLength)

    # 删除程序列表
    def onAdminTagHighProcDel(self):
        itemcnt = self.adminTagHighProcTable.rowCount()
        dellist = []
        
        for i in range(0, itemcnt):
            it = self.adminTagHighProcTable.item(i, 1)
            if it == None:
                continue
            chk = it.checkState()
            if chk == 2: # 状态有0和2
                proc = unicode(self.adminTagHighProcTable.item(i, 0).text())
                dellist.append(proc)

        url = 'https://%s:%s/highproc/del/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        #print url
        for proc in dellist:
            data = {
                'Tokey'   : self.Tokey,
                'Proc'    : proc
            }
            #print data
            param = {'Data' : json.dumps(data)} 
            rt = HttpsPost(url, param)
            #print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:             
                    #QtGui.QMessageBox.about(self, u'提示', u'删除程序成功:' + proc)
                    pass
                else:
                    QtGui.QMessageBox.about(self, u'错误提示', u'删除程序失败:' + proc + ':' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除程序失败:' + rt[1])
                
        #刷新列表
        self.AdminTagHighProcSet(0, self.adminTagHighProcPageLength)
        
    # 设置组列表
    def onAdminTagHighProcGroupSet(self):
        url = 'https://%s:%s/highproc/groupsearch/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.adminTagHighProcGroupTree.clear()
                if res['Groups'] == None:
                    return
                for group in res['Groups']:
                    self.AdddminTagHighProcGroupTree(group, group)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])
    
    # 弹出 - 添加组
    def onAdminTagHighProcGroupAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighProcGroupAddDlg.show()

    # 删除组
    def onAdminTagHighProcGroupDel(self):
        group = unicode(self.adminTagHighProcGroupName.text())
        if group == '':
            QtGui.QMessageBox.about(self, u'设置', u'请选择一个组')
            return
        url = 'https://%s:%s/highproc/groupdel/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.onAdminTagHighProcGroupSet()
                QtGui.QMessageBox.about(self, u'设置', u'删除组成功:')
                self.adminTagHighProcGroupName.setText(u'')
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除组失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'删除组失败:' + rt[1])
    

    # 弹出 - 添加组 - OK
    def onAdminTagHighProcGroupAddDlgOK(self):
        self.AdminBoardUnsetPopUp()        
        self.adminTagHighProcGroupAddDlg.hide()

        group = unicode(self.adminTagHighProcGroupAddDlgName.text())

        if group == '':
            QtGui.QMessageBox.about(self, u'设置', u'组名称不能为空')
            return
        
        url = 'https://%s:%s/highproc/groupadd/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.onAdminTagHighProcGroupSet()
                QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.adminTagHighProcGroupAddDlgName.setText(_fromUtf8(''))  
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加组失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加组失败:' + rt[1])

    # 弹出 - 添加组 - Cancel
    def onAdminTagHighProcGroupAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighProcGroupAddDlg.hide()

    # 弹出 - 添加程序
    def onAdminTagHighProcAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagHighProcAddDlg.show()
        
        # 获取系统程序列表
        url = 'https://%s:%s/highproc/list/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
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
                self.adminTagHighProcAddDlgTree.clear()
                for proc in res['Procs']:                    
                    self.AdddminTagHighProcTree(proc, proc)                
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'获取系统程序列表失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'获取系统程序列表失败:' + rt[1])
        

    # 弹出 - 程序 - OK
    def onAdminTagHighProcAddDlgOk(self):
        group = unicode(self.adminTagHighProcGroupName.text())
        uname = unicode(self.adminTagHighProcAddDlgUName.text())

        # 添加程序
        url = 'https://%s:%s/highproc/add/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
            'Group'   : group,
            'Proc'    : uname,
        }
        #print url, data
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        #print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:             
                #QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.AdminTagHighProcSet(0, self.adminTagHighProcPageLength)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加程序失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加程序失败:' + rt[1])
        

    # 弹出 - 程序 - Cancel
    def onAdminTagHighProcAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagHighProcAddDlg.hide()
        self.adminTagHighProcAddDlgUName.setText(u'')
        
import images_rc
