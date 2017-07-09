from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class LibraryTimeSpandCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select library_time_spand from students order by library_time_spand"
        self.executer.execute(sql)
        LibraryTimeSpand = self.executer.fetchall()
        A = LibraryTimeSpand[int(len(LibraryTimeSpand) * 0.25)][0]
        B = LibraryTimeSpand[int(len(LibraryTimeSpand) * 0.5)][0]
        C = LibraryTimeSpand[int(len(LibraryTimeSpand) * 0.75)][0]
        D = LibraryTimeSpand[len(LibraryTimeSpand)  - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        '''
            LibraryTimeSpandCalculater
        '''
        studentId = str(self.student.getStudentId())
        if self.level is None:
            studentId = self.student.getStudentId()
            sql = "insert into library_modify(select student_id,date(date),min(time(date)),max(time(date)),TIMESTAMPDIFF(minute,min(date),max(date)) from library where student_id = " + str(studentId) + " group by date(date))"
            self.executer.execute(sql)
            sql = "SELECT sum(totaltime) FROM library_modify where student_id = " + str(studentId) 
            self.executer.execute(sql)
            libraryTimeSpand = str(self.executer.fetchone()[0])
            sql = "update students set library_time_spand='" + libraryTimeSpand + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
        else:
            sql = "select library_time_spand from students where student_id=" + studentId   
            self.executer.execute(sql)
            libraryTimeSpand = self.executer.fetchone()[0]
            libraryTimeSpand = self.classify(libraryTimeSpand)
            sql = "update students_rank set library_time_spand='" + libraryTimeSpand + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
