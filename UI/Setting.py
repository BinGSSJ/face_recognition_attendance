# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Setting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(400, 270)
        Setting.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Setting)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 270))
        self.frame.setStyleSheet("\n"
"background-color:  rgb(42, 131, 162)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 140, 95, 35))
        self.pushButton.setStyleSheet("\n"
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
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 341, 31))
        self.label_2.setStyleSheet("color: rgb(211, 70, 0);\n"
"font: 10pt \"Adobe 黑体 Std R\";")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 80, 266, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Adobe 黑体 Std R\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image:url(:/new/res/Rectangle 5.png);\n"
"font: 9pt \"Adobe Caslon Pro\";\n"
"font: 25 12pt \"微软雅黑 Light\";")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Form"))
        self.pushButton.setText(_translate("Setting", "确定"))
        self.label_2.setText(_translate("Setting", "注:输入0代表本地摄像头(默认为本地摄像头)"))
        self.label.setText(_translate("Setting", "视频流地址"))

import photo_rc
