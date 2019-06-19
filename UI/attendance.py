# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attendance.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_attendance(object):
    def setupUi(self, attendance):
        attendance.setObjectName("attendance")
        attendance.resize(1158, 709)
        attendance.setStyleSheet("")
        self.frame = QtWidgets.QFrame(attendance)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1158, 709))
        self.frame.setStyleSheet("\n"
"background-color:  rgb(42, 131, 162)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.startButton = QtWidgets.QPushButton(self.frame)
        self.startButton.setGeometry(QtCore.QRect(790, 40, 90, 50))
        self.startButton.setStyleSheet("\n"
"\n"
"QPushButton{color: rgb(0,0,0);\n"
"border-image: url(:/new/res/43.gif);\n"
"font: 25 12pt \"微软雅黑 Light\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(22, 94, 131);\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 25 12pt \"微软雅黑 Light\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"QPushButton:pressed{\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 25 12pt \"微软雅黑 Light\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"")
        self.startButton.setObjectName("startButton")
        self.lesson_namelabel = QtWidgets.QLabel(self.frame)
        self.lesson_namelabel.setGeometry(QtCore.QRect(90, 30, 581, 51))
        self.lesson_namelabel.setStyleSheet("font: 20pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.lesson_namelabel.setObjectName("lesson_namelabel")
        self.settingButton = QtWidgets.QPushButton(self.frame)
        self.settingButton.setGeometry(QtCore.QRect(1100, 40, 50, 50))
        self.settingButton.setStyleSheet("QPushButton{border-image: url(:/new/res/设置 (2).png)}QPushButton:hover{border-image: url(:/new/res/设置 (3).png)}\n"
"QPushButton:pressed{border-image: url(:/new/res/设置 (3).png)}\n"
"")
        self.settingButton.setText("")
        self.settingButton.setObjectName("settingButton")
        self.videolabel = QtWidgets.QLabel(self.frame)
        self.videolabel.setGeometry(QtCore.QRect(20, 100, 701, 591))
        self.videolabel.setStyleSheet("border-image: url(:/new/res/Rectangle 5.png);")
        self.videolabel.setText("")
        self.videolabel.setObjectName("videolabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(760, 100, 391, 591))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 255))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.endButton = QtWidgets.QPushButton(self.frame)
        self.endButton.setGeometry(QtCore.QRect(910, 40, 90, 50))
        self.endButton.setStyleSheet("\n"
"\n"
"QPushButton{color: rgb(0,0,0);\n"
"border-image: url(:/new/res/43.gif);\n"
"font: 25 12pt \"微软雅黑 Light\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(22, 94, 131);\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 25 12pt \"微软雅黑 Light\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"QPushButton:pressed{\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 25 12pt \"微软雅黑 Light\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"")
        self.endButton.setObjectName("endButton")
        self.Back_indexButton = QtWidgets.QPushButton(self.frame)
        self.Back_indexButton.setGeometry(QtCore.QRect(1030, 40, 50, 50))
        self.Back_indexButton.setStyleSheet("QPushButton{border-image: url(:/new/res/主页 (1).png)}QPushButton:hover{border-image: url(:/new/res/主页.png)}\n"
"QPushButton:pressed{border-image: url(:/new/res/主页.png)}\n"
"")
        self.Back_indexButton.setText("")
        self.Back_indexButton.setObjectName("Back_indexButton")

        self.retranslateUi(attendance)
        QtCore.QMetaObject.connectSlotsByName(attendance)

    def retranslateUi(self, attendance):
        _translate = QtCore.QCoreApplication.translate
        attendance.setWindowTitle(_translate("attendance", "Form"))
        self.startButton.setText(_translate("attendance", "开始点名"))
        self.lesson_namelabel.setText(_translate("attendance", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.settingButton.setToolTip(_translate("attendance", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">设置视频流地址</span></p></body></html>"))
        self.settingButton.setWhatsThis(_translate("attendance", "<html><head/><body><p><br/></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("attendance", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("attendance", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("attendance", "状态"))
        self.endButton.setText(_translate("attendance", "结束点名"))
        self.Back_indexButton.setToolTip(_translate("attendance", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">返回主页</span></p></body></html>"))
        self.Back_indexButton.setWhatsThis(_translate("attendance", "<html><head/><body><p><br/></p></body></html>"))

import photo_rc
