# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
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


class AdminBoardHome(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AdminBoardHome, self).__init__(parent)
        # self.setupUi(self)

    def AddAdminTagHome(self):
        # webkit
        self.adminTagHomeWebkit = QtWebKit.QWebView(self.adminTagHomeBkg)
        self.adminTagHomeWebkit.setGeometry(QtCore.QRect(60, 40, 860, 400))

        load_html_file = './html/admin_board_home.default.html'

        url = 'https://%s:%s/home/admin/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey
        }
        param = {'Data': json.dumps(data)}
        rt = HttpsPost(url, param)
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                try:
                    fp = open("./html/admin_board_home.tpl", "r")
                    html_text = fp.read()
                    fp.close()
                    html_text = html_text.replace("{{.DATA}}", json.dumps(res["LabValues"]))

                    fp = open("./html/admin_board_home.html", "w")
                    fp.write(html_text)
                    fp.close()
                    load_html_file = "./html/admin_board_home.html"
                except Exception as e:
                    pass
        self.adminTagHomeWebkit.load(QtCore.QUrl(load_html_file))
