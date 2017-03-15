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


class AuditBoard(QtGui.QWidget):
    def __init__(self, parent=None):
        self._auditBoardPopUp = False
        super(AuditBoard, self).__init__(parent)
        self.setupUi(self)

    def AuditBoardSetPopUp(self):
        self._auditBoardPopUp = True

    def AuditBoardUnsetPopUp(self):
        self._auditBoardPopUp = False

    def AuditBoardCheckPopUp(self):
        return self._auditBoardPopUp

    def LoadAuditBoard(self):
        # Audit主面板
        self.auditBoard = QtGui.QWidget(self.mainBoard)
        self.auditBoard.setGeometry(QtCore.QRect(0, 128, 1000, 450))
        self.auditBoard.setObjectName(_fromUtf8("auditBoard"))
        self.auditBoard.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

        # Audit Home 标签页
        self.auditTagHome = QtGui.QPushButton(self.auditBoard)
        self.auditTagHome.setGeometry(QtCore.QRect(0, 0, 91, 30))
        self.auditTagHome.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
        self.auditTagHome.setObjectName(_fromUtf8("auditTagHome"))
        self.auditTagHome.setText(_translate("auditTagHome", "首页概览", None))

        self.auditTagHomeBkg = QtGui.QWidget(self.auditBoard)
        self.auditTagHomeBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.auditTagHomeBkg.setObjectName(_fromUtf8("auditTagHomeBkg"))
        self.auditTagHomeBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAuditTagHome()

        # Audit SafeEvent 标签页
        self.auditTagSafeEvent = QtGui.QPushButton(self.auditBoard)
        self.auditTagSafeEvent.setGeometry(QtCore.QRect(92, 0, 91, 30))
        self.auditTagSafeEvent.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
        self.auditTagSafeEvent.setObjectName(_fromUtf8("auditTagSafeEvent"))
        self.auditTagSafeEvent.setText(_translate("auditTagSafeEvent", "安全事件", None))

        self.auditTagSafeEventBkg = QtGui.QWidget(self.auditBoard)
        self.auditTagSafeEventBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.auditTagSafeEventBkg.setObjectName(_fromUtf8("auditTagSafeEventBkg"))
        self.auditTagSafeEventBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAuditTagSafeEvent()

        # Audit Sys Event 标签页
        self.auditTagSysEvent= QtGui.QPushButton(self.auditBoard)
        self.auditTagSysEvent.setGeometry(QtCore.QRect(184, 0, 91, 30))
        self.auditTagSysEvent.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
        self.auditTagSysEvent.setObjectName(_fromUtf8("auditTagSysEvent"))
        self.auditTagSysEvent.setText(_translate("auditTagSysEvent", "运行事件", None))

        self.auditTagSysEventBkg = QtGui.QWidget(self.auditBoard)
        self.auditTagSysEventBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.auditTagSysEventBkg.setObjectName(_fromUtf8("auditTagSysEventBkg"))
        self.auditTagSysEventBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAuditTagSysEvent()

        # Audit Config 标签页
        self.auditTagConfig = QtGui.QPushButton(self.auditBoard)
        self.auditTagConfig.setGeometry(QtCore.QRect(276, 0, 91, 30))
        self.auditTagConfig.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
        self.auditTagConfig.setObjectName(_fromUtf8("auditTagConfig"))
        self.auditTagConfig.setText(_translate("auditTagConfig", "系统设置", None))

        self.auditTagConfigBkg = QtGui.QWidget(self.auditBoard)
        self.auditTagConfigBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.auditTagConfigBkg.setObjectName(_fromUtf8("auditTagConfigBkg"))
        self.auditTagConfigBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAuditTagConfig()

        # 画线
        self.auditBoardSpace1 = QtGui.QWidget(self.auditBoard)
        self.auditBoardSpace1.setGeometry(QtCore.QRect(0, 32, 10000, 1))
        self.auditBoardSpace1.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.auditBoardSpace1.setObjectName(_fromUtf8("auditBoardSpace1"))

        # 初始化变量
        self.auditTags = {
            self.auditTagHome: self.auditTagHomeBkg,
            self.auditTagSafeEvent: self.auditTagSafeEventBkg,
            self.auditTagSysEvent: self.auditTagSysEventBkg,
            self.auditTagConfig: self.auditTagConfigBkg,
        }

        # 默认显示首页
        self._onAuditChangeTags(self.auditTagHome)

        # 消息处理
        self.connect(self.auditTagHome, QtCore.SIGNAL("clicked()"), self.onAuditTagHome)
        self.connect(self.auditTagSafeEvent, QtCore.SIGNAL("clicked()"), self.onAuditTagSafeEvent)
        self.connect(self.auditTagSysEvent, QtCore.SIGNAL("clicked()"), self.onAuditTagSysEvent)
        self.connect(self.auditTagConfig, QtCore.SIGNAL("clicked()"), self.onAuditTagConfig)

    def _onAuditChangeTags(self, tagBtn):
        for btn, bkg in self.auditTags.items():
            if btn == tagBtn:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue_sel.png);"))
                bkg.show()
            else:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_tag_blue.png);"))
                bkg.hide()

    def onAuditTagHome(self):
        if self.AuditBoardCheckPopUp():
            return
        self._onAuditChangeTags(self.auditTagHome)

    def onAuditTagSafeEvent(self):
        if self.AuditBoardCheckPopUp():
            return
        self._onAuditChangeTags(self.auditTagSafeEvent)

    def onAuditTagSysEvent(self):
        if self.AuditBoardCheckPopUp():
            return
        self._onAuditChangeTags(self.auditTagSysEvent)

    def onAuditTagConfig(self):
        if self.AuditBoardCheckPopUp():
            return
        self._onAuditChangeTags(self.auditTagConfig)

