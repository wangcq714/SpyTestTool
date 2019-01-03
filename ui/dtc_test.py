# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dtc_test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DTCTest(object):
    def setupUi(self, DTCTest):
        DTCTest.setObjectName("DTCTest")
        DTCTest.resize(579, 172)
        self.textBrowser = QtWidgets.QTextBrowser(DTCTest)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 361, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(DTCTest)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 100, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(DTCTest)
        self.pushButton.setGeometry(QtCore.QRect(420, 40, 121, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(DTCTest)
        self.pushButton.clicked.connect(DTCTest.select_file)
        self.pushButton_2.clicked.connect(DTCTest.run)
        QtCore.QMetaObject.connectSlotsByName(DTCTest)

    def retranslateUi(self, DTCTest):
        _translate = QtCore.QCoreApplication.translate
        DTCTest.setWindowTitle(_translate("DTCTest", "kanwairen"))
        self.pushButton_2.setText(_translate("DTCTest", "RUN"))
        self.pushButton.setText(_translate("DTCTest", "选择路由表"))

