from a_CalculateField import XXCalculater
from Tools import MyLog

class CostTimesDayCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cost_times_day_ from students order by cost_times_day_"
        self.executer.execute(sql)
        AverageCosts = self.executer.fetchall()
        A = AverageCosts[int(len(AverageCosts) * 0.25)][0]
        B = AverageCosts[int(len(AverageCosts) * 0.5)][0]
        C = AverageCosts[int(len(AverageCosts) * 0.75)][0]
        D = AverageCosts[int(len(AverageCosts) * 1) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每天每种消费的平均次数")
        studentId = self.student.getStudentId()
        dealWays = ['dinnerhall', 'supermarket', 'laundry']
        for i in dealWays:
            sql = "SELECT\
                        avg(t)\
                    FROM\
                        (\
                            SELECT\
                                count(*) AS t\
                            FROM\
                                card\
                            WHERE\
                                deal_way = '" + i + "'\
                            AND student_id = " + str(studentId) + "\
                            GROUP BY\
                                date(deal_date)\
                        )as tt"
            self.executer.execute(sql)
            result = str(self.executer.fetchone()[0])
            sql = "update students set cost_times_day_" + i + "='" + result + "' where student_id=" + str(studentId)
            if self.level is not None:
                result = self.classify(result)
                sql = "update students_rank set cost_amount='" + result + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
