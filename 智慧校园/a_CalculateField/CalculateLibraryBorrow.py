'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from tqdm import tqdm
import CalculateXX
from a_CalculateField.LevelConfig import BookBorrow_level as level

class CalculateLibraryBorrow(CalculateXX.CalculateXX):

    def calculate(self):
        
        print("CalculateLibraryBorrow")
        # 对每一个学生统计其借书的次数
        for student in tqdm(self.students):
            studentId = student[0]
            sql = "select count(student_id) from borrow where student_id='" + str(studentId) + "'"
            self.executer.execute(sql)

            data = self.executer.fetchone()
            read_time = data[0]
            weight = "C"
            if read_time < self.level["A"]:
                weight ="A"
            elif read_time < self.level["B"]:
                weight ="B"
            else:
                weight = "C"

            sql = "update students set library_borrow='" + str(weight) + "' where student_id='" + str(studentId) + "' "
            self.executer.execute(sql)

if __name__ == '__main__':
    t = CalculateLibraryBorrow(level)
    t.calculate()
