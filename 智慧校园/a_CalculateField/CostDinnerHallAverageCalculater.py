from a_CalculateField import XXCalculater

class CostDinnerHallAverageCalculater(XXCalculater.XXCalculater):

    def calculate(self):
        print("CalculateCostAverage")
        studentId = self.student.getStudentId()
        sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
        self.executer.execute(sql)
        result = self.executer.fetchall()
        for i in result:
            if "dinnerhall" in i[0]:
                avg_dinnerHall = i[1]
                if avg_dinnerHall < self.level["A"]:
                    avg_dinnerHall = "A"
                elif avg_dinnerHall < self.level["B"]:
                    avg_dinnerHall = "B"
                elif avg_dinnerHall < self.level["C"]:
                    avg_dinnerHall = "C"
                else:
                    avg_dinnerHall = "D"
        
        try:
            sql = "update students set cost_avg_dinnerHall='" + str(avg_dinnerHall) + "' where student_id=" + str(studentId) 
            self.executer.execute(sql)
            self.conn.commit()
        except:
            print(sql)
            continue
        self.db.close()