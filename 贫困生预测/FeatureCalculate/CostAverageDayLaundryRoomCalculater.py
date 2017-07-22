from FeatureCalculate import XXCalculater
from Tools import MyLog

class CostAverageDayLaundryRoomCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cost_avg_day_laundryroom from students order by cost_avg_day_laundryroom"
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
        CostAverageDayLaundryRoomCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "SELECT\
                    avg(t)\
                FROM\
                    (\
                        SELECT\
                            sum(deal_cost) AS t\
                        FROM\
                            card\
                        WHERE\
                            deal_way = 'LaundryRoom'\
                        AND student_id = " + str(studentId) + "\
                        GROUP BY\
                            date(deal_date)\
                    )as tt"
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set cost_avg_day_LaundryRoom='" + str(s) + "' where student_id=" + str(studentId)
        self.executer.execute(sql)

    @MyLog.myException
    def rankit(self):
        '''
        CostAverageDayLaundryRoomCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select cost_avg_day_LaundryRoom from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set cost_avg_day_LaundryRoom='" + s + "' where student_id=" + str(studentId) 
        self.executer.execute(sql)
