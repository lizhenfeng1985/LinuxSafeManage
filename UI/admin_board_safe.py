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
    
class AdminBoardSafe(QtGui.QWidget):
    def __init__(self,parent=None):
        super(AdminBoardSafe,self).__init__(parent)        
        #self.setupUi(self)

    def AddAdminTagSafe(self):
        self.adminTagSafeLogo = QtGui.QWidget(self.adminTagSafeBkg)
        self.adminTagSafeLogo.setGeometry(QtCore.QRect(40, 10, 70, 60))
        self.adminTagSafeLogo.setObjectName(_fromUtf8("adminTagSafeLogo"))
        self.adminTagSafeLogo.setStyleSheet(_fromUtf8("border-image: url(:/images/admin_safe_logo.png);"))

        self.adminTagSafeTitle = QtGui.QWidget(self.adminTagSafeBkg)
        self.adminTagSafeTitle.setGeometry(QtCore.QRect(120, 10, 200, 60))
        self.adminTagSafeTitle.setObjectName(_fromUtf8("adminTagSafeTitle"))
        self.adminTagSafeTitle.setStyleSheet(_fromUtf8("border-image: url(:/images/admin_safe_title.png);"))
        
        self.adminTagSafeSpace1 = QtGui.QWidget(self.adminTagSafeBkg)
        self.adminTagSafeSpace1.setGeometry(QtCore.QRect(0, 74, 10000, 1))
        self.adminTagSafeSpace1.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.adminTagSafeSpace1.setObjectName(_fromUtf8("adminTagSafeSpace1"))

        self.adminTagSafeSpace2 = QtGui.QWidget(self.adminTagSafeBkg)
        self.adminTagSafeSpace2.setGeometry(QtCore.QRect(0, 112, 10000, 1))
        self.adminTagSafeSpace2.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.adminTagSafeSpace2.setObjectName(_fromUtf8("adminTagSafeSpace2"))

        self.adminTagSafeModeTxet = QtGui.QLabel(self.adminTagSafeBkg)
        self.adminTagSafeModeTxet.setGeometry(QtCore.QRect(40, 80, 91, 30))
        self.adminTagSafeModeTxet.setObjectName(_fromUtf8("adminTagSafeModeTxet"))  
        self.adminTagSafeModeTxet.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_no_frame.png);"))
        self.adminTagSafeModeTxet.setText(_translate("adminTagSafeModeTxet", "当前模式", None))
        self.adminTagSafeModeTxet.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        # 当前模式
        self.adminTagSafeMode = QtGui.QPushButton(self.adminTagSafeBkg)
        self.adminTagSafeMode.setGeometry(QtCore.QRect(140, 80, 140, 30))
        self.adminTagSafeMode.setObjectName(_fromUtf8("adminTagSafeMode"))  
        self.adminTagSafeMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_off.png);"))
        self.adminTagSafeMode.setText(_translate("adminTagSafeMode", "", None))
        
        # 应用到服务器
        self.adminTagSafeOk = QtGui.QPushButton(self.adminTagSafeBkg)
        self.adminTagSafeOk.setGeometry(QtCore.QRect(800, 78, 140, 30))
        self.adminTagSafeOk.setObjectName(_fromUtf8("adminTagSafeOk"))  
        self.adminTagSafeOk.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagSafeOk.setText(_translate("adminTagSafeOk", "应用到服务器", None))

        self.adminTagSafeCount = 8
        self.adminTagSafeTable = QtGui.QTableWidget(self.adminTagSafeBkg)
        self.adminTagSafeTable.setGeometry(QtCore.QRect(25, 122, 950, 290))
        self.adminTagSafeTable.setObjectName(_fromUtf8("specrc_list_widget"))
        self.adminTagSafeTable.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.jpg);"))
        self.adminTagSafeTable.verticalHeader().setVisible(False)
        self.adminTagSafeTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagSafeTable.setAlternatingRowColors(True)
        #list_widget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.adminTagSafeTable.setRowCount(self.adminTagSafeCount)
        self.adminTagSafeTable.setColumnCount(4)
        self.adminTagSafeTable.setHorizontalHeaderLabels([_fromUtf8("功能"),_fromUtf8("模式"),_fromUtf8("状态"),_fromUtf8("操作")])
        self.adminTagSafeTable.setShowGrid(False)
        self.adminTagSafeTable.setColumnWidth(0,280)
        self.adminTagSafeTable.setColumnWidth(1,160)
        self.adminTagSafeTable.setColumnWidth(2,260)
        self.adminTagSafeTable.setColumnWidth(3,225)
        for i in range(0, self.adminTagSafeCount):
            self.adminTagSafeTable.setRowHeight(i,50)
        
        self.adminTagSafeFileEtcModeText, self.adminTagSafeFileEtcOnOff, self.adminTagSafeFileEtcText = self.AddAdminTagSafeTableItem(\
                            self.adminTagSafeTable, 0, '/images/admin_safe_etc.png', '禁止修改系统配置','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeFileLibModeText, self.adminTagSafeFileLibOnOff, self.adminTagSafeFileLibText = self.AddAdminTagSafeTableItem(\
                            self.adminTagSafeTable, 1, '/images/admin_safe_lib.png', '禁止修改系统库文件','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeFileBinModeText, self.adminTagSafeFileBinOnOff, self.adminTagSafeFileBinText = self.AddAdminTagSafeTableItem(\
                            self.adminTagSafeTable, 2, '/images/admin_safe_bin.png', '禁止修改系统程序文件','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeFileBootModeText, self.adminTagSafeFileBootOnOff, self.adminTagSafeFileBootText = self.AddAdminTagSafeTableItem(\
                            self.adminTagSafeTable, 3, '/images/admin_safe_boot.png', '禁止修改系统启动文件','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeNetFtpModeText, self.adminTagSafeNetFtpOnOff, self.adminTagSafeNetFtpText = self.AddAdminTagSafeTableItem(\
                            self.adminTagSafeTable, 4, '/images/admin_safe_ftp.png', '禁止FTP访问','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeNetTelnetModeText, self.adminTagSafeNetTelnetOnOff, self.adminTagSafeNetTelnetText = self.AddAdminTagSafeTableItem(\
                            self.adminTagSafeTable, 5, '/images/admin_safe_telnet.png', '禁止Telnet访问','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeNetMailModeText, self.adminTagSafeNetMailOnOff, self.adminTagSafeNetMailText = self.AddAdminTagSafeTableItem(\
                            self.adminTagSafeTable, 6, '/images/admin_safe_email.png', '禁止POP/SMTP访问','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeNetWebModeText, self.adminTagSafeNetWebOnOff, self.adminTagSafeNetWebText = self.AddAdminTagSafeTableItem(\
                            self.adminTagSafeTable, 7, '/images/admin_safe_web.png', '禁止HTTP访问','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')

        # 变量 - 安全保护
        self.adminTagSafeModeValue = 0
        self.adminTagSafeFileEtcValue = 0
        self.adminTagSafeFileLibValue = 0
        self.adminTagSafeFileBinValue = 0
        self.adminTagSafeFileBootValue = 0
        self.adminTagSafeNetFtpValue = 0
        self.adminTagSafeNetTelnetValue = 0
        self.adminTagSafeNetMailValue = 0
        self.adminTagSafeNetWebValue = 0

        # 获取Safe设置状态
        self.AdminSafeGetStatus()

        # 消息 - 标签 - 安全页
        self.connect(self.adminTagSafeMode, QtCore.SIGNAL("clicked()"), self.onAdminTagSafeModeClick)
        self.connect(self.adminTagSafeTable, QtCore.SIGNAL("cellClicked(int,int)"), self.onAdminTagSafeTableClick)
        self.connect(self.adminTagSafeOk, QtCore.SIGNAL("clicked()"), self.onAdminTagSafeSet)


    def AddAdminTagSafeTableItem(self, tableHandle, line,\
                             c1_logoImg, c1_logoText,\
                             c2_modeText,\
                             c3_onoffImg,\
                             c4_statusText):
        # c1
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 200, 50))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(40, 0, 45, 45))
        img.setAlignment(QtCore.Qt.AlignRight)
        img.setStyleSheet(_fromUtf8("image: url(:%s);" % (c1_logoImg)))
        text = QtGui.QLabel(item)
        text.setGeometry(QtCore.QRect(120, 0, 150, 50))
        text.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        text.setText(_fromUtf8("%s" % (c1_logoText)))
        tableHandle.setCellWidget(line, 0, item)
        
        # c2
        item = QtGui.QTableWidgetItem(_fromUtf8(c2_modeText))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        tableHandle.setItem(line, 1, item)
        c2_modeHandle = item
        
        # 2行 3列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 260, 50))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(55, 10, 150, 30))
        img.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        img.setStyleSheet(_fromUtf8("border-image: url(:%s);"%(c3_onoffImg)))
        tableHandle.setCellWidget(line, 2, item)
        c3_onoffHandle = img

        # 2行 4列
        item = QtGui.QTableWidgetItem(_fromUtf8(c4_statusText))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        tableHandle.setItem(line, 3, item)
        c4_statusHandle = item
 
        return [c2_modeHandle, c3_onoffHandle, c4_statusHandle]

    def onAdminTagSafeModeClick(self):
        if self.adminTagSafeModeValue == 0:
            self.adminTagSafeModeValue = 1
            self.adminTagSafeMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_on.png);"))
        else:            
            self.adminTagSafeModeValue = 0
            self.adminTagSafeMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_off.png);"))

    def onAdminTagSafeTableClick(self, line, col):        
        if line == 0 and col == 2:
            if self.adminTagSafeFileEtcValue == 0:
                self.adminTagSafeFileEtcValue = 1
                self.adminTagSafeFileEtcText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeFileEtcOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeFileEtcValue = 0
                self.adminTagSafeFileEtcText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeFileEtcOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
        elif line == 1 and col == 2:
            if self.adminTagSafeFileLibValue == 0:
                self.adminTagSafeFileLibValue = 1
                self.adminTagSafeFileLibText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeFileLibOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeFileLibValue = 0
                self.adminTagSafeFileLibText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeFileLibOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
        elif line == 2 and col == 2:
            if self.adminTagSafeFileBinValue == 0:
                self.adminTagSafeFileBinValue = 1
                self.adminTagSafeFileBinText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeFileBinOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeFileBinValue = 0
                self.adminTagSafeFileBinText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeFileBinOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))                
        elif line == 3 and col == 2:
            if self.adminTagSafeFileBootValue == 0:
                self.adminTagSafeFileBootValue = 1
                self.adminTagSafeFileBootText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeFileBootOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeFileBootValue = 0
                self.adminTagSafeFileBootText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeFileBootOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
        elif line == 4 and col == 2:
            if self.adminTagSafeNetFtpValue == 0:
                self.adminTagSafeNetFtpValue = 1
                self.adminTagSafeNetFtpText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeNetFtpOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeNetFtpValue = 0
                self.adminTagSafeNetFtpText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeNetFtpOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
        elif line == 5 and col == 2:
            if self.adminTagSafeNetTelnetValue == 0:
                self.adminTagSafeNetTelnetValue = 1
                self.adminTagSafeNetTelnetText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeNetTelnetOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeNetTelnetValue = 0
                self.adminTagSafeNetTelnetText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeNetTelnetOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
        elif line == 6 and col == 2:
            if self.adminTagSafeNetMailValue == 0:
                self.adminTagSafeNetMailValue = 1
                self.adminTagSafeNetMailText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeNetMailOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeNetMailValue = 0
                self.adminTagSafeNetMailText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeNetMailOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
        elif line == 7 and col == 2:
            if self.adminTagSafeNetWebValue == 0:
                self.adminTagSafeNetWebValue = 1
                self.adminTagSafeNetWebText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeNetWebOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeNetWebValue = 0
                self.adminTagSafeNetWebText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSafeNetWebOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))

    def onAdminTagSafeSet(self):
        url = 'https://%s:%s/safeset/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'    : self.Tokey,
            'Mode'     : self.adminTagSafeModeValue,
            'FileEtc'  : self.adminTagSafeFileEtcValue,
            'FileLib'  : self.adminTagSafeFileLibValue,
            'FileBin'  : self.adminTagSafeFileBinValue,
            'FileBoot' : self.adminTagSafeFileBootValue,
            'NetFtp'   : self.adminTagSafeNetFtpValue,
            'NetTelnet': self.adminTagSafeNetTelnetValue,
            'NetMail'  : self.adminTagSafeNetMailValue,
            'NetWeb'   : self.adminTagSafeNetWebValue,
        }
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        if rt[0] == 0:
            res = rt[1]
            #print 'safeset Request  Set:', data
            #print 'safeset Response Set:', res
            self._AdminSafeUpdateStaus(res)
        else:
            QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + rt[1])
            
        
    def AdminSafeGetStatus(self):
        url = 'https://%s:%s/safeget/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
        }        
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        
        if rt[0] == 0:
            res = rt[1]
            #print 'safeget Request  Get:', data
            #print 'safeget Response Get:', res
            self._AdminSafeUpdateStaus(res)
        else:
            QtGui.QMessageBox.about(self, u"设置", u"获取设置失败:" + rt[1])

    def _AdminSafeUpdateStaus(self, res):
        if res['Status'] == 0:
            self.adminTagSafeModeValue      = res['Mode']
            self.adminTagSafeFileEtcValue   = res['FileEtc']
            self.adminTagSafeFileLibValue   = res['FileLib']
            self.adminTagSafeFileBinValue   = res['FileBin']
            self.adminTagSafeFileBootValue  = res['FileBoot']
            self.adminTagSafeNetFtpValue    = res['NetFtp']
            self.adminTagSafeNetTelnetValue = res['NetTelnet']
            self.adminTagSafeNetMailValue   = res['NetMail']
            self.adminTagSafeNetWebValue    = res['NetWeb']
            # 更新数据
            self.adminTagSafeFileEtcText.setText(_fromUtf8("已应用到服务器"))
            self.adminTagSafeFileLibText.setText(_fromUtf8("已应用到服务器"))
            self.adminTagSafeFileBinText.setText(_fromUtf8("已应用到服务器"))
            self.adminTagSafeFileBootText.setText(_fromUtf8("已应用到服务器"))
            self.adminTagSafeNetFtpText.setText(_fromUtf8("已应用到服务器"))
            self.adminTagSafeNetTelnetText.setText(_fromUtf8("已应用到服务器"))
            self.adminTagSafeNetMailText.setText(_fromUtf8("已应用到服务器"))
            self.adminTagSafeNetWebText.setText(_fromUtf8("已应用到服务器"))

            if self.adminTagSafeModeValue == 1:
                self.adminTagSafeMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_on.png);"))
                self.adminTagSafeFileEtcModeText.setText(_fromUtf8("保护模式"))
                self.adminTagSafeFileLibModeText.setText(_fromUtf8("保护模式"))
                self.adminTagSafeFileBinModeText.setText(_fromUtf8("保护模式"))
                self.adminTagSafeFileBootModeText.setText(_fromUtf8("保护模式"))
                self.adminTagSafeNetFtpModeText.setText(_fromUtf8("保护模式"))
                self.adminTagSafeNetTelnetModeText.setText(_fromUtf8("保护模式"))
                self.adminTagSafeNetMailModeText.setText(_fromUtf8("保护模式"))
                self.adminTagSafeNetWebModeText.setText(_fromUtf8("保护模式"))
            else:
                self.adminTagSafeMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_off.png);"))
                self.adminTagSafeFileEtcModeText.setText(_fromUtf8("维护模式"))
                self.adminTagSafeFileLibModeText.setText(_fromUtf8("维护模式"))
                self.adminTagSafeFileBinModeText.setText(_fromUtf8("维护模式"))
                self.adminTagSafeFileBootModeText.setText(_fromUtf8("维护模式"))
                self.adminTagSafeNetFtpModeText.setText(_fromUtf8("维护模式"))
                self.adminTagSafeNetTelnetModeText.setText(_fromUtf8("维护模式"))
                self.adminTagSafeNetMailModeText.setText(_fromUtf8("维护模式"))
                self.adminTagSafeNetWebModeText.setText(_fromUtf8("维护模式"))
            
            if self.adminTagSafeFileEtcValue == 1:
                self.adminTagSafeFileEtcOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeFileEtcOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))

            if self.adminTagSafeFileLibValue == 1:
                self.adminTagSafeFileLibOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeFileLibOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))

            if self.adminTagSafeFileBinValue == 1:
                self.adminTagSafeFileBinOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeFileBinOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
                
            if self.adminTagSafeFileBootValue == 1:
                self.adminTagSafeFileBootOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeFileBootOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))

            if self.adminTagSafeNetFtpValue == 1:
                self.adminTagSafeNetFtpOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeNetFtpOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
                
            if self.adminTagSafeNetTelnetValue == 1:
                self.adminTagSafeNetTelnetOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeNetTelnetOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
                
            if self.adminTagSafeNetMailValue == 1:
                self.adminTagSafeNetMailOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeNetMailOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
                
            if self.adminTagSafeNetWebValue == 1:
                self.adminTagSafeNetWebOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSafeNetWebOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))          
        else:
            QtGui.QMessageBox.about(self, u"设置", u"获取设置失败:" + res['ErrMsg'])


import images_rc
