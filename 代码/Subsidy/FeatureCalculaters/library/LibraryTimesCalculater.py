from FeatureCalculate import XXCalculater
from Tools import MyLog

class LibraryTimesCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select library_times from students order by library_times"
        self.executer.execute(sql)
        LibraryTimes = self.executer.fetchall()
        A = LibraryTimes[int(len(LibraryTimes) * 0.125)][0]
        B = LibraryTimes[int(len(LibraryTimes) * 0.25)][0]
        C = LibraryTimes[int(len(LibraryTimes) * 0.375)][0]
        D = LibraryTimes[int(len(LibraryTimes) * 0.5)][0]
        E = LibraryTimes[int(len(LibraryTimes) * 0.625)][0]
        F = LibraryTimes[int(len(LibraryTimes) * 0.75)][0]
        G = LibraryTimes[int(len(LibraryTimes) * 0.875)][0]
        H = LibraryTimes[len(LibraryTimes) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
    @MyLog.myException
    def calculate(self):
        '''
        LibraryTimesCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select count(student_id) from library where student_id=" + str(studentId)
        self.executer.execute(sql)
        libraryTimes = str(self.executer.fetchone()[0])
        sql = "update students set library_times='" + libraryTimes + "' where student_id=" + str(studentId)
        self.executer.execute(sql)

    @MyLog.myException
    def rankit(self):
        '''
        LibraryTimesCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select library_times from students where student_id=" + studentId   
        self.executer.execute(sql)
        libraryTimes = self.executer.fetchone()[0]
        libraryTimes = self.classify(libraryTimes)
        sql = "update students_rank set library_times='" + libraryTimes + "' where student_id=" + str(studentId)
        self.executer.execute(sql)