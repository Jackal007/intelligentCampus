from FeatureCalculate import XXCalculater
from Tools import MyLog

class ScoreRankCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select score from students order by score"
        self.executer.execute(sql)
        scoreRank = self.executer.fetchall()
        A = scoreRank[int(len(scoreRank) * 0.125)][0]
        B = scoreRank[int(len(scoreRank) * 0.25)][0]
        C = scoreRank[int(len(scoreRank) * 0.375)][0]
        D = scoreRank[int(len(scoreRank) * 0.5)][0]
        E = scoreRank[int(len(scoreRank) * 0.625)][0]
        F = scoreRank[int(len(scoreRank) * 0.75)][0]
        G = scoreRank[int(len(scoreRank) * 0.875)][0]
        H = scoreRank[len(scoreRank) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
        
    @MyLog.myException
    def calculate(self):
        '''
        ScoreRankCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select rank from score where student_id=" + studentId
        self.executer.execute(sql)
        score = self.executer.fetchone()[0]
        sql = "insert into students(student_id,score) values(" + studentId + ",'" + str(score) + "')" 
        self.executer.execute(sql)

    @MyLog.myException
    def rankit(self):
        '''
        ScoreRankCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select score from students where student_id=" + studentId   
        self.executer.execute(sql)
        score = self.executer.fetchone()[0]
        score = self.classify(score)
        sql = "insert into students_rank(student_id,score) values(" + studentId + ",'" + str(score) + "')" 
        self.executer.execute(sql)