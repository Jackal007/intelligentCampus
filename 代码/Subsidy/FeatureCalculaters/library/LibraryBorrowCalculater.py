from FeatureCalculate import XXCalculater
from Tools import MyLog

class LibraryBorrowCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select library_borrow from students order by library_borrow"
        self.executer.execute(sql)
        LibraryBorrow = self.executer.fetchall()
        A = LibraryBorrow[int(len(LibraryBorrow) * 0.125)][0]
        B = LibraryBorrow[int(len(LibraryBorrow) * 0.25)][0]
        C = LibraryBorrow[int(len(LibraryBorrow) * 0.375)][0]
        D = LibraryBorrow[int(len(LibraryBorrow) * 0.5)][0]
        E = LibraryBorrow[int(len(LibraryBorrow) * 0.625)][0]
        F = LibraryBorrow[int(len(LibraryBorrow) * 0.75)][0]
        G = LibraryBorrow[int(len(LibraryBorrow) * 0.875)][0]
        H = LibraryBorrow[len(LibraryBorrow) - 1][0]
        self.level = [A, B, C, D, E, F, G]
     
    @MyLog.myException
    def calculate(self):
        '''
        LibraryBorrowCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select count(student_id) from borrow where student_id=" + str(studentId)
        self.executer.execute(sql)
        libraryBorrow = str(self.executer.fetchone()[0])
        sql = "update students set library_borrow='" + libraryBorrow + "' where student_id=" + str(studentId)
        self.executer.execute(sql)

    @MyLog.myException
    def rankit(self):
        '''
        LibraryBorrowCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select library_borrow from students where student_id=" + studentId   
        self.executer.execute(sql)
        libraryBorrow = self.executer.fetchone()[0]
        libraryBorrow = self.classify(libraryBorrow)
        sql = "update students_rank set library_borrow='" + libraryBorrow + "' where student_id=" + str(studentId)
        self.executer.execute(sql)