# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clock.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_world_clock(object):
    def setupUi(self, world_clock):
        world_clock.setObjectName("world_clock")
        world_clock.resize(462, 443)
        self.centralwidget = QtWidgets.QWidget(world_clock)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 90, 121, 16))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 130, 121, 16))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 170, 121, 16))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 210, 121, 16))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 250, 131, 20))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(70, 90, 161, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(70, 130, 161, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.timeEdit_3 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_3.setGeometry(QtCore.QRect(70, 170, 161, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit_3.setFont(font)
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.timeEdit_4 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_4.setGeometry(QtCore.QRect(70, 210, 161, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit_4.setFont(font)
        self.timeEdit_4.setObjectName("timeEdit_4")
        self.timeEdit_5 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_5.setGeometry(QtCore.QRect(70, 250, 161, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit_5.setFont(font)
        self.timeEdit_5.setObjectName("timeEdit_5")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(200, 330, 93, 28))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 30, 201, 20))
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        world_clock.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(world_clock)
        self.statusbar.setObjectName("statusbar")
        world_clock.setStatusBar(self.statusbar)

        self.retranslateUi(world_clock)
        QtCore.QMetaObject.connectSlotsByName(world_clock)

    def retranslateUi(self, world_clock):
        _translate = QtCore.QCoreApplication.translate
        world_clock.setWindowTitle(_translate("world_clock", "world clock"))
        self.label.setText(_translate("world_clock", "ساعت به وقت ایران"))
        self.label_2.setText(_translate("world_clock", "ساعت به وقت آمریکا"))
        self.label_3.setText(_translate("world_clock", "ساعت به وقت لندن"))
        self.label_4.setText(_translate("world_clock", "ساعت به وقت ژاپن"))
        self.label_5.setText(_translate("world_clock", "ساعت به وقت استرالیا"))
        self.update_button.setText(_translate("world_clock", "بروزرسانی"))
        self.label_6.setText(_translate("world_clock", "ساعت آنلاین چند کشور در جهان"))
