from a_CalculateField import XXCalculater
from Tools import MyLog

class LibraryBorrowCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select library_borrow from students order by library_borrow"
        self.executer.execute(sql)
        LibraryBorrow = self.executer.fetchall()
        A = LibraryBorrow[int(len(LibraryBorrow) * 0.25)][0]
        B = LibraryBorrow[int(len(LibraryBorrow) * 0.5)][0]
        C = LibraryBorrow[int(len(LibraryBorrow) * 0.75)][0]
        D = LibraryBorrow[int(len(LibraryBorrow) * 1) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正字计算图书馆借阅量")
        studentId = self.student.getStudentId()
        sql = "select count(student_id) from borrow where student_id=" + str(studentId)
        self.executer.execute(sql)
        libraryBorrow = str(self.executer.fetchone()[0])
        sql = "update students set library_borrow='" + libraryBorrow + "' where student_id=" + str(studentId)
        if self.level is not None:
            libraryBorrow = self.classify(libraryBorrow)
            sql = "update students_rank set cost_amount='" + libraryBorrow + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
