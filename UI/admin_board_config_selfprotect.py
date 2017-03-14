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


class AdminBoardConfigSelfProtect(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AdminBoardConfigSelfProtect, self).__init__(parent)
        # self.setupUi(self)

    def AddAdminTagConfigSelfProtect(self):
        # 变量
        self.adminTagConfigSelfProtectModeValue = 0

        # 画线 左
        self.adminTagConfigSelfProtectSpaceLeft = QtGui.QWidget(self.adminTagConfigTagSelfProtectBkg)
        self.adminTagConfigSelfProtectSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.adminTagConfigSelfProtectSpaceLeft.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigSelfProtectSpaceLeft.setObjectName(_fromUtf8('adminTagHighSpaceLeft'))

        # 画线 中
        self.adminTagConfigSelfProtectSpaceMid = QtGui.QWidget(self.adminTagConfigTagSelfProtectBkg)
        self.adminTagConfigSelfProtectSpaceMid.setGeometry(QtCore.QRect(500, 0, 1, 295))
        self.adminTagConfigSelfProtectSpaceMid.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigSelfProtectSpaceMid.setObjectName(_fromUtf8('adminTagHighSpaceMid'))

        # 画线 右
        self.adminTagConfigSelfProtectSpaceRight = QtGui.QWidget(self.adminTagConfigTagSelfProtectBkg)
        self.adminTagConfigSelfProtectSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.adminTagConfigSelfProtectSpaceRight.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigSelfProtectSpaceRight.setObjectName(_fromUtf8('adminTagConfigSelfProtectSpaceRight'))

        # 画线 底
        self.adminTagConfigSelfProtectSpaceBottom = QtGui.QWidget(self.adminTagConfigTagSelfProtectBkg)
        self.adminTagConfigSelfProtectSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.adminTagConfigSelfProtectSpaceBottom.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigSelfProtectSpaceBottom.setObjectName(_fromUtf8('adminTagConfigSelfProtectSpaceBottom'))

        # 当前模式 - 文字
        self.adminTagConfigSelfProtectModeTxet = QtGui.QLabel(self.adminTagConfigTagSelfProtectBkg)
        self.adminTagConfigSelfProtectModeTxet.setGeometry(QtCore.QRect(40, 80, 91, 30))
        self.adminTagConfigSelfProtectModeTxet.setObjectName(_fromUtf8("adminTagConfigSelfProtectModeTxet"))
        self.adminTagConfigSelfProtectModeTxet.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_no_frame.png);"))
        self.adminTagConfigSelfProtectModeTxet.setText(_translate("adminTagConfigSelfProtectModeTxet", "当前模式", None))
        self.adminTagConfigSelfProtectModeTxet.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        # 当前模式
        self.adminTagConfigSelfProtectMode = QtGui.QPushButton(self.adminTagConfigTagSelfProtectBkg)
        self.adminTagConfigSelfProtectMode.setGeometry(QtCore.QRect(140, 80, 140, 30))
        self.adminTagConfigSelfProtectMode.setObjectName(_fromUtf8("adminTagConfigSelfProtectMode"))
        self.adminTagConfigSelfProtectMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_off.png);"))
        self.adminTagConfigSelfProtectMode.setText(_translate("adminTagConfigSelfProtectMode", "", None))

        # 消息处理
        self.connect(self.adminTagConfigSelfProtectMode, QtCore.SIGNAL("clicked()"), self.onAdminTagConfigSelfProtectModeClick)

        # 获取自保护设置状态
        self.AdminTagConfigSelfProtectModeGet()

    def AdminTagConfigSelfProtectModeGet(self):
        pass

    def onAdminTagConfigSelfProtectModeClick(self):
        newMode = 0
        if self.adminTagConfigSelfProtectModeValue == 0:
            newMode = 1
        else:
            newMode = 0
        url = 'https://%s:%s/statself/set/%s' % (
            self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey,
            'Mode': newMode,
        }
        param = {'Data': json.dumps(data)}
        # print url, data
        rt = HttpsPost(url, param)
        # print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                if self.adminTagConfigSelfProtectModeValue == 0:
                    self.adminTagConfigSelfProtectModeValue = 1
                    self.adminTagConfigSelfProtectMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_on.png);"))
                else:
                    self.adminTagConfigSelfProtectModeValue = 0
                    self.adminTagConfigSelfProtectMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_off.png);"))
                QtGui.QMessageBox.about(self, u"设置", u"设置成功:")
            else:
                QtGui.QMessageBox.about(self, u"设置", u'错误提示:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + rt[1])
