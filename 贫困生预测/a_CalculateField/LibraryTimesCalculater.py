from a_CalculateField import XXCalculater
from Tools import MyLog

class LibraryTimesCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select library_times from students order by library_times"
        self.executer.execute(sql)
        LibraryTimes = self.executer.fetchall()
        A = LibraryTimes[int(len(LibraryTimes) * 0.25)][0]
        B = LibraryTimes[int(len(LibraryTimes) * 0.5)][0]
        C = LibraryTimes[int(len(LibraryTimes) * 0.75)][0]
        D = LibraryTimes[len(LibraryTimes) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算进图书馆次数")
        studentId = self.student.getStudentId()
        sql = "select count(student_id) from library where student_id=" + str(studentId)
        self.executer.execute(sql)
        libraryTimes = str(self.executer.fetchone()[0])
        sql = "update students set library_times='" + libraryTimes + "' where student_id=" + str(studentId)
        if self.level is not None:
            libraryTimes = self.classify(libraryTimes)
            sql = "update students_rank set library_times='" + libraryTimes + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
