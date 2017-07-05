from a_CalculateField import XXCalculater
from Tools import MyLog

class CostVarianceCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        self.level = [0.1, 0.2, 0.3, 0.4]
        
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
        result = self.executer.fetchone()[0]
        result = self.classify(result)
        sql = "update students set cost_variance='" + result + "' where student_id=" + str(studentId)
        self.executer.execute(sql)