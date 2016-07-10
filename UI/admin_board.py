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
    
class AdminBoard(QtGui.QWidget):
    def __init__(self,parent=None):  
        super(AdminBoard,self).__init__(parent)        
        self.setupUi(self)

    def LoadAdminBoard(self):
        # Admin主面板
        self.adminBoard = QtGui.QWidget(self.mainBoard)
        self.adminBoard.setGeometry(QtCore.QRect(0, 128, 1000, 450))
        self.adminBoard.setObjectName(_fromUtf8("adminBoard"))
        self.adminBoard.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

        # Admin Home 标签页
        self.adminTagHome = QtGui.QPushButton(self.adminBoard)
        self.adminTagHome.setGeometry(QtCore.QRect(0, 0, 91, 30))
        self.adminTagHome.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.adminTagHome.setObjectName(_fromUtf8("adminTagHome"))
        self.adminTagHome.setText(_translate("adminTagHome", "首页概览", None))

        self.adminTagHomeBkg = QtGui.QWidget(self.adminBoard)
        self.adminTagHomeBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagHomeBkg.setObjectName(_fromUtf8("adminTagHomeBkg"))
        self.adminTagHomeBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

        # Admin Safe 标签页
        self.adminTagSafe = QtGui.QPushButton(self.adminBoard)
        self.adminTagSafe.setGeometry(QtCore.QRect(92, 0, 91, 30))
        self.adminTagSafe.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.adminTagSafe.setObjectName(_fromUtf8("adminTagSafe"))
        self.adminTagSafe.setText(_translate("adminTagSafe", "安全防护", None))

        self.adminTagSafeBkg = QtGui.QWidget(self.adminBoard)
        self.adminTagSafeBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagSafeBkg.setObjectName(_fromUtf8("adminTagSafeBkg"))
        self.adminTagSafeBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
        self.AddAdminTagSafe()
        

        # Admin Special 标签页
        self.adminTagSpecial = QtGui.QPushButton(self.adminBoard)
        self.adminTagSpecial.setGeometry(QtCore.QRect(184, 0, 91, 30))
        self.adminTagSpecial.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.adminTagSpecial.setObjectName(_fromUtf8("adminTagSpecial"))
        self.adminTagSpecial.setText(_translate("adminTagSpecial", "特殊资源", None))

        self.adminTagSpecialBkg = QtGui.QWidget(self.adminBoard)
        self.adminTagSpecialBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagSpecialBkg.setObjectName(_fromUtf8("adminTagSpecialBkg"))
        self.adminTagSpecialBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

        self.AddAdminTagSpecial()

        # Admin Config 标签页
        self.adminTagConfig = QtGui.QPushButton(self.adminBoard)
        self.adminTagConfig.setGeometry(QtCore.QRect(276, 0, 91, 30))
        self.adminTagConfig.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
        self.adminTagConfig.setObjectName(_fromUtf8("adminTagConfig"))
        self.adminTagConfig.setText(_translate("adminTagConfig", "系统设置", None))

        self.adminTagConfigBkg = QtGui.QWidget(self.adminBoard)
        self.adminTagConfigBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagConfigBkg.setObjectName(_fromUtf8("adminTagConfigBkg"))
        self.adminTagConfigBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))        

        # 初始化变量
        self.adminTags = {
            self.adminTagHome    : self.adminTagHomeBkg,
            self.adminTagSafe    : self.adminTagSafeBkg,
            self.adminTagSpecial : self.adminTagSpecialBkg,
            self.adminTagConfig  : self.adminTagConfigBkg
        }

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
        
        # 变量 - 特殊资源
        self.adminTagSpecialModeValue = 0
        self.adminTagSpecialSetTimeValue = 0
        self.adminTagSpecialShutDownValue = 0
        self.adminTagSpecialUsbValue = 0
        self.adminTagSpecialCdromValue = 0

        # 默认显示首页
        self._onAdminChangeTags(self.adminTagHomeBkg)

        # 获取Safe设置状态
        self.AdminSafeGetStatus()
        
        # 获取Sepeical设置状态
        self.AdminSpecialGetStatus()
        
        # 消息处理        
        self.connect(self.adminTagHome, QtCore.SIGNAL("clicked()"), self.onAdminTagHome)
        self.connect(self.adminTagSafe, QtCore.SIGNAL("clicked()"), self.onAdminTagSafe)
        self.connect(self.adminTagSpecial, QtCore.SIGNAL("clicked()"), self.onAdminTagSpecial)
        self.connect(self.adminTagConfig, QtCore.SIGNAL("clicked()"), self.onAdminTagConfig)

        # 消息 - 标签 - 安全页
        self.connect(self.adminTagSafeMode, QtCore.SIGNAL("clicked()"), self.onAdminTagSafeModeClick)
        self.connect(self.adminTagSafeTable, QtCore.SIGNAL("cellClicked(int,int)"), self.onAdminTagSafeTableClick)
        self.connect(self.adminTagSafeOk, QtCore.SIGNAL("clicked()"), self.onAdminTagSafeSet)

        # 消息 - 标签 - 特殊资源页
        self.connect(self.adminTagSpecialMode, QtCore.SIGNAL("clicked()"), self.onAdminTagSpecialModeClick)
        self.connect(self.adminTagSpecialTable, QtCore.SIGNAL("cellClicked(int,int)"), self.onAdminTagSpecialTableClick)
        self.connect(self.adminTagSpecialOk, QtCore.SIGNAL("clicked()"), self.onAdminTagSpecialSet)

    def AddAdminTagSpecial(self):
        self.adminTagSpecialLogo = QtGui.QWidget(self.adminTagSpecialBkg)
        self.adminTagSpecialLogo.setGeometry(QtCore.QRect(40, 10, 70, 60))
        self.adminTagSpecialLogo.setObjectName(_fromUtf8("adminTagSpecialLogo"))
        self.adminTagSpecialLogo.setStyleSheet(_fromUtf8("border-image: url(:/images/admin_special_logo.png);"))

        self.adminTagSpecialTitle = QtGui.QWidget(self.adminTagSpecialBkg)
        self.adminTagSpecialTitle.setGeometry(QtCore.QRect(120, 10, 200, 60))
        self.adminTagSpecialTitle.setObjectName(_fromUtf8("adminTagSpecialTitle"))
        self.adminTagSpecialTitle.setStyleSheet(_fromUtf8("border-image: url(:/images/admin_special_title.png);"))
        
        self.adminTagSpecialSpace1 = QtGui.QWidget(self.adminTagSpecialBkg)
        self.adminTagSpecialSpace1.setGeometry(QtCore.QRect(0, 74, 10000, 1))
        self.adminTagSpecialSpace1.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.adminTagSpecialSpace1.setObjectName(_fromUtf8("adminTagSpecialSpace1"))

        self.adminTagSpecialSpace2 = QtGui.QWidget(self.adminTagSpecialBkg)
        self.adminTagSpecialSpace2.setGeometry(QtCore.QRect(0, 112, 10000, 1))
        self.adminTagSpecialSpace2.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.adminTagSpecialSpace2.setObjectName(_fromUtf8("adminTagSpecialSpace2"))

        self.adminTagSpecialModeTxet = QtGui.QLabel(self.adminTagSpecialBkg)
        self.adminTagSpecialModeTxet.setGeometry(QtCore.QRect(40, 80, 91, 30))
        self.adminTagSpecialModeTxet.setObjectName(_fromUtf8("adminTagSpecialModeTxet"))  
        self.adminTagSpecialModeTxet.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_no_frame.png);"))
        self.adminTagSpecialModeTxet.setText(_translate("adminTagSpecialModeTxet", "当前模式", None))
        self.adminTagSpecialModeTxet.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

        # 当前模式
        self.adminTagSpecialMode = QtGui.QPushButton(self.adminTagSpecialBkg)
        self.adminTagSpecialMode.setGeometry(QtCore.QRect(140, 80, 140, 30))
        self.adminTagSpecialMode.setObjectName(_fromUtf8("adminTagSpecialMode"))  
        self.adminTagSpecialMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_off.png);"))
        self.adminTagSpecialMode.setText(_translate("adminTagSpecialMode", "", None))
        
        # 应用到服务器
        self.adminTagSpecialOk = QtGui.QPushButton(self.adminTagSpecialBkg)
        self.adminTagSpecialOk.setGeometry(QtCore.QRect(800, 78, 140, 30))
        self.adminTagSpecialOk.setObjectName(_fromUtf8("adminTagSpecialOk"))  
        self.adminTagSpecialOk.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagSpecialOk.setText(_translate("Form", "应用到服务器", None))

        self.adminTagSpecialCount = 4
        self.adminTagSpecialTable = QtGui.QTableWidget(self.adminTagSpecialBkg)
        self.adminTagSpecialTable.setGeometry(QtCore.QRect(25, 122, 950, 290))
        self.adminTagSpecialTable.setObjectName(_fromUtf8("specrc_list_widget"))
        self.adminTagSpecialTable.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.jpg);"))
        self.adminTagSpecialTable.verticalHeader().setVisible(False)
        self.adminTagSpecialTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagSpecialTable.setAlternatingRowColors(True)
        #list_widget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.adminTagSpecialTable.setRowCount(self.adminTagSpecialCount)
        self.adminTagSpecialTable.setColumnCount(4)
        self.adminTagSpecialTable.setHorizontalHeaderLabels([_fromUtf8("功能"),_fromUtf8("模式"),_fromUtf8("状态"),_fromUtf8("操作")])
        self.adminTagSpecialTable.setShowGrid(False)
        self.adminTagSpecialTable.setColumnWidth(0,280)
        self.adminTagSpecialTable.setColumnWidth(1,160)
        self.adminTagSpecialTable.setColumnWidth(2,260)
        self.adminTagSpecialTable.setColumnWidth(3,225)
        for i in range(0, self.adminTagSpecialCount):
            self.adminTagSpecialTable.setRowHeight(i,50)

        self.adminTagSpecialSetTimeModeText, self.adminTagSpecialSetTimeOnOff, self.adminTagSpecialSetTimeText = self.AddAdminTagTableItem(\
                            self.adminTagSpecialTable, 0, '/images/specrc_settime.png', '禁止修改系统时间','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSpecialShutDownModeText, self.adminTagSpecialShutDownOnOff, self.adminTagSpecialShutDownText = self.AddAdminTagTableItem(\
                            self.adminTagSpecialTable, 1, '/images/specrc_shutdown.png', '禁止关机和重启','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSpecialCdromModeText, self.adminTagSpecialCdromOnOff, self.adminTagSpecialCdromText = self.AddAdminTagTableItem(\
                            self.adminTagSpecialTable, 2, '/images/device_cdrom.png', '禁用光驱','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSpecialUsbModeText, self.adminTagSpecialUsbOnOff, self.adminTagSpecialUsbText = self.AddAdminTagTableItem(\
                            self.adminTagSpecialTable, 3, '/images/device_usb.png', '禁用USB存储设备','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')


    def AddAdminTagTableItem(self, tableHandle, line,\
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


    ##### 标签页 - 安全项
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
        
        self.adminTagSafeFileEtcModeText, self.adminTagSafeFileEtcOnOff, self.adminTagSafeFileEtcText = self.AddAdminTagTableItem(\
                            self.adminTagSafeTable, 0, '/images/admin_safe_etc.png', '禁止修改系统配置','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeFileLibModeText, self.adminTagSafeFileLibOnOff, self.adminTagSafeFileLibText = self.AddAdminTagTableItem(\
                            self.adminTagSafeTable, 1, '/images/admin_safe_lib.png', '禁止修改系统库文件','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeFileBinModeText, self.adminTagSafeFileBinOnOff, self.adminTagSafeFileBinText = self.AddAdminTagTableItem(\
                            self.adminTagSafeTable, 2, '/images/admin_safe_bin.png', '禁止修改系统程序文件','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeFileBootModeText, self.adminTagSafeFileBootOnOff, self.adminTagSafeFileBootText = self.AddAdminTagTableItem(\
                            self.adminTagSafeTable, 3, '/images/admin_safe_boot.png', '禁止修改系统启动文件','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeNetFtpModeText, self.adminTagSafeNetFtpOnOff, self.adminTagSafeNetFtpText = self.AddAdminTagTableItem(\
                            self.adminTagSafeTable, 4, '/images/admin_safe_ftp.png', '禁止FTP访问','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeNetTelnetModeText, self.adminTagSafeNetTelnetOnOff, self.adminTagSafeNetTelnetText = self.AddAdminTagTableItem(\
                            self.adminTagSafeTable, 5, '/images/admin_safe_telnet.png', '禁止Telnet访问','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeNetMailModeText, self.adminTagSafeNetMailOnOff, self.adminTagSafeNetMailText = self.AddAdminTagTableItem(\
                            self.adminTagSafeTable, 6, '/images/admin_safe_email.png', '禁止POP/SMTP访问','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSafeNetWebModeText, self.adminTagSafeNetWebOnOff, self.adminTagSafeNetWebText = self.AddAdminTagTableItem(\
                            self.adminTagSafeTable, 7, '/images/admin_safe_web.png', '禁止HTTP访问','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        

    def _onAdminChangeTags(self, tagBtn):
        for btn, bkg in self.adminTags.items():
            if btn == tagBtn:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))
                bkg.show()
            else:
                btn.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_blue_lite.png);"))
                bkg.hide()

    def onAdminTagHome(self):
        self._onAdminChangeTags(self.adminTagHome)

    def onAdminTagSafe(self):
        self._onAdminChangeTags(self.adminTagSafe)

    def onAdminTagSpecial(self):
        self._onAdminChangeTags(self.adminTagSpecial)

    def onAdminTagConfig(self):
        self._onAdminChangeTags(self.adminTagConfig)

    def onAdminTagSpecialModeClick(self):
        if self.adminTagSpecialModeValue == 0:
            self.adminTagSpecialModeValue = 1
            self.adminTagSpecialMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_on.png);"))
        else:            
            self.adminTagSpecialModeValue = 0
            self.adminTagSpecialMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_off.png);"))

    def onAdminTagSpecialTableClick(self, line, col):
        if line == 0 and col == 2:
            if self.adminTagSpecialSetTimeValue == 0:
                self.adminTagSpecialSetTimeValue = 1
                self.adminTagSpecialSetTimeText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialSetTimeOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSpecialSetTimeValue = 0
                self.adminTagSpecialSetTimeText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialSetTimeOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
        elif line == 1 and col == 2:
            if self.adminTagSpecialShutDownValue == 0:
                self.adminTagSpecialShutDownValue = 1
                self.adminTagSpecialShutDownText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialShutDownOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSpecialShutDownValue = 0
                self.adminTagSpecialShutDownText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialShutDownOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
        elif line == 2 and col == 2:
            if self.adminTagSpecialCdromValue == 0:
                self.adminTagSpecialCdromValue = 1
                self.adminTagSpecialCdromText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialCdromOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSpecialCdromValue = 0
                self.adminTagSpecialCdromText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialCdromOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))                
        elif line == 3 and col == 2:
            if self.adminTagSpecialUsbValue == 0:
                self.adminTagSpecialUsbValue = 1
                self.adminTagSpecialUsbText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialUsbOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSpecialUsbValue = 0
                self.adminTagSpecialUsbText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialUsbOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))


    def onAdminTagSpecialSet(self):
        url = 'https://%s:%s/specialset/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self._loginName)
        data = {
            'Tokey'   : self._tokey,
            'Mode'    : self.adminTagSpecialModeValue,
            'SetTime' : self.adminTagSpecialSetTimeValue,
            'ShutDown': self.adminTagSpecialShutDownValue,
            'Usb'     : self.adminTagSpecialUsbValue,
            'Cdrom'   : self.adminTagSpecialCdromValue,
        }
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        if rt[0] == 0:
            res = rt[1]
            #print 'Request  Set:', data
            #print 'Response Set:', res
            self._AdminSpecialUpdateStaus(res)
        else:
            QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + rt[1])
            
        
    def AdminSpecialGetStatus(self):
        url = 'https://%s:%s/specialget/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self._loginName)
        data = {
            'Tokey'   : self._tokey,
        }        
        param = {'Data' : json.dumps(data)}        
        rt = HttpsPost(url, param)
        
        if rt[0] == 0:
            res = rt[1]
            #print 'Request  Get:', data
            #print 'Response Get:', res
            self._AdminSpecialUpdateStaus(res)
        else:
            QtGui.QMessageBox.about(self, u"设置", u"获取设置失败:" + rt[1])

    def _AdminSpecialUpdateStaus(self, res):
        if res['Status'] == 0:
            self.adminTagSpecialModeValue = res['Mode']
            self.adminTagSpecialSetTimeValue = res['SetTime']
            self.adminTagSpecialShutDownValue = res['ShutDown']
            self.adminTagSpecialUsbValue = res['Usb']
            self.adminTagSpecialCdromValue = res['Cdrom']
            # 更新数据
            self.adminTagSpecialSetTimeText.setText(_fromUtf8("已应用到服务器"))
            self.adminTagSpecialShutDownText.setText(_fromUtf8("已应用到服务器"))
            self.adminTagSpecialUsbText.setText(_fromUtf8("已应用到服务器"))
            self.adminTagSpecialCdromText.setText(_fromUtf8("已应用到服务器"))

            if self.adminTagSpecialModeValue == 1:
                self.adminTagSpecialMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_on.png);"))
                self.adminTagSpecialSetTimeModeText.setText(_fromUtf8("保护模式"))
                self.adminTagSpecialShutDownModeText.setText(_fromUtf8("保护模式"))
                self.adminTagSpecialUsbModeText.setText(_fromUtf8("保护模式"))
                self.adminTagSpecialCdromModeText.setText(_fromUtf8("保护模式"))
            else:
                self.adminTagSpecialMode.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_mode_off.png);"))                
                self.adminTagSpecialSetTimeModeText.setText(_fromUtf8("维护模式"))
                self.adminTagSpecialShutDownModeText.setText(_fromUtf8("维护模式"))
                self.adminTagSpecialUsbModeText.setText(_fromUtf8("维护模式"))
                self.adminTagSpecialCdromModeText.setText(_fromUtf8("维护模式"))
                
            if self.adminTagSpecialSetTimeValue == 1:
                self.adminTagSpecialSetTimeOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSpecialSetTimeOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))

            if self.adminTagSpecialShutDownValue == 1:
                self.adminTagSpecialShutDownOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSpecialShutDownOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))

            if self.adminTagSpecialUsbValue == 1:
                self.adminTagSpecialUsbOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSpecialUsbOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))

            if self.adminTagSpecialCdromValue == 1:
                self.adminTagSpecialCdromOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_open_1.png);"))
            else:
                self.adminTagSpecialCdromOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_close_1.png);"))
        else:
            QtGui.QMessageBox.about(self, u"设置", u"获取设置失败:" + res['ErrMsg'])


    ####### 安全页
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
        url = 'https://%s:%s/safeset/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self._loginName)
        data = {
            'Tokey'    : self._tokey,
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
        url = 'https://%s:%s/safeget/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self._loginName)
        data = {
            'Tokey'   : self._tokey,
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
