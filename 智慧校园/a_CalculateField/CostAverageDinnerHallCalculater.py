from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import CostAverageDinnerHall_level

class CostAverageDinnerHallCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CostDinnerHallAverageCalculater")
        studentId = self.student.getStudentId()
        sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
        self.executer.execute(sql)
        result = self.executer.fetchall()
        
        costDinnerHallAverage = "A"
        for i in result:
            if "dinnerhall" in i[0]:
                costDinnerHallAverage = i[1]
                costDinnerHallAverage = self.classify(costDinnerHallAverage, CostAverageDinnerHall_level)
    
        sql = "update students set cost_avg_dinnerHall='" + costDinnerHallAverage + "' where student_id=" + str(studentId) 
        self.executer.execute(sql)
        self.conn.commit()
        return costDinnerHallAverage
