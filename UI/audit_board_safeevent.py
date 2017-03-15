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
        self.auditTagSafeEventStartText.setGeometry(QtCore.QRect(20, 80, 40, 25))
        self.auditTagSafeEventStartText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSafeEventStartText.setObjectName(_fromUtf8("auditTagSafeEventStartText"))
        self.auditTagSafeEventStartText.setText(_translate("auditTagSafeEventStartText", "开始：", None))

        # 开始时间 - 日历
        self.auditTagSafeEventStart = QtGui.QDateTimeEdit(self.auditTagSafeEventBkg)
        self.auditTagSafeEventStart.setGeometry(QtCore.QRect(70, 80, 155, 25))
        self.auditTagSafeEventStart.setCalendarPopup(True)
        #self.auditTagSafeEventStart.setFrame(True)
        self.auditTagSafeEventStart.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.auditTagSafeEventStart.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_bg_disable.png);'))
        self.auditTagSafeEventStart.setObjectName(_fromUtf8("auditTagSafeEventStart"))
        self.auditTagSafeEventStart.setDateTime(QtCore.QDateTime.currentDateTime())

        # 结束时间 - 文字
        self.auditTagSafeEventStopText = QtGui.QLabel(self.auditTagSafeEventBkg)
        self.auditTagSafeEventStopText.setGeometry(QtCore.QRect(235, 80, 40, 25))
        self.auditTagSafeEventStopText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSafeEventStopText.setObjectName(_fromUtf8("auditTagSafeEventStopText"))
        self.auditTagSafeEventStopText.setText(_translate("auditTagSafeEventStopText", "结束：", None))

        # 结束时间 - 日历
        self.auditTagSafeEventStop = QtGui.QDateTimeEdit(self.auditTagSafeEventBkg)
        self.auditTagSafeEventStop.setGeometry(QtCore.QRect(285, 80, 155, 25))
        self.auditTagSafeEventStop.setCalendarPopup(True)
        # self.auditTagSafeEventStart.setFrame(True)
        self.auditTagSafeEventStop.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.auditTagSafeEventStop.setStyleSheet(_fromUtf8('border-image: url(:/images/btn_bg_disable.png);'))
        self.auditTagSafeEventStop.setObjectName(_fromUtf8("auditTagSafeEventStop"))
        self.auditTagSafeEventStop.setDateTime(QtCore.QDateTime.currentDateTime())

        # 上一页
        self.auditTagSafeEventPrev = QtGui.QPushButton(self.auditTagSafeEventBkg)
        self.auditTagSafeEventPrev.setGeometry(QtCore.QRect(450, 80, 70, 25))
        self.auditTagSafeEventPrev.setObjectName(_fromUtf8('auditTagSafeEventPrev'))
        self.auditTagSafeEventPrev.setText(_translate('auditTagSafeEventPrev', '<<  上一页', None))

        # 当前页
        self.auditTagSafeEventPageText = QtGui.QLabel(self.auditTagSafeEventBkg)
        self.auditTagSafeEventPageText.setGeometry(QtCore.QRect(530, 80, 50, 25))
        self.auditTagSafeEventPageText.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter)
        self.auditTagSafeEventPageText.setObjectName(_fromUtf8('auditTagSafeEventPageText'))
        self.auditTagSafeEventPageText.setText(_translate('auditTagSafeEventPageText', '0/0', None))

        # 下一页
        self.auditTagSafeEventNext = QtGui.QPushButton(self.auditTagSafeEventBkg)
        self.auditTagSafeEventNext.setGeometry(QtCore.QRect(590, 80, 70, 25))
        self.auditTagSafeEventNext.setObjectName(_fromUtf8('auditTagSafeEventNext'))
        self.auditTagSafeEventNext.setText(_translate('auditTagSafeEventNext', '下一页  >>', None))

        # 查询 - 输入框
        self.auditTagSafeEventQuery = QtGui.QLineEdit(self.auditTagSafeEventBkg)
        self.auditTagSafeEventQuery.setGeometry(QtCore.QRect(690, 80, 210, 25))
        self.auditTagSafeEventQuery.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.auditTagSafeEventQuery.setObjectName(_fromUtf8("auditTagSafeEventQuery"))
        self.auditTagSafeEventQuery.setText(_translate("auditTagSafeEventStopText", "", None))

        # 查询 - 文字
        self.auditTagSafeEventQueryText = QtGui.QPushButton(self.auditTagSafeEventBkg)
        self.auditTagSafeEventQueryText.setGeometry(QtCore.QRect(910, 80, 60, 25))
        self.auditTagSafeEventQueryText.setStyleSheet(_fromUtf8("border-image: url(:/images/btn_grey_line.png);"))
        self.auditTagSafeEventQueryText.setObjectName(_fromUtf8("auditTagSafeEventQueryText"))
        self.auditTagSafeEventQueryText.setText(_translate("auditTagSafeEventQueryText", "查询", None))

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
