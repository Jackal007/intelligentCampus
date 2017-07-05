from a_CalculateField import XXCalculater
from Tools import MyLog

class CostAverageDinnerHallCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select sum(deal_cost) as c from card group by student_id order by c"
        self.executer.execute(sql)
        CostAmounts = self.executer.fetchall()
        A = CostAmounts[int(len(CostAmounts) * 0.25)][0]
        B = CostAmounts[int(len(CostAmounts) * 0.5)][0]
        C = CostAmounts[int(len(CostAmounts) * 0.75)][0]
        D = CostAmounts[int(len(CostAmounts) * 1) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每日每种消费的平均金额")
        studentId = self.student.getStudentId()
        dealWays = ['dinnerhall', 'supermarket', 'laundry']
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
            result = self.executer.fetchone()[0]
            result = self.classify(result)
            sql = "update students set cost_avg_day_" + i + "='" + result + "' where student_id=" + str(studentId) 
            self.executer.execute(sql)
        self.conn.commit()
