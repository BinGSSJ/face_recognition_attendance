from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QDateTime
from UI.Loading import Ui_Loading
from PyQt5.QtWidgets import QWidget, QDialog, QApplication,QTableWidgetItem
import sys
from db import MysqlClient
from PyQt5.QtGui import QMovie,QFont,QColor,QBrush,QImage, QPixmap
from PyQt5.QtCore import Qt, QCoreApplication
from UI.attendance import Ui_attendance
from UI.videoaddress import Ui_Choose_Atten
from UI.Sel_lesson import Ui_Class
import time
from get_Face import detect_face
import cv2
import dlib
import numpy as np
import cv2
from recognition_by_features import predictor,cnn_face_detector,recognition_model,return_euclidean_distance
from config import threshold, model_dir, label_path, features_path  # 导入设置的阈值 模型 label标签路径 特征向量路径
import pandas as pd



lesson_id_list = []#课程id列表,在课程选择界面时使用
lesson_name_list = []#课程名列表
students_id_list = []#学生id列表
features_list = []#特征向量列表
status_list = []#状态列表，默认为0表示未出勤
id_name=[]#学号,姓名列表（存储的是从数据库中读取的元祖）
attendance_id = set() #出勤学生的id集合

class Video_Address(QWidget, Ui_Choose_Atten):
    def __init__(self):
        super(Video_Address, self).__init__()
        self.setupUi(self)
        self.db = MysqlClient()
        self.certain.clicked.connect(self.Cer_Btn)
        self.work = Thread_1()
        self.Choose_lesson = None
        self.work.trigger.connect(self.close_loading)
        self.loading = None
        self.stream = None

    def Cer_Btn(self):
        self.stream = self.address.text()
        if self.stream == "":
            print("未输入视频流地址")
            pass
        else:
            self.loading = Loading_UI()
            self.work.video_stream = self.stream
            self.work.start()
            self.loading.exec()

    def close_loading(self, command):
        if self.loading is not None:
            try:
                if command == "true":
                    print("视频流有效")
                    self.Choose_lesson = Class_UI()
                    self.Choose_lesson.video_str = self.stream
                    self.Choose_lesson.loading1 = Loading_UI()
                    # self.Choose_lesson.show()
                    # self.hide()
                else:
                    print("视频流无效")
                self.loading.close()
                self.Choose_lesson.work2.stream = self.stream
                self.Choose_lesson.db = self.db
                self.Choose_lesson.work2.db = self.db
                self.Choose_lesson.work2.start()
                self.hide()
                self.Choose_lesson.loading1.exec()
            except Exception as e:
                print("未知错误", e)

        else:
            pass


class Loading_UI(QDialog, Ui_Loading):
    def __init__(self):
        super(Loading_UI, self).__init__()
        self.setupUi(self)
        self.gif = QMovie('res/loading2.gif')
        self.label.setMovie(self.gif)
        self.label.setScaledContents(True)
        self.gif.start()


class Class_UI(QDialog, Ui_Class):
    def __init__(self):
        super(Class_UI, self).__init__()
        self.setupUi(self)
        self.video_str = None
        self.work2 = Thread_2()
        self.work2.sig1.connect(self.add_item)
        self.sureButton.clicked.connect(self.cer_btn_cli)
        self.loading1 = None
        self.db = None
        self.work3 = Thread_3()
        self.work3.sig3.connect(self.load_table_attendance)
        self.UI_ATTen = None

    def cer_btn_cli(self):
        print(self.comboBox_2.currentIndex())
        self.UI_ATTen = Attendance()
        self.UI_ATTen.video = self.video_str
        self.UI_ATTen.lesson_id = lesson_id_list[self.comboBox_2.currentIndex()]
        self.loading1 = Loading_UI()
        self.UI_ATTen.show()
        self.hide()
        self.work3.db = self.db
        self.work3.lesson_id = self.UI_ATTen.lesson_id
        self.work3.start()
        self.loading1.exec()

    def load_table_attendance(self, data):
        if data == "over":
            self.add_table_attendance(id_name)
            if self.loading1 is not None:
                try:
                    self.loading1.close()
                except Exception as e:
                    print("未知错误", e)

    def add_table_attendance(self, id_and_name):
        self.UI_ATTen.tableWidget.setRowCount(len(id_and_name))
        for i in range(0, len(id_and_name)):
            iditem = QTableWidgetItem(str(id_and_name[i][0]))
            iditem.setTextAlignment(Qt.AlignCenter)
            nameitem = QTableWidgetItem(str(id_and_name[i][1]))
            nameitem.setTextAlignment(Qt.AlignCenter)
            statusitem = QTableWidgetItem("未出勤")
            statusitem.setTextAlignment(Qt.AlignCenter)
            statusitem.setForeground(QBrush(QColor(255, 0, 0)))
            self.UI_ATTen.tableWidget.setItem(i, 0, iditem)
            self.UI_ATTen.tableWidget.setItem(i, 1, nameitem)
            self.UI_ATTen.tableWidget.setItem(i, 2, statusitem)

    def add_item(self, rev):
        if rev == "finish":
            self.comboBox_2.addItems(lesson_name_list)
        else:
            pass
        if self.loading1 is not None:
            try:
                self.loading1.close()
            except Exception as e:
                print("未知错误", e)
        self.show()


class Thread_1(QThread):
    '''线程1_检测视频流是否可用'''
    # 定义一个信号
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数，默认
        super(Thread_1, self).__init__()
        self.video_stream = None

    def run(self):
        time.sleep(0.5)
        try:
            cap = cv2.VideoCapture(self.video_stream)
            if cap.isOpened():
                self.trigger.emit("true")
            else:
                self.trigger.emit("false")
        except Exception as e:
            print("错误", e)
            self.trigger.emit("false")


class Thread_2(QThread):
    '''连接数据库，查询操作'''
    sig1 = pyqtSignal(str)

    def __int__(self):
        # 初始化函数，默认
        super(Thread_2, self).__init__()
        self.stream = None
        self.db = None

    def run(self):
        time.sleep(0.5)
        sqls = "select id,lesson_name from lesson where video_stream = \"%s\"" % (self.stream)
        try:
            result = self.db.search(sqls)
            if len(result) != 0:
                for item in result:
                    lesson_id_list.append(item[0])
                    lesson_name_list.append(item[1])
                self.sig1.emit("finish")  # 发送信号，传送课程名字
            else:
                self.sig1.emit("false")  # 该视频流在数据库中未有对应课程，发送失败信号
        except Exception as e:
            print("出错12", e)


class Thread_3(QThread):
    '''连接数据库，查询特征向量和对应的学号，写入全局变量列表中'''
    sig3 = pyqtSignal(str)

    def __int__(self):
        # 初始化函数，默认
        super(Thread_3, self).__init__()
        self.lesson_id = None
        self.db = None

    def run(self):
        time.sleep(0.5)
        if len(students_id_list) != 0:
            del students_id_list[:]
            del features_list[:]
            del id_name[:]
            del status_list[:]
        else:
            sql2 = "select stu_id from elective_course where lesson_id = %d" % (self.lesson_id)  # 获取选了这门课的学生学号
            b = self.db.search(sql2)
            length_b = len(b)  # 选取这门课的人数
            if length_b == 0:
                return False
            else:
                for i in b:
                    students_id_list.append(i[0])

            tm = ""
            for item in range(0, length_b - 1):
                tm = tm + "stu_id = " + str(students_id_list[item]) + " or "
            tm = tm + "stu_id = " + str(students_id_list[length_b - 1])
            sql3 = "SELECT stu_id,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65,f66,f67,f68,f69,f70," \
                   "f71,f72,f73,f74,f75,f76,f77,f78,f79,f80,f81,f82,f83,f84,f85,f86,f87,f88,f89,f90,f91,f92,f93,f94,f95,f96,f97,f98,f99,f100,f101,f102,f103,f104,f105,f106,f107,f108,f109,f110,f111,f112,f113,f114,f115,f116,f117,f118,f119,f120,f121,f122,f123,f124,f125,f126,f127,f128 FROM face_recognition.features where {0};".format(
                tm
            )
            a = self.db.search(sql3)
            if len(a) == 0:
                return False
            else:
                for item in a:
                    features_list.append(list(map(lambda x: float(x), item)))
            del students_id_list[:]
            for ites in features_list:
                students_id_list.append(int(ites[0]))
                del ites[0]
            sql4 = "select stu_id,name from students where {0}".format(tm)
            a1=self.db.search(sql4)
            for i in a1:
                status_list.append(0)
                id_name.append(i)
        self.sig3.emit("over")
        # print(students_id_list)
        # print(features_list)


class Attendance(QWidget, Ui_attendance):
    def __init__(self):
        super(Attendance, self).__init__()
        self.setupUi(self)
        self.db = None
        self.setFixedSize(self.size())
        self.timer_camera = QTimer()  # 定义定时器
        self.timer_tableWidget = QTimer()
        self.video = None  # 加载视频文件
        self.lesson_id = None  # 课程id 根据课程id查询所对应存在的学生id的特征向量
        # self.cap = cv2.VideoCapture(self.video)
        self.cap = None # 按钮关联槽函数
        self.startButton.clicked.connect(self.slotStart)
        self.endButton.clicked.connect(self.slotStop)
    def get_features(self):
        '''
        从数据库中获取该课程id所对应的上课班级，这些上课班级所对应同学的特征向量及对应同学的学号
        :return:
        '''
        # sqls = "select lesson_name,begintime,endtime from lesson where id = %d" % (self.lesson_id)
        pass

    def slotStart(self):
        """ Slot function to start the progamme
        """
        self.cap = cv2.VideoCapture(self.video)
        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.openFrame)
        self.timer_tableWidget.start(3000)
        self.timer_tableWidget.timeout.connect(self.update_tablewidget)

    def slotStop(self):
        """ Slot function to stop the programme
        """

        self.cap.release()
        self.timer_camera.stop()  # 停止计时器
        self.timer_tableWidget.stop()


    def update_tablewidget(self):
        try:
            for item in attendance_id:
                status1item = QTableWidgetItem("出勤")
                status1item.setTextAlignment(Qt.AlignCenter)
                status1item.setForeground(QBrush(QColor(0, 255, 0)))
                t = students_id_list.index(item)
                self.tableWidget.setItem(t,2,status1item)
                print("更新出勤表",t)
                #self.tableWidget.hide()
                #self.tableWidget.show()
        except Exception as e:
            print(e)

    def openFrame(self):
        """ Slot function to capture frame and process it
        """

        ret, frame = self.cap.read()
        if (self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)

                faces = detect_face(gray)
                self.faces_count = len(faces)
                if self.faces_count != 0:
                    self.pic = gray
                    self.results = faces
                    features_cap_arr = []
                    for k, d in enumerate(faces):
                        s = dlib.rectangle(d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom())
                        shape = predictor(gray, s)
                        features_cap_arr.append(recognition_model.compute_face_descriptor(gray, shape))
                        # 绘制矩形框
                        cv2.rectangle(frame, tuple([d.rect.left(), d.rect.top()]),
                                      tuple([d.rect.right(), d.rect.bottom()]), (0, 255, 255),
                                      2)

                        for i in range(len(id_name)):
                            print("with person_", str(i + 1), "the ", end='')
                            # 将某张人脸与存储的所有人脸数据进行比对
                            compare = return_euclidean_distance(features_cap_arr[k], features_list[i])
                            if compare:  # 找到了相似脸
                                attendance_id.add(id_name[i][0])
                                #print("加入到集合中",id_name[i][0])
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.videolabel.width(), self.videolabel.height())
                self.videolabel.setPixmap(QPixmap.fromImage(q_image))

            else:
                self.cap.release()
                self.timer_camera.stop()  # 停止计时器





app = QApplication(sys.argv)
a = Video_Address()
a.show()
sys.exit(app.exec_())
