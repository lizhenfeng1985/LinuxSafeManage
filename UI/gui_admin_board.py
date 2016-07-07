# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui 
import sys

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
    
class GuiAdminBoard(QtGui.QWidget):
    def __init__(self,parent=None):  
        super(GuiAdminBoard,self).__init__(parent)        
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
        self.adminTagSafe.setText(_translate("adminTagSafe", "安全保护", None))

        self.adminTagSafeBkg = QtGui.QWidget(self.adminBoard)
        self.adminTagSafeBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagSafeBkg.setObjectName(_fromUtf8("adminTagSafeBkg"))
        self.adminTagSafeBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

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
        self.adminTags = [
            self.adminTagHomeBkg,
            self.adminTagSafeBkg,
            self.adminTagSpecialBkg,
            self.adminTagConfigBkg
        ]

        self.adminTagSpecialSetTimeValue = 0
        self.adminTagSpecialShutDownValue = 0
        self.adminTagSpecialUsbValue = 0
        self.adminTagSpecialCdromValue = 0

        # 默认显示首页
        self._onAdminChangeTags(self.adminTagHomeBkg)

        self.AdminSpecialSetStatus()

        
        # 消息处理
        self.connect(self.adminTagHome, QtCore.SIGNAL("clicked()"), self.onAdminTagHome)
        self.connect(self.adminTagSafe, QtCore.SIGNAL("clicked()"), self.onAdminTagSafe)
        self.connect(self.adminTagSpecial, QtCore.SIGNAL("clicked()"), self.onAdminTagSpecial)
        self.connect(self.adminTagConfig, QtCore.SIGNAL("clicked()"), self.onAdminTagConfig)

        self.connect(self.adminTagSpecialTable, QtCore.SIGNAL("cellClicked(int,int)"), self.onAdminTagSpecialTableClick)
        self.connect(self.adminTagSpecialOk, QtCore.SIGNAL("clicked()"), self.onAdminTagSpecialOk)

    def AddAdminTagSpecial(self):
        self.adminTagSpecialLogo = QtGui.QWidget(self.adminTagSpecialBkg)
        self.adminTagSpecialLogo.setGeometry(QtCore.QRect(40, 10, 70, 60))
        self.adminTagSpecialLogo.setObjectName(_fromUtf8("adminTagSpecialLogo"))
        self.adminTagSpecialLogo.setStyleSheet(_fromUtf8("border-image: url(:/images/sys_ico.png);"))

        self.adminTagSpecialTitle = QtGui.QWidget(self.adminTagSpecialBkg)
        self.adminTagSpecialTitle.setGeometry(QtCore.QRect(120, 10, 200, 60))
        self.adminTagSpecialTitle.setObjectName(_fromUtf8("adminTagSpecialTitle"))
        self.adminTagSpecialTitle.setStyleSheet(_fromUtf8("border-image: url(:/images/sys_title.png);"))
        '''
        self.adminTagSpecialSpace = QtGui.QWidget(self.adminTagSpecialBkg)
        self.adminTagSpecialSpace.setGeometry(QtCore.QRect(0, 85, 10000, 1))
        self.adminTagSpecialSpace.setStyleSheet(_fromUtf8("border-image: url(:/images/line.jpg);"))
        self.adminTagSpecialSpace.setObjectName(_fromUtf8("adminTagSpecialSpace"))
        '''
        # 应用到服务器
        self.adminTagSpecialOk = QtGui.QPushButton(self.adminTagSpecialBkg)
        self.adminTagSpecialOk.setGeometry(QtCore.QRect(820, 65, 140, 30))
        self.adminTagSpecialOk.setObjectName(_fromUtf8("adminTagSpecialOk"))  
        self.adminTagSpecialOk.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.adminTagSpecialOk.setText(_translate("Form", "应用到服务器", None))

        self.adminTagSpecialCount = 4
        self.adminTagSpecialTable = QtGui.QTableWidget(self.adminTagSpecialBkg)
        self.adminTagSpecialTable.setGeometry(QtCore.QRect(25, 100, 950, 290))
        self.adminTagSpecialTable.setObjectName(_fromUtf8("specrc_list_widget"))
        self.adminTagSpecialTable.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.jpg);"))
        self.adminTagSpecialTable.verticalHeader().setVisible(False)
        self.adminTagSpecialTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.adminTagSpecialTable.setAlternatingRowColors(True)
        #list_widget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.adminTagSpecialTable.setRowCount(self.adminTagSpecialCount)
        self.adminTagSpecialTable.setColumnCount(5)
        self.adminTagSpecialTable.setHorizontalHeaderLabels([_fromUtf8(""), _fromUtf8("功能"),_fromUtf8("操作"),_fromUtf8("状态"),_fromUtf8("")])
        self.adminTagSpecialTable.setShowGrid(False)
        self.adminTagSpecialTable.setColumnWidth(0,50)
        self.adminTagSpecialTable.setColumnWidth(1,290)
        self.adminTagSpecialTable.setColumnWidth(2,260)
        self.adminTagSpecialTable.setColumnWidth(3,260)
        self.adminTagSpecialTable.setColumnWidth(4,50)
        for i in range(0, self.adminTagSpecialCount):
            self.adminTagSpecialTable.setRowHeight(i,50)

        self.AddAdminTagSpecialSetTime(0)
        self.AddAdminTagSpecialShutDown(1)
        self.AddAdminTagSpecialCdrom(2)
        self.AddAdminTagSpecialUsb(3)

        
    def AddAdminTagSpecialSetTime(self, line):
        # 2行 1列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 200, 50))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(40, 0, 45, 45))
        img.setAlignment(QtCore.Qt.AlignRight)
        img.setStyleSheet(_fromUtf8("image: url(:/images/specrc_settime.png);"))
        text = QtGui.QLabel(item)
        text.setGeometry(QtCore.QRect(120, 0, 110, 50))
        text.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        text.setText(_fromUtf8("禁止修改系统时间"))
        self.adminTagSpecialTable.setCellWidget(line, 1, item)
        
        # 2行 2列
        item = QtGui.QTableWidgetItem(_fromUtf8("已应用到服务器"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.adminTagSpecialTable.setItem(line, 2, item)
        self.adminTagSpecialSetTimeText = item
        
        # 2行 3列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 260, 50))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(55, 5, 150, 30))
        img.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        img.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))
        self.adminTagSpecialTable.setCellWidget(line, 3, item)
        self.adminTagSpecialSetTimeOnOff = img
        
    def AddAdminTagSpecialShutDown(self, line):
        # 1行 1列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 200, 50))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(40, 0, 45, 45))
        img.setAlignment(QtCore.Qt.AlignRight)
        img.setStyleSheet(_fromUtf8("image: url(:/images/specrc_shutdown.png);"))
        text = QtGui.QLabel(item)
        text.setGeometry(QtCore.QRect(120, 0, 110, 50))
        text.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        text.setText(_fromUtf8("禁止关机和重启"))
        self.adminTagSpecialTable.setCellWidget(line, 1, item)

        # 1行 2列
        item = QtGui.QTableWidgetItem(_fromUtf8("已应用到服务器"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.adminTagSpecialTable.setItem(line, 2, item)
        self.adminTagSpecialShutDownText = item
            
        # 1行 3列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 160, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(55, 5, 150, 30))
        img.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        img.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))
        self.adminTagSpecialTable.setCellWidget(line, 3, item)
        self.adminTagSpecialShutDownOnOff = img

    def AddAdminTagSpecialUsb(self, line):
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 200, 50))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(40, 0, 45, 45))
        img.setAlignment(QtCore.Qt.AlignRight)
        img.setStyleSheet(_fromUtf8("image: url(:/images/device_usb.png);"))
        text = QtGui.QLabel(item)
        text.setGeometry(QtCore.QRect(120, 0, 110, 50))
        text.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        text.setText(_fromUtf8("禁用USB存储设备"))
        self.adminTagSpecialTable.setCellWidget(line, 1, item)
        
        # 2行 2列
        item = QtGui.QTableWidgetItem(_fromUtf8("已应用到服务器"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.adminTagSpecialTable.setItem(line, 2, item)
        self.adminTagSpecialUsbText = item
        
        # 2行 3列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 160, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(55, 5, 150, 30))
        img.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        img.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))
        self.adminTagSpecialTable.setCellWidget(line, 3, item)
        self.adminTagSpecialUsbOnOff = img
        
    def AddAdminTagSpecialCdrom(self, line):
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 200, 50))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(40, 0, 45, 45))
        img.setAlignment(QtCore.Qt.AlignRight)
        img.setStyleSheet(_fromUtf8("image: url(:/images/device_cdrom.png);"))
        text = QtGui.QLabel(item)
        text.setGeometry(QtCore.QRect(120, 0, 110, 50))
        text.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        text.setText(_fromUtf8("禁用光驱"))
        self.adminTagSpecialTable.setCellWidget(line, 1, item)

        # 1行 2列
        item = QtGui.QTableWidgetItem(_fromUtf8("已应用到服务器"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.adminTagSpecialTable.setItem(line, 2, item)
        self.adminTagSpecialCdromText = item
            
        # 1行 3列
        item = QtGui.QWidget()
        item.setGeometry(QtCore.QRect(0, 0, 160, 40))
        img = QtGui.QLabel(item)
        img.setGeometry(QtCore.QRect(55, 5, 150, 30))
        img.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        img.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))
        self.adminTagSpecialTable.setCellWidget(line, 3, item)
        self.adminTagSpecialCdromOnOff = img
            
    def _onAdminChangeTags(self, tagBkg):
        for bkg in self.adminTags:
            if bkg == tagBkg:
                bkg.show()
            else:
                bkg.hide()

    def onAdminTagHome(self):
        self._onAdminChangeTags(self.adminTagHomeBkg)

    def onAdminTagSafe(self):
        self._onAdminChangeTags(self.adminTagSafeBkg)

    def onAdminTagSpecial(self):
        self._onAdminChangeTags(self.adminTagSpecialBkg)

    def onAdminTagConfig(self):
        self._onAdminChangeTags(self.adminTagConfigBkg)

    def onAdminTagSpecialTableClick(self, line, col):
        if line == 0 and col == 3:
            if self.adminTagSpecialSetTimeValue == 0:
                self.adminTagSpecialSetTimeValue = 1
                self.adminTagSpecialSetTimeText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialSetTimeOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_on_2.png);"))
            else:
                self.adminTagSpecialSetTimeValue = 0
                self.adminTagSpecialSetTimeText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialSetTimeOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))
        elif line == 1 and col == 3:
            if self.adminTagSpecialShutDownValue == 0:
                self.adminTagSpecialShutDownValue = 1
                self.adminTagSpecialShutDownText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialShutDownOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_on_2.png);"))
            else:
                self.adminTagSpecialShutDownValue = 0
                self.adminTagSpecialShutDownText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialShutDownOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))
        elif line == 2 and col == 3:
            if self.adminTagSpecialCdromValue == 0:
                self.adminTagSpecialCdromValue = 1
                self.adminTagSpecialCdromText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialCdromOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_on_2.png);"))
            else:
                self.adminTagSpecialCdromValue = 0
                self.adminTagSpecialCdromText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialCdromOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))                
        elif line == 3 and col == 3:
            if self.adminTagSpecialUsbValue == 0:
                self.adminTagSpecialUsbValue = 1
                self.adminTagSpecialUsbText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialUsbOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_on_2.png);"))
            else:
                self.adminTagSpecialUsbValue = 0
                self.adminTagSpecialUsbText.setText(_fromUtf8("等待应用到服务器"))
                self.adminTagSpecialUsbOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))


    def onAdminTagSpecialOk(self):
        rt = [0, {'Status':0, 'ErrMsg':'OK'}]
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                # 更新数据
                self.adminTagSpecialSetTimeText.setText(_fromUtf8("已应用到服务器"))
                self.adminTagSpecialShutDownText.setText(_fromUtf8("已应用到服务器"))
                self.adminTagSpecialUsbText.setText(_fromUtf8("已应用到服务器"))
                self.adminTagSpecialCdromText.setText(_fromUtf8("已应用到服务器"))
            else:
                QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + rt[1])

    def AdminSpecialSetStatus(self):
        rt = [
            0,
            {
                'Status'  :0,
                'ErrMsg'  :'OK',
                'SetTime' : 0,
                'ShutDown' : 1,
                'Usb' : 0,
                'Cdrom' : 1,
            }
        ]
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.adminTagSpecialSetTimeValue = res['SetTime']
                self.adminTagSpecialShutDownValue = res['ShutDown']
                self.adminTagSpecialUsbValue = res['Usb']
                self.adminTagSpecialCdromValue = res['Cdrom']
                # 更新数据
                if self.adminTagSpecialSetTimeValue == 1:
                    self.adminTagSpecialSetTimeOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_on_2.png);"))
                else:
                    self.adminTagSpecialSetTimeOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))

                if self.adminTagSpecialShutDownValue == 1:
                    self.adminTagSpecialShutDownOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_on_2.png);"))
                else:
                    self.adminTagSpecialShutDownOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))

                if self.adminTagSpecialUsbValue == 1:
                    self.adminTagSpecialUsbOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_on_2.png);"))
                else:
                    self.adminTagSpecialUsbOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))

                if self.adminTagSpecialCdromValue == 1:
                    self.adminTagSpecialCdromOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_on_2.png);"))
                else:
                    self.adminTagSpecialCdromOnOff.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_off_2.png);"))
            else:
                QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u"设置", u"设置失败:" + rt[1])
            
import images_rc
