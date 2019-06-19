# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GET_FACE.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_get_face_UI(object):
    def setupUi(self, get_face_UI):
        get_face_UI.setObjectName("get_face_UI")
        get_face_UI.resize(920, 673)
        self.saveButton = QtWidgets.QPushButton(get_face_UI)
        self.saveButton.setGeometry(QtCore.QRect(670, 410, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.namelabel = QtWidgets.QLabel(get_face_UI)
        self.namelabel.setGeometry(QtCore.QRect(680, 210, 31, 16))
        self.namelabel.setObjectName("namelabel")
        self.name_lineEdit = QtWidgets.QLineEdit(get_face_UI)
        self.name_lineEdit.setGeometry(QtCore.QRect(730, 210, 113, 21))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.label = QtWidgets.QLabel(get_face_UI)
        self.label.setGeometry(QtCore.QRect(370, 10, 201, 81))
        self.label.setObjectName("label")
        self.classlabel = QtWidgets.QLabel(get_face_UI)
        self.classlabel.setGeometry(QtCore.QRect(680, 280, 31, 20))
        self.classlabel.setObjectName("classlabel")
        self.stu_id_lineEdit = QtWidgets.QLineEdit(get_face_UI)
        self.stu_id_lineEdit.setGeometry(QtCore.QRect(730, 350, 113, 21))
        self.stu_id_lineEdit.setObjectName("stu_id_lineEdit")
        self.stuidlabel = QtWidgets.QLabel(get_face_UI)
        self.stuidlabel.setGeometry(QtCore.QRect(680, 350, 31, 16))
        self.stuidlabel.setObjectName("stuidlabel")
        self.video_label = QtWidgets.QLabel(get_face_UI)
        self.video_label.setGeometry(QtCore.QRect(50, 70, 621, 541))
        self.video_label.setText("")
        self.video_label.setObjectName("video_label")
        self.pushButton = QtWidgets.QPushButton(get_face_UI)
        self.pushButton.setGeometry(QtCore.QRect(730, 140, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.finishButton = QtWidgets.QPushButton(get_face_UI)
        self.finishButton.setGeometry(QtCore.QRect(790, 410, 93, 28))
        self.finishButton.setObjectName("finishButton")
        self.video_label_2 = QtWidgets.QLabel(get_face_UI)
        self.video_label_2.setGeometry(QtCore.QRect(-480, -430, 711, 651))
        self.video_label_2.setText("")
        self.video_label_2.setObjectName("video_label_2")
        self.class_name_label = QtWidgets.QLabel(get_face_UI)
        self.class_name_label.setGeometry(QtCore.QRect(730, 280, 111, 21))
        self.class_name_label.setText("")
        self.class_name_label.setObjectName("class_name_label")

        self.retranslateUi(get_face_UI)
        QtCore.QMetaObject.connectSlotsByName(get_face_UI)

    def retranslateUi(self, get_face_UI):
        _translate = QtCore.QCoreApplication.translate
        get_face_UI.setWindowTitle(_translate("get_face_UI", "Form"))
        self.saveButton.setText(_translate("get_face_UI", "保存"))
        self.namelabel.setText(_translate("get_face_UI", "姓名"))
        self.label.setText(_translate("get_face_UI", "人脸录入"))
        self.classlabel.setText(_translate("get_face_UI", "班级"))
        self.stuidlabel.setText(_translate("get_face_UI", "学号"))
        self.pushButton.setText(_translate("get_face_UI", "读取摄像头"))
        self.finishButton.setText(_translate("get_face_UI", "结束录入"))

