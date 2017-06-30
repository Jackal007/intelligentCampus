from a_CalculateField import XXCalculater

class CalculateCostAmount(XXCalculater.XXCalculater):

    def calculate(self):
        print("CalculateCostAmount")
        # 对每一个学生统计其消费金额的情况
        try:
            studentId = self.student.getStudentId()
            sql = "select sum(deal_cost) from card where student_id=" + str(studentId) 
            self.executer.execute(sql)
            dealCost = self.executer.fetchone()[0]
            if dealCost < self.level["A"]:
                dealCost = "A"
            elif dealCost < self.level["B"]:
                dealCost ="B"
            elif dealCost < self.level["C"]:
                dealCost = "C"
            else:
                dealCost="D"
        
            sql = "update students set cost_amount='" + dealCost + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
            self.conn.commit()
        except:
            print(sql)
            continue
        
        self.db.close()
