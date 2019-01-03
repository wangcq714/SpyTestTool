# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 323)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 371, 341))
        self.tabWidget.setObjectName("tabWidget")
        self.Msg = QtWidgets.QWidget()
        self.Msg.setObjectName("Msg")
        self.pushButton_2 = QtWidgets.QPushButton(self.Msg)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 40, 181, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Msg)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 110, 181, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Msg)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 180, 181, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.Msg, "")
        self.Signal = QtWidgets.QWidget()
        self.Signal.setObjectName("Signal")
        self.pushButton_5 = QtWidgets.QPushButton(self.Signal)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 40, 181, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.Signal)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 180, 181, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.Signal, "")
        self.DTC = QtWidgets.QWidget()
        self.DTC.setObjectName("DTC")
        self.pushButton_7 = QtWidgets.QPushButton(self.DTC)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 40, 181, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.DTC)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 180, 181, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.DTC, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(MainWindow.msg_test)
        self.pushButton_3.clicked.connect(MainWindow.clone_test)
        self.pushButton_4.clicked.connect(MainWindow.msg_report)
        self.pushButton_5.clicked.connect(MainWindow.signal_test)
        self.pushButton_6.clicked.connect(MainWindow.signal_report)
        self.pushButton_7.clicked.connect(MainWindow.dtc_test)
        self.pushButton_8.clicked.connect(MainWindow.dtc_report)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "kanwairen"))
        self.pushButton_2.setText(_translate("MainWindow", "路由转发测试"))
        self.pushButton_3.setText(_translate("MainWindow", "克隆转发测试"))
        self.pushButton_4.setText(_translate("MainWindow", "测试报告"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Msg), _translate("MainWindow", "MsgTest"))
        self.pushButton_5.setText(_translate("MainWindow", "信号转发测试"))
        self.pushButton_6.setText(_translate("MainWindow", "测试报告"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Signal), _translate("MainWindow", "SignalTest"))
        self.pushButton_7.setText(_translate("MainWindow", "DTC测试"))
        self.pushButton_8.setText(_translate("MainWindow", "测试报告"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DTC), _translate("MainWindow", "DTCTest"))

