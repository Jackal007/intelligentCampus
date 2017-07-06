from a_CalculateField import XXCalculater
from Tools import MyLog

class CostVarianceCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cost_variance from students order by cost_variance"
        self.executer.execute(sql)
        CostVariance = self.executer.fetchall()
        A = CostVariance[int(len(CostVariance) * 0.25)][0]
        B = CostVariance[int(len(CostVariance) * 0.5)][0]
        C = CostVariance[int(len(CostVariance) * 0.75)][0]
        D = CostVariance[int(len(CostVariance) * 1) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算按日消费的方差")
        studentId = self.student.getStudentId()
        sql = "SELECT\
                sum(item) / days\
                FROM\
                    (\
                        SELECT\
                            pow((sum(deal_cost) - (total_cost/days)),2) AS item,\
                            days as days\
                        FROM\
                            card,\
                            (\
                                SELECT\
                                    count(date(deal_date)) AS days,\
                                    sum(deal_cost)  as total_cost\
                                FROM\
                                    card\
                                WHERE\
                                    student_id = " + str(studentId) + "\
                            ) AS a\
                        WHERE\
                            student_id = " + str(studentId) + "\
                        GROUP BY\
                            date(deal_date)\
                    ) AS b"
        self.executer.execute(sql)
        result = str(self.executer.fetchone()[0])
        sql = "update students set cost_variance='" + result + "' where student_id=" + str(studentId)
        if self.level is not None:
            result = self.classify(result)
            sql = "update students_rank set cost_variance='" + result + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
