# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dtc_report.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DTCReport(object):
    def setupUi(self, DTCReport):
        DTCReport.setObjectName("DTCReport")
        DTCReport.resize(577, 216)
        self.pushButton_3 = QtWidgets.QPushButton(DTCReport)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 150, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(DTCReport)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 90, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(DTCReport)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 40, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(DTCReport)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 40, 361, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(DTCReport)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 90, 361, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(DTCReport)
        self.pushButton_4.clicked.connect(DTCReport.select_router_table)
        self.pushButton_5.clicked.connect(DTCReport.select_test_log)
        self.pushButton_3.clicked.connect(DTCReport.run)
        QtCore.QMetaObject.connectSlotsByName(DTCReport)

    def retranslateUi(self, DTCReport):
        _translate = QtCore.QCoreApplication.translate
        DTCReport.setWindowTitle(_translate("DTCReport", "kanwairen"))
        self.pushButton_3.setText(_translate("DTCReport", "RUN"))
        self.pushButton_5.setText(_translate("DTCReport", "选择测试log"))
        self.pushButton_4.setText(_translate("DTCReport", "选择路由表"))

