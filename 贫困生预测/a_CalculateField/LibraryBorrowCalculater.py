from a_CalculateField import XXCalculater
from Tools import MyLog

class LibraryBorrowCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select COUNT(*) as c from borrow group by student_id order by c"
        self.executer.execute(sql)
        LibraryBorrows = self.executer.fetchone()[0]
        A = int(LibraryBorrows * 0.25)
        B = int(LibraryBorrows * 0.5)
        C = int(LibraryBorrows * 0.5)
        D = int(LibraryBorrows * 1)
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正字计算图书馆借阅量")
        studentId = self.student.getStudentId()
        sql = "select count(student_id) from borrow where student_id=" + str(studentId)
        self.executer.execute(sql)
        libraryBorrow = self.executer.fetchone()[0]
        libraryBorrow = self.classify(libraryBorrow)
        sql = "update students set library_borrow='" + libraryBorrow + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
