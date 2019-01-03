# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg_report.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestReport(object):
    def setupUi(self, TestReport):
        TestReport.setObjectName("TestReport")
        TestReport.resize(562, 190)
        self.pushButton = QtWidgets.QPushButton(TestReport)
        self.pushButton.setGeometry(QtCore.QRect(410, 20, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(TestReport)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 341, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(TestReport)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 70, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(TestReport)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 70, 341, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_3 = QtWidgets.QPushButton(TestReport)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 130, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(TestReport)
        self.pushButton_3.clicked.connect(TestReport.run)
        self.pushButton.clicked.connect(TestReport.select_router_table)
        self.pushButton_2.clicked.connect(TestReport.select_test_log)
        QtCore.QMetaObject.connectSlotsByName(TestReport)

    def retranslateUi(self, TestReport):
        _translate = QtCore.QCoreApplication.translate
        TestReport.setWindowTitle(_translate("TestReport", "kanwairen"))
        self.pushButton.setText(_translate("TestReport", "选择路由表"))
        self.pushButton_2.setText(_translate("TestReport", "选择测试log"))
        self.pushButton_3.setText(_translate("TestReport", "RUN"))

