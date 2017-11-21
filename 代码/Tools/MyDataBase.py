import pymysql

class MyDataBase:
    def __init__(self, database):
        print("connect to data base " + database + " ......")
        self.db = pymysql.connect("localhost", "root", "", database, charset='utf8')
        self.cursor = self.db.cursor()
        self.db.autocommit(True)
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
