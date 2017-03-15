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


class AuditBoardSafeEvent(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AuditBoardSafeEvent, self).__init__(parent)
        # self.setupUi(self)

    def AddAuditTagSafeEvent(self):
        self.auditTagSafeEventPageLength = 10
        self.auditTagSafeEventPage = 0
        selfauditTagSafeEventTotal = 0

        # Logo
        self.auditTagSafeEventLogo = QtGui.QWidget(self.auditTagSafeEventBkg)
        self.auditTagSafeEventLogo.setGeometry(QtCore.QRect(40, 10, 70, 60))
        self.auditTagSafeEventLogo.setObjectName(_fromUtf8("auditTagSafeEventLogo"))
        self.auditTagSafeEventLogo.setStyleSheet(_fromUtf8("border-image: url(:/images/audit_config_logo.png);"))

        # 标题
        self.auditTagSafeEventTitle = QtGui.QWidget(self.auditTagSafeEventBkg)
        self.auditTagSafeEventTitle.setGeometry(QtCore.QRect(120, 10, 200, 60))
        self.auditTagSafeEventTitle.setObjectName(_fromUtf8("auditTagSafeEventTitle"))
        self.auditTagSafeEventTitle.setStyleSheet(_fromUtf8("border-image: url(:/images/audit_config_title.png);"))

        # 画线
        self.auditTagSafeEventSpace1 = QtGui.QWidget(self.auditTagSafeEventBkg)
        self.auditTagSafeEventSpace1.setGeometry(QtCore.QRect(0, 74, 10000, 1))
        self.auditTagSafeEventSpace1.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.auditTagSafeEventSpace1.setObjectName(_fromUtf8("auditTagSafeEventSpace1"))

        # 画线 上
        self.auditTagSafeEventSpaceTop = QtGui.QWidget(self.auditTagSafeEventBkg)
        self.auditTagSafeEventSpaceTop.setGeometry(QtCore.QRect(0, 112, 10000, 1))
        self.auditTagSafeEventSpaceTop.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_bg_disable.png);"))
        self.auditTagSafeEventSpaceTop.setObjectName(_fromUtf8("auditTagSafeEventSpaceTop"))

        # 开始时间 - 文字
        self.auditTagSafeEventStartText = QtGui.QLabel(self.auditTagSafeEventBkg)
        self.auditTagSafeEventStartText.setGeometry(QtCore.QRect(20, 80, 35, 25))
        self.auditTagSafeEventStartText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSafeEventStartText.setObjectName(_fromUtf8("auditTagSafeEventStartText"))
        self.auditTagSafeEventStartText.setText(_translate("auditTagSafeEventStartText", "开始：", None))

        # 开始时间 - 日历
        self.auditTagSafeEventStart = QtGui.QDateTimeEdit(self.auditTagSafeEventBkg)
        self.auditTagSafeEventStart.setGeometry(QtCore.QRect(65, 80, 170, 25))
        self.auditTagSafeEventStart.setCalendarPopup(True)
        self.auditTagSafeEventStart.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        #self.auditTagSafeEventStart.setFrame(True)
        self.auditTagSafeEventStart.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.auditTagSafeEventStart.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.auditTagSafeEventStart.setObjectName(_fromUtf8("auditTagSafeEventStart"))
        self.auditTagSafeEventStart.setDateTime(QtCore.QDateTime.currentDateTime())

        # 结束时间 - 文字
        self.auditTagSafeEventStopText = QtGui.QLabel(self.auditTagSafeEventBkg)
        self.auditTagSafeEventStopText.setGeometry(QtCore.QRect(245, 80, 35, 25))
        self.auditTagSafeEventStopText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSafeEventStopText.setObjectName(_fromUtf8("auditTagSafeEventStopText"))
        self.auditTagSafeEventStopText.setText(_translate("auditTagSafeEventStopText", "结束：", None))

        # 结束时间 - 日历
        self.auditTagSafeEventStop = QtGui.QDateTimeEdit(self.auditTagSafeEventBkg)
        self.auditTagSafeEventStop.setGeometry(QtCore.QRect(285, 80, 170, 25))
        self.auditTagSafeEventStop.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSafeEventStop.setCalendarPopup(True)
        # self.auditTagSafeEventStart.setFrame(True)
        self.auditTagSafeEventStop.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.auditTagSafeEventStop.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.png);'))
        self.auditTagSafeEventStop.setObjectName(_fromUtf8("auditTagSafeEventStop"))
        self.auditTagSafeEventStop.setDateTime(QtCore.QDateTime.currentDateTime())

        # 上一页
        self.auditTagSafeEventPrev = QtGui.QPushButton(self.auditTagSafeEventBkg)
        self.auditTagSafeEventPrev.setGeometry(QtCore.QRect(465, 80, 70, 25))
        self.auditTagSafeEventPrev.setObjectName(_fromUtf8('auditTagSafeEventPrev'))
        self.auditTagSafeEventPrev.setText(_translate('auditTagSafeEventPrev', '<<  上一页', None))

        # 当前页
        self.auditTagSafeEventPageText = QtGui.QLabel(self.auditTagSafeEventBkg)
        self.auditTagSafeEventPageText.setGeometry(QtCore.QRect(545, 80, 50, 25))
        self.auditTagSafeEventPageText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSafeEventPageText.setObjectName(_fromUtf8('auditTagSafeEventPageText'))
        self.auditTagSafeEventPageText.setText(_translate('auditTagSafeEventPageText', '0/0', None))

        # 下一页
        self.auditTagSafeEventNext = QtGui.QPushButton(self.auditTagSafeEventBkg)
        self.auditTagSafeEventNext.setGeometry(QtCore.QRect(605, 80, 70, 25))
        self.auditTagSafeEventNext.setObjectName(_fromUtf8('auditTagSafeEventNext'))
        self.auditTagSafeEventNext.setText(_translate('auditTagSafeEventNext', '下一页  >>', None))

        # 查询 - 输入框
        self.auditTagSafeEventQuery = QtGui.QLineEdit(self.auditTagSafeEventBkg)
        self.auditTagSafeEventQuery.setGeometry(QtCore.QRect(705, 80, 190, 25))
        self.auditTagSafeEventQuery.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.auditTagSafeEventQuery.setObjectName(_fromUtf8("auditTagSafeEventQuery"))
        self.auditTagSafeEventQuery.setText(_translate("auditTagSafeEventStopText", "", None))

        # 查询
        self.auditTagSafeEventQuerySubmit = QtGui.QPushButton(self.auditTagSafeEventBkg)
        self.auditTagSafeEventQuerySubmit.setGeometry(QtCore.QRect(910, 80, 60, 25))
        self.auditTagSafeEventQuerySubmit.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.auditTagSafeEventQuerySubmit.setObjectName(_fromUtf8("auditTagSafeEventQuerySubmit"))
        self.auditTagSafeEventQuerySubmit.setText(_translate("auditTagSafeEventQuerySubmit", "查询", None))

        # 日志表格
        self.auditTagSafeEventTable = QtGui.QTableWidget(self.auditTagSafeEventBkg)
        self.auditTagSafeEventTable.setGeometry(QtCore.QRect(20, 120, 950, 290))
        self.auditTagSafeEventTable.setObjectName(_fromUtf8('auditTagSafeEventTable'))
        self.auditTagSafeEventTable.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_grey_line.jpg);'))
        self.auditTagSafeEventTable.verticalHeader().setVisible(False)
        self.auditTagSafeEventTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.auditTagSafeEventTable.setAlternatingRowColors(True)
        # list_widget.adminTagConfigProcWhiteTable(QtGui.QAbstractItemView.SelectRows)
        self.auditTagSafeEventTable.setRowCount(self.auditTagSafeEventPageLength)
        self.auditTagSafeEventTable.setColumnCount(9)
        self.auditTagSafeEventTable.setHorizontalHeaderLabels([_fromUtf8('模块名称'), _fromUtf8('保护状态'), _fromUtf8('事件类型')
                                                              , _fromUtf8('行为'), _fromUtf8('结果'), _fromUtf8('用户名')
                                                              , _fromUtf8('进程'), _fromUtf8('对象'), _fromUtf8('时间')])
        self.auditTagSafeEventTable.setShowGrid(False)
        self.auditTagSafeEventTable.setColumnWidth(0, 80)
        self.auditTagSafeEventTable.setColumnWidth(1, 80)
        self.auditTagSafeEventTable.setColumnWidth(2, 80)
        self.auditTagSafeEventTable.setColumnWidth(3, 80)
        self.auditTagSafeEventTable.setColumnWidth(4, 80)
        self.auditTagSafeEventTable.setColumnWidth(5, 80)
        self.auditTagSafeEventTable.setColumnWidth(6, 200)
        self.auditTagSafeEventTable.setColumnWidth(7, 200)
        self.auditTagSafeEventTable.setColumnWidth(8, 110)
        for i in range(0, self.auditTagSafeEventPageLength):
            self.auditTagSafeEventTable.setRowHeight(i, 23)

        # 添加消息
        self.connect(self.auditTagSafeEventPrev, QtCore.SIGNAL('clicked()'), self.onAuditTagSafeEventPrev)
        self.connect(self.auditTagSafeEventNext, QtCore.SIGNAL('clicked()'), self.onAuditTagSafeEventNext)
        self.connect(self.auditTagSafeEventQuerySubmit, QtCore.SIGNAL('clicked()'), self.onAuditTagSafeEventQuerySubmit)

        
    # 上一页
    def onAuditTagSafeEventPrev(self):
        start = self.auditTagSafeEventPageLength * (self.auditTagSafeEventPage - 1)
        if start < 0:
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是第一页')
        else:
            self.AuditTagSafeEventQuerySet(start, self.auditTagSafeEventPageLength)

    # 下一页
    def onAuditTagSafeEventNext(self):
        start = self.auditTagSafeEventPageLength * (self.auditTagSafeEventPage + 1)
        if start >= self.selfauditTagSafeEventTotal:
            QtGui.QMessageBox.about(self, u'错误提示', u'已经是最后一页')
        else:
            self.AuditTagSafeEventQuerySet(start, self.auditTagSafeEventPageLength)

    # 更新页计数
    def setAuditTagSafeEventPageText(self):
        tot = self.selfauditTagSafeEventTotal
        page = self.auditTagSafeEventPage
        length = self.auditTagSafeEventPageLength
        page_str = '0/0'
        if tot > 0:
            if tot % length > 0:
                page_str = '%d/%d' % (page + 1, (tot / length) + 1)
            else:
                page_str = '%d/%d' % (page + 1, tot / length)
        self.auditTagSafeEventPageText.setText(_translate('auditTagSafeEventPageText', page_str, None))

    def AuditTagSafeEventQuerySet(self, start, length):
        start_time = unicode(self.auditTagSafeEventStart.dateTime().toString('yyyy-MM-dd HH:mm:ss'))
        stop_time = unicode(self.auditTagSafeEventStop.dateTime().toString('yyyy-MM-dd HH:mm:ss'))
        key_word = unicode(self.auditTagSafeEventQuery.text())

        url = 'https://%s:%s/log/eventsafe/query/%s' % (
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
                self.selfauditTagSafeEventTotal = res['Total']

                # 清空列表
                for i in xrange(0, self.auditTagSafeEventPageLength):
                    self.auditTagSafeEventTable.setItem(i, 0, None)
                    self.auditTagSafeEventTable.setItem(i, 1, None)
                    self.auditTagSafeEventTable.setItem(i, 2, None)
                    self.auditTagSafeEventTable.setItem(i, 3, None)
                    self.auditTagSafeEventTable.setItem(i, 4, None)
                    self.auditTagSafeEventTable.setItem(i, 5, None)
                    self.auditTagSafeEventTable.setItem(i, 6, None)
                    self.auditTagSafeEventTable.setItem(i, 7, None)
                    self.auditTagSafeEventTable.setItem(i, 8, None)
                    self.auditTagSafeEventPage = 0

                if res['Results'] != None:
                    # 添加列表
                    cnt = len(res['Results'])
                    for i in xrange(0, cnt):
                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Module'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSafeEventTable.setItem(i, 0, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Status'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSafeEventTable.setItem(i, 1, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Etype'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSafeEventTable.setItem(i, 2, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Eop'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSafeEventTable.setItem(i, 3, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Result'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSafeEventTable.setItem(i, 4, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Uname'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSafeEventTable.setItem(i, 5, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Proc'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSafeEventTable.setItem(i, 6, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['Obj'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.adminTagConfigProcWhiteTable.setItem(i, 7, newItem)

                        newItem = QtGui.QTableWidgetItem(res['Results'][i]['LogTime'])
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.auditTagSafeEventTable.setItem(i, 8, newItem)

                    self.auditTagSafeEventPage = start / self.auditTagSafeEventPageLength
                self.setAuditTagSafeEventPageText()
            else:
                QtGui.QMessageBox.about(self, u'错误提示', res['ErrMsg'])
        else:
            QtGui.QMessageBox.about(self, u'错误提示', u'查找日志失败:' + rt[1])

    def onAuditTagSafeEventQuerySubmit(self):
        AuditTagSafeEventQuerySet(0, self.auditTagSafeEventPageLength)

