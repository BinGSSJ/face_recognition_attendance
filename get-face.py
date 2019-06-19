# 人脸录入

import dlib
import os
import numpy as np
import cv2
from config import dir, model_dir  # 导入文件夹路径
face_dir = dir + "face/"  # 人脸图片文件夹 (所有人都存储在这个文件夹下)


count = 0
# 初始化检测器 导入cnn模型进行检测
cnn_face_detector = dlib.cnn_face_detection_model_v1(model_dir["cnn"])


# 检测人脸
def detect_face(img):
    # 转换成灰度图片
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = cnn_face_detector(img_gray, 1)
    return results


# 生成人脸文件夹，存储检测到的人脸图片
def make_face_dir(face_name):
    '''
    :param face_name: 该人脸图片所对应的姓名
    :return:
    '''
    face_name_dir = face_dir + face_name  # 当前人脸的图片文件夹(当前名字人的人脸文件夹)
    if os.path.isdir(dir):
        pass
    else:
        os.mkdir(dir)
    if os.path.isdir(face_dir):
        pass
    else:
        os.mkdir(face_dir)
    if os.path.isdir(face_name_dir):
        pass
    else:
        os.mkdir(
            face_name_dir
        )


# 查询当前检测到人脸数目
def check_face_num(results):
    '''
    :param results: 使用cnn模型的检测结果
    :return: -1未检测到人脸; -2人脸数目大于1;  1人脸数目为1
    '''
    if len(results) == 0:
        return -1
    elif len(results) > 1:
        return -2
    else:
        return 1

def save_image(img,result,face_name):
    '''
    调用检测人脸数目函数，
    存储人脸图片到相对应的文件夹
    :param result: 使用cnn模型得到的结果
    :param face_name: 人脸名字
    :return: 0保存成功 ;-1保存失败
    '''
    res = check_face_num(result)
    if res:
        for i ,d in enumerate(result):
            face = d.rect
            left = face.left()
            top = face.top()
            right = face.right()
            bottom = face.bottom()
            add_w = int((right - left) / 8)
            add_h = int((bottom - top) / 8)
            im_blank = np.zeros((int((bottom - top) +add_h), (right - left)+add_w, 3), np.uint8)
            print(((bottom - top)+add_h),(right - left)+add_w)
            for ii in range((bottom - top)+add_h):
                for jj in range((right - left)+add_w):
                    im_blank[ii][jj] = img[face.top() + ii][face.left() + jj]
            cv2.imwrite(face_dir + face_name +"/{0}{1}.jpg".format(face_name,count),im_blank)
            cv2.imshow("sdsd", im_blank)


if __name__ == '__main__':
    video = "http://admin:admin@192.168.1.113:8081/"
    cap = cv2.VideoCapture(video)
    while cap.isOpened():
        # 480 height * 640 width
        flag, img_rd = cap.read()
        kk = cv2.waitKey(1)
        dets = detect_face(img_rd)
        # 窗口显示
        # cv2.namedWindow("camera", 0) # 如果需要摄像头窗口大小可调
        if kk == ord('s'):
            print("Sds")
            make_face_dir("bing")
            save_image(img_rd,dets,"bing")
        cv2.imshow("sd",img_rd)


    # 释放摄像头
    cap.release()

    # 删除建立的窗口
    cv2.destroyAllWindows()
