# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Jul 04 23:56:44 2016
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import login
import admin_board
import admin_board_special
import admin_board_safe
import admin_board_high
import admin_board_high_user
import admin_board_high_proc
import admin_board_high_objproc
import admin_board_high_objfile


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

class GuiMain(QtGui.QDialog, \
              login.LoginBoard, admin_board.AdminBoard, \
              admin_board_special.AdminBoardSpecial, \
              admin_board_safe.AdminBoardSafe, \
              admin_board_high.AdminBoardHigh, \
              admin_board_high_user.AdminBoardHighUser, \
              admin_board_high_proc.AdminBoardHighProc, \
              admin_board_high_objproc.AdminBoardHighObjProc, \
              admin_board_high_objfile.AdminBoardHighObjFile):
    def __init__(self,parent=None):
        super(GuiMain,self).__init__(parent)        
        self.setupUi(self)
        
    def setupUi(self, mainBoard):
        self.mainBoard = mainBoard
        # 主面板
        self.AddMainBoard()

        # 登录主面板
        self.AddLoginBoard()
        
    def AddMainBoard(self):
        # 主面板
        self.mainBoard.setObjectName(_fromUtf8("mainBoard"))
        self.mainBoard.resize(1000, 600)
        self.mainBoard.setStyleSheet(_fromUtf8("border-image: url(:/images/main_bk.png);"))
        self.mainBoard.setWindowTitle(_translate("Linux安全客户端", "Linux安全客户端", None))

        # 标题 - 欢迎
        self.mainBoardTitle = QtGui.QWidget(self.mainBoard)
        self.mainBoardTitle.setGeometry(QtCore.QRect(10, 10, 345, 90))
        self.mainBoardTitle.setStyleSheet(_fromUtf8("border-image: url(:/images/login_title.png);"))
        self.mainBoardTitle.setObjectName(_fromUtf8("mainBoardTitle"))

    def AddLoginBoard(self):
        self.LoadLoginBoard()
        

import images_rc

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    win=GuiMain()
    win.show()
    app.exec_()
