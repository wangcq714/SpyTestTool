from ui.mainwindow import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from ui import msg_test, msg_report, clone_test
from ui import signal_test, signal_report
from ui import dtc_test, dtc_report

import msgtest
from msgtest import spy_msg_test

import signaltest
from signaltest import spy_signal_test

import dtctest
from dtctest import spy_dtc_test


class MyRouterTest(msg_test.Ui_RouterTest, QMainWindow):
    def __init__(self):
        super().__init__()
        self.pathname = ['', '']
        self.runPattern = ["Default", "NA"]

    def run(self):
        try:
            msgtest.config.config.RunPattern = self.runPattern
            _translate = QtCore.QCoreApplication.translate
            if self.pathname[0] != '':
                self.pushButton_2.setText(_translate("RouterTest", "Running"))
                spy_msg_test.SpyCCodemain_pandas(self.pathname[0])
                self.pushButton_2.setText(_translate("RouterTest", "Finished"))
            else:
                self.pushButton_2.setText(_translate("RouterTest", "Error"))
        except:
            self.pushButton_2.setText(_translate("RouterTest", "Error"))

    def select_file(self):
        self.pathname = QFileDialog.getOpenFileName()
        self.pathname_show()
        if self.pathname[0] != '':
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_2.setText(_translate("RouterTest", "RUN"))

        # print(self.pathname)

    def pathname_show(self):
        self.textBrowser.clear()
        self.textBrowser.append(self.pathname[0])


class MyMsgReport(msg_report.Ui_TestReport, QMainWindow):
    def __init__(self):
        super().__init__()
        self.router_table_pathname = ['', '']
        self.log_pathname = ['', '']
        self.runPattern = ["Report", "NA"]

    def run(self):
        try:
            msgtest.config.config.RunPattern = self.runPattern
            _translate = QtCore.QCoreApplication.translate
            if self.router_table_pathname[0] != '' and self.log_pathname[0] != '':
                self.pushButton_3.setText(_translate("TestReport", "Running"))
                spy_msg_test.reportmain_pandas(self.router_table_pathname[0], self.log_pathname[0])
                self.pushButton_3.setText(_translate("TestReport", "Finished"))
            else:
                self.pushButton_3.setText(_translate("TestReport", "Error"))
        except:
            self.pushButton_3.setText(_translate("TestReport", "Error"))

    def select_router_table(self):
        self.router_table_pathname = QFileDialog.getOpenFileName()
        self.router_table_pathname_show()
        print(self.router_table_pathname)
        if self.router_table_pathname[0] != '' and self.log_pathname[0] != '':
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_3.setText(_translate("TestReport", "RUN"))
        print(self.router_table_pathname)

    def select_test_log(self):
        self.log_pathname = QFileDialog.getOpenFileName()
        self.log_pathname_show()
        if self.router_table_pathname[0] != '' and self.log_pathname[0] != '':
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_3.setText(_translate("TestReport", "RUN"))
        print(self.log_pathname)

    def router_table_pathname_show(self):
        self.textBrowser.clear()
        self.textBrowser.append(self.router_table_pathname[0])

    def log_pathname_show(self):
        self.textBrowser_2.clear()
        self.textBrowser_2.append(self.log_pathname[0])


class MyCloneTest(clone_test.Ui_CloneTest, QMainWindow):
    def __init__(self):
        super().__init__()
        self.pathname = ['', '']
        self.runPattern = ["Clone", "NA"]

    def run(self):
        try:
            msgtest.config.config.RunPattern = self.runPattern
            _translate = QtCore.QCoreApplication.translate
            if self.pathname[0] != '' and self.runPattern[1] != "NA" and self.runPattern[1] != "":
                self.pushButton_3.setText(_translate("CloneTest", "Running"))
                # print(self.runPattern)
                spy_msg_test.SpyCCodemain_pandas(self.pathname[0])
                self.pushButton_3.setText(_translate("CloneTest", "Finished"))
            else:
                self.pushButton_3.setText(_translate("CloneTest", "Error"))
        except:
            self.pushButton_3.setText(_translate("CloneTest", "Error"))

    def select_file(self):
        self.pathname = QFileDialog.getOpenFileName()
        self.pathname_show()
        if self.pathname[0] != '' and self.runPattern[1] != "NA":
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_3.setText(_translate("CloneTest", "RUN"))
        print(self.pathname)

    def pathname_show(self):
        self.textBrowser.clear()
        self.textBrowser.append(self.pathname[0])

    def clone_ch(self):
        self.runPattern[1] = self.textEdit.toPlainText()
        print(type(self.runPattern))
        if self.pathname != '' and self.runPattern[1] != "NA" and self.runPattern[1] != "":
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_3.setText(_translate("CloneTest", "RUN"))
        print(self.runPattern)


class MySignalTest(signal_test.Ui_SignalTest, QMainWindow):
    def __init__(self):
        super().__init__()
        self.pathname = ['', '']
        self.runPattern = ["Test"]

    def run(self):
        try:
            signaltest.config.config.RunPattern = self.runPattern
            _translate = QtCore.QCoreApplication.translate
            if self.pathname[0] != '':
                self.pushButton_2.setText(_translate("SignalTest", "Running"))
                spy_signal_test.SpyCCodemain_pandas(self.pathname[0])
                self.pushButton_2.setText(_translate("SignalTest", "Finished"))
            else:
                self.pushButton_2.setText(_translate("SignalTest", "Error"))
        except:
            self.pushButton_2.setText(_translate("SignalTest", "Error"))

    def select_file(self):
        self.pathname = QFileDialog.getOpenFileName()
        self.pathname_show()
        if self.pathname[0] != '':
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_2.setText(_translate("SignalTest", "RUN"))

    def pathname_show(self):
        self.textBrowser.clear()
        self.textBrowser.append(self.pathname[0])


class MySignalReport(signal_report.Ui_SignalReport, QMainWindow):
    def __init__(self):
        super().__init__()
        self.router_table_pathname = ['', '']
        self.log_pathname = ['', '']
        self.runPattern = ["Report"]

    def run(self):
        try:
            signaltest.config.config.RunPattern = self.runPattern
            _translate = QtCore.QCoreApplication.translate
            if self.router_table_pathname[0] != '' and self.log_pathname[0] != '':
                self.pushButton_3.setText(_translate("SignalReport", "Running"))
                spy_signal_test.reportmain_pandas(self.log_pathname[0], self.router_table_pathname[0])
                self.pushButton_3.setText(_translate("SignalReport", "Finished"))
            else:
                self.pushButton_3.setText(_translate("SignalReport", "Error"))
        except:
            self.pushButton_3.setText(_translate("SignalReport", "Error"))

    def select_router_table(self):
        self.router_table_pathname = QFileDialog.getOpenFileName()
        self.router_table_pathname_show()
        print(self.router_table_pathname)
        if self.router_table_pathname[0] != '' and self.log_pathname[0] != '':
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_3.setText(_translate("SignalReport", "RUN"))
        print(self.router_table_pathname)

    def select_test_log(self):
        self.log_pathname = QFileDialog.getOpenFileName()
        self.log_pathname_show()
        if self.router_table_pathname[0] != '' and self.log_pathname[0] != '':
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_3.setText(_translate("SignalReport", "RUN"))
        print(self.log_pathname)

    def router_table_pathname_show(self):
        self.textBrowser_3.clear()
        self.textBrowser_3.append(self.router_table_pathname[0])

    def log_pathname_show(self):
        self.textBrowser_2.clear()
        self.textBrowser_2.append(self.log_pathname[0])


class MyDTCTest(dtc_test.Ui_DTCTest, QMainWindow):
    def __init__(self):
        super().__init__()
        self.pathname = ['', '']
        self.runPattern = ["Test"]

    def run(self):
        try:
            dtctest.config.config.RunPattern = self.runPattern
            _translate = QtCore.QCoreApplication.translate
            if self.pathname[0] != '':
                self.pushButton_2.setText(_translate("DTCTest", "Running"))
                spy_dtc_test.SpyCCodemain(self.pathname[0])
                self.pushButton_2.setText(_translate("DTCTest", "Finished"))
            else:
                self.pushButton_2.setText(_translate("DTCTest", "Error"))
        except:
            self.pushButton_2.setText(_translate("DTCTest", "Error"))

    def select_file(self):
        self.pathname = QFileDialog.getOpenFileName()
        self.pathname_show()
        if self.pathname[0] != '':
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_2.setText(_translate("DTCTest", "RUN"))

    def pathname_show(self):
        self.textBrowser.clear()
        self.textBrowser.append(self.pathname[0])


class MyDTCReport(dtc_report.Ui_DTCReport, QMainWindow):
    def __init__(self):
        super().__init__()
        self.router_table_pathname = ['', '']
        self.log_pathname = ['', '']
        self.runPattern = ["Report"]

    def run(self):
        try:
            dtctest.config.config.RunPattern = self.runPattern
            _translate = QtCore.QCoreApplication.translate
            if self.router_table_pathname[0] != '' and self.log_pathname[0] != '':
                self.pushButton_3.setText(_translate("DTCReport", "Running"))
                spy_dtc_test.reportmain(self.log_pathname[0], self.router_table_pathname[0])
                self.pushButton_3.setText(_translate("DTCReport", "Finished"))
            else:
                self.pushButton_3.setText(_translate("DTCReport", "Error"))
        except:
            self.pushButton_3.setText(_translate("DTCReport", "Error"))

    def select_router_table(self):
        self.router_table_pathname = QFileDialog.getOpenFileName()
        self.router_table_pathname_show()
        print(self.router_table_pathname)
        if self.router_table_pathname[0] != '' and self.log_pathname[0] != '':
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_3.setText(_translate("DTCReport", "RUN"))
        print(self.router_table_pathname)

    def select_test_log(self):
        self.log_pathname = QFileDialog.getOpenFileName()
        self.log_pathname_show()
        if self.router_table_pathname[0] != '' and self.log_pathname[0] != '':
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_3.setText(_translate("DTCReport", "RUN"))
        print(self.log_pathname)

    def router_table_pathname_show(self):
        self.textBrowser_3.clear()
        self.textBrowser_3.append(self.router_table_pathname[0])

    def log_pathname_show(self):
        self.textBrowser_2.clear()
        self.textBrowser_2.append(self.log_pathname[0])


class MyMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.myRouterTest = MyRouterTest()
        self.myMsgReport = MyMsgReport()
        self.myCloneTest = MyCloneTest()
        self.mySignalTest = MySignalTest()
        self.mySignalReport = MySignalReport()
        self.myDTCTest = MyDTCTest()
        self.myDTCReport = MyDTCReport()


    def setup(self):
        self.myRouterTest.setupUi(self.myRouterTest)
        self.myMsgReport.setupUi(self.myMsgReport)
        self.myCloneTest.setupUi(self.myCloneTest)
        self.mySignalTest.setupUi(self.mySignalTest)
        self.mySignalReport.setupUi(self.mySignalReport)
        self.myDTCTest.setupUi(self.myDTCTest)
        self.myDTCReport.setupUi(self.myDTCReport)

    def msg_test(self):
        self.myRouterTest.show()

    def msg_report(self):
        self.myMsgReport.show()

    def clone_test(self):
        self.myCloneTest.show()

    def signal_test(self):
        self.mySignalTest.show()

    def signal_report(self):
        self.mySignalReport.show()

    def dtc_test(self):
        self.myDTCTest.show()

    def dtc_report(self):
        self.myDTCReport.show()





