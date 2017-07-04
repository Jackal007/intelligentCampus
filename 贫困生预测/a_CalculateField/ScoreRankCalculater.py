from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import Score_level

class ScoreRankCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("ScoreRankCalculater")

        studentId = self.student.getStudentId()
        sql = "select rank from score where student_id=" + str(studentId)
        self.executer.execute(sql)
        score = self.executer.fetchone()[0]
        score = self.classify(score, Score_level)

        sql = "insert into students(student_id,score) values(" + str(studentId) + ",'" + score + "')" 
        self.executer.execute(sql)
        self.conn.commit()
        return score
