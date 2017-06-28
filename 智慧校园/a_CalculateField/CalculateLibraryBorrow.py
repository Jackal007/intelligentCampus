'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from tqdm import tqdm
import CalculateXX
from MyConfig import LibraryBorrow_level as level

class CalculateLibraryBorrow(CalculateXX.CalculateXX):

    def calculate(self):
        
        print("CalculateLibraryBorrow")
        # 对每一个学生统计其借书的次数
        for studentId in tqdm(self.students):
            sql = "select count(student_id) from borrow where student_id=" + str(studentId)
            self.executer.execute(sql)

            data = self.executer.fetchone()
            readTimes = data[0]
            weight = "D"
            if readTimes < self.level["A"]:
                weight = "A"
            elif readTimes < self.level["B"]:
                weight = "B"
            elif readTimes < self.level["C"]:
                weight = "C"
            try:
                sql = "update students set library_borrow='" + str(weight) + "' where student_id=" + str(studentId)
                self.executer.execute(sql)
            except:
                pass
        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateLibraryBorrow(level)
    t.calculate()
