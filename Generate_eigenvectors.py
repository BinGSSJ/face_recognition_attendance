# 生成特征向量,写入csv文件

from config import dir, model_dir,features_dir
from skimage import io
import dlib
import csv
import cv2
import os
import pandas as pd
import numpy as np

face_dir = dir + "face/"  # 人脸图片文件夹 (所有人都存储在这个文件夹下)
from get_Face import cnn_face_detector

predictor = dlib.shape_predictor(model_dir["predictor"])  # 导入dlib人脸预测器
recognition_model = dlib.face_recognition_model_v1(model_dir["recognition_model"])  # 导入dlib人脸识别模型

def check_features_dir(dirt):
    '''
    检查存储人脸特征向量的文件夹是否存在
    :param dir: 存储人脸特征向量的文件夹
    :return:
    '''
    if os.path.isdir(dirt):
        pass
    else:
        os.mkdir(dirt)



def return_features(face_img):
    '''
    :param path_img: 人脸图片
    :return: 人脸图片的特征向量
    '''
    img = io.imread(face_img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 彩色图片转灰度
    face = cnn_face_detector(img_gray, 1)  # 使用cnn模型进行检测

    print("检测到人脸的图像：", face_img, "\n")

    if len(face) != 0:
        for i, d in enumerate(face):
            s = dlib.rectangle(d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom())
        shape = predictor(img_gray, s)
        face_descriptor = recognition_model.compute_face_descriptor(img_gray, shape)  # 计算脸部特征向量
    else:
        face_descriptor = 0
        print("no face")

    print(face_descriptor)
    return face_descriptor



def compute_one_people_all(face_name):
    '''
    计算一个人脸文件夹下的所有特征向量,写入到对应的csv文件中
    :param face_name:
    :return: 0表示成功
    '''
    check_features_dir(features_dir)
    face_list = os.listdir(face_dir+face_name)
    print(face_list)
    # newline 设置为空，直接另起一行写入，否则中间会隔一行
    with open(features_dir + "/{0}.csv".format(face_name), "w",newline="") as f:
        writer = csv.writer(f)
        if face_list:
            for item in range(len(face_list)):
                print("jisuan第{0}张 {1}".format(item,face_list[item]))
                features = return_features(face_dir + face_name +"/" + face_list[item])
                if features==0:
                    item +=1
                else:
                    writer.writerow(features)
    return 0



def update_all_person_features():
    '''
    更新face文件夹下所有人脸的特征向量
    :return: 0成功
    '''
    dirlist = os.listdir(face_dir)
    try:
        for item in dirlist:
            compute_one_people_all(item)
        print("更新向量完毕")
        return 0
    except Exception as e:
        print("出错",e)
        return -1
    print(dirlist)


def compute_one_person_average(path):
    '''
    计算一个人的特征向量的平均值
    :param path: 具体某一个csv文件路径
    :return: 0成功
    '''
    col_names = []
    # 128D 特征
    for item in range(128):
        col_names.append("features_" + str(item + 1))

    # 利用 pandas 读取 csv
    rd = pd.read_csv(path, names=col_names)

    if rd.size != 0:
        # 存放 128D 特征的均值
        feature_mean_list = []

        for feature_num in range(128):
            tmp_arr = rd["features_" + str(feature_num + 1)]
            tmp_arr = np.array(tmp_arr)
            # 计算某一个特征的均值
            tmp_mean = np.mean(tmp_arr)
            feature_mean_list.append(tmp_mean)
    else:
        feature_mean_list = []
    print(feature_mean_list)
    return feature_mean_list




def merge_all_features(path):
    '''
    将所有的csv文件整合，同时形成映射关系,将映射标签列表写入到label.csv文件中
    :param path:存储所有特征向量的文件夹(features文件夹)
    :return: 0 表示成功 -1表示没有检测到csv文件
    '''
    labels = []
    features_list = os.listdir(path)
    with open(dir + "features.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for i in range(len(features_list)):
            feature_mean_list = compute_one_person_average(path + features_list[i])
            writer.writerow(feature_mean_list)
            labels.append(features_list[i].split(".")[0])
    if len(labels)==0:
        return -1
    with open(dir + "label.csv","w",newline="") as c:
        writer = csv.writer(c)
        writer.writerow(labels)
    return 0


if __name__ == '__main__':
    img = r"D:\face_class\face\刘德华\1.jpg"
    a =  list(return_features(img))
    print(a)
    # merge_all_features(features_dir)
    # compute_one_people_all("bing")


    # update_all_person_features()
    # merge_all_features(features_dir)
