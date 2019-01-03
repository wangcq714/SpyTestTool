# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signal_test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignalTest(object):
    def setupUi(self, SignalTest):
        SignalTest.setObjectName("SignalTest")
        SignalTest.resize(570, 171)
        self.pushButton = QtWidgets.QPushButton(SignalTest)
        self.pushButton.setGeometry(QtCore.QRect(420, 40, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(SignalTest)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 361, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(SignalTest)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 100, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(SignalTest)
        self.pushButton.clicked.connect(SignalTest.select_file)
        self.pushButton_2.clicked.connect(SignalTest.run)
        QtCore.QMetaObject.connectSlotsByName(SignalTest)

    def retranslateUi(self, SignalTest):
        _translate = QtCore.QCoreApplication.translate
        SignalTest.setWindowTitle(_translate("SignalTest", "kanwairen"))
        self.pushButton.setText(_translate("SignalTest", "选择路由表"))
        self.pushButton_2.setText(_translate("SignalTest", "RUN"))

