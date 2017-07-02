from a_CalculateField import XXCalculater
from Tools import MyLog

class ScoreRankCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("ScoreRankCalculater")

        studentId = self.student.getStudentId()
        sql = "select rank from score where student_id=" + str(studentId)
        self.executer.execute(sql)
        scoreRank = self.executer.fetchone()[0]
        if int(scoreRank) < self.level["A"]:
            scoreRank = "A"
        elif int(scoreRank) < self.level["B"]:
            scoreRank = "B"
        elif int(scoreRank) < self.level["C"]:
            scoreRank = "C"
        else:
            scoreRank = "D"

        sql = "insert into students(student_id,score) values(" + str(studentId) + ",'" + scoreRank + "')" 
        self.executer.execute(sql)
        self.conn.commit()
        return scoreRank