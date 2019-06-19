# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'courseelect.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CourseElect(object):
    def setupUi(self, CourseElect):
        CourseElect.setObjectName("CourseElect")
        CourseElect.resize(1100, 650)
        self.frame = QtWidgets.QFrame(CourseElect)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1100, 650))
        self.frame.setStyleSheet("\n"
"background-color:  rgb(42, 131, 162)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_2.setGeometry(QtCore.QRect(710, 190, 381, 391))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("color: rgb(40, 40, 40);\n"
"QHeaderView::section{\n"
"font: 10pt \"Adobe 黑体 Std R\";\n"
"background-color:lightblue;\n"
"color: black;\n"
"padding-left: 8px;\n"
"border: 1px solid#6c6c6c;\n"
"};\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 681, 391))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 131, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 131, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 131, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 131, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 131, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 131, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 131, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 131, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 131, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(40, 40, 40);\n"
"QHeaderView::section{\n"
"font: 10pt \"Adobe 黑体 Std R\";\n"
"background-color:lightblue;\n"
"color: black;\n"
"padding-left: 8px;\n"
"border: 1px solid#6c6c6c;\n"
"};\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.Back_indexButton = QtWidgets.QPushButton(self.frame)
        self.Back_indexButton.setGeometry(QtCore.QRect(1030, 10, 50, 50))
        self.Back_indexButton.setStyleSheet("QPushButton{border-image: url(:/new/res/主页 (1).png)}QPushButton:hover{border-image: url(:/new/res/主页.png)}\n"
"QPushButton:pressed{border-image: url(:/new/res/主页.png)}\n"
"")
        self.Back_indexButton.setText("")
        self.Back_indexButton.setObjectName("Back_indexButton")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(31, 123, 401, 39))
        self.pushButton.setStyleSheet("QPushButton{color: rgb(0,0,0);\n"
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
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(84, 88, 351, 27))
        self.comboBox_2.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"color:rgb(223, 223, 223);\n"
"QComboBox::hover { color: rgb(137, 163, 178); }")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(114, 52, 321, 27))
        self.comboBox.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"color:rgb(223, 223, 223);\n"
"QComboBox::hover { color: rgb(137, 163, 178); }")
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(26, 88, 51, 31))
        self.label_2.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(26, 52, 81, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Adobe 黑体 Std R\";")
        self.label.setObjectName("label")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(769, 66, 320, 27))
        self.comboBox_3.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"color:rgb(223, 223, 223);\n"
"QComboBox::hover { color: rgb(137, 163, 178); }")
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(702, 65, 60, 25))
        self.label_3.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame)
        self.comboBox_5.setGeometry(QtCore.QRect(769, 137, 320, 27))
        self.comboBox_5.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"color:rgb(223, 223, 223);\n"
"QComboBox::hover { color: rgb(137, 163, 178); }")
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(702, 140, 60, 25))
        self.label_5.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(702, 100, 60, 25))
        self.label_4.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(769, 101, 320, 27))
        self.comboBox_4.setStyleSheet("font: 12pt \"Adobe 黑体 Std R\";\n"
"color:rgb(223, 223, 223);\n"
"QComboBox::hover { color: rgb(137, 163, 178); }")
        self.comboBox_4.setObjectName("comboBox_4")

        self.retranslateUi(CourseElect)
        QtCore.QMetaObject.connectSlotsByName(CourseElect)

    def retranslateUi(self, CourseElect):
        _translate = QtCore.QCoreApplication.translate
        CourseElect.setWindowTitle(_translate("CourseElect", "Dialog"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("CourseElect", "未选"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("CourseElect", "学号"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("CourseElect", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("CourseElect", "已选"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("CourseElect", "学号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("CourseElect", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("CourseElect", "班级"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("CourseElect", "学院"))
        self.Back_indexButton.setToolTip(_translate("CourseElect", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">返回主页</span></p></body></html>"))
        self.Back_indexButton.setWhatsThis(_translate("CourseElect", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("CourseElect", "保存"))
        self.label_2.setText(_translate("CourseElect", "课程："))
        self.label.setText(_translate("CourseElect", "开课学院："))
        self.label_3.setText(_translate("CourseElect", "学院："))
        self.label_5.setText(_translate("CourseElect", "班级："))
        self.label_4.setText(_translate("CourseElect", "专业："))

import photo_rc
