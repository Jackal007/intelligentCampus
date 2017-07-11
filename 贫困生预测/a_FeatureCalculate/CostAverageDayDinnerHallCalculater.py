from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class CostAverageDayDinnerHallCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cost_avg_day_dinnerhall from students order by cost_avg_day_dinnerhall"
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
        CostAverageDayDinnerHallCalculater
        '''
        studentId = str(self.student.getStudentId())
        dealWays = ['dinnerhall']
        for i in dealWays:
            if self.level is None:
                sql = "SELECT\
                            avg(t)\
                        FROM\
                            (\
                                SELECT\
                                    sum(deal_cost) AS t\
                                FROM\
                                    card\
                                WHERE\
                                    deal_way = '" + i + "'\
                                AND student_id = " + str(studentId) + "\
                                GROUP BY\
                                    date(deal_date)\
                            )as tt"
                self.executer.execute(sql)
                s = self.executer.fetchone()[0]
                sql = "update students set cost_avg_day_" + i + "='" + str(s) + "' where student_id=" + str(studentId)
                self.executer.execute(sql)
            else:
                sql = "select cost_avg_day_" + i + " from students where student_id=" + studentId   
                self.executer.execute(sql)
                s = self.executer.fetchone()[0]
                s = self.classify(s)
            sql = "update students_rank set cost_avg_day_" + i + "='" + s + "' where student_id=" + str(studentId) 
            self.executer.execute(sql)
