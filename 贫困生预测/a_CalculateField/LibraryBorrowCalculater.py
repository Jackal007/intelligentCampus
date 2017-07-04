from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import LibraryBorrow_level

class LibraryBorrowCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("LibraryBorrowCalculater")
        # 对每一个学生统计其借书的次数
        studentId = self.student.getStudentId()
        sql = "select count(student_id) from borrow where student_id=" + str(studentId)
        self.executer.execute(sql)
        libraryBorrow = self.executer.fetchone()[0]
        libraryBorrow = self.classify(libraryBorrow, LibraryBorrow_level)
        sql = "update students set library_borrow='" + libraryBorrow + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return libraryBorrow
