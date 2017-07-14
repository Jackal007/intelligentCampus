from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class CostTimesDayDinnerHallCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cost_times_day_dinnerhall from students order by cost_times_day_dinnerhall"
        self.executer.execute(sql)
        AverageCosts = self.executer.fetchall()
        A = AverageCosts[int(len(AverageCosts) * 0.25)][0]
        B = AverageCosts[int(len(AverageCosts) * 0.5)][0]
        C = AverageCosts[int(len(AverageCosts) * 0.75)][0]
        D = AverageCosts[len(AverageCosts) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        '''
        CostTimesDayDinnerHallCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        i='DinnerHall'
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
        self.executer.execute(sql)

    @MyLog.myException
    def rankit(self):
        '''
        CostTimesDayDinnerHallCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        i='DinnerHall'
        sql = "select cost_times_day_" + i + " from students where student_id=" + studentId   
        self.executer.execute(sql)
        result = self.executer.fetchone()[0]
        result = self.classify(result)
        sql = "update students_rank set cost_times_day_" + i + "='" + result + "' where student_id=" + str(studentId)
        self.executer.execute(sql)