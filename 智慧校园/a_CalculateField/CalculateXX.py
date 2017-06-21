'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from time import sleep
from tqdm import tqdm
import sys
from Tools import MyDataBase

class CalculateXX:

    def __init__(self, level_1, level_2, level_3, level_4):
        # levels about the weight
        self.level_1 = level_1
        self.level_2 = level_2
        self.level_3 = level_3
        self.level_4 = level_4
        self.db = MyDataBase.MyDataBase()
        self.conn = self.db.getConn()
        self.executer = self.db.getExcuter()
        
        # 从这边读取到所有学生的id
        sql = "select student_id from score"
        self.executer.execute(sql)
        self.students = self.executer.fetchall()

    def calculate(self):
        for i in tqdm(range(1, 100)):
            sleep(0.01)
            sys.stdout.flush()   

if __name__ == '__main__':
    print('一个父类')