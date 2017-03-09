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


class AdminBoardConfig(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AdminBoardConfig, self).__init__(parent)
        # self.setupUi(self)

    def AddAdminTagConfig(self):
        # Logo
        self.adminTagConfigLogo = QtGui.QWidget(self.adminTagConfigBkg)
        self.adminTagConfigLogo.setGeometry(QtCore.QRect(40, 10, 70, 60))
        self.adminTagConfigLogo.setObjectName(_fromUtf8("adminTagConfigLogo"))
        self.adminTagConfigLogo.setStyleSheet(_fromUtf8("border-image: url(:/images/admin_config_logo.png);"))

        # 标题
        self.adminTagConfigTitle = QtGui.QWidget(self.adminTagConfigBkg)
        self.adminTagConfigTitle.setGeometry(QtCore.QRect(120, 10, 200, 60))
        self.adminTagConfigTitle.setObjectName(_fromUtf8("adminTagConfigTitle"))
        self.adminTagConfigTitle.setStyleSheet(_fromUtf8("border-image: url(:/images/admin_config_title.png);"))

        # 画线
        self.adminTagConfigSpace1 = QtGui.QWidget(self.adminTagConfigBkg)
        self.adminTagConfigSpace1.setGeometry(QtCore.QRect(0, 74, 10000, 1))
        self.adminTagConfigSpace1.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.adminTagConfigSpace1.setObjectName(_fromUtf8("adminTagConfigSpace1"))

        # 画线 上
        self.adminTagConfigSpaceTop = QtGui.QWidget(self.adminTagConfigBkg)
        self.adminTagConfigSpaceTop.setGeometry(QtCore.QRect(0, 112, 10000, 1))
        self.adminTagConfigSpaceTop.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.adminTagConfigSpaceTop.setObjectName(_fromUtf8("adminTagConfigSpaceTop"))

        # 密码-授权 标签页
        self.adminTagConfigTagPasswdSerial = QtGui.QPushButton(self.adminTagConfigBkg)
        self.adminTagConfigTagPasswdSerial.setGeometry(QtCore.QRect(40, 90, 90, 20))
        self.adminTagConfigTagPasswdSerial.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
        self.adminTagConfigTagPasswdSerial.setObjectName(_fromUtf8("adminTagConfigTagPasswdSerial"))
        self.adminTagConfigTagPasswdSerial.setText(_translate("adminTagConfigTagPasswdSerial", "密码/授权", None))

        self.adminTagConfigTagPasswdSerialBkg = QtGui.QWidget(self.adminTagConfigBkg)
        self.adminTagConfigTagPasswdSerialBkg.setGeometry(QtCore.QRect(0, 113, 1000, 307))
        self.adminTagConfigTagPasswdSerialBkg.setObjectName(_fromUtf8("adminTagConfigTagPasswdSerialBkg"))
        self.adminTagConfigTagPasswdSerialBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAdminTagConfigPasswdSerial()

        # 白名单 标签页
        self.adminTagConfigTagProcWhite = QtGui.QPushButton(self.adminTagConfigBkg)
        self.adminTagConfigTagProcWhite.setGeometry(QtCore.QRect(123, 90, 90, 20))
        self.adminTagConfigTagProcWhite.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
        self.adminTagConfigTagProcWhite.setObjectName(_fromUtf8("adminTagConfigTagProcWhite"))
        self.adminTagConfigTagProcWhite.setText(_translate("adminTagConfigTagProcWhite", "白名单", None))

        self.adminTagConfigTagProcWhiteBkg = QtGui.QWidget(self.adminTagConfigBkg)
        self.adminTagConfigTagProcWhiteBkg.setGeometry(QtCore.QRect(0, 113, 1000, 307))
        self.adminTagConfigTagProcWhiteBkg.setObjectName(_fromUtf8("adminTagConfigTagProcWhiteBkg"))
        self.adminTagConfigTagProcWhiteBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAdminTagConfigProcWhite()

        # 自保护 标签页
        self.adminTagConfigTagSelfProtect = QtGui.QPushButton(self.adminTagConfigBkg)
        self.adminTagConfigTagSelfProtect.setGeometry(QtCore.QRect(206, 90, 90, 20))
        self.adminTagConfigTagSelfProtect.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
        self.adminTagConfigTagSelfProtect.setObjectName(_fromUtf8("adminTagConfigTagSelfProtect"))
        self.adminTagConfigTagSelfProtect.setText(_translate("adminTagConfigTagSelfProtect", "自保护", None))

        self.adminTagConfigTagSelfProtectBkg = QtGui.QWidget(self.adminTagConfigBkg)
        self.adminTagConfigTagSelfProtectBkg.setGeometry(QtCore.QRect(0, 113, 1000, 307))
        self.adminTagConfigTagSelfProtectBkg.setObjectName(_fromUtf8("adminTagConfigTagSelfProtectBkg"))
        self.adminTagConfigTagSelfProtectBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        #self.AddAdminTagConfigSelfProtect()

        # 初始化变量
        self.adminTagsConfigTags = {
            self.adminTagConfigTagPasswdSerial: self.adminTagConfigTagPasswdSerialBkg,
            self.adminTagConfigTagProcWhite: self.adminTagConfigTagProcWhiteBkg,
            self.adminTagConfigTagSelfProtect: self.adminTagConfigTagSelfProtectBkg,
        }

        # 默认显示首页
        self._onAdminConfigChangeTags(self.adminTagConfigTagPasswdSerial)

        # 消息处理
        self.connect(self.adminTagConfigTagPasswdSerial, QtCore.SIGNAL("clicked()"), self.onAdminTagConfigTagPasswdSerial)
        self.connect(self.adminTagConfigTagProcWhite, QtCore.SIGNAL("clicked()"), self.onAdminTagConfigTagProcWhite)
        self.connect(self.adminTagConfigTagSelfProtect, QtCore.SIGNAL("clicked()"), self.onAdminTagConfigTagSelfProtect)

    def _onAdminConfigChangeTags(self, tagBtn):
        for btn, bkg in self.adminTagsConfigTags.items():
            if btn == tagBtn:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey_sel.png);"))
                bkg.show()
            else:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
                bkg.hide()

    def onAdminTagConfigTagPasswdSerial(self):
        if self.AdminBoardCheckPopUp():
            return
        self._onAdminConfigChangeTags(self.adminTagConfigTagPasswdSerial)

    def onAdminTagConfigTagProcWhite(self):
        if self.AdminBoardCheckPopUp():
            return
        self._onAdminConfigChangeTags(self.adminTagConfigTagProcWhite)

    def onAdminTagConfigTagSelfProtect(self):
        if self.AdminBoardCheckPopUp():
            return
        self._onAdminConfigChangeTags(self.adminTagConfigTagSelfProtect)

import images_rc
