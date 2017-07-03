from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import CostRateSuperMarket_level

class CostRateSuperMarketCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CostRateSuperMarketCalculater")
        studentId = self.student.getStudentId()
        sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
        self.executer.execute(sql)
        result = self.executer.fetchall()
        total = dinnerHall = superMarket = 0
        for i in result:
            total += i[1]
            if "supermarket" in i[0]:
                superMarket = i[1]
        
        costRateSupermarket = superMarket / total
        costRateSupermarket = self.classify(costRateSupermarket, CostRateSuperMarket_level)
        
        sql = "update students set cost_rate_superMarket='" + costRateSupermarket + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return costRateSupermarket
