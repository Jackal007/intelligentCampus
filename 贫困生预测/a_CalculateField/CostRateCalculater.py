from a_CalculateField import XXCalculater
from Tools import MyLog

class CostRateCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        self.level = [0.1, 0.2, 0.3, 0.4]
    
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
            result = self.executer.fetchone()[0]
            result = self.classify(result)
            sql = "update students set cost_avg_" + i + "='" + result + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
        self.conn.commit()
