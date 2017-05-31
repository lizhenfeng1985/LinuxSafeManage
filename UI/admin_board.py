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
    
class AdminBoard(QtGui.QWidget):
    def __init__(self,parent=None):
        self._adminBoardPopUp = False
        super(AdminBoard,self).__init__(parent)        
        self.setupUi(self)

    def AdminBoardSetPopUp(self):
        self._adminBoardPopUp = True

    def AdminBoardUnsetPopUp(self):
        self._adminBoardPopUp = False
        
    def AdminBoardCheckPopUp(self):
        return self._adminBoardPopUp

    def LoadAdminBoard(self):
        # Admin主面板
        self.adminBoard = QtGui.QWidget(self.mainBoard)
        self.adminBoard.setGeometry(QtCore.QRect(0, 128, 1000, 450))
        self.adminBoard.setObjectName(_fromUtf8("adminBoard"))
        self.adminBoard.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

        # Admin Home 标签页
        self.adminTagHome = QtGui.QPushButton(self.adminBoard)
        self.adminTagHome.setGeometry(QtCore.QRect(0, 0, 91, 30))
        self.adminTagHome.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
        self.adminTagHome.setObjectName(_fromUtf8("adminTagHome"))
        self.adminTagHome.setText(_translate("adminTagHome", "首页概览", None))

        self.adminTagHomeBkg = QtGui.QWidget(self.adminBoard)
        self.adminTagHomeBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagHomeBkg.setObjectName(_fromUtf8("adminTagHomeBkg"))
        self.adminTagHomeBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAdminTagHome()


        # Admin Safe 标签页
        self.adminTagSafe = QtGui.QPushButton(self.adminBoard)
        self.adminTagSafe.setGeometry(QtCore.QRect(92, 0, 91, 30))
        self.adminTagSafe.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
        self.adminTagSafe.setObjectName(_fromUtf8("adminTagSafe"))
        self.adminTagSafe.setText(_translate("adminTagSafe", "基础防护", None))

        self.adminTagSafeBkg = QtGui.QWidget(self.adminBoard)
        self.adminTagSafeBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagSafeBkg.setObjectName(_fromUtf8("adminTagSafeBkg"))
        self.adminTagSafeBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAdminTagSafe()

        # Admin Special 标签页
        self.adminTagSpecial = QtGui.QPushButton(self.adminBoard)
        self.adminTagSpecial.setGeometry(QtCore.QRect(184, 0, 91, 30))
        self.adminTagSpecial.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
        self.adminTagSpecial.setObjectName(_fromUtf8("adminTagSpecial"))
        self.adminTagSpecial.setText(_translate("adminTagSpecial", "特殊资源", None))

        self.adminTagSpecialBkg = QtGui.QWidget(self.adminBoard)
        self.adminTagSpecialBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagSpecialBkg.setObjectName(_fromUtf8("adminTagSpecialBkg"))
        self.adminTagSpecialBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAdminTagSpecial()

        # 高级配置 标签页
        self.adminTagHigh = QtGui.QPushButton(self.adminBoard)
        self.adminTagHigh.setGeometry(QtCore.QRect(276, 0, 91, 30))
        self.adminTagHigh.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
        self.adminTagHigh.setObjectName(_fromUtf8("adminTagHigh"))
        self.adminTagHigh.setText(_translate("adminTagHigh", "高级配置", None))

        self.adminTagHighBkg = QtGui.QWidget(self.adminBoard)
        self.adminTagHighBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagHighBkg.setObjectName(_fromUtf8("adminTagHighBkg"))
        self.adminTagHighBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAdminTagHigh()

        # Admin Config 标签页
        self.adminTagConfig = QtGui.QPushButton(self.adminBoard)
        self.adminTagConfig.setGeometry(QtCore.QRect(368, 0, 91, 30))
        self.adminTagConfig.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
        self.adminTagConfig.setObjectName(_fromUtf8("adminTagConfig"))
        self.adminTagConfig.setText(_translate("adminTagConfig", "系统设置", None))

        self.adminTagConfigBkg = QtGui.QWidget(self.adminBoard)
        self.adminTagConfigBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagConfigBkg.setObjectName(_fromUtf8("adminTagConfigBkg"))
        self.adminTagConfigBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAdminTagConfig()

        # 画线 
        self.adminBoardSpace1 = QtGui.QWidget(self.adminBoard)
        self.adminBoardSpace1.setGeometry(QtCore.QRect(0, 32, 10000, 1))
        self.adminBoardSpace1.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.adminBoardSpace1.setObjectName(_fromUtf8("adminBoardSpace1"))

        # 初始化变量
        self.adminTags = {
            self.adminTagHome    : self.adminTagHomeBkg,
            self.adminTagSafe    : self.adminTagSafeBkg,
            self.adminTagSpecial : self.adminTagSpecialBkg,
            self.adminTagHigh    : self.adminTagHighBkg,
            self.adminTagConfig  : self.adminTagConfigBkg,
        }

        # 默认显示首页
        self._onAdminChangeTags(self.adminTagHome)
        
        # 消息处理        
        self.connect(self.adminTagHome, QtCore.SIGNAL("clicked()"), self.onAdminTagHome)
        self.connect(self.adminTagSafe, QtCore.SIGNAL("clicked()"), self.onAdminTagSafe)
        self.connect(self.adminTagSpecial, QtCore.SIGNAL("clicked()"), self.onAdminTagSpecial)
        self.connect(self.adminTagHigh, QtCore.SIGNAL("clicked()"), self.onAdminTagHigh)
        self.connect(self.adminTagConfig, QtCore.SIGNAL("clicked()"), self.onAdminTagConfig)

    def _onAdminChangeTags(self, tagBtn):
        for btn, bkg in self.adminTags.items():
            if btn == tagBtn:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue_sel.png);"))
                bkg.show()
            else:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
                bkg.hide()

    def onAdminTagHome(self):
        if self.AdminBoardCheckPopUp():
            return
        self._onAdminChangeTags(self.adminTagHome)
        self.AdminTagHomeReloadData()

    def onAdminTagSafe(self):
        if self.AdminBoardCheckPopUp():
            return
        self._onAdminChangeTags(self.adminTagSafe)

    def onAdminTagSpecial(self):
        if self.AdminBoardCheckPopUp():
            return
        self._onAdminChangeTags(self.adminTagSpecial)

    def onAdminTagHigh(self):
        if self.AdminBoardCheckPopUp():
            return
        self._onAdminChangeTags(self.adminTagHigh)
        
    def onAdminTagConfig(self):
        if self.AdminBoardCheckPopUp():
            return
        self._onAdminChangeTags(self.adminTagConfig)


import images_rc
