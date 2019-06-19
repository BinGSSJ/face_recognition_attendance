import pymysql

class MysqlClient(object):
    def __init__(self,host='gz-cdb-8it1ulvx.sql.tencentcdb.com', port=61933,
                              user="root", pwd="We17361730539", db="face_recognition"):
        self.conn = None
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        #self.conn = None
        self.cur = None

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port,user=self.user,
                           password=self.pwd, db=self.db,charset='utf8')
        except Exception as e:
            print("连接数据库出错",e)
            return False
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        return True

    #关闭mysql连接
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    def execute(self, sql):
        # 连接数据库
        self.connectDatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql)
                self.conn.commit()
        except Exception as e:
            print("插入数据失败",e,sql)
            self.close()
            return False
        return True
    def execute_many(self, sql,values):
        # 连接数据库
        self.connectDatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.executemany(sql,values)
                self.conn.commit()
        except Exception as e:
            print("插入数据失败",e,sql)
            self.close()
            return False
        return True



    def search(self,sqls):
        self.connectDatabase()
        self.cur = self.conn.cursor()
        cur = self.cur
        cur.execute(sqls)
        r = self.cur.fetchall()
        return r

if __name__ == '__main__':
    sql = "insert into attendance values (4,2,1,1,1,\"2019-04-15 13:12:54\")"
    print(sql)
    db = MysqlClient()
    print(db.execute(sql))






