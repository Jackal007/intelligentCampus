from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class CostRateCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
#         sql = "select cost_amount from students order by cost_amount"
#         self.executer.execute(sql)
#         CostAmounts = self.executer.fetchall()
#         A = CostAmounts[int(len(CostAmounts) * 0.25)][0]
#         B = CostAmounts[int(len(CostAmounts) * 0.5)][0]
#         C = CostAmounts[int(len(CostAmounts) * 0.75)][0]
#         D = CostAmounts[int(len(CostAmounts) * 1) - 1][0]
#         self.level = [A, B, C, D]
        pass
    
    @MyLog.myException
    def calculate(self):
        print("正在计算每种消费占比")
        studentId = self.student.getStudentId()
        dealWays = ['dinnerhall', 'supermarket', 'laundry']
        for i in dealWays:
            sql = "SELECT\
                        sum(deal_cost)/s\
                    FROM\
                        card,\
                        (\
                            SELECT\
                                sum(deal_cost) AS s\
                            FROM\
                                card\
                            WHERE\
                                student_id = " + str(studentId) + "\
                        )as t\
                    WHERE\
                        deal_way = '" + i + "'\
                    AND student_id = " + str(studentId)
            self.executer.execute(sql)
            s = self.executer.fetchone()[0]
            sql = "update students set cost_avg_" + i + "='" + str(s) + "' where student_id=" + str(studentId)
            if self.level is not None:
                s = self.classify(s)
                sql = "update students_rank set cost_avg_" + i + "='" + str(s) + "' where student_id=" + str(studentId)
            self.executer.execute(sql)