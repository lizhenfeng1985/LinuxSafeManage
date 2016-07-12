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
    
class AdminBoardHighUser(QtGui.QWidget):
    def __init__(self,parent=None):
        super(AdminBoardHighUser,self).__init__(parent)        
        #self.setupUi(self)

    def AddAdminTagHighUser(self):
        # 画线 左
        self.adminTagHighUserSpaceLeft = QtGui.QWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.adminTagHighUserSpaceLeft.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey.png);"))
        self.adminTagHighUserSpaceLeft.setObjectName(_fromUtf8("adminTagHighSpaceLeft"))

        # 画线 中
        self.adminTagHighUserSpaceMid = QtGui.QWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserSpaceMid.setGeometry(QtCore.QRect(160, 0, 1, 295))
        self.adminTagHighUserSpaceMid.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey.png);"))
        self.adminTagHighUserSpaceMid.setObjectName(_fromUtf8("adminTagHighSpaceMid"))

        # 画线 右
        self.adminTagHighUserSpaceRight = QtGui.QWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.adminTagHighUserSpaceRight.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey.png);"))
        self.adminTagHighUserSpaceRight.setObjectName(_fromUtf8("adminTagHighUserSpaceRight"))

        # 画线 底
        self.adminTagHighUserSpaceBottom = QtGui.QWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.adminTagHighUserSpaceBottom.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey.png);"))
        self.adminTagHighUserSpaceBottom.setObjectName(_fromUtf8("adminTagHighUserSpaceBottom"))

        # 组 - 添加
        self.adminTagHighUserGroupAdd = QtGui.QPushButton(self.adminTagHighTagUserBkg)
        self.adminTagHighUserGroupAdd.setGeometry(QtCore.QRect(30, 5, 55, 30))
        self.adminTagHighUserGroupAdd.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.adminTagHighUserGroupAdd.setObjectName(_fromUtf8("adminTagHighUserGroupAdd"))
        self.adminTagHighUserGroupAdd.setText(_translate("adminTagHighUserGroupAdd", "添加+", None))

        # 组 - 删除
        self.adminTagHighUserGroupDel = QtGui.QPushButton(self.adminTagHighTagUserBkg)
        self.adminTagHighUserGroupDel.setGeometry(QtCore.QRect(90, 5, 55, 30))
        self.adminTagHighUserGroupDel.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.adminTagHighUserGroupDel.setObjectName(_fromUtf8("adminTagHighUserGroupDel"))
        self.adminTagHighUserGroupDel.setText(_translate("adminTagHighUserGroupDel", "删除+", None))

        # 组 - 列表
        self.adminTagHighUserGroupTree = QtGui.QTreeWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserGroupTree.setGeometry(QtCore.QRect(30, 40, 120, 245))
        self.adminTagHighUserGroupTree.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.adminTagHighUserGroupTree.setObjectName(_fromUtf8("adminTagHighUserGroupTree"))
        self.adminTagHighUserGroupTree.setHeaderHidden(True)

        # 组标题显示
        self.adminTagHighUserGroupName = QtGui.QLabel(self.adminTagHighTagUserBkg)
        self.adminTagHighUserGroupName.setGeometry(QtCore.QRect(190, 5, 120, 30))
        self.adminTagHighUserGroupName.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_no_frame.png.png);"))
        self.adminTagHighUserGroupName.setObjectName(_fromUtf8("adminTagHighUserGroupName"))
        self.adminTagHighUserGroupName.setText(_translate("adminTagHighUserGroupName", "默认组", None))

        # 用户 - 添加
        self.adminTagHighUserAdd = QtGui.QPushButton(self.adminTagHighTagUserBkg)
        self.adminTagHighUserAdd.setGeometry(QtCore.QRect(710, 5, 90, 30))
        self.adminTagHighUserAdd.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.adminTagHighUserAdd.setObjectName(_fromUtf8("adminTagHighUserAdd"))
        self.adminTagHighUserAdd.setText(_translate("adminTagHighUserAdd", "添加用户", None))

        # 用户 - 删除
        self.adminTagHighUserDel = QtGui.QPushButton(self.adminTagHighTagUserBkg)
        self.adminTagHighUserDel.setGeometry(QtCore.QRect(820, 5, 90, 30))
        self.adminTagHighUserDel.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.adminTagHighUserDel.setObjectName(_fromUtf8("adminTagHighUserDel"))
        self.adminTagHighUserDel.setText(_translate("adminTagHighUserDel", "删除用户", None))

        # 用户 - 列表表格
        self.adminTagHighUserTableCount = 10
        self.adminTagHighUserTable = QtGui.QTableWidget(self.adminTagHighTagUserBkg)
        self.adminTagHighUserTable.setGeometry(QtCore.QRect(175, 40, 785, 245))
        self.adminTagHighUserTable.setObjectName(_fromUtf8("adminTagSpecialTable"))
        self.adminTagHighUserTable.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.jpg);"))
        self.adminTagHighUserTable.verticalHeader().setVisible(False)
        self.adminTagHighUserTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagHighUserTable.setAlternatingRowColors(True)
        #list_widget.adminTagHighUserTable(QtGui.QAbstractItemView.SelectRows)
        self.adminTagHighUserTable.setRowCount(self.adminTagHighUserTableCount)
        self.adminTagHighUserTable.setColumnCount(2)
        self.adminTagHighUserTable.setHorizontalHeaderLabels([_fromUtf8("用户名"),_fromUtf8("选择")])
        self.adminTagHighUserTable.setShowGrid(False)
        self.adminTagHighUserTable.setColumnWidth(0,300)
        self.adminTagHighUserTable.setColumnWidth(1,300)
        for i in range(0, self.adminTagHighUserTableCount):
            self.adminTagHighUserTable.setRowHeight(i,21)
import images_rc
