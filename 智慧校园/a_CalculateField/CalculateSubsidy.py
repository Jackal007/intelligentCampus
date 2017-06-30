'''
Created on 2017年6月21日

@author: zhenglongtian
'''

impfrom a_CalculateField import XXCalculaterrom tqdm import tqdm
from MyConfig import Subsidy_level as level

class CalculateSubsidy(CalXXCalculaterlXXCalculater

    def calculate(self):
        print("CalculateSubsidy")
        # 对每一个学生统计其奖学金获得情况
        for studentId in tqdm(self.students):
            sql = "select stipend from subsidy where student_id=" + str(studentId)
            self.executer.execute(sql)
            subsidy = self.executer.fetchone()[0]

            weight = "D"
            if int(subsidy) <= level["A"]:
                weight = "A"
            elif int(subsidy) <= level["B"]:
                weight = "B"
            elif int(subsidy) <= level["C"]:
                weight = "C"

            sql = "update students set subsidy= '" + weight + "' where student_id = " + str(studentId)
            try:
                self.executer.execute(sql)
            except:
                pass

        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateSubsidy(level)
    t.calculate()
