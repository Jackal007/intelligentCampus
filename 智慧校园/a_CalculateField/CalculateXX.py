from Tools import MyDataBase
from Tools import MyLog

class CalculateXX:

    def __init__(self, level):
        # levels about the weight
        self.level = level
        self.db = MyDataBase.MyDataBase()
        self.conn = self.db.getConn()
        self.executer = self.db.getExcuter()
        
        # 从这边读取到所有学生的id
        sql = "select student_id from score"
        self.executer.execute(sql)
        self.students = []
        for i in self.executer.fetchall():
            self.students.append(i[0])
    @MyLog.myException
    def calculate(self):
        pass  

if __name__ == '__main__':
    print('a father')
