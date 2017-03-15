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


class AuditBoardConfigPasswd(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AuditBoardConfigPasswd, self).__init__(parent)
        # self.setupUi(self)

    def AddAuditTagConfigPasswd(self):
        # 画线 左
        self.auditTagConfigPasswdSpaceLeft = QtGui.QWidget(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.auditTagConfigPasswdSpaceLeft.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.auditTagConfigPasswdSpaceLeft.setObjectName(_fromUtf8('auditTagHighSpaceLeft'))

        # 画线 中
        self.auditTagConfigPasswdSpaceMid = QtGui.QWidget(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdSpaceMid.setGeometry(QtCore.QRect(500, 0, 1, 295))
        self.auditTagConfigPasswdSpaceMid.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.auditTagConfigPasswdSpaceMid.setObjectName(_fromUtf8('auditTagHighSpaceMid'))

        # 画线 右
        self.auditTagConfigPasswdSpaceRight = QtGui.QWidget(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.auditTagConfigPasswdSpaceRight.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.auditTagConfigPasswdSpaceRight.setObjectName(_fromUtf8('auditTagConfigPasswdSpaceRight'))

        # 画线 底
        self.auditTagConfigPasswdSpaceBottom = QtGui.QWidget(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.auditTagConfigPasswdSpaceBottom.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.auditTagConfigPasswdSpaceBottom.setObjectName(_fromUtf8('auditTagConfigPasswdSpaceBottom'))

        # 密码 - 标题
        self.auditTagConfigPasswdTitle = QtGui.QLabel(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdTitle.setGeometry(QtCore.QRect(80, 25, 340, 25))
        self.auditTagConfigPasswdTitle.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagConfigPasswdTitle.setObjectName(_fromUtf8('auditTagConfigPasswdTitle'))
        self.auditTagConfigPasswdTitle.setText(_translate('auditTagConfigPasswdTitle', '修改登录密码', None))

        # 密码 - 旧 - 文字
        self.auditTagConfigPasswdOldText = QtGui.QLabel(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdOldText.setGeometry(QtCore.QRect(80, 75, 50, 25))
        self.auditTagConfigPasswdOldText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagConfigPasswdOldText.setObjectName(_fromUtf8('auditTagConfigPasswdOldText'))
        self.auditTagConfigPasswdOldText.setText(_translate('auditTagConfigPasswdOldText', '旧密码：', None))

        # 密码 - 旧
        self.auditTagConfigPasswdOld = QtGui.QLineEdit(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdOld.setGeometry(QtCore.QRect(130, 75, 290, 25))
        self.auditTagConfigPasswdOld.setEchoMode(QtGui.QLineEdit.Password)
        self.auditTagConfigPasswdOld.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        #self.auditTagConfigPasswdOld.setInputMethodHints(QtCore.Qt.ImhNone)
        self.auditTagConfigPasswdOld.setObjectName(_fromUtf8('auditTagConfigPasswdOldText'))

        # 密码 - 新 - 文字
        self.auditTagConfigPasswdNewText = QtGui.QLabel(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdNewText.setGeometry(QtCore.QRect(80, 125, 50, 25))
        self.auditTagConfigPasswdNewText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagConfigPasswdNewText.setObjectName(_fromUtf8('auditTagConfigPasswdNewText'))
        self.auditTagConfigPasswdNewText.setText(_translate('auditTagConfigPasswdNewText', '新密码：', None))

        # 密码 - 新
        self.auditTagConfigPasswdNew = QtGui.QLineEdit(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdNew.setGeometry(QtCore.QRect(130, 125, 290, 25))
        self.auditTagConfigPasswdNew.setEchoMode(QtGui.QLineEdit.Password)
        self.auditTagConfigPasswdNew.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        #self.auditTagConfigPasswdNew.setInputMethodHints(QtCore.Qt.ImhNone)
        self.auditTagConfigPasswdNew.setObjectName(_fromUtf8('auditTagConfigPasswdNew'))

        # 密码 - 确认新 - 文字
        self.auditTagConfigPasswdConfirmNewText = QtGui.QLabel(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdConfirmNewText.setGeometry(QtCore.QRect(80, 175, 50, 25))
        self.auditTagConfigPasswdConfirmNewText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagConfigPasswdConfirmNewText.setObjectName(_fromUtf8('auditTagConfigPasswdConfirmNewText'))
        self.auditTagConfigPasswdConfirmNewText.setText(_translate('auditTagConfigPasswdConfirmNewText', '新密码：', None))

        # 密码 - 确认新
        self.auditTagConfigPasswdConfirmNew = QtGui.QLineEdit(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswdConfirmNew.setGeometry(QtCore.QRect(130, 175, 290, 25))
        self.auditTagConfigPasswdConfirmNew.setEchoMode(QtGui.QLineEdit.Password)
        self.auditTagConfigPasswdConfirmNew.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        #self.auditTagConfigPasswdConfirmNew.setInputMethodHints(QtCore.Qt.ImhNone)
        self.auditTagConfigPasswdConfirmNew.setObjectName(_fromUtf8('auditTagConfigPasswdConfirmNew'))

        # 密码 - 提交修改
        self.auditTagConfigPasswSubmit = QtGui.QPushButton(self.auditTagConfigTagPasswdBkg)
        self.auditTagConfigPasswSubmit.setGeometry(QtCore.QRect(220, 230, 70, 31))
        self.auditTagConfigPasswSubmit.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.auditTagConfigPasswSubmit.setObjectName(_fromUtf8("auditTagConfigPasswSubmit"))
        self.auditTagConfigPasswSubmit.setText(_translate("auditTagConfigPasswSubmit", "提交", None))

        # 添加用户消息
        self.connect(self.auditTagConfigPasswSubmit, QtCore.SIGNAL('clicked()'), self.onAuditTagConfigPasswSubmit)

    def onAuditTagConfigPasswSubmit(self):
        old_pwd = unicode(self.auditTagConfigPasswdOld.text())
        new_pwd = unicode(self.auditTagConfigPasswdNew.text())
        new_pwd_confirm = unicode(self.auditTagConfigPasswdConfirmNew.text())
        if len(old_pwd) < 1 or len(new_pwd) < 1:
            QtGui.QMessageBox.about(self, u"修改密码", u'错误提示:输入的密码不能为空')
            return
        if new_pwd != new_pwd_confirm:
            QtGui.QMessageBox.about(self, u"修改密码", u'错误提示:两次输入的新密码不一致')
            return
        if new_pwd == old_pwd:
            QtGui.QMessageBox.about(self, u"修改密码",  u'错误提示:新旧密码相同')
            return
        else:
            url = 'https://%s:%s/sysconfig/passwd/set/%s' % (
                self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
            data = {
                'Tokey': self.Tokey,
                'OldPwd': old_pwd,
                'NewPwd': new_pwd
            }
            # print url, data
            param = {'Data': json.dumps(data)}
            rt = HttpsPost(url, param)
            # print rt
            if rt[0] == 0:
                res = rt[1]
                if res['Status'] == 0:
                    QtGui.QMessageBox.about(self, u"修改密码", u'成功')
                else:
                    QtGui.QMessageBox.about(self, u'修改密码', u'错误提示:' + res['ErrMsg'])
            else:
                QtGui.QMessageBox.about(self, u'修改密码', u'错误提示:' + rt[1])
