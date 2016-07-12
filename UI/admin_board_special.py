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
    
class AdminBoardSpecial(QtGui.QWidget):
    def __init__(self,parent=None):
        super(AdminBoardSpecial,self).__init__(parent)        
        #self.setupUi(self)

    def AddAdminTagSpecial(self):
        self.adminTagSpecialBkg.setGeometry(QtCore.QRect(0, 30, 1000, 420))
        self.adminTagSpecialBkg.setObjectName(_fromUtf8("adminTagSpecialBkg"))
        self.adminTagSpecialBkg.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_white.png);"))

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

        self.adminTagSpecialSetTimeModeText, self.adminTagSpecialSetTimeOnOff, self.adminTagSpecialSetTimeText = self.AddAdminTagSpecialTableItem(\
                            self.adminTagSpecialTable, 0, '/images/specrc_settime.png', '禁止修改系统时间','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSpecialShutDownModeText, self.adminTagSpecialShutDownOnOff, self.adminTagSpecialShutDownText = self.AddAdminTagSpecialTableItem(\
                            self.adminTagSpecialTable, 1, '/images/specrc_shutdown.png', '禁止关机和重启','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSpecialCdromModeText, self.adminTagSpecialCdromOnOff, self.adminTagSpecialCdromText = self.AddAdminTagSpecialTableItem(\
                            self.adminTagSpecialTable, 2, '/images/device_cdrom.png', '禁用光驱','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        self.adminTagSpecialUsbModeText, self.adminTagSpecialUsbOnOff, self.adminTagSpecialUsbText = self.AddAdminTagSpecialTableItem(\
                            self.adminTagSpecialTable, 3, '/images/device_usb.png', '禁用USB存储设备','维护模式',\
                             '/images/btn_close_1.png','已应用到服务器')
        

        # 变量 - 特殊资源
        self.adminTagSpecialModeValue = 0
        self.adminTagSpecialSetTimeValue = 0
        self.adminTagSpecialShutDownValue = 0
        self.adminTagSpecialUsbValue = 0
        self.adminTagSpecialCdromValue = 0
        
        # 获取Sepeical设置状态
        self.AdminSpecialGetStatus()

        self.connect(self.adminTagSpecialMode, QtCore.SIGNAL("clicked()"), self.onAdminTagSpecialModeClick)
        self.connect(self.adminTagSpecialTable, QtCore.SIGNAL("cellClicked(int,int)"), self.onAdminTagSpecialTableClick)
        self.connect(self.adminTagSpecialOk, QtCore.SIGNAL("clicked()"), self.onAdminTagSpecialSet)


    def AddAdminTagSpecialTableItem(self, tableHandle, line,\
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
        url = 'https://%s:%s/specialset/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
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
        url = 'https://%s:%s/specialget/%s' % (self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey'   : self.Tokey,
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


import images_rc
