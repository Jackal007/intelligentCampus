'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from tqdm import tqdm
import CalculateXX
from MyConfig import BalanceRank_level as level

class CalculateBalanceRank(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateBalanceRank")
        for studentId in tqdm(self.students):
            sql = "select min(balance),max(balance) from card where student_id='" + str(studentId)+"'"
            self.executer.execute(sql)
            s = self.executer.fetchone()
            try:
                minBalance = s[0]
                maxBalance = s[1]
                averageBalance = (minBalance + maxBalance) / 2
                
                balanceRank = "D";
                if averageBalance < self.level["A"]:
                    balanceRank = "A"
                elif averageBalance < self.level["B"]:
                    balanceRank = "B"
                elif averageBalance < self.level["C"]:
                    balanceRank = "C"
                    
                sql = "update students set balance_rank='" + str(balanceRank) + "' where student_id='" + str(studentId) + "'"
                self.executer.execute(sql)
            except:
                pass

        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateBalanceRank(level)
    t.calculate()
