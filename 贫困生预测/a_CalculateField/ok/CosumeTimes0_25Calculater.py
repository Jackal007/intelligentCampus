from a_CalculateField import XXCalculater
from Tools import MyLog

class CosumeTimes0_25Calculater(XXCalculater.XXCalculater):
    def setLevel(self):
        A = 0
        B = 1000
        C = 1500
        D = 2000
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每个学生单次消费金额在0-2.5元之间的次数")
        studentId = str(self.student.getStudentId())
        sql = "select count(*) from card where student_id=" + studentId +" and deal_cost between 0 and 2.5"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s=self.classify(s)
        
        sql = "update students set  consumetimes0_25 ='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
        self.conn.commit()
