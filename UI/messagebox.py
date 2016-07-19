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
    
class MessageBox(QtGui.QWidget):
    def __init__(self,parent=None):
        super(MessageBox,self).__init__(parent)
        self.setupUi(self)

    def AddMessageBox(self):
        # 背景
        self.messageBoxBkg = QtGui.QWidget()
        self.messageBoxBkg.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.messageBoxBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.messageBoxBkg.setObjectName(_fromUtf8("messageBoxBkg"))

        # 标题
        self.messageBoxTitle = QtGui.QLabel(self.messageBoxBkg)
        self.messageBoxTitle.setGeometry(QtCore.QRect(210, 0, 1, 295))
        self.messageBoxTitle.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.messageBoxTitle.setObjectName(_fromUtf8("messageBoxTitle"))
        self.messageBoxTitle.setText(_fromUtf8("标题"))

        # 正文
        self.messageBoxText = QtGui.QTextEdit(self.messageBoxBkg)
        self.messageBoxText.setGeometry(QtCore.QRect(10, 30, 321, 101))
        self.messageBoxText.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white_frame.png);"))
        self.messageBoxText.setObjectName(_fromUtf8("messageBoxText"))

        # 确定
        self.messageBoxOK = QtGui.QPushButton(self.messageBoxBkg)
        self.messageBoxOK.setGeometry(QtCore.QRect(120, 140, 77, 23))
        self.messageBoxOK.setObjectName(_fromUtf8("messageBoxOK"))
        self.messageBoxOK.setText(_translate("messageBoxOK", "确定", None))
        
        self.messageBoxBkg.hide()
        
        # 添加用户消息
        self.connect(self.messageBoxOK, QtCore.SIGNAL("clicked()"), self.onMessageBoxOK)
        print 'ADDD'

    def MessageBox(self, msg, title=u"标题", width=340, length=210):
        self.messageBoxBkg.show()
        self.messageBoxBkg.setGeometry(QtCore.QRect(0, 0, width, length))
        self.messageBoxTitle.setText(title)
        self.messageBoxText.setText(msg)
        print 'msgbox',msg, title
    
    def onMessageBoxOK(self):
        self.messageBoxBkg.hide()
        self.messageBoxTitle.setText(_fromUtf8(""))
        self.messageBoxText.setText(_fromUtf8(""))
        
        
import images_rc
