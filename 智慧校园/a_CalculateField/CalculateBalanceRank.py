'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from tqdm import tqdm
import CalculateXX
from a_CalculateField.LevelConfig import BalanceRank_level as level

class CalculateBalanceRank(CalculateXX.CalculateXX):

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
            if averageBalance < self.level_1:
                balanceRank = self.level_1
            elif averageBalance < self.level_2:
                balanceRank = self.level_2
            elif averageBalance < self.level_3:
                balanceRank = self.level_3
            elif averageBalance < self.level_4:
                balanceRank = self.level_4
            else:
                balanceRank = self.level_4
                
            sql = "update students set balance_rank='" + str(balanceRank) + "' where student_id='" + str(studentId) + "'"
            self.executer.execute(sql)

        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateBalanceRank(level[0], level[1], level[2], level[3])
    t.calculate()
