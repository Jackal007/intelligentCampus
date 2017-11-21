from FeatureCalculate import XXCalculater
from Tools import MyLog

class Below2_5_RankCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select Below2_5_Rank from students order by Below2_5_Rank "
        self.executer.execute(sql)
        Below2_5_Rank = self.executer.fetchall()
        A = Below2_5_Rank[int(len(Below2_5_Rank) * 0.125)][0]
        B = Below2_5_Rank[int(len(Below2_5_Rank) * 0.25)][0]
        C = Below2_5_Rank[int(len(Below2_5_Rank) * 0.375)][0]
        D = Below2_5_Rank[int(len(Below2_5_Rank) * 0.5)][0]
        E = Below2_5_Rank[int(len(Below2_5_Rank) * 0.625)][0]
        F = Below2_5_Rank[int(len(Below2_5_Rank) * 0.75)][0]
        G = Below2_5_Rank[int(len(Below2_5_Rank) * 0.875)][0]
        H = Below2_5_Rank[len(Below2_5_Rank) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
        
    @MyLog.myException
    def calculate(self):
        '''
        Below25_RankCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "SELECT count(*) from card where student_id = "+ studentId
        self.executer.execute(sql)
        all = self.executer.fetchone()[0]
        sql = "SELECT count(*) from card where student_id = "+ studentId+" and deal_cost > 0 and deal_cost<2.5"  
        self.executer.execute(sql)
        below25 = self.executer.fetchone()[0]
        rank = below25/all
        sql = "update students set Below2_5_Rank ='" + str(rank) + "' where student_id=" + studentId
        self.executer.execute(sql)
    
    @MyLog.myException
    def rankit(self):
        '''
        Below25_RankCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select Below2_5_Rank from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set Below2_5_Rank='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)