from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import CostAverageSupermarket_level

class CostAverageSuperMarketCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CostAverageSuperMarketCalculater")
        studentId = self.student.getStudentId()
        sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
        self.executer.execute(sql)
        result = self.executer.fetchall()
        
        costAverageSuperMarket = "A"
        for i in result:
            if "supermarket" in i[0]:
                costAverageSuperMarket = i[1]
                costAverageSuperMarket = self.classify(costAverageSuperMarket, CostAverageSupermarket_level)
    
        sql = "update students set cost_avg_superMarket='" + costAverageSuperMarket + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return costAverageSuperMarket
