'''
项目统一数据库连接工具类
'''
import pymysql

class MyDataBase:
    '''
            使用手册：
        db = MyDataBase("DataBaseName")
        executer = db.getExcuter()
        
        executer.execute(sql)
        data = executer.fetchall()
        
        db.close
    '''
    def __init__(self, database):
        print("connect to data base " + database + " ......")
        self.db = pymysql.connect("172.16.20.5", "root", "", database, charset='utf8')
        self.cursor = self.db.cursor()
        self.db.autocommit(True)  # 设置每次执行自动提交
        print("connect success!")

    def getConn(self):
        return self.db

    def getExcuter(self):
        return self.cursor

    def close(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    print("a module used to connect db")
