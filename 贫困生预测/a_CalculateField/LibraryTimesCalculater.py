from a_CalculateField import XXCalculater
from Tools import MyLog

class LibraryTimesCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select (min(balance)+max(balance))/2 as a from card group by student_id order by a"
        self.executer.execute(sql)
        LibraryTimes = self.executer.fetchall()
        A = int(LibraryTimes * 0.25)
        B = int(LibraryTimes * 0.5)
        C = int(LibraryTimes * 0.5)
        D = int(LibraryTimes * 1)
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算进图书馆次数")
        studentId = self.student.getStudentId()
        sql = "select count(student_id) from library where student_id=" + str(studentId)
        self.executer.execute(sql)
        libraryTimes = self.executer.fetchone()[0]
        libraryTimes = self.classify(libraryTimes)
        sql = "update students set library_times='" + libraryTimes + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
