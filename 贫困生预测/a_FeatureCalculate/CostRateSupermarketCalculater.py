from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class CostRateSupermarketCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cost_rate_supermarket from students order by cost_rate_supermarket"
        self.executer.execute(sql)
        CostAmounts = self.executer.fetchall()
        A = CostAmounts[int(len(CostAmounts) * 0.25)][0]
        B = CostAmounts[int(len(CostAmounts) * 0.5)][0]
        C = CostAmounts[int(len(CostAmounts) * 0.75)][0]
        D = CostAmounts[len(CostAmounts) - 1][0]
        self.level = [A, B, C, D]
    
    @MyLog.myException
    def calculate(self):
        '''
        CostRateSupermarketCalculater
        '''
        studentId = str(self.student.getStudentId())
        if self.level is None:
            dealWays = ['Supermarket']
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
                sql = "update students set cost_rate_" + i + "='" + str(s) + "' where student_id=" + str(studentId)
                self.executer.execute(sql)
        else:
            sql = "select set cost_rate_" + i + " from students where student_id=" + studentId   
            self.executer.execute(sql)
            s = self.executer.fetchone()[0]
            s = self.classify(s)
            sql = "update students_rank set cost_rate_" + i + "='" + str(s) + "' where student_id=" + str(studentId)
            self.executer.execute(sql)