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
        self.auditTagSysEventStartText.setGeometry(QtCore.QRect(20, 80, 40, 25))
        self.auditTagSysEventStartText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSysEventStartText.setObjectName(_fromUtf8("auditTagSysEventStartText"))
        self.auditTagSysEventStartText.setText(_translate("auditTagSysEventStartText", "开始：", None))

        # 开始时间 - 日历
        self.auditTagSysEventStart = QtGui.QDateTimeEdit(self.auditTagSysEventBkg)
        self.auditTagSysEventStart.setGeometry(QtCore.QRect(70, 80, 150, 25))
        self.auditTagSysEventStart.setCalendarPopup(True)
        # self.auditTagSysEventStart.setFrame(True)
        self.auditTagSysEventStart.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.auditTagSysEventStart.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_bg_disable.png);'))
        self.auditTagSysEventStart.setObjectName(_fromUtf8("auditTagSysEventStart"))
        self.auditTagSysEventStart.setDateTime(QtCore.QDateTime.currentDateTime())

        # 结束时间 - 文字
        self.auditTagSysEventStopText = QtGui.QLabel(self.auditTagSysEventBkg)
        self.auditTagSysEventStopText.setGeometry(QtCore.QRect(230, 80, 40, 25))
        self.auditTagSysEventStopText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSysEventStopText.setObjectName(_fromUtf8("auditTagSysEventStopText"))
        self.auditTagSysEventStopText.setText(_translate("auditTagSysEventStopText", "结束：", None))

        # 结束时间 - 日历
        self.auditTagSysEventStop = QtGui.QDateTimeEdit(self.auditTagSysEventBkg)
        self.auditTagSysEventStop.setGeometry(QtCore.QRect(280, 80, 150, 25))
        self.auditTagSysEventStop.setCalendarPopup(True)
        # self.auditTagSysEventStart.setFrame(True)
        self.auditTagSysEventStop.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.auditTagSysEventStop.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_bg_disable.png);'))
        self.auditTagSysEventStop.setObjectName(_fromUtf8("auditTagSysEventStop"))
        self.auditTagSysEventStop.setDateTime(QtCore.QDateTime.currentDateTime())

        # 上一页
        self.auditTagSysEventPrev = QtGui.QPushButton(self.auditTagSysEventBkg)
        self.auditTagSysEventPrev.setGeometry(QtCore.QRect(440, 80, 70, 25))
        self.auditTagSysEventPrev.setObjectName(_fromUtf8('auditTagSysEventPrev'))
        self.auditTagSysEventPrev.setText(_translate('auditTagSysEventPrev', '<<  上一页', None))

        # 当前页
        self.auditTagSysEventPageText = QtGui.QLabel(self.auditTagSysEventBkg)
        self.auditTagSysEventPageText.setGeometry(QtCore.QRect(520, 80, 50, 25))
        self.auditTagSysEventPageText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSysEventPageText.setObjectName(_fromUtf8('auditTagSysEventPageText'))
        self.auditTagSysEventPageText.setText(_translate('auditTagSysEventPageText', '0/0', None))

        # 下一页
        self.auditTagSysEventNext = QtGui.QPushButton(self.auditTagSysEventBkg)
        self.auditTagSysEventNext.setGeometry(QtCore.QRect(580, 80, 70, 25))
        self.auditTagSysEventNext.setObjectName(_fromUtf8('auditTagSysEventNext'))
        self.auditTagSysEventNext.setText(_translate('auditTagSysEventNext', '下一页  >>', None))

        # 查询 - 输入框
        self.auditTagSysEventQuery = QtGui.QLineEdit(self.auditTagSysEventBkg)
        self.auditTagSysEventQuery.setGeometry(QtCore.QRect(680, 80, 220, 25))
        self.auditTagSysEventQuery.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.auditTagSysEventQuery.setObjectName(_fromUtf8("auditTagSysEventQuery"))
        self.auditTagSysEventQuery.setText(_translate("auditTagSysEventStopText", "", None))

        # 查询 - 文字
        self.auditTagSysEventQueryText = QtGui.QPushButton(self.auditTagSysEventBkg)
        self.auditTagSysEventQueryText.setGeometry(QtCore.QRect(910, 80, 60, 25))
        self.auditTagSysEventQueryText.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.auditTagSysEventQueryText.setObjectName(_fromUtf8("auditTagSysEventQueryText"))
        self.auditTagSysEventQueryText.setText(_translate("auditTagSysEventQueryText", "查询", None))

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
        self.auditTagSysEventTable.setColumnWidth(3, 120)
        self.auditTagSysEventTable.setColumnWidth(4, 490)
        for i in range(0, self.auditTagSysEventPageLength):
            self.auditTagSysEventTable.setRowHeight(i, 23)
