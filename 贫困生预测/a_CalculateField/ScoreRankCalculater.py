from a_CalculateField import XXCalculater
from Tools import MyLog

class ScoreRankCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select max(rank) from score"
        self.executer.execute(sql)
        studentNum = self.executer.fetchone()[0]
        A = int(studentNum * 0.25)
        B = int(studentNum * 0.5)
        C = int(studentNum * 0.5)
        D = int(studentNum * 1)
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算成绩")
        studentId = str(self.student.getStudentId())
        sql = "select rank from score where student_id=" + studentId
        self.executer.execute(sql)
        score = self.executer.fetchone()[0]
        score = str(self.classify(score))

        sql = "insert into students(student_id,score) values(" + studentId + ",'" + score + "')" 
        self.executer.execute(sql)
