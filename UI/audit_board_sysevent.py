# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import json
from http import *
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


class AuditBoardSysEvent(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AuditBoardSysEvent, self).__init__(parent)
        # self.setupUi(self)

    def AddAuditTagSysEvent(self):
        self.auditTagSysEventPageLength = 10
        self.auditTagSysEventPage = 0
        selfauditTagSysEventTotal = 0
        
        # Logo
        self.auditTagSysEventLogo = QtGui.QWidget(self.auditTagSysEventBkg)
        self.auditTagSysEventLogo.setGeometry(QtCore.QRect(40, 10, 70, 60))
        self.auditTagSysEventLogo.setObjectName(_fromUtf8("auditTagSysEventLogo"))
        self.auditTagSysEventLogo.setStyleSheet(_fromUtf8("border-image: url(:/images/audit_config_logo.png);"))

        # 标题
        self.auditTagSysEventTitle = QtGui.QWidget(self.auditTagSysEventBkg)
        self.auditTagSysEventTitle.setGeometry(QtCore.QRect(120, 10, 200, 60))
        self.auditTagSysEventTitle.setObjectName(_fromUtf8("auditTagSysEventTitle"))
        self.auditTagSysEventTitle.setStyleSheet(_fromUtf8("border-image: url(:/images/audit_config_title.png);"))

        # 画线
        self.auditTagSysEventSpace1 = QtGui.QWidget(self.auditTagSysEventBkg)
        self.auditTagSysEventSpace1.setGeometry(QtCore.QRect(0, 74, 10000, 1))
        self.auditTagSysEventSpace1.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.auditTagSysEventSpace1.setObjectName(_fromUtf8("auditTagSysEventSpace1"))

        # 画线 上
        self.auditTagSysEventSpaceTop = QtGui.QWidget(self.auditTagSysEventBkg)
        self.auditTagSysEventSpaceTop.setGeometry(QtCore.QRect(0, 112, 10000, 1))
        self.auditTagSysEventSpaceTop.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.auditTagSysEventSpaceTop.setObjectName(_fromUtf8("auditTagSysEventSpaceTop"))

        # 开始时间 - 文字
        self.auditTagSysEventStartText = QtGui.QLabel(self.auditTagSysEventBkg)
        self.auditTagSysEventStartText.setGeometry(QtCore.QRect(20, 80, 35, 25))
        self.auditTagSysEventStartText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSysEventStartText.setObjectName(_fromUtf8("auditTagSysEventStartText"))
        self.auditTagSysEventStartText.setText(_translate("auditTagSysEventStartText", "开始：", None))

        # 开始时间 - 日历
        self.auditTagSysEventStart = QtGui.QDateTimeEdit(self.auditTagSysEventBkg)
        self.auditTagSysEventStart.setGeometry(QtCore.QRect(65, 80, 170, 25))
        self.auditTagSysEventStart.setCalendarPopup(True)
        self.auditTagSysEventStart.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        # self.auditTagSysEventStart.setFrame(True)
        self.auditTagSysEventStart.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.auditTagSysEventStart.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.auditTagSysEventStart.setObjectName(_fromUtf8("auditTagSysEventStart"))
        self.auditTagSysEventStart.setDateTime(QtCore.QDateTime.currentDateTime())

        # 结束时间 - 文字
        self.auditTagSysEventStopText = QtGui.QLabel(self.auditTagSysEventBkg)
        self.auditTagSysEventStopText.setGeometry(QtCore.QRect(245, 80, 35, 25))
        self.auditTagSysEventStopText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSysEventStopText.setObjectName(_fromUtf8("auditTagSysEventStopText"))
        self.auditTagSysEventStopText.setText(_translate("auditTagSysEventStopText", "结束：", None))

        # 结束时间 - 日历
        self.auditTagSysEventStop = QtGui.QDateTimeEdit(self.auditTagSysEventBkg)
        self.auditTagSysEventStop.setGeometry(QtCore.QRect(285, 80, 170, 25))
        self.auditTagSysEventStop.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSysEventStop.setCalendarPopup(True)
        # self.auditTagSysEventStart.setFrame(True)
        self.auditTagSysEventStop.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.auditTagSysEventStop.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.auditTagSysEventStop.setObjectName(_fromUtf8("auditTagSysEventStop"))
        self.auditTagSysEventStop.setDateTime(QtCore.QDateTime.currentDateTime())

        # 上一页
        self.auditTagSysEventPrev = QtGui.QPushButton(self.auditTagSysEventBkg)
        self.auditTagSysEventPrev.setGeometry(QtCore.QRect(465, 80, 70, 25))
        self.auditTagSysEventPrev.setObjectName(_fromUtf8('auditTagSysEventPrev'))
        self.auditTagSysEventPrev.setText(_translate('auditTagSysEventPrev', '<<  上一页', None))

        # 当前页
        self.auditTagSysEventPageText = QtGui.QLabel(self.auditTagSysEventBkg)
        self.auditTagSysEventPageText.setGeometry(QtCore.QRect(545, 80, 50, 25))
        self.auditTagSysEventPageText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSysEventPageText.setObjectName(_fromUtf8('auditTagSysEventPageText'))
        self.auditTagSysEventPageText.setText(_translate('auditTagSysEventPageText', '0/0', None))

        # 下一页
        self.auditTagSysEventNext = QtGui.QPushButton(self.auditTagSysEventBkg)
        self.auditTagSysEventNext.setGeometry(QtCore.QRect(605, 80, 70, 25))
        self.auditTagSysEventNext.setObjectName(_fromUtf8('auditTagSysEventNext'))
        self.auditTagSysEventNext.setText(_translate('auditTagSysEventNext', '下一页  >>', None))

        # 查询 - 输入框
        self.auditTagSysEventQuery = QtGui.QLineEdit(self.auditTagSysEventBkg)
        self.auditTagSysEventQuery.setGeometry(QtCore.QRect(705, 80, 190, 25))
        self.auditTagSysEventQuery.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.auditTagSysEventQuery.setObjectName(_fromUtf8("auditTagSysEventQuery"))
        self.auditTagSysEventQuery.setText(_translate("auditTagSysEventStopText", "", None))

        # 查询
        self.auditTagSysEventQuerySubmit = QtGui.QPushButton(self.auditTagSysEventBkg)
        self.auditTagSysEventQuerySubmit.setGeometry(QtCore.QRect(910, 80, 60, 25))
        self.auditTagSysEventQuerySubmit.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.auditTagSysEventQuerySubmit.setObjectName(_fromUtf8("auditTagSysEventQuerySubmit"))
        self.auditTagSysEventQuerySubmit.setText(_translate("auditTagSysEventQuerySubmit", "查询", None))

        # 日志表格
        self.auditTagSysEventTable = QtGui.QTableWidget(self.auditTagSysEventBkg)
        self.auditTagSysEventTable.setGeometry(QtCore.QRect(20, 120, 950, 290))
        self.auditTagSysEventTable.setObjectName(_fromUtf8('auditTagSysEventTable'))
        self.auditTagSysEventTable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.jpg);'))
        self.auditTagSysEventTable.verticalHeader().setVisible(False)
        self.auditTagSysEventTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.auditTagSysEventTable.setAlternatingRowColors(True)
        # list_widget.adminTagConfigProcWhiteTable(QtGui.QAbstractItemView.SelectRows)
        self.auditTagSysEventTable.setRowCount(self.auditTagSysEventPageLength)
        self.auditTagSysEventTable.setColumnCount(5)
        self.auditTagSysEventTable.setHorizontalHeaderLabels(
            [_fromUtf8('帐号'), _fromUtf8('行为'), _fromUtf8('结果'), _fromUtf8('时间'), _fromUtf8('操作内容')])
        self.auditTagSysEventTable.setShowGrid(False)
        self.auditTagSysEventTable.setColumnWidth(0, 100)
        self.auditTagSysEventTable.setColumnWidth(1, 130)
        self.auditTagSysEventTable.setColumnWidth(2, 80)
        self.auditTagSysEventTable.setColumnWidth(3, 135)
        self.auditTagSysEventTable.setColumnWidth(4, 480)
        for i in range(0, self.auditTagSysEventPageLength):
            self.auditTagSysEventTable.setRowHeight(i, 23)
            
        # 添加消息
        self.connect(self.auditTagSysEventPrev, QtCore.SIGNAL('clicked()'), self.onAuditTagSysEventPrev)
        self.connect(self.auditTagSysEventNext, QtCore.SIGNAL('clicked()'), self.onAuditTagSysEventNext)
        self.connect(self.auditTagSysEventQuerySubmit, QtCore.SIGNAL('clicked()'), self.onAuditTagSysEventQuerySubmit)

        
    # 上一页
    def onAuditTagSysEventPrev(self):
        start = self.auditTagSysEventPageLength * (self.auditTagSysEventPage - 1)
        if start < 0:
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是第一页')
        else:
            self.AuditTagSysEventQuerySet(start, self.auditTagSysEventPageLength)

    # 下一页
    def onAuditTagSysEventNext(self):
        start = self.auditTagSysEventPageLength * (self.auditTagSysEventPage + 1)
        if start >= self.selfauditTagSysEventTotal:
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是最后一页')
        else:
            self.AuditTagSysEventQuerySet(start, self.auditTagSysEventPageLength)

    # 更新页计数
    def setAuditTagSysEventPageText(self):
        tot = self.selfauditTagSysEventTotal
        page = self.auditTagSysEventPage
        length = self.auditTagSysEventPageLength
        page_str = '0/0'
        if tot > 0:
            if tot % length > 0:
                page_str = '%d/%d' % (page + 1, (tot / length) + 1)
            else:
                page_str = '%d/%d' % (page + 1, tot / length)
        self.auditTagSysEventPageText.setText(_translate('auditTagSysEventPageText', page_str, None))

    def AuditTagSysEventQuerySet(self, start, length):
        start_time = unicode(self.auditTagSysEventStart.dateTime().toString('yyyy-MM-dd HH:mm:ss'))
        stop_time = unicode(self.auditTagSysEventStop.dateTime().toString('yyyy-MM-dd HH:mm:ss'))
        key_word = unicode(self.auditTagSysEventQuery.text())

        url = 'https://%s:%s/log/eventsys/query/%s' % (
                self._Config['Service']['IP'], self._Config['Service']['Port'], self.LoginName)
        data = {
            'Tokey': self.Tokey,
            'TimeStart': start_time,
            'TimeStop': stop_time,
            'KeyWord': key_word,
            'Start': start,
            'Length': length
        }
        # print url, data
        param = {'Data': json.dumps(data)}
        rt = HttpsPost(url, param)
        # print rt
        if rt[0] == 0:
            res = rt[1]
            if res['Status'] == 0:
                self.selfauditTagSysEventTotal = res['Total']

                # 清空列表
                for i in xrange(0, self.auditTagSysEventPageLength):
                    self.auditTagSysEventTable.setItem(i, 0, None)
                    self.auditTagSysEventTable.setItem(i, 1, None)
                    self.auditTagSysEventTable.setItem(i, 2, None)
                    self.auditTagSysEventTable.setItem(i, 3, None)
                    self.auditTagSysEventTable.setItem(i, 4, None)
                    self.auditTagSysEventPage = 0

                if res['Results'] != None:
                    # 添加列表
                    cnt = len(res['Results'])
                    for i in xrange(0, cnt):
                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['LoginName'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSysEventTable.setItem(i, 0, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Op'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSysEventTable.setItem(i, 1, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Result'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSysEventTable.setItem(i, 2, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['LogTime'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSysEventTable.setItem(i, 3, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Info'])
                        newItem.setTextAlignment(QtCore.Qt.AlignLeft)
                        self.auditTagSysEventTable.setItem(i, 4, newItem)

                    self.auditTagSysEventPage = start / self.auditTagSysEventPageLength
                self.setAuditTagSysEventPageText()
            else:
                QtGui.QMessageBox.about(self, u'错误提示', res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找日志失败:' + rt[1])
            
    def onAuditTagSysEventQuerySubmit(self):
        self.AuditTagSysEventQuerySet(0, self.auditTagSysEventPageLength)

