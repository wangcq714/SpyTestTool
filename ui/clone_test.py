# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clone_test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CloneTest(object):
    def setupUi(self, CloneTest):
        CloneTest.setObjectName("CloneTest")
        CloneTest.resize(571, 192)
        self.pushButton = QtWidgets.QPushButton(CloneTest)
        self.pushButton.setGeometry(QtCore.QRect(420, 20, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(CloneTest)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 381, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(CloneTest)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 70, 261, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(CloneTest)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 130, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(CloneTest)
        self.textEdit.setGeometry(QtCore.QRect(310, 70, 101, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(CloneTest)
        self.pushButton_3.clicked.connect(CloneTest.run)
        self.pushButton.clicked.connect(CloneTest.select_file)
        self.textEdit.textChanged.connect(CloneTest.clone_ch)
        QtCore.QMetaObject.connectSlotsByName(CloneTest)

    def retranslateUi(self, CloneTest):
        _translate = QtCore.QCoreApplication.translate
        CloneTest.setWindowTitle(_translate("CloneTest", "kanwairen"))
        self.pushButton.setText(_translate("CloneTest", "选择路由表"))
        self.pushButton_2.setText(_translate("CloneTest", "克隆通道输入(测试表中定义的网段名称)："))
        self.pushButton_3.setText(_translate("CloneTest", "RUN"))

