from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import LibraryTimes_level

class LibraryTimesCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("LibraryTimesCalculater")
        
        studentId = self.student.getStudentId()
        sql = "select count(student_id) from library where student_id=" + str(studentId)
        self.executer.execute(sql)
        libraryTimes = self.executer.fetchone()[0]
        libraryTimes = self.classify(libraryTimes, LibraryTimes_level)
        sql = "update students set library_times='" + libraryTimes + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return libraryTimes
