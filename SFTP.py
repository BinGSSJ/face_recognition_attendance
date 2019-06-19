#!/usr/bin/env python
# coding=utf-8
# 与服务器建立连接

import paramiko
import time
import os


class SFTP():

    def __init__(self, ip="118.31.36.35",name="medical",pwd="medical01"):
        self.ip = ip
        self.name = name
        self.pwd = pwd

    def connect(self):
        # 连接
        try:
            conn = paramiko.Transport((self.ip, 22))
        except Exception as e:
            print(e)
        else:
            # 用户名，用户密码
            try:
                # 尝试与远程服务器连接
                conn.connect(username=self.name, password=self.pwd)
                self.sftp_ob = paramiko.SFTPClient.from_transport(conn)
            except Exception as e:
                # 失败则打印原因
                print(e)
                return

    def download(self,remote,local,filename):
        self.sftp_ob.get(remote + filename, local + filename)
        print("Completely!")

    def upload(self,remote,local,filename):
        self.sftp_ob.put(local + filename, remote + filename)
        print("Completely!")


    def down_load_dir(self,remote_dir_id,local_dir_id):
        self.connect()
        r = "/home/medical/faces/%d/"%(remote_dir_id)
        l = "D:/face_class/face/%d/"%(local_dir_id)
        try:
            files = self.sftp_ob.listdir(r)  # 下载多个文件
            os.mkdir(l)
            for f in files:
                print(f)
                self.download(r, l, f)
        except:
            pass


    def up_load_dir(self,remote_dir_id,local_dir_id):
        self.connect()
        r = "/home/medical/faces/%d/"%(remote_dir_id)
        l = "D:/face_class/face/%d/"%(local_dir_id)
        try:
            self.sftp_ob.mkdir(r)
        except:
            pass
        try:
            with open(l + "time.txt", "w") as f:
                f.write(str(time.time()))
        except:
            pass
        files = os.listdir(l)  # 上传多个文件
        for f in files:
            print(f)
            self.upload(r,l,f)


    def mkdi(self,remote_dir):
        self.connect()
        try:
            self.sftp_ob.mkdir(remote_dir)
        except Exception as e:
            print(e)

    def get_change_time(self,remote_dir_id):
        self.connect()
        remote = "/home/medical/faces/%d/time.txt"%(remote_dir_id)
        try:
            with self.sftp_ob.open(remote) as f:
                return f.read().decode('utf-8')
        except:
            return "false"


def main():
    try:
        sftp = SFTP()
    except:
        pass


    print(sftp.get_change_time(3))
    #sftp.up_load_dir(3,3)


if __name__ == "__main__":
    main()
