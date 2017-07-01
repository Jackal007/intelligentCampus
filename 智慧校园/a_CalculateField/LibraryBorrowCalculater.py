from a_CalculateField import XXCalculater

class LibraryBorrowCalculater(XXCalculater.XXCalculater):

    def calculate(self):
        print("LibraryBorrowCalculater")
        # 对每一个学生统计其借书的次数
        try:
            studentId = self.student.getStudentId()
            sql = "select count(student_id) from borrow where student_id=" + str(studentId)
            self.executer.execute(sql)
            t = readTimes = self.executer.fetchone()[0]
            if readTimes < self.level["A"]:
                readTimes = "A"
            elif readTimes < self.level["B"]:
                readTimes = "B"
            elif readTimes < self.level["C"]:
                readTimes = "C"
            else:
                readTimes = "D"
            sql = "update students set library_borrow='" + readTimes + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
            self.conn.commit()
        except:
            print(sql)
            pass
        return t