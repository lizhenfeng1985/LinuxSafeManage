# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Jul 04 23:56:44 2016
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import gui_login
import gui_admin_board

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

class GuiMain(QtGui.QDialog, gui_login.GuiLogin, gui_admin_board.GuiAdminBoard):
    def __init__(self,parent=None):
        super(GuiMain,self).__init__(parent)        
        self.setupUi(self)
        
    def setupUi(self, mainBoard):
        self.mainBoard = mainBoard
        # 主面板
        self.AddMainBoard()

        # 登录主面板
        self.AddLoginBoard()        

        # 管理员面板
        self.AddAdminBoard()  
        #QtCore.QMetaObject.connectSlotsByName(mainBoard)
        
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

    def AddAdminBoard(self):        
        self.LoadAdminBoard()
        self.adminBoard.hide()
        

import images_rc

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    win=GuiMain()
    win.show()
    app.exec_()
