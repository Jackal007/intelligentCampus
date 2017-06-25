'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from Tools import MyDataBase

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

    def calculate(self):
        pass  

if __name__ == '__main__':
    print('一个父类')
