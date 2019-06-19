# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loading.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Loading(object):
    def setupUi(self, Loading):
        Loading.setObjectName("Loading")
        Loading.resize(120, 120)
        Loading.setWindowOpacity(0.7)
        self.label = QtWidgets.QLabel(Loading)
        self.label.setGeometry(QtCore.QRect(0, 0, 120, 120))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)

    def retranslateUi(self, Loading):
        _translate = QtCore.QCoreApplication.translate
        Loading.setWindowTitle(_translate("Loading", "loading"))

import photo_rc
