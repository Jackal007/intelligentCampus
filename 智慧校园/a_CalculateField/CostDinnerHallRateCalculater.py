from a_CalculateField import XXCalculater

class CostDinnerHallRateCalculater(XXCalculater.XXCalculater):

    def calculate(self):
        print("CalculateCostRate")
        
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
        
        dinnerHall_rate = dinnerHall / total
        if dinnerHall_rate < self.level["A"]:
            dinnerHall_rate = "A"
        elif dinnerHall_rate < self.level["B"]:
            dinnerHall_rate = "B"
        elif dinnerHall_rate < self.level["C"]:
            dinnerHall_rate = "C"
        else:
            dinnerHall_rate = "D"
        
        try:
            sql = "update students set cost_avg_dinnerHall='" + dinnerHall_rate + "' where student_id=" + str(studentId) 
            self.executer.execute(sql)
            self.conn.commit()
        except:
            print(sql)
            continue
        self.db.close()