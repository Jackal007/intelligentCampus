import pymysql

class MyDataBase:
    def __init__(self):
        self.db = pymysql.connect("localhost","root","053062","abcd" )
        self.cursor = self.db.cursor()

    def getConn(self):
        return self.db

    def getExcuter(self):
        return self.cursor

    def close(self):
        self.cursor.close()
        self.db.close()


if __name__=='__main__':
    print("a module used to connect db")
