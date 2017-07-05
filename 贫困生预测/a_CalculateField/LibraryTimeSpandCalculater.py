from a_CalculateField import XXCalculater
from Tools import MyLog

class LibraryTimeSpandCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        A = 90
        B = 120
        C = 150
        D = 180
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算图书馆时长")
        studentId = self.student.getStudentId()
        sql = "insert into library_modify(select student_id,date(date),min(time(date)),max(time(date)),TIMESTAMPDIFF(minute,min(date),max(date)) from library where student_id = " + str(studentId) + " group by date(date))"
        self.executer.execute(sql)
        sql = "SELECT sum(totaltime) FROM library_modify where student_id = " + str(studentId) 
        self.executer.execute(sql)
        
        libraryTimeSpand = self.executer.fetchone()[0]
        libraryTimeSpand = self.classify(libraryTimeSpand)
        
        sql = "update students set library_time_spand='" + libraryTimeSpand + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
