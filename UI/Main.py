# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1010, 671)
        Main.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Main)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1011, 671))
        self.frame.setStyleSheet("\n"
"background-color:  rgb(42, 131, 162)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(350, 20, 301, 71))
        self.label.setStyleSheet("font: 18pt \"黑体\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.settingButton = QtWidgets.QPushButton(self.frame)
        self.settingButton.setGeometry(QtCore.QRect(930, 30, 50, 50))
        self.settingButton.setStyleSheet("QPushButton{border-image: url(:/new/res/设置 (2).png)}QPushButton:hover{border-image: url(:/new/res/设置 (3).png)}\n"
"QPushButton:pressed{border-image: url(:/new/res/设置 (3).png)}\n"
"")
        self.settingButton.setText("")
        self.settingButton.setObjectName("settingButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 100, 641, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("image: url(:/new/res/eye.jpg);\n"
"font: 72pt \"黑体\";")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.commandLinkButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.commandLinkButton_1.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"color: rgb(0,0,0);\n"
"border-image: url(:/new/res/43.gif);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(22, 94, 131);\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"QPushButton:pressed{\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"")
        self.commandLinkButton_1.setObjectName("commandLinkButton_1")
        self.verticalLayout_3.addWidget(self.commandLinkButton_1)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("image: url(:/new/res/camera_2.jpg);\n"
"font: 72pt \"黑体\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.commandLinkButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.commandLinkButton_3.setStyleSheet("\n"
"\n"
"QPushButton{color: rgb(0,0,0);\n"
"border-image: url(:/new/res/43.gif);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(22, 94, 131);\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"QPushButton:pressed{\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"")
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.verticalLayout_2.addWidget(self.commandLinkButton_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("image: url(:/new/res/write.jpg);\n"
"font: 72pt \"黑体\";")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.class_info_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.class_info_Button.setStyleSheet("\n"
"\n"
"QPushButton{color: rgb(0,0,0);;\n"
"border-image: url(:/new/res/43.gif);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(22, 94, 131);\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"QPushButton:pressed{\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"")
        self.class_info_Button.setObjectName("class_info_Button")
        self.verticalLayout_4.addWidget(self.class_info_Button)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("image: url(:/new/res/manifier.jpg);\n"
"font: 72pt \"黑体\";")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.commandLinkButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.commandLinkButton_2.setStyleSheet("\n"
"\n"
"QPushButton{color: rgb(0,0,0);\n"
"border-image: url(:/new/res/43.gif);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(22, 94, 131);\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"QPushButton:pressed{\n"
"border-image: url(:/new/res/46.gif);color: rgb(0, 255, 255);\n"
"font: 16pt \"黑体\";\n"
"border:2px groove gray;\n"
"border-radius:15px;\n"
"padding:4px 4px;}\n"
"")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.verticalLayout.addWidget(self.commandLinkButton_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.label.setText(_translate("Main", "人脸识别课堂点名系统"))
        self.settingButton.setToolTip(_translate("Main", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">设置视频流地址</span></p></body></html>"))
        self.settingButton.setWhatsThis(_translate("Main", "<html><head/><body><p><br/></p></body></html>"))
        self.commandLinkButton_1.setText(_translate("Main", "签到"))
        self.commandLinkButton_3.setText(_translate("Main", "人脸录入"))
        self.class_info_Button.setText(_translate("Main", "选课情况录入"))
        self.commandLinkButton_2.setText(_translate("Main", "人脸查看"))

import photo_rc
