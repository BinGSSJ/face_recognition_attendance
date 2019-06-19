# 基于已经存储的特征向量进行人脸识别

import dlib
import numpy as np
import cv2
from config import threshold, model_dir, label_path, features_path  # 导入设置的阈值 模型 label标签路径 特征向量路径
import pandas as pd
import csv

# 人脸识别模型，提取128D的特征矢量
# face recognition model, the object maps human faces into 128D vectors
recognition_model = dlib.face_recognition_model_v1(model_dir["recognition_model"])
cnn_face_detector = dlib.cnn_face_detection_model_v1(model_dir["cnn"])
predictor = dlib.shape_predictor(model_dir["predictor"])


def get_labels(csv_path):
    '''
    从csv文件中获取标签(学生姓名)
    :param csv_path: label.csv路径
    :return: 列表存储学生姓名
    '''
    with open(csv_path, "r") as f:
        reader = csv.reader(f)
        labels = list(reader)
    return labels


def get_local_features(path):
    '''
    获取本地存储的特征向量，加载到列表中
    :param path: 所有人的特征向量
    :return: 向量列表
    '''
    with open(path, "r") as f:
        reader = csv.reader(f)
        local_fea = (list(reader))

    local_features = []
    for item in local_fea:
        local_features.append(list(map(lambda x: float(x), item)))
    return local_features


def return_euclidean_distance(feature_1, feature_2):
    '''
    计算两个128D向量间的欧式距离
    :param feature_1: 特征向量1
    :param feature_2: 特征向量2
    :return:
    '''
    feature_1 = np.array(feature_1)
    feature_2 = np.array(feature_2)
    a = np.square(feature_1 - feature_2)
    dist = np.sqrt(np.sum(np.square(feature_1 - feature_2)))
    print("求得的欧式距离为: ", dist)
    if dist > threshold:
        return False
    else:
        return True


def get_128d_features(img_gray):
    '''
    返回一张图片中的所检测到的每个人脸的特征向量
    :param img_gray: 图片
    :return: 检测
    '''
    faces = cnn_face_detector(img_gray, 1)
    if len(faces) != 0:
        face_feas = []
        for i in range(len(faces)):
            shape = predictor(img_gray, faces[i])
            face_feas.append(recognition_model.compute_face_descriptor(img_gray, shape))
    else:
        face_feas = []
    return face_feas


def chage_opencv_to_Pil():
    '''
    opencv无法显示中文，将其转换为PIL格式
    暂时不显示
    :return:
    '''
    pass

if __name__ == '__main__':
    labelss = get_labels(label_path)[0]
    local_features = get_local_features(features_path)
    print(local_features)
    # video = "http://admin:admin@172.20.10.9:8081/"
    # cap = cv2.VideoCapture(video)
    #
    # # cap.set(propId, value)
    # # 设置视频参数，propId 设置的视频参数，value 设置的参数值
    # cap.set(3, 480)
    #
    # while cap.isOpened():
    #
    #     flag, img_rd = cap.read()
    #     kk = cv2.waitKey(1)
    #
    #     # 取灰度
    #     img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)
    #
    #     # 人脸数 faces
    #     faces = cnn_face_detector(img_gray, 0)
    #
    #     # 待会要写的字体
    #     font = cv2.FONT_HERSHEY_COMPLEX
    #
    #     # 存储当前摄像头中捕获到的所有人脸的坐标/名字
    #     pos_namelist = []
    #     name_namelist = []
    #
    #     # 按下 q 键退出
    #     if kk == ord('q'):
    #         break
    #     else:
    #         # 检测到人脸
    #         if len(faces) != 0:
    #             # 获取当前捕获到的图像的所有人脸的特征，存储到 features_cap_arr
    #             features_cap_arr = []
    #             for i, d in enumerate(faces):
    #                 s = dlib.rectangle(d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom())
    #                 shape = predictor(img_rd, s)
    #                 features_cap_arr.append(recognition_model.compute_face_descriptor(img_rd, shape))
    #
    #             # 遍历捕获到的图像中所有的人脸
    #             for k in range(len(faces)):
    #                 # 让人名跟随在矩形框的下方
    #                 # 确定人名的位置坐标
    #                 # 先默认所有人不认识，是 unknown
    #                 name_namelist.append("unknown")
    #
    #                 # 每个捕获人脸的名字坐标
    #                 pos_namelist.append(
    #                     tuple([faces[k].rect.left(),
    #                            int(faces[k].rect.bottom() + (faces[k].rect.bottom() - faces[k].rect.top()) / 4)]))
    #
    #                 # 对于某张人脸，遍历所有存储的人脸特征
    #                 for i in range(len(labelss)):
    #                     print("with person_", str(i + 1), "the ", end='')
    #                     # 将某张人脸与存储的所有人脸数据进行比对
    #                     compare = return_euclidean_distance(features_cap_arr[k], local_features[i])
    #                     if compare:  # 找到了相似脸
    #                         name_namelist[k] = labelss[i]
    #
    #                 # 矩形框
    #                 for kk, d in enumerate(faces):
    #                     # 绘制矩形框
    #                     cv2.rectangle(img_rd, tuple([d.rect.left(), d.rect.top()]), tuple([d.rect.right(), d.rect.bottom()]), (0, 255, 255),
    #                                   2)
    #
    #             # 在人脸框下面写人脸名字
    #             for i in range(len(faces)):
    #                 cv2.putText(img_rd, name_namelist[i], pos_namelist[i], font, 0.8, (0, 255, 255), 1, cv2.LINE_AA)
    #
    #     print("Name list now:", name_namelist, "\n")
    #
    #     cv2.putText(img_rd, "Press 'q': Quit", (20, 450), font, 0.8, (84, 255, 159), 1, cv2.LINE_AA)
    #     cv2.putText(img_rd, "Face Recognition", (20, 40), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
    #     cv2.putText(img_rd, "Faces: " + str(len(faces)), (20, 100), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
    #
    #     # 窗口显示
    #     cv2.imshow("camera", img_rd)
    #
    # # 释放摄像头
    # cap.release()
    #
    # # 删除建立的窗口
    # cv2.destroyAllWindows()
