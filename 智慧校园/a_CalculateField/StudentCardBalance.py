'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from tqdm import tqdm
import CalculateXX
from a_CalculateField.LevelConfig import StudentCardBalance_level as level

class StudentCardBalance(CalculateXX.CalculateXX):

    def calculate(self):
        for student in tqdm(self.students):
            studentId = student[0]
            sql = "select min(balance),max(balance) from card where student_id=" + str(studentId)
            self.executer.execute(sql)
            s = self.executer.fetchone()
            
            minBalance = s[0]
            maxBalance = s[1]
            averageBalance = (minBalance + maxBalance) / 2
            
            balanceRank = -1;
            if averageBalance < 100:
                balanceRank = 1
            elif averageBalance < 200:
                balanceRank = 2
            elif averageBalance < 300:
                balanceRank = 3
            elif averageBalance < 500:
                balanceRank = 4
            else:
                balanceRank = 5
                
            sql = "update students set balanceRank='" + str(balanceRank) + "' where student_id='" + str(studentId) + "'"
            self.executer.execute(sql)

        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = StudentCardBalance(level[0], level[1], level[2], level[3])
    t.calculate()
