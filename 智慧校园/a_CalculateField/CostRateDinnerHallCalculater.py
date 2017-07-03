from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import CostRateDinnerHall_level

class CostRateDinnerHallCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CostRateDinnerHallCalculater")
        
        studentId = self.student.getStudentId()
        sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
        self.executer.execute(sql)
        result = self.executer.fetchall()
        total = 0
        dinnerHall = 0
        for i in result:
            total += i[1]
            if "dinnerhall" in i[0]:
                dinnerHall = i[1]
        
        costRateDinnerHall = dinnerHall / total
        costRateDinnerHall = self.classify(costRateDinnerHall, CostRateDinnerHall_level)
    
        sql = "update students set cost_rate_dinnerHall='" + costRateDinnerHall + "' where student_id=" + str(studentId) 
        self.executer.execute(sql)
        self.conn.commit()
        return costRateDinnerHall
