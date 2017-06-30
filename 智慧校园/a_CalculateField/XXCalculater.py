from Tools import *
class XXCalculater:

    def __init__(self, student, level):
        # levels about the weight
        self.level = level
        self.db = MyDataBase.MyDataBase()
        self.conn = self.db.getConn()
        self.executer = self.db.getExcuter()
        self.student = student
        
    @MyLog.myException
    def calculate(self):
        pass  

if __name__ == '__main__':
    print('a father')
