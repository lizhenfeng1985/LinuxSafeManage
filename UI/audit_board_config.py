# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import images_rc

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


class AuditBoardConfig(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AuditBoardConfig, self).__init__(parent)
        # self.setupUi(self)

    def AddAuditTagConfig(self):
        # Logo
        self.auditTagConfigLogo = QtGui.QWidget(self.auditTagConfigBkg)
        self.auditTagConfigLogo.setGeometry(QtCore.QRect(40, 10, 70, 60))
        self.auditTagConfigLogo.setObjectName(_fromUtf8("auditTagConfigLogo"))
        self.auditTagConfigLogo.setStyleSheet(_fromUtf8("border-image: url(:/images/audit_config_logo.png);"))

        # 标题
        self.auditTagConfigTitle = QtGui.QWidget(self.auditTagConfigBkg)
        self.auditTagConfigTitle.setGeometry(QtCore.QRect(120, 10, 200, 60))
        self.auditTagConfigTitle.setObjectName(_fromUtf8("auditTagConfigTitle"))
        self.auditTagConfigTitle.setStyleSheet(_fromUtf8("border-image: url(:/images/audit_config_title.png);"))

        # 画线
        self.auditTagConfigSpace1 = QtGui.QWidget(self.auditTagConfigBkg)
        self.auditTagConfigSpace1.setGeometry(QtCore.QRect(0, 74, 10000, 1))
        self.auditTagConfigSpace1.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.auditTagConfigSpace1.setObjectName(_fromUtf8("auditTagConfigSpace1"))

        # 画线 上
        self.auditTagConfigSpaceTop = QtGui.QWidget(self.auditTagConfigBkg)
        self.auditTagConfigSpaceTop.setGeometry(QtCore.QRect(0, 112, 10000, 1))
        self.auditTagConfigSpaceTop.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.auditTagConfigSpaceTop.setObjectName(_fromUtf8("auditTagConfigSpaceTop"))

        # 修改密码 标签页
        self.auditTagConfigTagPasswd = QtGui.QPushButton(self.auditTagConfigBkg)
        self.auditTagConfigTagPasswd.setGeometry(QtCore.QRect(40, 90, 90, 20))
        self.auditTagConfigTagPasswd.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
        self.auditTagConfigTagPasswd.setObjectName(_fromUtf8("auditTagConfigTagPasswd"))
        self.auditTagConfigTagPasswd.setText(_translate("auditTagConfigTagPasswd", "修改密码", None))

        self.auditTagConfigTagPasswdBkg = QtGui.QWidget(self.auditTagConfigBkg)
        self.auditTagConfigTagPasswdBkg.setGeometry(QtCore.QRect(0, 113, 1000, 307))
        self.auditTagConfigTagPasswdBkg.setObjectName(_fromUtf8("auditTagConfigTagPasswdBkg"))
        self.auditTagConfigTagPasswdBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAuditTagConfigPasswd()

        # 初始化变量
        self.auditTagsConfigTags = {
            self.auditTagConfigTagPasswd: self.auditTagConfigTagPasswdBkg,
        }

        # 默认显示首页
        self._onAuditConfigChangeTags(self.auditTagConfigTagPasswd)

        # 消息处理
        self.connect(self.auditTagConfigTagPasswd, QtCore.SIGNAL("clicked()"), self.onAuditTagConfigTagPasswd)

    def _onAuditConfigChangeTags(self, tagBtn):
        for btn, bkg in self.auditTagsConfigTags.items():
            if btn == tagBtn:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey_sel.png);"))
                bkg.show()
            else:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_sub_grey.png);"))
                bkg.hide()

    def onAuditTagConfigTagPasswd(self):
        if self.AuditBoardCheckPopUp():
            return
        self._onAuditConfigChangeTags(self.auditTagConfigTagPasswd)
