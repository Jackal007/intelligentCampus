from a_CalculateField import XXCalculater

class CostTimesCalculater(XXCalculater.XXCalculater):

    def calculate(self):
        print("CalculateLibraryBorrow")
        # 对每一个学生统计其消费次数
        studentId = self.student.getStudentId()
        sql = "select count(*) from card where student_id=" + str(studentId)
        self.executer.execute(sql)

        t=costTimes = self.executer.fetchone()[0]
        if costTimes < self.level["A"]:
            costTimes ="A"
        elif costTimes < self.level["B"]:
            weight ="B"
        elif costTimes < self.level["C"]:
            costTimes = "C"
        else:
            costTimes = "D"
        try:
            sql = "update students set cost_times='" + str(weight) + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
            self.conn.commit()
        except:
            print(sql)
            continue
        self.db.close()
        return t