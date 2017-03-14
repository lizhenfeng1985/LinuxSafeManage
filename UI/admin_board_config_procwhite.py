# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
import json
import images_rc
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


class AdminBoardConfigProcWhite(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AdminBoardConfigProcWhite, self).__init__(parent)
        # self.setupUi(self)

    def AddAdminTagConfigProcWhite(self):
        # 变量
        self.adminTagConfigProcWhitePageLength = 10
        self.adminTagConfigProcWhitePage = 0
        self.adminTagConfigProcWhiteTotal = 0

        # 画线 左
        self.adminTagConfigProcWhiteSpaceLeft = QtGui.QWidget(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhiteSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.adminTagConfigProcWhiteSpaceLeft.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigProcWhiteSpaceLeft.setObjectName(_fromUtf8('adminTagHighSpaceLeft'))

        # 画线 右
        self.adminTagConfigProcWhiteSpaceRight = QtGui.QWidget(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhiteSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.adminTagConfigProcWhiteSpaceRight.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigProcWhiteSpaceRight.setObjectName(_fromUtf8('adminTagConfigProcWhiteSpaceRight'))

        # 画线 底
        self.adminTagConfigProcWhiteSpaceBottom = QtGui.QWidget(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhiteSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.adminTagConfigProcWhiteSpaceBottom.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigProcWhiteSpaceBottom.setObjectName(_fromUtf8('adminTagConfigProcWhiteSpaceBottom'))

        # 上一页
        self.adminTagConfigProcWhitePrev = QtGui.QPushButton(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhitePrev.setGeometry(QtCore.QRect(220, 8, 70, 25))
        # self.adminTagConfigProcWhitePrev.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigProcWhitePrev.setObjectName(_fromUtf8('adminTagConfigProcWhitePrev'))
        self.adminTagConfigProcWhitePrev.setText(_translate('adminTagConfigProcWhitePrev', '<<  上一页', None))

        # 当前页
        self.adminTagConfigProcWhitePageText = QtGui.QLabel(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhitePageText.setGeometry(QtCore.QRect(320, 8, 30, 25))
        self.adminTagConfigProcWhitePageText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.adminTagConfigProcWhitePageText.setObjectName(_fromUtf8('adminTagConfigProcWhitePageText'))
        self.adminTagConfigProcWhitePageText.setText(_translate('adminTagConfigProcWhitePageText', '0/0', None))

        # 下一页
        self.adminTagConfigProcWhiteNext = QtGui.QPushButton(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhiteNext.setGeometry(QtCore.QRect(390, 8, 70, 25))
        # self.adminTagConfigProcWhiteNext.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigProcWhiteNext.setObjectName(_fromUtf8('adminTagConfigProcWhiteNext'))
        self.adminTagConfigProcWhiteNext.setText(_translate('adminTagConfigProcWhiteNext', '下一页  >>', None))

        # 白名单程序 - 添加
        self.adminTagConfigProcWhiteAdd = QtGui.QPushButton(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhiteAdd.setGeometry(QtCore.QRect(670, 8, 70, 25))
        self.adminTagConfigProcWhiteAdd.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigProcWhiteAdd.setObjectName(_fromUtf8('adminTagConfigProcWhiteAdd'))
        self.adminTagConfigProcWhiteAdd.setText(_translate('adminTagConfigProcWhiteAdd', '添加程序', None))

        # 白名单程序 - 删除
        self.adminTagConfigProcWhiteDel = QtGui.QPushButton(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhiteDel.setGeometry(QtCore.QRect(750, 8, 70, 25))
        self.adminTagConfigProcWhiteDel.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigProcWhiteDel.setObjectName(_fromUtf8('adminTagConfigProcWhiteDel'))
        self.adminTagConfigProcWhiteDel.setText(_translate('adminTagConfigProcWhiteDel', '删除程序', None))

        # 白名单程序 - 全选
        self.adminTagConfigProcWhiteSelect = QtGui.QCheckBox(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhiteSelect.setGeometry(QtCore.QRect(850, 8, 55, 25))
        self.adminTagConfigProcWhiteSelect.setObjectName(_fromUtf8('adminTagConfigProcWhiteSelect'))
        self.adminTagConfigProcWhiteSelect.setText(_translate('adminTagConfigProcWhiteSelect', '全选', None))

        # 白名单程序 - 列表表格
        self.adminTagConfigProcWhiteTable = QtGui.QTableWidget(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhiteTable.setGeometry(QtCore.QRect(60, 40, 880, 245))
        self.adminTagConfigProcWhiteTable.setObjectName(_fromUtf8('adminTagConfigProcWhiteTable'))
        self.adminTagConfigProcWhiteTable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.jpg);'))
        self.adminTagConfigProcWhiteTable.verticalHeader().setVisible(False)
        self.adminTagConfigProcWhiteTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagConfigProcWhiteTable.setAlternatingRowColors(True)
        # list_widget.adminTagConfigProcWhiteTable(QtGui.QAbstractItemView.SelectRows)
        self.adminTagConfigProcWhiteTable.setRowCount(self.adminTagConfigProcWhitePageLength)
        self.adminTagConfigProcWhiteTable.setColumnCount(2)
        self.adminTagConfigProcWhiteTable.setHorizontalHeaderLabels([_fromUtf8('白名单程序绝对路径'), _fromUtf8('选择')])
        self.adminTagConfigProcWhiteTable.setShowGrid(False)
        self.adminTagConfigProcWhiteTable.setColumnWidth(0, 700)
        self.adminTagConfigProcWhiteTable.setColumnWidth(1, 170)
        for i in range(0, self.adminTagConfigProcWhitePageLength):
            self.adminTagConfigProcWhiteTable.setRowHeight(i, 21)

        ###########################################################
        # 添加白名单程序 弹出
        self.adminTagConfigProcWhiteAddDlg = QtGui.QWidget(self.adminTagConfigTagProcWhiteBkg)
        self.adminTagConfigProcWhiteAddDlg.setGeometry(QtCore.QRect(300, 0, 271, 105))
        self.adminTagConfigProcWhiteAddDlg.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_frame.png);'))
        self.adminTagConfigProcWhiteAddDlg.setObjectName(_fromUtf8('adminTagConfigProcWhiteAddDlg'))
        self.adminTagConfigProcWhiteAddDlg.hide()

        # 添加白名单程序 弹出 - 输入程序路径
        self.adminTagConfigProcWhiteAddDlgText = QtGui.QLabel(self.adminTagConfigProcWhiteAddDlg)
        self.adminTagConfigProcWhiteAddDlgText.setGeometry(QtCore.QRect(20, 10, 141, 21))
        self.adminTagConfigProcWhiteAddDlgText.setObjectName(_fromUtf8('adminTagConfigProcWhiteAddDlgText'))
        self.adminTagConfigProcWhiteAddDlgText.setText(_translate('adminTagConfigProcWhiteAddDlgText', '请输程序绝对路径:', None))

        # 添加白名单程序 弹出 - 程序路径
        self.adminTagConfigProcWhiteAddDlgPath = QtGui.QLineEdit(self.adminTagConfigProcWhiteAddDlg)
        self.adminTagConfigProcWhiteAddDlgPath.setGeometry(QtCore.QRect(20, 30, 231, 31))
        self.adminTagConfigProcWhiteAddDlgPath.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_white.png);'))
        self.adminTagConfigProcWhiteAddDlgPath.setObjectName(_fromUtf8('adminTagConfigProcWhiteAddDlgPath'))
        self.adminTagConfigProcWhiteAddDlgPath.setText(_translate('adminTagConfigProcWhiteAddDlgPath', '', None))

        # 添加白名单程序 弹出 - 添加
        self.adminTagConfigProcWhiteAddDlgOK = QtGui.QPushButton(self.adminTagConfigProcWhiteAddDlg)
        self.adminTagConfigProcWhiteAddDlgOK.setGeometry(QtCore.QRect(40, 70, 75, 23))
        self.adminTagConfigProcWhiteAddDlgOK.setStyleSheet(
            _fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagConfigProcWhiteAddDlgOK.setObjectName(_fromUtf8('adminTagConfigProcWhiteAddDlgOK'))
        self.adminTagConfigProcWhiteAddDlgOK.setText(_translate('adminTagConfigProcWhiteAddDlgOK', '添加', None))

        # 添加白名单程序 弹出 - 取消
        self.adminTagConfigProcWhiteAddDlgCancel = QtGui.QPushButton(self.adminTagConfigProcWhiteAddDlg)
        self.adminTagConfigProcWhiteAddDlgCancel.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.adminTagConfigProcWhiteAddDlgCancel.setStyleSheet(
            _fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.adminTagConfigProcWhiteAddDlgCancel.setObjectName(_fromUtf8('adminTagConfigProcWhiteAddDlgCancel'))
        self.adminTagConfigProcWhiteAddDlgCancel.setText(_translate('adminTagConfigProcWhiteAddDlgCancel', '取消', None))

        # 添加消息
        self.connect(self.adminTagConfigProcWhiteAdd, QtCore.SIGNAL('clicked()'), self.onAdminTagConfigProcWhiteAdd)
        self.connect(self.adminTagConfigProcWhitePrev, QtCore.SIGNAL('clicked()'), self.onAdminTagConfigProcWhitePrev)
        self.connect(self.adminTagConfigProcWhiteNext, QtCore.SIGNAL('clicked()'), self.onAdminTagConfigProcWhiteNext)
        self.connect(self.adminTagConfigProcWhiteDel, QtCore.SIGNAL('clicked()'), self.onAdminTagConfigProcWhiteDel)
        self.connect(self.adminTagConfigProcWhiteSelect, QtCore.SIGNAL('clicked()'), self.onAdminTagConfigProcWhiteSelect)
        self.connect(self.adminTagConfigProcWhiteAddDlgOK, QtCore.SIGNAL('clicked()'), self.onAdminTagConfigProcWhiteAddDlgOK)
        self.connect(self.adminTagConfigProcWhiteAddDlgCancel, QtCore.SIGNAL('clicked()'), self.onAdminTagConfigProcWhiteAddDlgCancel)

        # 设置列表
        self.AdminTagConfigProcWhiteSet(0, 10)

    # 弹出 - 添加程序
    def onAdminTagConfigProcWhiteAdd(self):
        if self.AdminBoardCheckPopUp():
            return
        self.AdminBoardSetPopUp()
        self.adminTagConfigProcWhiteAddDlg.show()

    # 上一页
    def onAdminTagConfigProcWhitePrev(self):
        start = self.adminTagConfigProcWhitePageLength * (self.adminTagConfigProcWhitePage - 1)
        if start < 0:
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是第一页')
        else:
            self.AdminTagConfigProcWhiteSet(start, self.adminTagConfigProcWhitePageLength)

    # 下一页
    def onAdminTagConfigProcWhiteNext(self):
        start = self.adminTagConfigProcWhitePageLength * (self.adminTagConfigProcWhitePage + 1)
        if start >= self.adminTagConfigProcWhiteTotal:
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是最后一页')
        else:
            self.AdminTagConfigProcWhiteSet(start, self.adminTagConfigProcWhitePageLength)

    # 删除
    def onAdminTagConfigProcWhiteDel(self):
        itemcnt = self.adminTagConfigProcWhiteTable.rowCount()
        dellist = []

        for i in range(0, itemcnt):
            it = self.adminTagConfigProcWhiteTable.item(i, 1)
            if it == None:
                continue
            chk = it.checkState()
            if chk == 2:  # 状态有0和2
                proc = unicode(self.adminTagConfigProcWhiteTable.item(i, 0).text())
                dellist.append(proc)

        url = 'https://%s:%s/sysconfig/whiteproc/del/%s' % (
        self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        # print url
        for proc in dellist:
            data = {
                'Tokey': self.Tokey,
                'Proc': proc
            }
            # print data
            param = {'Data': json.dumps(data)}
            rt = HttpsPost(url, param)
            # print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:
                    # QtGui.QMessageBox.about(self, u'提示', u'删除客体程序成功:' + proc)
                    pass
                else:
                    QtGui.QMessageBox.about(self, u'错误提示', u'删除白名单程序失败:' + proc + ':' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'删除白名单程序失败:' + rt[1])

        # 刷新列表
        self.AdminTagConfigProcWhiteSet(0, self.adminTagConfigProcWhitePageLength)

    # 更新页计数
    def setAdminTagConfigProcWhiteNowPageText(self):
        tot = self.adminTagConfigProcWhiteTotal
        page = self.adminTagConfigProcWhitePage
        length = self.adminTagConfigProcWhitePageLength
        page_str = '0/0'
        if tot > 0:
            if tot % length > 0:
                page_str = '%d/%d' % (page + 1, (tot / length) + 1)
            else:
                page_str = '%d/%d' % (page + 1, tot / length)
        self.adminTagConfigProcWhitePageText.setText(_translate('adminTagConfigProcWhitePageText', page_str, None))
        
    # 设置白名单列表
    def AdminTagConfigProcWhiteSet(self, start, length):
        url = 'https://%s:%s/sysconfig/whiteproc/search/%s' % (
        self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey,
            'Start': start,
            'Length': length
        }
        # print url, data
        param = {'Data': json.dumps(data)}
        rt = HttpsPost(url, param)
        # print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.adminTagConfigProcWhiteTotal = res['Total']

                # 清空列表
                for i in xrange(0, self.adminTagConfigProcWhitePageLength):
                    self.adminTagConfigProcWhiteTable.setItem(i, 0, None)
                    self.adminTagConfigProcWhiteTable.setItem(i, 1, None)
                    self.adminTagConfigProcWhitePage = 0

                if res['Procs'] != None:
                    # 添加列表
                    cnt = len(res['Procs'])
                    for i in xrange(0, cnt):
                        newItem = QtGui.QTableWidgetItem(res['Procs'][i])
                        #newItem.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagConfigProcWhiteTable.setItem(i, 0, newItem)

                        newItemChkbox = QtGui.QTableWidgetItem()
                        newItemChkbox.setCheckState(False)
                        newItemChkbox.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagConfigProcWhiteTable.setItem(i, 1, newItemChkbox)
                    self.adminTagConfigProcWhitePage = start / self.adminTagConfigProcWhitePageLength
                self.setAdminTagConfigProcWhiteNowPageText()
            else:
                QtGui.QMessageBox.about(self, u'错误提示', res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找组列表失败:' + rt[1])


    # 用户 - 全选
    def onAdminTagConfigProcWhiteSelect(self):
        chk = self.adminTagConfigProcWhiteSelect.checkState()
        if chk == 0:  # 全不选
            itemcnt = self.adminTagConfigProcWhiteTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagConfigProcWhiteTable.item(i, 1)
                if it is None:
                    continue
                it.setCheckState(False)
        elif chk == 2:  # 全选
            itemcnt = self.adminTagConfigProcWhiteTable.rowCount()
            for i in range(0, itemcnt):
                it = self.adminTagConfigProcWhiteTable.item(i, 1)
                if it is None:
                    continue
                it.setCheckState(2)
        else:
            pass

    # 弹出 - 添加 - 确认
    def onAdminTagConfigProcWhiteAddDlgOK(self):
        proc_path = unicode(self.adminTagConfigProcWhiteAddDlgPath.text())
        # 添加客体程序
        url = 'https://%s:%s/sysconfig/whiteproc/add/%s' % (
        self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey,
            'Proc': proc_path
        }
        # print url, data
        param = {'Data': json.dumps(data)}
        rt = HttpsPost(url, param)
        # print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                # QtGui.QMessageBox.about(self, u'设置', u'添加成功:')
                self.AdminTagConfigProcWhiteSet(0, self.adminTagConfigProcWhitePageLength)
            else:
                QtGui.QMessageBox.about(self, u'错误提示', u'添加白名单程序失败:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'添加白名单程序失败:' + rt[1])

    # 弹出 - 添加 - 取消
    def onAdminTagConfigProcWhiteAddDlgCancel(self):
        self.AdminBoardUnsetPopUp()
        self.adminTagConfigProcWhiteAddDlg.hide()
        self.adminTagConfigProcWhiteAddDlgPath.setText(u'')
