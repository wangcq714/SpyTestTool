# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg_test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RouterTest(object):
    def setupUi(self, RouterTest):
        RouterTest.setObjectName("RouterTest")
        RouterTest.resize(569, 161)
        self.pushButton = QtWidgets.QPushButton(RouterTest)
        self.pushButton.setGeometry(QtCore.QRect(420, 40, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(RouterTest)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 381, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(RouterTest)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 100, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(RouterTest)
        self.pushButton.clicked.connect(RouterTest.select_file)
        self.pushButton_2.clicked.connect(RouterTest.run)
        QtCore.QMetaObject.connectSlotsByName(RouterTest)

    def retranslateUi(self, RouterTest):
        _translate = QtCore.QCoreApplication.translate
        RouterTest.setWindowTitle(_translate("RouterTest", "kanwairen"))
        self.pushButton.setText(_translate("RouterTest", "选择路由表"))
        self.pushButton_2.setText(_translate("RouterTest", "RUN"))

