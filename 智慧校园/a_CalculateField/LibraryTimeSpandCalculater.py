from a_CalculateField import XXCalculater
from Tools import MyLog

class LibraryTimeSpandCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("LibraryTimeSpandCalculater")
        studentId = self.student.getStudentId()
        sql = "insert into library_modify(select student_id,date(date),min(time(date)),max(time(date)),TIMESTAMPDIFF(minute,min(date),max(date)) from library where student_id = " + str(studentId) + " group by date(date))"
        self.executer.execute(sql)
        sql = "SELECT sum(totaltime) FROM library_modify where student_id = " + str(studentId) 
        self.executer.execute(sql)
        LibraryTimeRank = self.executer.fetchone()[0]
        if LibraryTimeRank < self.level["A"]:
            LibraryTimeRank = "A"
        elif LibraryTimeRank < self.level["B"]:
            LibraryTimeRank = "B"
        elif LibraryTimeRank < self.level["C"]:
            LibraryTimeRank = "C"
        else:
            LibraryTimeRank = "D"
        
        sql = "update students set library_time_spand='" + LibraryTimeRank + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return LibraryTimeRank
