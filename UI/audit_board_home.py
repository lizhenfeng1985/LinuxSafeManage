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


class AuditBoardHome(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AuditBoardHome, self).__init__(parent)
        # self.setupUi(self)

    def AddAuditTagHome(self):
        # webkit
        self.auditTagHomeWebkit = QtWebKit.QWebView(self.auditTagHomeBkg)
        self.auditTagHomeWebkit.setGeometry(QtCore.QRect(60, 40, 860, 400))

        self.AuditTagHomeReloadData()

    def AuditTagHomeReloadData(self):
        load_html_file = './html/audit_board_home.default.html'

        # use same page as admin
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
                    fp = open("./html/audit_board_home.tpl", "r")
                    html_text = fp.read()
                    fp.close()
                    html_text = html_text.replace("{{.DATA}}", json.dumps(res["LabValues"]))

                    fp = open("./html/audit_board_home.html", "w")
                    fp.write(html_text)
                    fp.close()
                    load_html_file = "./html/audit_board_home.html"
                except Exception as e:
                    pass
        self.auditTagHomeWebkit.load(QtCore.QUrl(load_html_file))