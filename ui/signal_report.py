# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signal_report.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignalReport(object):
    def setupUi(self, SignalReport):
        SignalReport.setObjectName("SignalReport")
        SignalReport.resize(574, 223)
        self.pushButton_3 = QtWidgets.QPushButton(SignalReport)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 150, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(SignalReport)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 90, 361, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_4 = QtWidgets.QPushButton(SignalReport)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 40, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(SignalReport)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 40, 361, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_5 = QtWidgets.QPushButton(SignalReport)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 90, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(SignalReport)
        self.pushButton_4.clicked.connect(SignalReport.select_router_table)
        self.pushButton_5.clicked.connect(SignalReport.select_test_log)
        self.pushButton_3.clicked.connect(SignalReport.run)
        QtCore.QMetaObject.connectSlotsByName(SignalReport)

    def retranslateUi(self, SignalReport):
        _translate = QtCore.QCoreApplication.translate
        SignalReport.setWindowTitle(_translate("SignalReport", "kanwairen"))
        self.pushButton_3.setText(_translate("SignalReport", "RUN"))
        self.pushButton_4.setText(_translate("SignalReport", "选择路由表"))
        self.pushButton_5.setText(_translate("SignalReport", "选择测试log"))

