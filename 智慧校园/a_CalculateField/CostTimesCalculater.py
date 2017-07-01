from a_CalculateField import XXCalculater

class CostTimesCalculater(XXCalculater.XXCalculater):

    def calculate(self):
        print("CostTimesCalculater")
        # 对每一个学生统计其消费次数
        try:
            studentId = self.student.getStudentId()
            sql = "select count(*) from card where student_id=" + str(studentId)
            self.executer.execute(sql)
    
            t = costTimes = self.executer.fetchone()[0]
            if costTimes < self.level["A"]:
                costTimes = "A"
            elif costTimes < self.level["B"]:
                costTimes = "B"
            elif costTimes < self.level["C"]:
                costTimes = "C"
            else:
                costTimes = "D"
            sql = "update students set cost_times='" + costTimes + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
            self.conn.commit()
        except:
            print(sql)
            pass
        return t
