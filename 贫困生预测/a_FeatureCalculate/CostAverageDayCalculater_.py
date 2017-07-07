from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class CostAverageDayCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cost_avg_day_ from students order by cost_avg_day_"
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
            CostAverageDayCalculater
        '''
        studentId = self.student.getStudentId()
        dealWays = ['dinnerhall', 'supermarket', 'laundryroom']
        for i in dealWays:
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
            if self.level is not None:
                s = self.classify(s)
                sql = "update students_rank set cost_avg_day_" + i + "='" + s + "' where student_id=" + str(studentId) 
            self.executer.execute(sql)
