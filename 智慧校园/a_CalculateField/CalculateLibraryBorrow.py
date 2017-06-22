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
            sql = "select count(student_id) from brrow where student_id='" + str(studentId) + "'"
            self.executer.execute(sql)

            total = 0
            data = self.executer.fetchone()
            read_time = data[0]
            weight = 1
            if read_time < self.level_1:
                weight *= self.level_1
            elif read_time < self.level_2:
                weight *= self.level_2
            else:
                weight *= self.level_3

                total += weight

            sql = "update students set bookBorrow='" + str(weight) + "' where student_id='" + str(studentId) + "' "
            self.executer.execute(sql)

if __name__ == '__main__':
    t = CalculateLibraryBorrow(level[0], level[1], level[2], level[3])
    t.calculate()
