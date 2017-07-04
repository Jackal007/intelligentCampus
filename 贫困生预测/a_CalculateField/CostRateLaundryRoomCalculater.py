from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import CostRateLaundryRoom_level

class CostRateLaundryRoomCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CostRateLaundryRoomCalculater")
        
        studentId = self.student.getStudentId()
        sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
        self.executer.execute(sql)
        result = self.executer.fetchall()
        total = 0
        dinnerHall = 0
        for i in result:
            total += i[1]
            if "laundryroom" in i[0]:
                dinnerHall = i[1]
        
        costRateLaundryRoom = dinnerHall / total
        costRateLaundryRoom = self.classify(costRateLaundryRoom, CostRateLaundryRoom_level)
    
        sql = "update students set cost_rate_laundryroom='" + costRateLaundryRoom + "' where student_id=" + str(studentId) 
        self.executer.execute(sql)
        self.conn.commit()
        return costRateLaundryRoom
