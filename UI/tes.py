# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tes.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_get_face_UI(object):
    def setupUi(self, get_face_UI):
        get_face_UI.setObjectName("get_face_UI")
        get_face_UI.resize(948, 664)
        get_face_UI.setStyleSheet("")
        self.frame = QtWidgets.QFrame(get_face_UI)
        self.frame.setGeometry(QtCore.QRect(0, 0, 948, 664))
        self.frame.setStyleSheet("\n"
"background-color:  rgb(42, 131, 162)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.classlabel_2 = QtWidgets.QLabel(self.frame)
        self.classlabel_2.setGeometry(QtCore.QRect(670, 250, 45, 20))
        self.classlabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Adobe 黑体 Std R\";")
        self.classlabel_2.setObjectName("classlabel_2")
        self.class_comboBox = QtWidgets.QComboBox(self.frame)
        self.class_comboBox.setGeometry(QtCore.QRect(730, 320, 200, 25))
        self.class_comboBox.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"color:rgb(223, 223, 223)")
        self.class_comboBox.setObjectName("class_comboBox")
        self.namelabel = QtWidgets.QLabel(self.frame)
        self.namelabel.setGeometry(QtCore.QRect(670, 390, 45, 20))
        self.namelabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Adobe 黑体 Std R\";")
        self.namelabel.setObjectName("namelabel")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(750, 100, 120, 40))
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
        self.institute_combox = QtWidgets.QComboBox(self.frame)
        self.institute_combox.setGeometry(QtCore.QRect(730, 180, 200, 25))
        self.institute_combox.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"color:rgb(223, 223, 223)")
        self.institute_combox.setObjectName("institute_combox")
        self.stu_id_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.stu_id_lineEdit.setGeometry(QtCore.QRect(730, 460, 200, 25))
        self.stu_id_lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image:url(:/new/res/Rectangle 5.png);\n"
"font: 9pt \"Adobe Caslon Pro\";\n"
"font: 25 12pt \"微软雅黑 Light\";")
        self.stu_id_lineEdit.setObjectName("stu_id_lineEdit")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(690, 510, 221, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(self.layoutWidget)
        self.saveButton.setStyleSheet("\n"
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
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.finishButton = QtWidgets.QPushButton(self.layoutWidget)
        self.finishButton.setStyleSheet("\n"
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
        self.finishButton.setObjectName("finishButton")
        self.horizontalLayout.addWidget(self.finishButton)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(360, 20, 201, 51))
        self.label.setStyleSheet("font: 14pt \"黑体\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.classlabel_3 = QtWidgets.QLabel(self.frame)
        self.classlabel_3.setGeometry(QtCore.QRect(670, 180, 45, 20))
        self.classlabel_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Adobe 黑体 Std R\";")
        self.classlabel_3.setObjectName("classlabel_3")
        self.pro_combox = QtWidgets.QComboBox(self.frame)
        self.pro_combox.setGeometry(QtCore.QRect(730, 250, 200, 25))
        self.pro_combox.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"color:rgb(223, 223, 223)")
        self.pro_combox.setObjectName("pro_combox")
        self.classlabel = QtWidgets.QLabel(self.frame)
        self.classlabel.setGeometry(QtCore.QRect(670, 320, 45, 20))
        self.classlabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Adobe 黑体 Std R\";")
        self.classlabel.setObjectName("classlabel")
        self.stuidlabel = QtWidgets.QLabel(self.frame)
        self.stuidlabel.setGeometry(QtCore.QRect(670, 460, 45, 20))
        self.stuidlabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Adobe 黑体 Std R\";")
        self.stuidlabel.setObjectName("stuidlabel")
        self.video_label = QtWidgets.QLabel(self.frame)
        self.video_label.setGeometry(QtCore.QRect(40, 80, 621, 541))
        self.video_label.setStyleSheet("border-image: url(:/new/res/Rectangle 5.png);\n"
"background-color: rgb(255, 255, 255);")
        self.video_label.setText("")
        self.video_label.setObjectName("video_label")
        self.name_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.name_lineEdit.setGeometry(QtCore.QRect(730, 390, 200, 25))
        self.name_lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image:url(:/new/res/Rectangle 5.png);\n"
"font: 9pt \"Adobe Caslon Pro\";\n"
"font: 25 12pt \"微软雅黑 Light\";")
        self.name_lineEdit.setText("")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.settingButton = QtWidgets.QPushButton(self.frame)
        self.settingButton.setGeometry(QtCore.QRect(870, 30, 50, 50))
        self.settingButton.setStyleSheet("QPushButton{border-image: url(:/new/res/设置 (2).png)}QPushButton:hover{border-image: url(:/new/res/设置 (3).png)}\n"
"QPushButton:pressed{border-image: url(:/new/res/设置 (3).png)}\n"
"")
        self.settingButton.setText("")
        self.settingButton.setObjectName("settingButton")

        self.retranslateUi(get_face_UI)
        QtCore.QMetaObject.connectSlotsByName(get_face_UI)

    def retranslateUi(self, get_face_UI):
        _translate = QtCore.QCoreApplication.translate
        get_face_UI.setWindowTitle(_translate("get_face_UI", "Form"))
        self.classlabel_2.setText(_translate("get_face_UI", "专业"))
        self.namelabel.setText(_translate("get_face_UI", "姓名"))
        self.pushButton.setText(_translate("get_face_UI", "读取摄像头"))
        self.saveButton.setText(_translate("get_face_UI", "保存"))
        self.finishButton.setText(_translate("get_face_UI", "结束录入"))
        self.label.setText(_translate("get_face_UI", "人脸录入"))
        self.classlabel_3.setText(_translate("get_face_UI", "学院"))
        self.classlabel.setText(_translate("get_face_UI", "班级"))
        self.stuidlabel.setText(_translate("get_face_UI", "学号"))
        self.settingButton.setToolTip(_translate("get_face_UI", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">设置视频流地址</span></p></body></html>"))
        self.settingButton.setWhatsThis(_translate("get_face_UI", "<html><head/><body><p><br/></p></body></html>"))

import photo_rc
