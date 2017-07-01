from a_CalculateField import XXCalculater

class ScoreRankCalculater(XXCalculater.XXCalculater):

    def calculate(self):
        print("ScoreRankCalculater")

        studentId = self.student.getStudentId()
        sql = "select rank from score where student_id=" + str(studentId)
        self.executer.execute(sql)
        t = scoreRank = self.executer.fetchone()[0]
        if int(scoreRank) < self.level["A"]:
            scoreRank = "A"
        elif int(scoreRank) < self.level["B"]:
            scoreRank = "B"
        elif int(scoreRank) < self.level["C"]:
            scoreRank = "C"
        else:
            scoreRank = "D"

        sql = "insert into students(student_id,score) values(" + str(studentId) + ",'" + scoreRank + "')" 
#         try:
        self.executer.execute(sql)
        self.conn.commit()
#         except:
#             print(sql)
#             pass
        return t