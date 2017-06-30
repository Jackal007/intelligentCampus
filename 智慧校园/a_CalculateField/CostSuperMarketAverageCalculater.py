from a_CalculateField import XXCalculater

class CostSuperMarketAverageCalculater(XXCalculater.XXCalculater):

    def calculate(self):
        print("CalculateCostAverage")
        studentId = self.student.getStudentId()
        sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
        self.executer.execute(sql)
        result = self.executer.fetchall()
        for i in result:
            if "supermarket" in i[0]:
                avg_superMarket = i[1]
                if avg_superMarket < self.level["A"]:
                    avg_superMarket = "A"
                elif avg_superMarket < self.level["B"]:
                    avg_superMarket = "B"
                elif avg_superMarket < self.level["C"]:
                    avg_superMarket = "C"
                else:
                    avg_superMarket = "D"
        
        try:
            sql = "update students set cost_avg_superMarket='" + str(avg_superMarket) + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
            self.conn.commit()
        except:
            print(sql)
            continue
        self.db.close()