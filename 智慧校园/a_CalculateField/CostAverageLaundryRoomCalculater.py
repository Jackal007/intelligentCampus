from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import CostAverageLaundryRoom_level

class CostAverageLaundryRoomCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CostAverageLaundryRoomCalculater")
        studentId = self.student.getStudentId()
        sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
        self.executer.execute(sql)
        result = self.executer.fetchall()
        
        costAverageLaundryRom = "A"
        for i in result:
            if "laundryroom" in i[0]:
                costAverageLaundryRom = i[1]
                costAverageLaundryRom = self.classify(costAverageLaundryRom, CostAverageLaundryRoom_level)
    
    
        sql = "update students set cost_avg_laundryroom='" + costAverageLaundryRom + "' where student_id=" + str(studentId) 
        self.executer.execute(sql)
        self.conn.commit()
        return costAverageLaundryRom
