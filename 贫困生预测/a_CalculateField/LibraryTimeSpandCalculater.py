from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import LibraryTimeSpand_level

class LibraryTimeSpandCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("LibraryTimeSpandCalculater")
        studentId = self.student.getStudentId()
        sql = "insert into library_modify(select student_id,date(date),min(time(date)),max(time(date)),TIMESTAMPDIFF(minute,min(date),max(date)) from library where student_id = " + str(studentId) + " group by date(date))"
        self.executer.execute(sql)
        sql = "SELECT sum(totaltime) FROM library_modify where student_id = " + str(studentId) 
        self.executer.execute(sql)
        
        libraryTimeSpand = self.executer.fetchone()[0]
        libraryTimeSpand = self.classify(libraryTimeSpand, LibraryTimeSpand_level)
        
        sql = "update students set library_time_spand='" + libraryTimeSpand + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return libraryTimeSpand
