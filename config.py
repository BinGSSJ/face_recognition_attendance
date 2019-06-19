# 配置文件

dir = "D:/face_class/" # 设置存储文件夹
features_dir = dir + "features/" # 设置存储特征向量的文件夹
features_path =dir + "features.csv"
label_path = dir +"label.csv"
model_dir = {
    "cnn":"D:\calculate_dis\data\data_dlib\mmod_human_face_detector.dat",
    "predictor":"D:\calculate_dis\data\data_dlib\shape_predictor_5_face_landmarks.dat",
    "recognition_model":"D:\calculate_dis\data\data_dlib\dlib_face_recognition_resnet_model_v1.dat"
} # 设置模型存储文件夹

temp_dir = dir+"face/temp/"
face_dir = dir+"face/"
video_streams="0"


threshold = 0.45 # 设置检测阈值