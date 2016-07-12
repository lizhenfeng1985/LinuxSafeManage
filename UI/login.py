# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui 
import sys
import config
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
    
class LoginBoard(QtGui.QWidget):
    def __init__(self,parent=None):
        self._configfile = 'config.ini'
        super(LoginBoard,self).__init__(parent)
        self.setupUi(self)

    def LoadLoginBoard(self):
        self.loginBoard = QtGui.QWidget(self.mainBoard)
        self.loginBoard.setGeometry(QtCore.QRect(0, 128, 1000, 450))
        self.loginBoard.setObjectName(_fromUtf8("loginBoard"))
        self.loginBoard.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        
        self.loginLogo = QtGui.QWidget(self.loginBoard)
        self.loginLogo.setGeometry(QtCore.QRect(80, 150, 301, 151))
        self.loginLogo.setStyleSheet(_fromUtf8("border-image: url(:/images/login_logo.png);"))
        self.loginLogo.setObjectName(_fromUtf8("loginLogo"))

        self.loginAdminIco = QtGui.QWidget(self.loginBoard)
        self.loginAdminIco.setGeometry(QtCore.QRect(665, 37, 121, 93))
        self.loginAdminIco.setStyleSheet(_fromUtf8("border-image: url(:/images/login_admin_ico.png);"))
        self.loginAdminIco.setObjectName(_fromUtf8("loginAdminIco"))

        self.loginAuditIco = QtGui.QWidget(self.loginBoard)
        self.loginAuditIco.setGeometry(QtCore.QRect(665, 37, 121, 93))
        self.loginAuditIco.setStyleSheet(_fromUtf8("border-image: url(:/images/login_audit_ico.png);"))
        self.loginAuditIco.setObjectName(_fromUtf8("loginAuditIco"))
        self.loginAuditIco.hide()
        
        self.loginChangeUser = QtGui.QPushButton(self.loginBoard)
        self.loginChangeUser.setGeometry(QtCore.QRect(610, 140, 250, 31))
        self.loginChangeUser.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.loginChangeUser.setObjectName(_fromUtf8("loginChangeUser"))
        self.loginChangeUser.setText(_translate("login_bkg", "点 击 切 换 登 录 账 户", None))

        self.loginPwdText = QtGui.QLabel(self.loginBoard)
        self.loginPwdText.setGeometry(QtCore.QRect(618, 180, 110, 16))
        self.loginPwdText.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_no_frame.png);"))
        self.loginPwdText.setObjectName(_fromUtf8("loginPwdText"))
        self.loginPwdText.setText(_translate("login_bkg", "密码", None))
        
        self.loginPwd = QtGui.QLineEdit(self.loginBoard)
        self.loginPwd.setGeometry(QtCore.QRect(610, 200, 250, 31))
        self.loginPwd.setEchoMode( QtGui.QLineEdit.Password )
        self.loginPwd.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.loginPwd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.loginPwd.setText(_fromUtf8("123456"))
        self.loginPwd.setObjectName(_fromUtf8("loginPwd"))

        self.loginLocalIPPortText = QtGui.QLabel(self.loginBoard)
        self.loginLocalIPPortText.setGeometry(QtCore.QRect(618, 240, 110, 16))
        self.loginLocalIPPortText.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_no_frame.png);"))
        self.loginLocalIPPortText.setObjectName(_fromUtf8("loginLocalIPPortText"))
        self.loginLocalIPPortText.setText(_translate("loginLocalIPPortText", "本地服务IP:端口", None))

        self.loginLocalIPPort = QtGui.QLineEdit(self.loginBoard)
        self.loginLocalIPPort.setGeometry(QtCore.QRect(610, 260, 250, 31))
        self.loginLocalIPPort.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.loginLocalIPPort.setText(_fromUtf8("127.0.0.1:9003"))
        self.loginLocalIPPort.setObjectName(_fromUtf8("loginLocalIPPort"))
        
        self.loginCenterIpportText = QtGui.QLabel(self.loginBoard)
        self.loginCenterIpportText.setGeometry(QtCore.QRect(618, 300, 110, 16))
        self.loginCenterIpportText.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_no_frame.png);"))
        self.loginCenterIpportText.setObjectName(_fromUtf8("loginCenterIpportText"))        
        self.loginCenterIpportText.setText(_translate("login_bkg", "管理中心IP:端口", None))

        self.loginCenterIpport = QtGui.QLineEdit(self.loginBoard)
        self.loginCenterIpport.setGeometry(QtCore.QRect(610, 320, 250, 31))
        self.loginCenterIpport.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.loginCenterIpport.setText(_fromUtf8("127.0.0.1:9003"))
        self.loginCenterIpport.setObjectName(_fromUtf8("loginCenterIpport"))
        
        self.loginClick = QtGui.QPushButton(self.loginBoard)
        self.loginClick.setGeometry(QtCore.QRect(610, 370, 250, 31))
        self.loginClick.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.loginClick.setObjectName(_fromUtf8("loginClick"))
        self.loginClick.setText(_translate("login_bkg", "登  录", None))
        
        self.loginSpace = QtGui.QWidget(self.loginBoard)
        self.loginSpace.setGeometry(QtCore.QRect(480, 20, 1, 410))
        self.loginSpace.setStyleSheet(_fromUtf8("border-image: url(:/images/line.jpg);"))
        self.loginSpace.setObjectName(_fromUtf8("loginSpace"))

        # 初始化变量        
        self.Tokey = ''
        self.LoginName = 'Admin'
        self.loadConfig()
        
        # 消息处理
        self.connect(self.loginChangeUser, QtCore.SIGNAL("clicked()"), self.onLoginChangeUser)
        self.connect(self.loginClick, QtCore.SIGNAL("clicked()"), self.onLoginClick)

    def loadConfig(self):
        self._Config = config.ReadConfigFile(self._configfile)
        self.loginLocalIPPort.setText(_fromUtf8("%s:%s" % (self._Config['Service']['IP'], self._Config['Service']['Port'])))
        self.loginCenterIpport.setText(_fromUtf8("%s:%s" % (self._Config['Center']['IP'], self._Config['Center']['Port'])))
        
    def onLoginChangeUser(self):
        if self.loginAdminIco.isHidden():
            self.loginAuditIco.hide()
            self.loginAdminIco.show()
            self.loginLocalIPPort.setReadOnly(False)
            self.loginCenterIpport.setReadOnly(False)  
            self.LoginName = u'Admin'
        elif self.loginAuditIco.isHidden():            
            self.loginAdminIco.hide()
            self.loginAuditIco.show()
            self.loginLocalIPPort.setReadOnly(True)
            self.loginCenterIpport.setReadOnly(True)
            self.LoginName = u'Audit'
        else:
            pass

    def onLoginClick(self):
        pwd = str(self.loginPwd.text())
        localIpPort  = str(self.loginLocalIPPort.text())
        CenterIpPort = str(self.loginCenterIpport.text())

        # 检查是否需要更新配置
        if localIpPort != '%s:%s' % (self._Config['Service']['IP'], self._Config['Service']['Port']) or \
            CenterIpPort != '%s:%s' % (self._Config['Center']['IP'], self._Config['Center']['Port']):
                col = localIpPort.split(':')
                self._Config['Service']['IP'] = col[0]
                self._Config['Service']['Port'] = col[1]
                col = CenterIpPort.split(':')
                self._Config['Center']['IP'] = col[0]
                self._Config['Center']['Port'] = col[1]
                config.UpdateConfigFile(self._configfile, self._Config)

        url = 'https://%s:%s/login/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Password'    : pwd,
            'LocalIPPort' : localIpPort,
            'CenterIPPort': CenterIpPort,
        }
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self._user = res['User']
                self.Tokey = res['Tokey']
                print 'Login OK :', self._user, self.Tokey
                # 进入Admin页面
                if self.LoginName == 'Admin':
                    self.LoadAdminBoard()
                    self.loginBoard.hide()
                    self.adminBoard.show()
                # 进入Audit页面
                elif self.LoginName == 'Audit':
                    QtGui.QMessageBox.about(self, u"登录", u'页面未添加')
            else:
                QtGui.QMessageBox.about(self, u"登录", u'%s' % (res['ErrMsg']))
        else:
            QtGui.QMessageBox.about(self, u"登录", u'%s' % (rt[1]))

import images_rc
