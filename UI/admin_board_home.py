# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
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


class AdminBoardHome(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AdminBoardHome, self).__init__(parent)
        # self.setupUi(self)

    def AddAdminTagHome(self):
        # webkit
        self.adminTagHomeWebkit = QtWebKit.QWebView(self.adminTagHomeBkg)
        self.adminTagHomeWebkit.setGeometry(QtCore.QRect(60, 40, 860, 400))
        url = 'http://%s:%s/home/admin/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        self.adminTagHomeWebkit.load(QtCore.QUrl(url))


import images_rc
