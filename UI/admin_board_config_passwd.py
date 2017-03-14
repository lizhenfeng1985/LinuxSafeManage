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


class AdminBoardConfigPasswd(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AdminBoardConfigPasswd, self).__init__(parent)
        # self.setupUi(self)

    def AddAdminTagConfigPasswdSerial(self):
        # 画线 左
        self.adminTagConfigPasswdSpaceLeft = QtGui.QWidget(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdSpaceLeft.setGeometry(QtCore.QRect(20, 0, 1, 295))
        self.adminTagConfigPasswdSpaceLeft.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigPasswdSpaceLeft.setObjectName(_fromUtf8('adminTagHighSpaceLeft'))

        # 画线 中
        self.adminTagConfigPasswdSpaceMid = QtGui.QWidget(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdSpaceMid.setGeometry(QtCore.QRect(500, 0, 1, 295))
        self.adminTagConfigPasswdSpaceMid.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigPasswdSpaceMid.setObjectName(_fromUtf8('adminTagHighSpaceMid'))

        # 画线 右
        self.adminTagConfigPasswdSpaceRight = QtGui.QWidget(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdSpaceRight.setGeometry(QtCore.QRect(980, 0, 1, 295))
        self.adminTagConfigPasswdSpaceRight.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigPasswdSpaceRight.setObjectName(_fromUtf8('adminTagConfigPasswdSpaceRight'))

        # 画线 底
        self.adminTagConfigPasswdSpaceBottom = QtGui.QWidget(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdSpaceBottom.setGeometry(QtCore.QRect(20, 295, 960, 1))
        self.adminTagConfigPasswdSpaceBottom.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey.png);'))
        self.adminTagConfigPasswdSpaceBottom.setObjectName(_fromUtf8('adminTagConfigPasswdSpaceBottom'))

        # 密码 - 标题
        self.adminTagConfigPasswdTitle = QtGui.QLabel(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdTitle.setGeometry(QtCore.QRect(80, 25, 340, 25))
        self.adminTagConfigPasswdTitle.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.adminTagConfigPasswdTitle.setObjectName(_fromUtf8('adminTagConfigPasswdTitle'))
        self.adminTagConfigPasswdTitle.setText(_translate('adminTagConfigPasswdTitle', '修改登录密码', None))

        # 密码 - 旧 - 文字
        self.adminTagConfigPasswdOldText = QtGui.QLabel(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdOldText.setGeometry(QtCore.QRect(80, 75, 50, 25))
        self.adminTagConfigPasswdOldText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.adminTagConfigPasswdOldText.setObjectName(_fromUtf8('adminTagConfigPasswdOldText'))
        self.adminTagConfigPasswdOldText.setText(_translate('adminTagConfigPasswdOldText', '旧密码：', None))

        # 密码 - 旧
        self.adminTagConfigPasswdOld = QtGui.QLineEdit(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdOld.setGeometry(QtCore.QRect(130, 75, 290, 25))
        self.adminTagConfigPasswdOld.setEchoMode(QtGui.QLineEdit.Password)
        self.adminTagConfigPasswdOld.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagConfigPasswdOld.setInputMethodHints(QtCore.Qt.ImhNone)
        self.adminTagConfigPasswdOld.setObjectName(_fromUtf8('adminTagConfigPasswdOldText'))

        # 密码 - 新 - 文字
        self.adminTagConfigPasswdNewText = QtGui.QLabel(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdNewText.setGeometry(QtCore.QRect(80, 125, 50, 25))
        self.adminTagConfigPasswdNewText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.adminTagConfigPasswdNewText.setObjectName(_fromUtf8('adminTagConfigPasswdNewText'))
        self.adminTagConfigPasswdNewText.setText(_translate('adminTagConfigPasswdNewText', '新密码：', None))

        # 密码 - 新
        self.adminTagConfigPasswdNew = QtGui.QLineEdit(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdNew.setGeometry(QtCore.QRect(130, 125, 290, 25))
        self.adminTagConfigPasswdNew.setEchoMode(QtGui.QLineEdit.Password)
        self.adminTagConfigPasswdNew.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagConfigPasswdNew.setInputMethodHints(QtCore.Qt.ImhNone)
        self.adminTagConfigPasswdNew.setObjectName(_fromUtf8('adminTagConfigPasswdNew'))

        # 密码 - 确认新 - 文字
        self.adminTagConfigPasswdConfirmNewText = QtGui.QLabel(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdConfirmNewText.setGeometry(QtCore.QRect(80, 175, 50, 25))
        self.adminTagConfigPasswdConfirmNewText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.adminTagConfigPasswdConfirmNewText.setObjectName(_fromUtf8('adminTagConfigPasswdConfirmNewText'))
        self.adminTagConfigPasswdConfirmNewText.setText(_translate('adminTagConfigPasswdConfirmNewText', '新密码：', None))

        # 密码 - 确认新
        self.adminTagConfigPasswdConfirmNew = QtGui.QLineEdit(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswdConfirmNew.setGeometry(QtCore.QRect(130, 175, 290, 25))
        self.adminTagConfigPasswdConfirmNew.setEchoMode(QtGui.QLineEdit.Password)
        self.adminTagConfigPasswdConfirmNew.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagConfigPasswdConfirmNew.setInputMethodHints(QtCore.Qt.ImhNone)
        self.adminTagConfigPasswdConfirmNew.setObjectName(_fromUtf8('adminTagConfigPasswdConfirmNew'))

        # 密码 - 提交修改
        self.adminTagConfigPasswSubmit = QtGui.QPushButton(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigPasswSubmit.setGeometry(QtCore.QRect(220, 230, 70, 31))
        self.adminTagConfigPasswSubmit.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagConfigPasswSubmit.setObjectName(_fromUtf8("adminTagConfigPasswSubmit"))
        self.adminTagConfigPasswSubmit.setText(_translate("adminTagConfigPasswSubmit", "提交", None))

        ######
        # 授权 - 标题
        self.adminTagConfigSerialTitle = QtGui.QLabel(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigSerialTitle.setGeometry(QtCore.QRect(580, 25, 340, 25))
        self.adminTagConfigSerialTitle.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.adminTagConfigSerialTitle.setObjectName(_fromUtf8('adminTagConfigSerialTitle'))
        self.adminTagConfigSerialTitle.setText(_translate('adminTagConfigSerialTitle', '软件授权', None))

        # 授权 - 状态 - 文字
        self.adminTagConfigSerialStatusText = QtGui.QLabel(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigSerialStatusText.setGeometry(QtCore.QRect(580, 75, 70, 25))
        self.adminTagConfigSerialStatusText.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        self.adminTagConfigSerialStatusText.setObjectName(_fromUtf8('adminTagConfigSerialStatusText'))
        self.adminTagConfigSerialStatusText.setText(_translate('adminTagConfigSerialStatusText', '授权状态：', None))

        # 授权 - 状态
        self.adminTagConfigSerialStatus = QtGui.QLineEdit(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigSerialStatus.setGeometry(QtCore.QRect(650, 75, 270, 25))
        self.adminTagConfigSerialStatus.setReadOnly(True)
        self.adminTagConfigSerialStatus.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagConfigSerialStatus.setObjectName(_fromUtf8('adminTagConfigSerialStatus'))
        self.adminTagConfigSerialStatus.setText(_translate('adminTagConfigSerialStatus', '未注册  有效期：1900-01-01', None))

        # 授权 - 机器码 - 文字
        self.adminTagConfigSerialCodeText = QtGui.QLabel(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigSerialCodeText.setGeometry(QtCore.QRect(580, 125, 70, 25))
        self.adminTagConfigSerialCodeText.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        self.adminTagConfigSerialCodeText.setObjectName(_fromUtf8('adminTagConfigSerialCodeText'))
        self.adminTagConfigSerialCodeText.setText(_translate('adminTagConfigSerialCodeText', '机器码：', None))

        # 授权 - 机器码
        self.adminTagConfigSerialCode = QtGui.QLineEdit(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigSerialCode.setGeometry(QtCore.QRect(650, 125, 270, 25))
        self.adminTagConfigSerialCode.setReadOnly(True)
        self.adminTagConfigSerialCode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagConfigSerialCode.setObjectName(_fromUtf8('adminTagConfigSerialCode'))
        self.adminTagConfigSerialCode.setText(_translate('adminTagConfigSerialCode', 'XXXXXXXX-XXXXXXXX-XXXXXXXX', None))

        # 授权 - 注册码 - 文字
        self.adminTagConfigSerialSNText = QtGui.QLabel(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigSerialSNText.setGeometry(QtCore.QRect(580, 175, 70, 25))
        self.adminTagConfigSerialSNText.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)
        self.adminTagConfigSerialSNText.setObjectName(_fromUtf8('adminTagConfigSerialSNText'))
        self.adminTagConfigSerialSNText.setText(_translate('adminTagConfigSerialSNText', '注册码：', None))

        # 授权 - 注册码
        self.adminTagConfigSerialSN = QtGui.QTextEdit(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigSerialSN.setGeometry(QtCore.QRect(650, 175, 270, 40))
        self.adminTagConfigSerialSN.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagConfigSerialSN.setObjectName(_fromUtf8('adminTagConfigSerialCode'))
        self.adminTagConfigSerialSN.setText(_translate('adminTagConfigSerialCode', '', None))

        # 注册 - 提交修改
        self.adminTagConfigSerialSubmit = QtGui.QPushButton(self.adminTagConfigTagPasswdSerialBkg)
        self.adminTagConfigSerialSubmit.setGeometry(QtCore.QRect(720, 230, 70, 31))
        self.adminTagConfigSerialSubmit.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagConfigSerialSubmit.setObjectName(_fromUtf8("adminTagConfigSerialSubmit"))
        self.adminTagConfigSerialSubmit.setText(_translate("adminTagConfigSerialSubmit", "注册", None))

        # 添加用户消息
        self.connect(self.adminTagConfigPasswSubmit, QtCore.SIGNAL('clicked()'), self.onAdminTagConfigPasswSubmit)
        self.connect(self.adminTagConfigSerialSubmit, QtCore.SIGNAL('clicked()'), self.onAdminTagConfigSerialSubmit)

        # 获取授权状态
        self.onAdminTagConfigSerialGet()

    def onAdminTagConfigPasswSubmit(self):
        old_pwd = unicode(self.adminTagConfigPasswdOld.text())
        new_pwd = unicode(self.adminTagConfigPasswdNew.text())
        new_pwd_confirm = unicode(self.adminTagConfigPasswdConfirmNew.text())
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

    def onAdminTagConfigSerialSubmit(self):
        code = unicode(self.adminTagConfigSerialCode.text())
        sn = unicode(self.adminTagConfigSerialSN.toPlainText())
        if len(sn) < 1:
            QtGui.QMessageBox.about(self, u"注册", u'错误提示:注册码不能为空')
            return
        # 注册授权
        url = 'https://%s:%s/sysconfig/serial/set/%s' % (
        self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey,
            'Lic': sn
        }
        # print url, data
        param = {'Data': json.dumps(data)}
        rt = HttpsPost(url, param)
        # print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.onAdminTagConfigSerialGet()
                QtGui.QMessageBox.about(self, u"注册授权", u'成功')
            else:
                QtGui.QMessageBox.about(self, u'注册授权', u'错误提示:' + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'注册授权', u'错误提示:' + rt[1])

    def onAdminTagConfigSerialGet(self):
        # 获取授权
        url = 'https://%s:%s/sysconfig/serial/get/%s' % (
            self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey
        }
        # print url, data
        param = {'Data': json.dumps(data)}
        rt = HttpsPost(url, param)
        # print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] != 0:
                QtGui.QMessageBox.about(self, u'获取授权', u'获取授权失败:' + res['ErrMsg'])
            self.adminTagConfigSerialCode.setText(
                _translate('adminTagConfigSerialCode', res['Code'], None))
            self.adminTagConfigSerialSN.setText(_translate('adminTagConfigSerialCode', res['Lic'], None))
            if res['IsReg'] == 1:
                self.adminTagConfigSerialStatus.setText(u'有效期 ' + res['Validate'])
            else:
                self.adminTagConfigSerialStatus.setText(
                    _translate('adminTagConfigSerialStatus', '未注册', None))
        else:
            QtGui.QMessageBox.about(self, u'获取授权', u'错误提示:' + rt[1])


