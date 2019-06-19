from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QDateTime, Qt
from PyQt5.QtGui import QMovie, QFont, QColor, QBrush, QImage, QPixmap,QIcon
from UI.Loading import Ui_Loading
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QTableWidgetItem, QMessageBox,QAbstractItemView,QHeaderView
from UI.tes import Ui_get_face_UI
from UI.attendance import Ui_attendance
from UI.videoaddress import Ui_Choose_Atten
from UI.Main import Ui_Main
from UI.Setting import Ui_Setting
from db import MysqlClient
from Generate_eigenvectors import return_features
from get_Face import detect_face, make_face_dir, check_face_num, save_image
from UI.show_face import Ui_Face_display
import cv2
import sys, time, datetime
from SFTP import SFTP
import os
import shutil  # 拷贝图片至另一个文件夹
from config import temp_dir, face_dir, video_streams
from get_Face import detect_face
import cv2
import dlib
import numpy as np
from recognition_by_features import predictor, cnn_face_detector, recognition_model, return_euclidean_distance
from config import threshold, model_dir, label_path, features_path  # 导入设置的阈值 模型 label标签路径 特征向量路径
from Selection import TreeWidget
from UI.courseelect import Ui_CourseElect

id_name = []  # 学号,姓名列表（存储的是从数据库中读取的元祖）
ins = []  # 学院编号，名称
pro = []  # 专业编号,名称
class_li = []  # 班级编号，名称
lesson_list = []  # 课程编号，名称
features_list = []  # 特征向量列表
stu = []
stu_id = []


class Main_UI(QWidget, Ui_Main):
    def __init__(self):
        super(Main_UI, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        icon = QIcon()
        icon.addPixmap(QPixmap(":/new/res/1.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.db = MysqlClient()
        self.setWindowTitle("人脸考勤系统")
        self.Collect_Fa = None
        self.Choose_Att = None
        self.work6 = Thread_6()  # 开启线程从服务器下载图片至本地
        self.work7 = None
        self.loading = None
        self.dis_Face = None
        self.select_course = None
        self.SET = None
        self.commandLinkButton_2.clicked.connect(self.com_Button_2)
        self.commandLinkButton_3.clicked.connect(self.com_Button_3)
        self.commandLinkButton_1.clicked.connect(self.com_Button_1)
        self.settingButton.clicked.connect(self.Setting_btn)
        self.class_info_Button.clicked.connect(self.choose_class)

    def com_Button_1(self):
        '''
        点击课堂点名按钮，跳转至选择课程界面
        :return:
        '''
        self.Choose_Att = Choose_Atten()
        self.Choose_Att.db = self.db
        self.Choose_Att.back2.connect(self.Show_main)
        # self.Collect_Fa.class_name_label.hide()
        # sql = "SELECT * FROM face_recognition.class; "
        self.work7 = Thread_7()
        self.work7.choice = 2
        self.work7.sig7.connect(self.update_Combox)
        self.work7.db = self.db
        self.work7.start()
        self.Choose_Att.show()
        if loading.isVisible() is False:
            loading.exec()

    def com_Button_2(self):
        '''人脸查看按钮'''
        # 从服务器下载图片至本地
        # self.work6
        # self.work6.start()

        self.dis_Face = FACE_dis()
        self.dis_Face.db = self.db
        self.dis_Face.back1.connect(self.Show_main)
        self.work7 = Thread_7()
        self.work7.choice = 0
        self.work7.sig7.connect(self.update_Combox)
        self.work7.db = self.db
        self.work7.start()
        if loading.isVisible() is False:
            loading.exec()

    def com_Button_3(self):
        '''
        人脸录入界面，该界面同时可对已经存入库的人脸进行更新。
        :return:
        '''
        self.Collect_Fa = Collect_Faces()
        self.Collect_Fa.db = self.db
        self.Collect_Fa.back2.connect(self.Show_main)
        self.work7 = Thread_7()
        self.work7.choice = 1
        self.work7.sig7.connect(self.update_Combox)
        self.work7.db = self.db
        self.work7.start()
        if loading.isVisible() is False:
            loading.exec()

    def update_Combox(self, data):
        if data == "over":
            if self.dis_Face is not None:
                for item in ins:
                    self.dis_Face.comboBox.addItem(item[1])
            if loading.isVisible():
                try:
                    loading.hide()
                except Exception as e:
                    print("未知错误", e)
            if self.dis_Face is not None:
                self.dis_Face.setWindowTitle("人脸信息查看")
                self.dis_Face.show()
                # self.dis_Face.listWidget.itemClicked(0)
                # self.dis_Face.download_pic()
        elif data == "over2":  # 人脸录入界面的查询结果
            if self.Collect_Fa is not None:
                for item in ins:
                    self.Collect_Fa.institute_combox.addItem(item[1])
            if loading.isVisible():
                try:
                    loading.hide()
                except Exception as e:
                    print("未知错误", e)
            if self.Collect_Fa is not None:
                # self.Collect_Fa.work7 = self.work7
                self.Collect_Fa.show()
                self.Collect_Fa.setWindowTitle("人脸信息录入")
            if self.dis_Face is not None:
                self.dis_Face.close()
        elif data == "over3":  # 选择点名界面的查询结果
            if self.Choose_Att is not None:
                for item in ins:
                    self.Choose_Att.ins_comBox.addItem(item[1])
            if loading.isVisible():
                try:
                    loading.hide()
                except Exception as e:
                    print("未知错误", e)
            if self.Choose_Att is not None:
                self.Choose_Att.setWindowTitle("选择课程")
                self.Choose_Att.show()
        else:
            if self.select_course is not None:
                for item in ins:
                    self.select_course.comboBox.addItem(item[1])
                    self.select_course.comboBox_3.addItem(item[1])
                self.select_course.show()
            if loading.isVisible():
                try:
                    loading.hide()
                except Exception as e:
                    print("未知错误", e)
        self.hide()

    def Show_main(self, da):
        if da == "back":
            self.show()
            if self.Collect_Fa is not None:
                self.Collect_Fa.close()
        elif da == "back3":
            self.com_Button_3()
        elif da == "back1":
            self.show()
            if self.Choose_Att is not None:
                if self.Choose_Att.Atten is not None:
                    self.Choose_Att.Atten.close()
                self.Choose_Att.close()
        elif da == "back2":
            self.show()
            if self.dis_Face is not None:
                self.dis_Face.close()
        elif da == "go_index":
            self.show()
            if self.select_course is not None:
                self.select_course.close()

    def Setting_btn(self):
        if Sett.isVisible() is False:
            Sett.lineEdit.clear()
            Sett.show()

    def choose_class(self):
        self.select_course = SELECT_COU()
        self.select_course.db = self.db
        self.select_course.backs_index.connect(self.Show_main)
        self.work7 = Thread_7()
        self.work7.choice = 3
        self.work7.sig7.connect(self.update_Combox)
        self.work7.db = self.db
        self.work7.start()
        if loading.isVisible() is False:
            loading.exec()


class Loading_UI(QDialog, Ui_Loading):
    def __init__(self):
        super(Loading_UI, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.gif = QMovie('res/loadi.gif')
        self.label.setMovie(self.gif)
        self.label.setScaledContents(True)
        self.gif.start()


class Collect_Faces(QWidget, Ui_get_face_UI):
    back2 = pyqtSignal(str)

    def __init__(self):
        super(Collect_Faces, self).__init__()
        self.setupUi(self)
        self.db = None
        icon = QIcon()
        icon.addPixmap(QPixmap(":/new/res/1.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setFixedSize(self.size())
        self.results = None  # 存储当前检测到的人脸坐标
        self.pic = None  # 存储当前截取到的照片
        self.class_id = None
        self.choice = 0  # 更新哪个下拉框
        self.loading = None  # 等待界面
        self.photo_main_path = None  # 存储班级的主路径
        self.work5 = Thread_5()  # 线程5，将学号，姓名存储到数据库
        self.work5.sftp_o = SFTP()
        self.work5.sig5.connect(self.close_loading)
        self.IF_NEW = 0  # 是否未曾录入过

        self.work8 = Thread_8()
        self.work9 = Thread_9()
        self.work10 = Thread_10()  # 10号线程用于查询该图片所对应的同学是否已已经存入到数据库中
        self.work10.sig10.connect(self.close_loading)
        self.faces_count = 0
        self.timer_camera = QTimer()  # 定义定时器
        # self.video = "http://admin:admin@172.20.10.9:8081/"  # 加载视频文件
        # self.cap = cv2.VideoCapture(self.video)
        self.cap = None
        self.pushButton.clicked.connect(self.slotStart)  # 按钮关联槽函数
        self.saveButton.clicked.connect(self.save_face_and_info)
        self.finishButton.clicked.connect(self.finish_get)
        self.institute_combox.currentIndexChanged.connect(self.update_pro)
        self.pro_combox.currentIndexChanged.connect(self.update_class)
        self.settingButton.clicked.connect(self.sett)

    def sett(self):
        if Sett.isVisible() is False:
            Sett.lineEdit.clear()
            Sett.show()

    def slotStart(self):
        """ Slot function to start the progamme
        """
        if video_streams == "0":
            video = 0
        else:
            video = video_streams
        self.cap = cv2.VideoCapture(video)
        if self.cap.isOpened() is False:
            QMessageBox.information(self, "失败", "检查视频流地址")
            return
        if self.timer_camera.isActive() is False:
            self.cap = cv2.VideoCapture(video)
            self.timer_camera.start(100)
            self.timer_camera.timeout.connect(self.openFrame)
        pass

    def slotStop(self):
        """ Slot function to stop the programme
        """
        if self.cap is not None:
            self.cap.release()
        self.timer_camera.stop()  # 停止计时器

    def msg_success(self):
        reply = QMessageBox.information(self,  # 使用infomation信息框
                                        "提示",
                                        "录入成功",
                                        QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            pass
        self.name_lineEdit.clear()
        self.stu_id_lineEdit.clear()
        if self.timer_camera.isActive() is False:
            self.slotStart()

    def msg_failed(self, data):
        message = QMessageBox.information(self, "录入失败", data, QMessageBox.Yes)
        if message == QMessageBox.Yes:
            pass
        if self.timer_camera.isActive() is False:
            self.slotStart()

    def save_face_and_info(self):
        '''保存脸部图片及学生信息
        :return:
        '''
        if self.timer_camera.isActive():
            self.slotStop()
        name = self.name_lineEdit.text()
        stu_id = self.stu_id_lineEdit.text()

        flag = 0
        if name == None:
            print("名字为空")
            flag = 1
        if stu_id == None:
            print("学号为空")
            flag = 1
        # 学号已经在数据库中
        # for i in id_name:
        #     if i[0] == stu_id:
        #         flag = 2
        stu_id = int(stu_id)
        if self.faces_count != 1:  # 检测到人脸数为0
            flag = 2

        if flag == 1:
            self.msg_failed("姓名信息不能为空")
            return
        elif flag == 2:
            self.msg_failed("未检测到人脸，或人脸数大于1")
            return
        else:
            id_name.append((stu_id, name))  # id,name 以元祖形式加入到列表中
            make_face_dir(str(class_li[self.class_comboBox.currentIndex()][0]))  # opencv不识别中文，建立以数字主键命名的文件夹，保存的照片以学号命名
            save_image(self.pic, self.results,
                       "D:/face_class/face/temp/%d/" % (class_li[self.class_comboBox.currentIndex()][0]), stu_id)
            # 建立一个缓存文件夹
            self.loading = Loading_UI()

            # 这两句话写到上个界面去，省的每次都执行

            self.work10.stu_id = stu_id
            if self.work10.db is None:
                self.work10.db = self.db
            self.work10.start()
            self.loading.exec()
            self.work5.if_exist = 0
            if self.IF_NEW == 1:  # 已经录入过，询问是否需要更新
                msg = QMessageBox.question(self, '询问', '这是一个询问消息对话框，默认是No',
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
                if msg == QMessageBox.Yes:  # 更新所填学号对应的人脸照片
                    self.work5.if_exist = 1
                    self.work5.db = self.db
                    shutil.copyfile(
                        temp_dir + "%d/%d.jpg" % (class_li[self.class_comboBox.currentIndex()][0], stu_id),
                        face_dir + "%d/%d.jpg" % (class_li[self.class_comboBox.currentIndex()][0], stu_id))
                    self.work5.stu_id = stu_id
                    self.work5.class_id = class_li[self.class_comboBox.currentIndex()][0]
                    self.work5.stu_name = name
                    self.work5.photo_path = face_dir + "%d/%d.jpg" % (
                        class_li[self.class_comboBox.currentIndex()][0], stu_id)
                    self.work5.start()
                    self.loading.exec()

                    self.msg_success()
                else:
                    print("选择不更新")
                    if self.timer_camera.isActive() is False:
                        self.slotStart()
            else:  # 未曾录入，直接存储
                self.work5.db = self.db
                shutil.copyfile(temp_dir + "%d/%d.jpg" % (class_li[self.class_comboBox.currentIndex()][0], stu_id),
                                face_dir + "%d/%d.jpg" % (class_li[self.class_comboBox.currentIndex()][0], stu_id))
                self.work5.stu_id = stu_id
                self.work5.class_id = class_li[self.class_comboBox.currentIndex()][0]
                self.work5.stu_name = name
                self.work5.photo_path = face_dir + "%d/%d.jpg" % (
                    class_li[self.class_comboBox.currentIndex()][0], stu_id)
                self.work5.start()
                self.loading.exec()

                self.msg_success()
            cv2.destroyAllWindows()

    def close_loading(self, command):
        if self.loading is not None:
            try:
                if command == "finish":
                    self.loading.close()
                elif command == "true":
                    self.IF_NEW = 0
                    self.loading.close()
                elif command == "false":  # 该学号所对应人脸已经存储过了
                    self.IF_NEW = 1
                    self.loading.close()
                else:
                    pass

            except Exception as e:
                print("未知错误", e)

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
                    for k, d in enumerate(faces):
                        # 绘制矩形框
                        cv2.rectangle(frame, tuple([d.rect.left(), d.rect.top()]),
                                      tuple([d.rect.right(), d.rect.bottom()]), (0, 255, 255),
                                      2)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.video_label.width(), self.video_label.height())
                self.video_label.setPixmap(QPixmap.fromImage(q_image))

            else:
                self.cap.release()
                self.timer_camera.stop()  # 停止计时器

    def finish_get(self):
        if self.timer_camera.isActive():
            self.slotStop()
        self.back2.emit("back")
        # self.close()

    # 关闭loading 并且添加至combox
    def close_loading2(self, da):

        if self.choice == 0:
            for i in pro:
                self.pro_combox.addItem(i[1])
        else:
            for it in class_li:
                self.class_comboBox.addItem(it[1])
        if self.isVisible() is False:
            self.show()
        if loading.isVisible():
            loading.hide()

    # 更新专业
    def update_pro(self):
        if len(pro) != 0:
            self.pro_combox.clear()
            del pro[:]
        if self.work8.db is None:
            self.work8.db = self.db
            self.work8.sig8.connect(self.close_loading2)
        self.choice = 0
        if self.work8 is not None:
            self.work8.ins_id = self.institute_combox.currentIndex()
            self.work8.start()
        if loading.isVisible() is False:
            loading.exec()

    # 更新班级
    def update_class(self):
        time.sleep(0.3)
        if len(class_li) != 0:
            self.class_comboBox.clear()
            del class_li[:]
        if self.work9.db is None:
            self.work9.db = self.db
            self.work9.sig9.connect(self.close_loading2)
        self.choice = 1
        if self.work9 is not None:
            self.work9.pro_id = pro[self.pro_combox.currentIndex()][0]
            self.work9.start()
        if loading.isVisible() is False:
            loading.exec()


class FACE_dis(QWidget, Ui_Face_display):
    back1 = pyqtSignal(str)

    def __init__(self):
        super(FACE_dis, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        icon = QIcon()
        icon.addPixmap(QPixmap(":/new/res/1.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.photo_main_path = None
        self.db = None
        self.choice = 0
        self.page = 0
        self.loading = None
        self.Collect_face = None
        self.sftp = SFTP()
        self.work6 = Thread_6()
        self.work8 = Thread_8()
        self.work9 = Thread_9()
        self.backButton.clicked.connect(self.back_main22)
        self.comboBox.currentIndexChanged.connect(self.update_pro)
        self.comboBox_2.currentIndexChanged.connect(self.update_class)
        self.listWidget.itemClicked.connect(self.download_pic)
        self.addstuButton.clicked.connect(self.add_stu)
        self.nextButton.clicked.connect(self.next_page)
        self.preButton.clicked.connect(self.pre_page)
        self.work6.sig6.connect(self.show_pic)
        self.listWidget.setStyleSheet(
            "QListWidget{color:rgb(173,175,178); background:rgb(25,27,31);border:0px solid gray;}"
            "QListWidget::Item{height:30px;border:0px solid gray;padding-left:15;}"
            "QListWidget::Item:hover{color:rgb(255,255,255);background:transparent;border:0px solid gray;}"
            "QListWidget::Item:selected{border-image:url(images/listwidget_h.png); color:rgb(255,255,255);border:0px solid gray;}"
            "QListWidget::Item:selected:active{background:#00FFFFFF;color:#FFFFFF;border-width:0;}"
        )

    def pre_page(self):
        self.page = self.page - 1
        self.SHOW()

    def next_page(self):
        self.page = self.page + 1
        self.SHOW()

    def add_stu(self):
        self.back_main("back3")

    def SHOW(self):
        if self.isVisible() is False:
            self.show()
        self.show_pic("n")

    # 更新专业
    def update_pro(self):
        if len(pro) != 0:
            self.comboBox_2.clear()
            del pro[:]
        if self.work8.db is None:
            self.work8.db = self.db
            self.work8.sig8.connect(self.close_loading)
        self.choice = 0
        if self.work8 is not None:
            self.work8.ins_id = self.comboBox.currentIndex()
            self.work8.start()
        if loading.isVisible() is False:
            loading.exec()

    def back_main(self, dad):
        self.back1.emit(dad)

    def back_main22(self):
        self.back1.emit("back2")

    # 更新班级
    def update_class(self):
        time.sleep(0.3)
        if len(class_li) != 0:
            self.listWidget.clear()
            del class_li[:]
        if self.work9.db is None:
            self.work9.db = self.db
            self.work9.sig9.connect(self.close_loading)
        self.choice = 1
        if self.work9 is not None:
            self.work9.pro_id = pro[self.comboBox_2.currentIndex()][0]
            self.work9.start()
        if loading.isVisible() is False:
            loading.exec()

    def download_pic(self):
        if len(id_name) != 0:
            del id_name[:]
        cla_id = class_li[self.listWidget.currentRow()][0]
        path = r"D:\face_class\face\%d" % (cla_id)
        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)
        if self.work6.db is None:
            self.work6.sftp_o = self.sftp
            self.work6.db = self.db
        self.work6.class_id = cla_id
        self.work6.start()
        if loading.isVisible() is False:
            loading.exec()

    def show_pic(self, d):
        num = len(id_name)
        maxpage = int(num / 9)
        self.preButton.setDisabled(False)
        self.nextButton.setDisabled(False)
        if (self.page == 0):
            self.preButton.setDisabled(True)
        if (self.page == maxpage):
            self.nextButton.setDisabled(True)
        self.widget_1.hide()
        self.widget_2.hide()
        self.widget_3.hide()
        self.widget_4.hide()
        self.widget_5.hide()
        self.widget_6.hide()
        self.widget_7.hide()
        self.widget_8.hide()
        self.widget_9.hide()

        if int((num - self.page * 9) / 9) != 0:
            self.id1.setText("%d" % (id_name[0 + self.page * 9][0]))
            self.name1.setText("%s" % (id_name[0 + self.page * 9][1]))
            self.photo_label1.setPixmap(QPixmap(
                "D:/face_class/face/%d/%d.jpg" % (
                    class_li[self.listWidget.currentRow()][0], id_name[0 + self.page * 9][0])))
            self.id2.setText("%d" % (id_name[1 + self.page * 9][0]))
            self.name2.setText("%s" % (id_name[1 + self.page * 9][1]))
            self.photo1_label2.setPixmap(QPixmap(
                "D:/face_class/face/%d/%d.jpg" % (
                    class_li[self.listWidget.currentRow()][0], id_name[1 + self.page * 9][0])))
            self.id3.setText("%d" % (id_name[2 + self.page * 9][0]))
            self.name3.setText("%s" % (id_name[2 + self.page * 9][1]))
            self.photo1_label_3.setPixmap(QPixmap(
                "D:/face_class/face/%d/%d.jpg" % (
                    class_li[self.listWidget.currentRow()][0], id_name[2 + self.page * 9][0])))
            self.id4.setText("%d" % (id_name[3 + self.page * 9][0]))
            self.name4.setText("%s" % (id_name[3 + self.page * 9][1]))
            self.photo1_label_4.setPixmap(QPixmap(
                "D:/face_class/face/%d/%d.jpg" % (
                    class_li[self.listWidget.currentRow()][0], id_name[3 + self.page * 9][0])))
            self.id5.setText("%d" % (id_name[4 + self.page * 9][0]))
            self.name5.setText("%s" % (id_name[4 + self.page * 9][1]))
            self.photo1_label_5.setPixmap(QPixmap(
                "D:/face_class/face/%d/%d.jpg" % (
                    class_li[self.listWidget.currentRow()][0], id_name[4 + self.page * 9][0])))
            self.id6.setText("%d" % (id_name[5 + self.page * 9][0]))
            self.name_6.setText("%s" % (id_name[5 + self.page * 9][1]))
            self.photo1_label_6.setPixmap(QPixmap(
                "D:/face_class/face/%d/%d.jpg" % (
                    class_li[self.listWidget.currentRow()][0], id_name[5 + self.page * 9][0])))
            self.id7.setText("%d" % (id_name[6 + self.page * 9][0]))
            self.name_7.setText("%s" % (id_name[6 + self.page * 9][1]))
            self.photo1_label_7.setPixmap(QPixmap(
                "D:/face_class/face/%d/%d.jpg" % (
                    class_li[self.listWidget.currentRow()][0], id_name[6 + self.page * 9][0])))
            self.id8.setText("%d" % (id_name[7 + self.page * 9][0]))
            self.name8.setText("%s" % (id_name[7 + self.page * 9][1]))
            self.photo1_label_8.setPixmap(QPixmap(
                "D:/face_class/face/%d/%d.jpg" % (
                    class_li[self.listWidget.currentRow()][0], id_name[7 + self.page * 9][0])))
            self.id9.setText("%d" % (id_name[8 + self.page * 9][0]))
            self.name9.setText("%s" % (id_name[8 + self.page * 9][1]))
            self.photo1_label_9.setPixmap(
                QPixmap("D:/face_class/face/%d/%d.jpg" % (
                    class_li[self.listWidget.currentRow()][0], id_name[8 + self.page * 9][0])))
            self.widget_1.show()
            self.widget_2.show()
            self.widget_3.show()
            self.widget_4.show()
            self.widget_5.show()
            self.widget_6.show()
            self.widget_7.show()
            self.widget_8.show()
            self.widget_9.show()
        else:
            if (num - self.page * 9) == 1:
                self.id1.setText("%d" % (id_name[0 + self.page * 9][0]))
                self.name1.setText("%s" % (id_name[0 + self.page * 9][1]))
                self.photo_label1.setPixmap(
                    QPixmap("D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[0 + self.page * 9][0])))
                self.widget_1.show()
            elif (num - self.page * 9) == 2:
                self.id1.setText("%d" % (id_name[0 + self.page * 9][0]))
                self.name1.setText("%s" % (id_name[0 + self.page * 9][1]))
                self.photo_label1.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[0 + self.page * 9][0])))
                self.id2.setText("%d" % (id_name[1 + self.page * 9][0]))
                self.name2.setText("%s" % (id_name[1 + self.page * 9][1]))
                self.photo1_label2.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[1 + self.page * 9][0])))
                self.widget_1.show()
                self.widget_2.show()
            elif (num - self.page * 9) == 3:
                self.id1.setText("%d" % (id_name[0 + self.page * 9][0]))
                self.name1.setText("%s" % (id_name[0 + self.page * 9][1]))
                self.photo_label1.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[0 + self.page * 9][0])))
                self.id2.setText("%d" % (id_name[1 + self.page * 9][0]))
                self.name2.setText("%s" % (id_name[1 + self.page * 9][1]))
                self.photo1_label2.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[1 + self.page * 9][0])))
                self.id3.setText("%d" % (id_name[2 + self.page * 9][0]))
                self.name3.setText("%s" % (id_name[2 + self.page * 9][1]))
                self.photo1_label_3.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[2 + self.page * 9][0])))
                self.widget_1.show()
                self.widget_2.show()
                self.widget_3.show()
            elif (num - self.page * 9) == 4:
                self.id1.setText("%d" % (id_name[0 + self.page * 9][0]))
                self.name1.setText("%s" % (id_name[0 + self.page * 9][1]))
                self.photo_label1.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[0 + self.page * 9][0])))
                self.id2.setText("%d" % (id_name[1 + self.page * 9][0]))
                self.name2.setText("%s" % (id_name[1 + self.page * 9][1]))
                self.photo1_label2.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[1 + self.page * 9][0])))
                self.id3.setText("%d" % (id_name[2 + self.page * 9][0]))
                self.name3.setText("%s" % (id_name[2 + self.page * 9][1]))
                self.photo1_label_3.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[2 + self.page * 9][0])))
                self.id4.setText("%d" % (id_name[3 + self.page * 9][0]))
                self.name4.setText("%s" % (id_name[3 + self.page * 9][1]))
                self.photo1_label_4.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[3 + self.page * 9][0])))
                self.widget_1.show()
                self.widget_2.show()
                self.widget_3.show()
                self.widget_4.show()
            elif (num - self.page * 9) == 5:
                self.id1.setText("%d" % (id_name[0 + self.page * 9][0]))
                self.name1.setText("%s" % (id_name[0 + self.page * 9][1]))
                self.photo_label1.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[0 + self.page * 9][0])))
                self.id2.setText("%d" % (id_name[1 + self.page * 9][0]))
                self.name2.setText("%s" % (id_name[1 + self.page * 9][1]))
                self.photo1_label2.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[1 + self.page * 9][0])))
                self.id3.setText("%d" % (id_name[2 + self.page * 9][0]))
                self.name3.setText("%s" % (id_name[2 + self.page * 9][1]))
                self.photo1_label_3.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[2 + self.page * 9][0])))
                self.id4.setText("%d" % (id_name[3 + self.page * 9][0]))
                self.name4.setText("%s" % (id_name[3 + self.page * 9][1]))
                self.photo1_label_4.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[3 + self.page * 9][0])))
                self.id5.setText("%d" % (id_name[4 + self.page * 9][0]))
                self.name5.setText("%s" % (id_name[4 + self.page * 9][1]))
                self.photo1_label_5.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[4 + self.page * 9][0])))
                self.widget_1.show()
                self.widget_2.show()
                self.widget_3.show()
                self.widget_4.show()
                self.widget_5.show()
            elif (num - self.page * 9) == 6:
                self.id1.setText("%d" % (id_name[0 + self.page * 9][0]))
                self.name1.setText("%s" % (id_name[0 + self.page * 9][1]))
                self.photo_label1.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[0 + self.page * 9][0])))
                self.id2.setText("%d" % (id_name[1 + self.page * 9][0]))
                self.name2.setText("%s" % (id_name[1 + self.page * 9][1]))
                self.photo1_label2.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[1 + self.page * 9][0])))
                self.id3.setText("%d" % (id_name[2 + self.page * 9][0]))
                self.name3.setText("%s" % (id_name[2 + self.page * 9][1]))
                self.photo1_label_3.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[2 + self.page * 9][0])))
                self.id4.setText("%d" % (id_name[3 + self.page * 9][0]))
                self.name4.setText("%s" % (id_name[3 + self.page * 9][1]))
                self.photo1_label_4.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[3 + self.page * 9][0])))
                self.id5.setText("%d" % (id_name[4 + self.page * 9][0]))
                self.name5.setText("%s" % (id_name[4 + self.page * 9][1]))
                self.photo1_label_5.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[4 + self.page * 9][0])))
                self.id6.setText("%d" % (id_name[5 + self.page * 9][0]))
                self.name_6.setText("%s" % (id_name[5 + self.page * 9][1]))
                self.photo1_label_6.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[5 + self.page * 9][0])))
                self.widget_1.show()
                self.widget_2.show()
                self.widget_3.show()
                self.widget_4.show()
                self.widget_5.show()
                self.widget_6.show()
            elif (num - self.page * 9) == 7:
                self.id1.setText("%d" % (id_name[0 + self.page * 9][0]))
                self.name1.setText("%s" % (id_name[0 + self.page * 9][1]))
                self.photo_label1.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[0 + self.page * 9][0])))
                self.id2.setText("%d" % (id_name[1 + self.page * 9][0]))
                self.name2.setText("%s" % (id_name[1 + self.page * 9][1]))
                self.photo1_label2.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[1 + self.page * 9][0])))
                self.id3.setText("%d" % (id_name[2 + self.page * 9][0]))
                self.name3.setText("%s" % (id_name[2 + self.page * 9][1]))
                self.photo1_label_3.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[2 + self.page * 9][0])))
                self.id4.setText("%d" % (id_name[3 + self.page * 9][0]))
                self.name4.setText("%s" % (id_name[3 + self.page * 9][1]))
                self.photo1_label_4.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[3 + self.page * 9][0])))
                self.id5.setText("%d" % (id_name[4 + self.page * 9][0]))
                self.name5.setText("%s" % (id_name[4 + self.page * 9][1]))
                self.photo1_label_5.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[4 + self.page * 9][0])))
                self.id6.setText("%d" % (id_name[5 + self.page * 9][0]))
                self.name_6.setText("%s" % (id_name[5 + self.page * 9][1]))
                self.photo1_label_6.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[5 + self.page * 9][0])))
                self.id7.setText("%d" % (id_name[6 + self.page * 9][0]))
                self.name_7.setText("%s" % (id_name[6 + self.page * 9][1]))
                self.photo1_label_7.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[6 + self.page * 9][0])))
                self.widget_1.show()
                self.widget_2.show()
                self.widget_3.show()
                self.widget_4.show()
                self.widget_5.show()
                self.widget_6.show()
                self.widget_7.show()
            elif (num - self.page * 9) == 8:
                self.id1.setText("%d" % (id_name[0 + self.page * 9][0]))
                self.name1.setText("%s" % (id_name[0 + self.page * 9][1]))
                self.photo_label1.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[0 + self.page * 9][0])))
                self.id2.setText("%d" % (id_name[1 + self.page * 9][0]))
                self.name2.setText("%s" % (id_name[1 + self.page * 9][1]))
                self.photo1_label2.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[1 + self.page * 9][0])))
                self.id3.setText("%d" % (id_name[2 + self.page * 9][0]))
                self.name3.setText("%s" % (id_name[2 + self.page * 9][1]))
                self.photo1_label_3.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[2 + self.page * 9][0])))
                self.id4.setText("%d" % (id_name[3 + self.page * 9][0]))
                self.name4.setText("%s" % (id_name[3 + self.page * 9][1]))
                self.photo1_label_4.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[3 + self.page * 9][0])))
                self.id5.setText("%d" % (id_name[4 + self.page * 9][0]))
                self.name5.setText("%s" % (id_name[4 + self.page * 9][1]))
                self.photo1_label_5.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[4 + self.page * 9][0])))
                self.id6.setText("%d" % (id_name[5 + self.page * 9][0]))
                self.name_6.setText("%s" % (id_name[5 + self.page * 9][1]))
                self.photo1_label_6.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[5 + self.page * 9][0])))
                self.id7.setText("%d" % (id_name[6 + self.page * 9][0]))
                self.name_7.setText("%s" % (id_name[6 + self.page * 9][1]))
                self.photo1_label_7.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[6 + self.page * 9][0])))
                self.id8.setText("%d" % (id_name[7 + self.page * 9][0]))
                self.name8.setText("%s" % (id_name[7 + self.page * 9][1]))
                self.photo1_label_8.setPixmap(QPixmap(
                    "D:/face_class/face/%d/%d.jpg" % (
                        class_li[self.listWidget.currentRow()][0], id_name[7 + self.page * 9][0])))
                self.widget_1.show()
                self.widget_2.show()
                self.widget_3.show()
                self.widget_4.show()
                self.widget_5.show()
                self.widget_6.show()
                self.widget_7.show()
                self.widget_8.show()

        if loading.isVisible:
            loading.hide()

    def close_loading(self, da):

        if self.choice == 0:
            for i in pro:
                self.comboBox_2.addItem(i[1])
        else:
            for it in class_li:
                self.listWidget.addItem(it[1])
        if self.isVisible() is False:
            self.show()
        if loading.isVisible():
            loading.hide()


class Choose_Atten(QWidget, Ui_Choose_Atten):
    back2 = pyqtSignal(str)

    def __init__(self):
        super(Choose_Atten, self).__init__()
        self.setupUi(self)
        self.db = None
        icon = QIcon()
        icon.addPixmap(QPixmap(":/new/res/1.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setFixedSize(self.size())
        self.certain.clicked.connect(self.Cer_Btn)
        self.work4 = Thread_4()
        self.work3 = Thread_3()
        self.loading = None
        self.Atten = None
        self.ins_comBox.currentIndexChanged.connect(self.update_lesson)
        self.back_button.clicked.connect(self.Back_Btn)

    # 关闭loading 并且添加至combox
    def close_loading2(self, da):
        for it in lesson_list:
            self.les_comBox.addItem(it[1])
        if self.isVisible() is False:
            self.show()
        if loading.isVisible():
            loading.hide()

    # 更新课程
    def update_lesson(self):
        if len(lesson_list) != 0:
            self.les_comBox.clear()
            del lesson_list[:]
        if self.work4.db is None:
            self.work4.db = self.db
            self.work4.sig4.connect(self.close_loading2)
        if self.work4 is not None:
            self.work4.ins_id = ins[self.ins_comBox.currentIndex()][0]
            self.work4.start()
        if loading.isVisible() is False:
            loading.exec()

    # 跳转到出勤界面
    def go_to_Attendance(self, da):
        if self.Atten is None:
            self.Atten = Attendance()
        self.Atten.back_index.connect(self.Back_Btn)
        self.Atten.initiate_tablewidget()
        self.Atten.lesson_namelabel.setText(lesson_list[self.les_comBox.currentIndex()][1])
        self.hide()
        self.Atten.setWindowTitle("%s 考勤" % (lesson_list[self.les_comBox.currentIndex()][1]))
        self.Atten.show()
        if loading.isVisible():
            loading.hide()

    def Cer_Btn(self):
        if self.work3.db is None:
            self.work3.db = self.db
        self.work3.lesson_id = lesson_list[self.les_comBox.currentIndex()][0]
        self.work3.sig3.connect(self.go_to_Attendance)
        self.work3.start()
        if loading.isVisible() is False:
            loading.exec()

    def Back_Btn(self):
        self.back2.emit("back1")


class Attendance(QWidget, Ui_attendance):
    back_index = pyqtSignal()

    def __init__(self):
        super(Attendance, self).__init__()
        self.setupUi(self)
        self.db = None
        icon = QIcon()
        icon.addPixmap(QPixmap(":/new/res/1.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setFixedSize(self.size())
        self.attendance_id = set()  # 出勤的学生id
        self.setFixedSize(self.size())
        self.timer_camera = QTimer()  # 定义定时器
        self.timer_tableWidget = QTimer()
        self.video = "http://admin:admin@172.20.10.9:8081/"  # 加载视频文件
        self.lesson_id = None  # 课程id 根据课程id查询所对应存在的学生id的特征向量
        self.work1 = Thread_1()
        self.cap = None  # 按钮关联槽函数
        self.startButton.clicked.connect(self.slotStart)
        self.endButton.clicked.connect(self.slotStop)
        self.Back_indexButton.clicked.connect(self.Back_bbtn)
        self.settingButton.clicked.connect(self.sett)

    def sett(self):
        if Sett.isVisible() is False:
            Sett.lineEdit.clear()
            Sett.show()

    def slotStart(self):
        """ Slot function to start the progamme
        """
        if video_streams == "0":
            video = 0
        else:
            video = video_streams
        self.cap = cv2.VideoCapture(video)
        if self.cap.isOpened() is False:
            QMessageBox.information(self, "失败", "检查视频流地址")
            return
        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.openFrame)
        self.timer_tableWidget.start(1500)
        self.timer_tableWidget.timeout.connect(self.update_tablewidget)

    def slotStop(self):
        """ Slot function to stop the programme
        """
        if self.cap is not None:
            self.cap.release()
        if self.timer_camera.isActive() is True:
            self.timer_camera.stop()  # 停止计时器
            self.timer_tableWidget.stop()
            QMessageBox.information(self, "点名结束", "应到%d人  实到%d人" % (len(id_name), len(self.attendance_id)))
            print(self.attendance_id)
        else:
            QMessageBox.warning(self, "警告", "还未开始点名，请点击开始点名按钮")

    def Back_bbtn(self):
        self.back_index.emit()

    def initiate_tablewidget(self):
        self.tableWidget.setRowCount(len(id_name))
        for i in range(0, len(id_name)):
            iditem = QTableWidgetItem(str(id_name[i][0]))
            iditem.setForeground(QBrush(QColor(245, 245, 245)))
            iditem.setTextAlignment(Qt.AlignCenter)
            nameitem = QTableWidgetItem(str(id_name[i][1]))
            nameitem.setForeground(QBrush(QColor(245, 245, 245)))
            nameitem.setTextAlignment(Qt.AlignCenter)
            statusitem = QTableWidgetItem("未出勤")
            statusitem.setTextAlignment(Qt.AlignCenter)
            statusitem.setForeground(QBrush(QColor(255, 0, 0)))
            self.tableWidget.setItem(i, 0, iditem)
            self.tableWidget.setItem(i, 1, nameitem)
            self.tableWidget.setItem(i, 2, statusitem)

    def update_tablewidget(self):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        try:
            for item in self.attendance_id:
                status1item = QTableWidgetItem("出勤")
                status1item.setTextAlignment(Qt.AlignCenter)
                status1item.setForeground(QBrush(QColor(0, 255, 0)))
                t = self.find_index(id_name, item)
                self.tableWidget.setItem(t, 2, status1item)
                print("更新出勤表", t)
        except Exception as e:
            print(e)

    def find_index(self, li, i):
        for it in range(0, len(li)):
            if li[it][0] == i:
                print(it)
                return it

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
                            print("with person_", id_name[i], "the ", end='')
                            # 将某张人脸与存储的所有人脸数据进行比对
                            compare = return_euclidean_distance(features_cap_arr[k], features_list[i])
                            if compare:  # 找到了相似脸
                                self.attendance_id.add(id_name[i][0])
                                # print("加入到集合中",id_name[i][0])
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.videolabel.width(), self.videolabel.height())
                self.videolabel.setPixmap(QPixmap.fromImage(q_image))

            else:
                self.cap.release()
                self.timer_camera.stop()  # 停止计时器


class Setting(QWidget, Ui_Setting):
    def __init__(self):
        super(Setting, self).__init__()
        self.setupUi(self)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/new/res/1.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.work1 = Thread_1()
        self.setWindowTitle("视频流地址设置")
        self.work1.trigger.connect(self.change_video)
        self.pushButton.clicked.connect(self.test_video)

    def change_video(self, d):
        if d == "true":
            if loading.isVisible():
                loading.hide()
            QMessageBox.information(self, "成功", "更改视频地址成功")
            global video_streams
            video_streams = self.lineEdit.text()
            self.hide()
        else:
            if loading.isVisible():
                loading.hide()
            QMessageBox.information(self, "失败", "地址不可用")

    def test_video(self):
        self.work1.video_stream = self.lineEdit.text()
        self.work1.start()
        # 开始测试
        loading.exec()


class SELECT_COU(QWidget, Ui_CourseElect):
    backs_index = pyqtSignal(str)
    sss = pyqtSignal(str)

    def __init__(self):
        super(SELECT_COU, self).__init__()
        self.setupUi(self)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/new/res/1.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.db = None
        self.db2 = MysqlClient()
        self.times = 0
        self.flag = 0
        self.work4 = Thread_4()
        self.work8 = Thread_8()
        self.work9 = Thread_9()
        self.work11 = Thread_11()
        self.work12 = Thread_12()
        self.work13 = Thread_13()
        self.Back_indexButton.clicked.connect(self.back_main)
        self.comboBox.currentIndexChanged.connect(self.update_lesson)
        self.sss.connect(self.set_connect)
        self.pushButton.clicked.connect(self.update_all_sql)

    def back_main(self):
        self.backs_index.emit("go_index")

    # 更新课程下拉框
    def close_loading2(self, da):
        for it in lesson_list:
            self.comboBox_2.addItem(it[1])
        if self.times == 0:
            self.times += 1
            self.sss.emit("1")

        if self.isVisible() is False:
            self.show()
        if loading.isVisible():
            loading.hide()

    # 更新专业下拉框
    def close_loading(self, da):
        for it in pro:
            self.comboBox_4.addItem(it[1])
        if self.isVisible() is False:
            self.show()
        if self.times == 2:
            self.times += 1
            self.sss.emit("3")
        if loading.isVisible():
            loading.hide()

    # 更新班级下拉框
    def close_loading3(self, da):
        for it in class_li:
            self.comboBox_5.addItem(it[1])
        if self.isVisible() is False:
            self.show()
        if self.times == 3:
            self.sss.emit("4")
            self.times += 1
        if loading.isVisible():
            loading.hide()

    def set_connect(self, da):
        if da == "1":
            self.comboBox_2.currentIndexChanged.connect(self.update_students)
            self.update_students()
        elif da == "2":
            self.comboBox_3.currentIndexChanged.connect(self.update_pro)
            self.update_pro()
        elif da == "3":
            self.comboBox_4.currentIndexChanged.connect(self.update_class)
            self.update_class()
        else:
            self.comboBox_5.currentIndexChanged.connect(self.update_no_students)
            self.update_no_students()

    def close_loading4(self, da):
        num_selected = self.tableWidget.rowCount()
        for i in range(num_selected):
            self.tableWidget.removeRow(0)
        i = 0
        for item in stu:
            a = QTableWidgetItem(str(stu[i][0]))
            b = QTableWidgetItem(stu[i][1])
            c = QTableWidgetItem(stu[i][2])
            d = QTableWidgetItem(stu[i][3])

            self.tableWidget.insertRow(i)
            checkBox = QTableWidgetItem("")  # 设置单选框为选中
            checkBox.setCheckState(Qt.Checked)
            self.tableWidget.setItem(i, 0, checkBox)
            self.tableWidget.setItem(i, 1, a)
            self.tableWidget.setItem(i, 2, b)
            self.tableWidget.setItem(i, 3, c)
            self.tableWidget.setItem(i, 4, d)
            i += 1
        if self.times == 1:
            self.times += 1
            self.sss.emit("2")
        if self.flag == 1:
            self.update_no_students()
            self.flag =0
        if loading.isVisible():
            loading.hide()

    def close_loading5(self, da):
        num_selecting = self.tableWidget_2.rowCount()
        for i in range(num_selecting):
            self.tableWidget_2.removeRow(0)
        i = 0
        for item in id_name:
            a = QTableWidgetItem(str(item[0]))
            b = QTableWidgetItem(item[1])
            self.tableWidget_2.insertRow(i)
            checkBox = QTableWidgetItem("")
            checkBox.setCheckState(Qt.Unchecked)  # 设置单选框为未选中
            self.tableWidget_2.setItem(i, 0, checkBox)
            self.tableWidget_2.setItem(i, 1, a)
            self.tableWidget_2.setItem(i, 2, b)
            i += 1
        if loading.isVisible():
            loading.hide()
    def close_loading6(self, da):
        if loading.isVisible():
            loading.hide()
        QMessageBox.information(self,"提示","更新课程信息成功")
        self.flag=1
        self.update_students()


    # 更新课程
    def update_lesson(self):
        if len(lesson_list) != 0:
            self.comboBox_2.clear()
            del lesson_list[:]
        if self.work4.db is None:
            self.work4.db = self.db
            self.work4.sig4.connect(self.close_loading2)
        if self.work4 is not None:
            self.work4.ins_id = ins[self.comboBox.currentIndex()][0]
            self.work4.start()
        if loading.isVisible() is False:
            loading.exec()

    def update_pro(self):
        if len(pro) != 0:
            self.comboBox_4.clear()
            del pro[:]
        if self.work8.db is None:
            self.work8.db = self.db
            self.work8.sig8.connect(self.close_loading)
        if self.work8 is not None:
            self.work8.ins_id = self.comboBox_3.currentIndex()
            self.work8.start()
        if loading.isVisible() is False:
            loading.exec()

    def update_class(self):
        time.sleep(0.1)
        if len(class_li) != 0:
            self.comboBox_5.clear()
            del class_li[:]
        if self.work9.db is None:
            self.work9.db = self.db
            self.work9.sig9.connect(self.close_loading3)
        if self.work9 is not None:
            self.work9.pro_id = pro[self.comboBox_4.currentIndex()][0]
            self.work9.start()
        if loading.isVisible() is False:
            loading.exec()

    # 填充已选学生
    def update_students(self):
        if len(stu) != 0:
            num_selected = self.tableWidget.rowCount()
            for i in range(num_selected):
                self.tableWidget.removeRow(0)
            del stu[:]
            del stu_id[:]
        if self.work11.db is None:
            self.work11.db = self.db
            self.work11.sig11.connect(self.close_loading4)
        if self.work11 is not None:
            self.work11.lesson_id = lesson_list[self.comboBox_2.currentIndex()][0]
            self.work11.start()
        if loading.isVisible() is False:
            loading.exec()

    def update_no_students(self):
        if len(stu_id) == 0:
            self.update_students()
        if len(id_name) != 0:
            num_selecting = self.tableWidget_2.rowCount()
            for i in range(num_selecting):
                self.tableWidget_2.removeRow(0)
            del id_name[:]
        if self.work12.db is None:
            self.work12.db = self.db2
            self.work12.sig12.connect(self.close_loading5)
        if self.work12 is not None:
            self.work12.class_name = self.comboBox_5.currentText()
            self.work12.start()
        if loading.isVisible() is False:
            loading.exec()

    def update_all_sql(self):
        a = []
        b = []
        for i in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(i, 0).checkState() == Qt.Unchecked:
                a.append(self.tableWidget.item(i, 1).text())
        for i in range(self.tableWidget_2.rowCount()):
            if self.tableWidget_2.item(i, 0).checkState() == Qt.Checked:
                b.append((lesson_list[self.comboBox_2.currentIndex()][0], class_li[self.comboBox_5.currentIndex()][0],
                          self.tableWidget_2.item(i, 1).text()))
        if len(a) > 0:
            sql1 = "delete from elective_course where lesson_id = %d and (stu_id = " % (
            lesson_list[self.comboBox_2.currentIndex()][0])
            for i in range(len(a) - 1):
                sql1 = sql1 + a[i] + " or stu_id = "
            sql1 = sql1 + a[-1] + " );"
        else:
            sql1 = "no_del"
        if len(b) > 0:
            sql2 = "insert into elective_course (lesson_id, class_id, stu_id) VALUES (%s, %s, %s)"
        else:
            sql2 = "no_insert"
        print(sql1)
        print(sql2)
        if self.work13.db is None:
            self.work13.db = self.db
            self.work13.sig13.connect(self.close_loading6)
        if self.work11 is not None:
            self.work13.sql1 = sql1
            self.work13.sql2 = sql2
            self.work13.values = b
            self.work13.start()
        if loading.isVisible() is False:
            loading.exec()


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
            if self.video_stream == "0":
                self.video_stream = 0
            cap = cv2.VideoCapture(self.video_stream)
            if cap.isOpened() is True:
                self.trigger.emit("true")
            else:
                self.trigger.emit("false")
        except Exception as e:
            print("错误", e)
            self.trigger.emit("false")


class Thread_3(QThread):
    '''连接数据库，查询特征向量和课程所选学生的学号，写入全局变量列表中'''
    sig3 = pyqtSignal(str)
    db = None

    def __int__(self):
        # 初始化函数，默认
        super(Thread_3, self).__init__()
        self.lesson_id = None

    def run(self):
        time.sleep(0.5)
        if len(id_name) != 0:
            del id_name[:]
            del features_list[:]

        sql2 = "select elective_course.stu_id,students.name from elective_course,students where elective_course.lesson_id =%d and elective_course.stu_id=students.stu_id order by students.stu_id asc;" % (
            self.lesson_id)  # 获取选了这门课的学生学号
        for item1 in self.db.search(sql2):
            id_name.append(item1)
        tm = ""
        for item in range(0, len(id_name) - 1):
            tm = tm + "stu_id = " + str(id_name[item][0]) + " or "
        tm = tm + "stu_id = " + str(id_name[-1][0]) + " order by features.stu_id asc"
        # print(tm)
        sql3 = "SELECT f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65,f66,f67,f68,f69,f70," \
               "f71,f72,f73,f74,f75,f76,f77,f78,f79,f80,f81,f82,f83,f84,f85,f86,f87,f88,f89,f90,f91,f92,f93,f94,f95,f96,f97,f98,f99,f100,f101,f102,f103,f104,f105,f106,f107,f108,f109,f110,f111,f112,f113,f114,f115,f116,f117,f118,f119,f120,f121,f122,f123,f124,f125,f126,f127,f128 FROM face_recognition.features where {0};".format(
            tm
        )
        for item in self.db.search(sql3):
            features_list.append(list(map(lambda x: float(x), item)))
        self.sig3.emit("get_features")


class Thread_4(QThread):
    '''线程4 通过学院查找开设的课程'''
    sig4 = pyqtSignal(str)
    db = None

    def __int__(self):
        # 初始化函数，默认
        super(Thread_4, self).__init__()
        self.ins_id = 1

    def run(self):
        sql = "select * from face_recognition.lesson where ins_id=%d;" % (self.ins_id)
        a = self.db.search(sql)
        for item in a:
            lesson_list.append(item)
        self.sig4.emit("search_over")
        # print(students_id_list)
        # print(features_list)


class Thread_5(QThread):
    '''线程5，将学号姓名信息以及生成人脸特征向量存入数据库'''
    sig5 = pyqtSignal(str)
    sftp_o = None
    if_exist = 0  # 是否已经存在，存在即删除重新插入，否则直接插入

    def __int__(self):
        # 初始化函数，默认
        super(Thread_5, self).__init__()
        self.stu_id = None
        self.db = None
        self.stu_name = None
        self.class_id = None
        self.photo_path = None

    def run(self):
        time.sleep(0.1)
        # 删除已经存在的学生信息
        if self.if_exist == 1:
            sql_de1 = "DELETE FROM face_recognition.students WHERE (stu_id = %d);" % (self.stu_id)
            sql_de2 = "DELETE FROM face_recognition.features WHERE (stu_id = %d);" % (self.stu_id)
            self.db.execute(sql_de1)
            self.db.execute(sql_de2)
        # 插入新信息
        sql2 = "INSERT INTO students values (%d,\"%s\",%d)" % (self.stu_id, self.stu_name, self.class_id)
        self.db.execute(sql2)
        a = list(return_features(self.photo_path))
        a.insert(0, self.class_id)  # 插入class_id
        a.insert(0, self.stu_id)  # 插入stu_id
        # 存储特征向量
        sql3 = "insert into features(stu_id,class_id,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,f31,f32,f33,f34,f35,f36,f37,f38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65,f66,f67,f68,f69,f70,f71,f72,f73,f74,f75,f76,f77,f78,f79,f80,f81,f82,f83,f84,f85,f86,f87,f88,f89,f90,f91,f92,f93,f94,f95,f96,f97,f98,f99,f100,f101,f102,f103,f104,f105,f106,f107,f108,f109,f110,f111,f112,f113,f114,f115,f116,f117,f118,f119,f120,f121,f122,f123,f124,f125,f126,f127,f128) values {0}".format(
            tuple(a))
        self.db.execute(sql3)
        print("执行sql")
        self.sftp_o.up_load_dir(self.class_id, self.class_id)
        print("执行up")
        self.sig5.emit("finish")


class Thread_6(QThread):
    '''线程6，查询班级学生学号、从服务器拷贝图片'''
    sig6 = pyqtSignal(str)
    db = None
    class_id = None
    sftp_o = None

    def __int__(self):
        # 初始化函数，默认
        super(Thread_6, self).__init__()

    def run(self):
        sql_stu = "SELECT stu_id,name FROM face_recognition.students where class_id = %d" % (self.class_id)
        for item in self.db.search(sql_stu):
            id_name.append(item)
        flag = 0
        if os.path.exists("D:/face_class/face/%d/time.txt" % (self.class_id)):
            remote_time = self.sftp_o.get_change_time(self.class_id)
            with open("D:/face_class/face/%d/time.txt" % (self.class_id)) as f:
                tmp = f.read()
            if tmp == remote_time:
                flag = 1
        if flag == 0:  # 0，从服务器下载图片至本地
            self.sftp_o.down_load_dir(self.class_id, self.class_id)

        # self.sftp_o.down_load_dir
        self.sig6.emit("ok")


class Thread_7(QThread):
    '''线程7，查询数据库中的学院信息'''
    sig7 = pyqtSignal(str)  # 对应主界面

    def __int__(self):
        # 初始化函数，默认
        super(Thread_7, self).__init__()
        self.db = None
        self.ins_id = None
        self.choice = 0

    def run(self):
        if len(ins) != 0:
            del ins[:]
        sql1 = "SELECT * FROM face_recognition.institute;"
        for item in self.db.search(sql1):
            ins.append(item)
        if self.choice == 0:
            self.sig7.emit("over")
        elif self.choice == 1:
            self.sig7.emit("over2")
        elif self.choice == 2:
            self.sig7.emit("over3")
        else:
            self.sig7.emit("over4")


class Thread_8(QThread):
    '''线程8，查询数据库通过学院查找专业'''
    sig8 = pyqtSignal(str)  # 对应显示人脸界面
    db = None
    ins_id = None

    def __int__(self):
        # 初始化函数，默认
        super(Thread_8, self).__init__()

    def run(self):
        sql_pro = "SELECT id,name FROM face_recognition.profession where ins_id = %d" % (ins[self.ins_id][0])
        print(sql_pro)
        b = self.db.search(sql_pro)
        for item in b:
            pro.append(item)
        self.sig8.emit("ok")
        # print("发出信号")


class Thread_9(QThread):
    '''线程9，查询数据库,通过专业查找班级'''
    sig9 = pyqtSignal(str)  # 对应显示人脸界面
    db = None
    pro_id = None

    def __int__(self):
        # 初始化函数，默认
        super(Thread_9, self).__init__()

    def run(self):
        sql_class = "SELECT id,cla_name FROM face_recognition.class where pro_id = %d" % (self.pro_id)
        c = self.db.search(sql_class)
        for item in c:
            class_li.append(item)
        self.sig9.emit("ok")
        # print("发出信号,更新班级")


class Thread_10(QThread):
    '''线程10，查询输入的学生学号是否已经存在'''
    sig10 = pyqtSignal(str)  # 对应录入人脸界面
    db = None

    # pro_id = None

    def __int__(self):
        # 初始化函数，默认
        super(Thread_10, self).__init__()
        self.stu_id = None

    def run(self):
        sqlsss = "select count(idfeatures) from face_recognition.features where stu_id=%d;" % (self.stu_id)
        resu = self.db.search(sqlsss)
        if resu[0][0] == 0:
            self.sig10.emit("true")
        else:
            self.sig10.emit("false")


class Thread_11(QThread):
    '''连接数据库，查询课程所选学生的学号，写入全局变量列表中'''
    sig11 = pyqtSignal(str)
    db = None

    def __int__(self):
        # 初始化函数，默认
        super(Thread_11, self).__init__()
        self.lesson_id = None

    def run(self):
        sql_stu = "SELECT students.stu_id,students.name,cla_name,institute.name \
                    FROM students,class,elective_course,institute,lesson\
                    where elective_course.stu_id = students.stu_id AND \
                           elective_course.class_id = class.id AND \
                           elective_course.lesson_id = lesson.id AND \
                           class.ins_id = institute.id AND\
                           lesson_id = '%s'" % (self.lesson_id)
        for item in self.db.search(sql_stu):
            stu.append(item)
            stu_id.append(item[0])
        self.sig11.emit("oo")


class Thread_12(QThread):
    '''连接数据库，查询课程未选学生的学号，写入全局变量列表中'''
    sig12 = pyqtSignal(str)
    db = None

    def __int__(self):
        # 初始化函数，默认
        super(Thread_12, self).__init__()
        self.class_name = None

    def run(self):
        sql_stu = "SELECT stu_id,students.name \
                  FROM students,class\
                  where class_id = class.id AND cla_name = '%s'" % (self.class_name)
        for item in self.db.search(sql_stu):
            if item[0] not in stu_id:
                id_name.append(item)
        self.sig12.emit("oo")


class Thread_13(QThread):
    '''更新数据库'''
    sig13 = pyqtSignal(str)
    db = None
    sql1 = None
    sql2 = None
    values = None

    def __int__(self):
        # 初始化函数，默认
        super(Thread_13, self).__init__()

    def run(self):
        if self.sql1=="no_del":
            pass
        else:
            self.db.execute(self.sql1)
        if self.sql2=="no_insert":
            pass
        else:
            self.db.execute_many(self.sql2,self.values)
        self.sig13.emit("oo")


app = QApplication(sys.argv)
a = Main_UI()
loading = Loading_UI()
Sett = Setting()
a.show()
sys.exit(app.exec_())
