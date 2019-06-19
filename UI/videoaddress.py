# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoaddress.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Choose_Atten(object):
    def setupUi(self, Choose_Atten):
        Choose_Atten.setObjectName("Choose_Atten")
        Choose_Atten.resize(380, 264)
        Choose_Atten.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Choose_Atten)
        self.frame.setGeometry(QtCore.QRect(0, 0, 380, 264))
        self.frame.setStyleSheet("\n"
"background-color:  rgb(42, 131, 162)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ins_comBox = QtWidgets.QComboBox(self.frame)
        self.ins_comBox.setGeometry(QtCore.QRect(160, 80, 200, 25))
        self.ins_comBox.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"color:rgb(223, 223, 223)")
        self.ins_comBox.setObjectName("ins_comBox")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 80, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Adobe 黑体 Std R\";")
        self.label_2.setObjectName("label_2")
        self.les_comBox = QtWidgets.QComboBox(self.frame)
        self.les_comBox.setGeometry(QtCore.QRect(160, 130, 200, 25))
        self.les_comBox.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"color:rgb(223, 223, 223)")
        self.les_comBox.setObjectName("les_comBox")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 20, 181, 51))
        self.label.setStyleSheet("font: 14pt \"黑体\";\n"
"color: rgb(0, 255, 255);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 80, 20))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Adobe 黑体 Std R\";")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 190, 201, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.certain = QtWidgets.QPushButton(self.layoutWidget)
        self.certain.setStyleSheet("\n"
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
        self.certain.setObjectName("certain")
        self.horizontalLayout.addWidget(self.certain)
        self.back_button = QtWidgets.QPushButton(self.layoutWidget)
        self.back_button.setStyleSheet("\n"
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
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.back_button)

        self.retranslateUi(Choose_Atten)
        QtCore.QMetaObject.connectSlotsByName(Choose_Atten)

    def retranslateUi(self, Choose_Atten):
        _translate = QtCore.QCoreApplication.translate
        Choose_Atten.setWindowTitle(_translate("Choose_Atten", "Form"))
        self.label_2.setText(_translate("Choose_Atten", "开课学院"))
        self.label.setText(_translate("Choose_Atten", "选择点名课程"))
        self.label_3.setText(_translate("Choose_Atten", "开设课程"))
        self.certain.setText(_translate("Choose_Atten", "确认"))
        self.back_button.setText(_translate("Choose_Atten", "返回"))

import photo_rc
