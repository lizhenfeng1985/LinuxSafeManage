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
    
class AdminBoardHigh(QtGui.QWidget):
    def __init__(self,parent=None):
        super(AdminBoardHigh,self).__init__(parent)        
        #self.setupUi(self)

    def AddAdminTagHigh(self):
        # Logo
        self.adminTagHighLogo = QtGui.QWidget(self.adminTagHighBkg)
        self.adminTagHighLogo.setGeometry(QtCore.QRect(40, 10, 70, 60))
        self.adminTagHighLogo.setObjectName(_fromUtf8("adminTagHighLogo"))
        self.adminTagHighLogo.setStyleSheet(_fromUtf8("border-image: url(:/images/admin_special_logo.png);"))

        # 标题
        self.adminTagHighTitle = QtGui.QWidget(self.adminTagHighBkg)
        self.adminTagHighTitle.setGeometry(QtCore.QRect(120, 10, 200, 60))
        self.adminTagHighTitle.setObjectName(_fromUtf8("adminTagHighTitle"))
        self.adminTagHighTitle.setStyleSheet(_fromUtf8("border-image: url(:/images/admin_special_title.png);"))

        # 画线 
        self.adminTagHighSpace1 = QtGui.QWidget(self.adminTagHighBkg)
        self.adminTagHighSpace1.setGeometry(QtCore.QRect(0, 74, 10000, 1))
        self.adminTagHighSpace1.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.adminTagHighSpace1.setObjectName(_fromUtf8("adminTagHighSpace1"))

        # 画线 上
        self.adminTagHighSpaceTop = QtGui.QWidget(self.adminTagHighBkg)
        self.adminTagHighSpaceTop.setGeometry(QtCore.QRect(0, 112, 10000, 1))
        self.adminTagHighSpaceTop.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.adminTagHighSpaceTop.setObjectName(_fromUtf8("adminTagHighSpaceTop"))
              
        # 用户组 标签页
        self.adminTagHighTagUser = QtGui.QPushButton(self.adminTagHighBkg)
        self.adminTagHighTagUser.setGeometry(QtCore.QRect(40, 90, 90, 20))
        self.adminTagHighTagUser.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
        self.adminTagHighTagUser.setObjectName(_fromUtf8("adminTagHighTagUser"))
        self.adminTagHighTagUser.setText(_translate("adminTagHighTagUser", "用户组", None))

        self.adminTagHighTagUserBkg = QtGui.QWidget(self.adminTagHighBkg)
        self.adminTagHighTagUserBkg.setGeometry(QtCore.QRect(0, 113, 1000, 307))
        self.adminTagHighTagUserBkg.setObjectName(_fromUtf8("adminTagHighTagUserBkg"))
        self.adminTagHighTagUserBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAdminTagHighUser()

        # 程序组 标签页
        self.adminTagHighTagProc = QtGui.QPushButton(self.adminTagHighBkg)
        self.adminTagHighTagProc.setGeometry(QtCore.QRect(123, 90, 90, 20))
        self.adminTagHighTagProc.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
        self.adminTagHighTagProc.setObjectName(_fromUtf8("adminTagHighTagProc"))
        self.adminTagHighTagProc.setText(_translate("adminTagHighTagUser", "程序组", None))

        self.adminTagHighTagProcBkg = QtGui.QWidget(self.adminTagHighBkg)
        self.adminTagHighTagProcBkg.setGeometry(QtCore.QRect(0, 113, 1000, 307))
        self.adminTagHighTagProcBkg.setObjectName(_fromUtf8("adminTagHighTagProcBkg"))
        self.adminTagHighTagProcBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

        # 对象 - 文件组 标签页
        self.adminTagHighTagObjFile = QtGui.QPushButton(self.adminTagHighBkg)
        self.adminTagHighTagObjFile.setGeometry(QtCore.QRect(206, 90, 90, 20))
        self.adminTagHighTagObjFile.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
        self.adminTagHighTagObjFile.setObjectName(_fromUtf8("adminTagHighTagObjFile"))
        self.adminTagHighTagObjFile.setText(_translate("adminTagHighTagObjFile", "文件对象", None))

        self.adminTagHighTagObjFileBkg = QtGui.QWidget(self.adminTagHighBkg)
        self.adminTagHighTagObjFileBkg.setGeometry(QtCore.QRect(0, 113, 1000, 307))
        self.adminTagHighTagObjFileBkg.setObjectName(_fromUtf8("adminTagHighTagObjFileBkg"))
        self.adminTagHighTagObjFileBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

        # 对象 - 进程组 标签页
        self.adminTagHighTagObjProc = QtGui.QPushButton(self.adminTagHighBkg)
        self.adminTagHighTagObjProc.setGeometry(QtCore.QRect(289, 90, 90, 20))
        self.adminTagHighTagObjProc.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
        self.adminTagHighTagObjProc.setObjectName(_fromUtf8("adminTagHighTagObjProc"))
        self.adminTagHighTagObjProc.setText(_translate("adminTagHighTagObjFile", "进程对象", None))

        self.adminTagHighTagObjProcBkg = QtGui.QWidget(self.adminTagHighBkg)
        self.adminTagHighTagObjProcBkg.setGeometry(QtCore.QRect(0, 113, 1000, 307))
        self.adminTagHighTagObjProcBkg.setObjectName(_fromUtf8("adminTagHighTagObjProcBkg"))
        self.adminTagHighTagObjProcBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

        # 对象 - 网络组 标签页
        self.adminTagHighTagObjNet = QtGui.QPushButton(self.adminTagHighBkg)
        self.adminTagHighTagObjNet.setGeometry(QtCore.QRect(372, 90, 90, 20))
        self.adminTagHighTagObjNet.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
        self.adminTagHighTagObjNet.setObjectName(_fromUtf8("adminTagHighTagObjNet"))
        self.adminTagHighTagObjNet.setText(_translate("adminTagHighTagObjNet", "网络对象", None))

        self.adminTagHighTagObjNetBkg = QtGui.QWidget(self.adminTagHighBkg)
        self.adminTagHighTagObjNetBkg.setGeometry(QtCore.QRect(0, 113, 1000, 307))
        self.adminTagHighTagObjNetBkg.setObjectName(_fromUtf8("adminTagHighTagObjNetBkg"))
        self.adminTagHighTagObjNetBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

        # 权限表 标签页
        self.adminTagHighTagPerm = QtGui.QPushButton(self.adminTagHighBkg)
        self.adminTagHighTagPerm.setGeometry(QtCore.QRect(455, 90, 90, 20))
        self.adminTagHighTagPerm.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
        self.adminTagHighTagPerm.setObjectName(_fromUtf8("adminTagHighTagPerm"))
        self.adminTagHighTagPerm.setText(_translate("adminTagHighTagObjNet", "权限表", None))

        self.adminTagHighTagPermBkg = QtGui.QWidget(self.adminTagHighBkg)
        self.adminTagHighTagPermBkg.setGeometry(QtCore.QRect(0, 113, 1000, 307))
        self.adminTagHighTagPermBkg.setObjectName(_fromUtf8("adminTagHighTagPermBkg"))
        self.adminTagHighTagPermBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

        # 初始化变量
        self.adminTagsHighTags = {
            self.adminTagHighTagUser      : self.adminTagHighTagUserBkg,
            self.adminTagHighTagProc      : self.adminTagHighTagProcBkg,
            self.adminTagHighTagObjFile   : self.adminTagHighTagObjFileBkg,
            self.adminTagHighTagObjProc   : self.adminTagHighTagObjProcBkg,
            self.adminTagHighTagObjNet    : self.adminTagHighTagObjNetBkg,
            self.adminTagHighTagPerm      : self.adminTagHighTagPermBkg,
        }

        # 默认显示首页
        self._onAdminHighChangeTags(self.adminTagHighTagUser)
        
        # 消息处理        
        self.connect(self.adminTagHighTagUser, QtCore.SIGNAL("clicked()"), self.onAdminTagHighTagUser)
        self.connect(self.adminTagHighTagProc, QtCore.SIGNAL("clicked()"), self.onAdminTagHighTagProc)
        self.connect(self.adminTagHighTagObjFile, QtCore.SIGNAL("clicked()"), self.onAdminTagHighTagObjFile)
        self.connect(self.adminTagHighTagObjProc, QtCore.SIGNAL("clicked()"), self.onAdminTagHighTagObjProc)
        self.connect(self.adminTagHighTagObjNet, QtCore.SIGNAL("clicked()"), self.onAdminTagHighTagObjNet)
        self.connect(self.adminTagHighTagPerm, QtCore.SIGNAL("clicked()"), self.onAdminTagHighTagPerm)

    def _onAdminHighChangeTags(self, tagBtn):
        for btn, bkg in self.adminTagsHighTags.items():
            if btn == tagBtn:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey_sel.png);"))
                bkg.show()
            else:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
                bkg.hide()

    def onAdminTagHighTagUser(self):
        self._onAdminHighChangeTags(self.adminTagHighTagUser)

    def onAdminTagHighTagProc(self):
        self._onAdminHighChangeTags(self.adminTagHighTagProc)

    def onAdminTagHighTagObjFile(self):
        self._onAdminHighChangeTags(self.adminTagHighTagObjFile)

    def onAdminTagHighTagObjProc(self):
        self._onAdminHighChangeTags(self.adminTagHighTagObjProc)

    def onAdminTagHighTagObjNet(self):
        self._onAdminHighChangeTags(self.adminTagHighTagObjNet)

    def onAdminTagHighTagPerm(self):
        self._onAdminHighChangeTags(self.adminTagHighTagPerm)

import images_rc
