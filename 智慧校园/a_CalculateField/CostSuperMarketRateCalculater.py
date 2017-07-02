from a_CalculateField import XXCalculater
from Tools import MyLog

class CostSuperMarketRateCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CostSuperMarketRateCalculater")
        studentId = self.student.getStudentId()
        sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
        self.executer.execute(sql)
        result = self.executer.fetchall()
        total,dinnerHall,superMarket = 0
        for i in result:
            total += i[1]
            if "supermarket" in i[0]:
                superMarket = i[1]
        
        superMarket_rate = superMarket / total
        if superMarket_rate < self.level["A"]:
            superMarket_rate = "A"
        elif superMarket_rate < self.level["B"]:
            superMarket_rate = "B"
        elif superMarket_rate < self.level["C"]:
            superMarket_rate = "C"
        else:
            superMarket_rate = "D"
        
        sql = "update students set cost_avg_superMarket='" + superMarket_rate + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return superMarket_rate