from a_CalculateField import XXCalculater

class LibraryTimeSpandCalculater(XXCalculater.XXCalculater):

    def calculate(self):
        print("LibraryTimeSpandCalculater")
        try:
            studentId = self.student.getStudentId()
            sql = "insert into library_modify(select student_id,date(date),min(time(date)),max(time(date)),TIMESTAMPDIFF(minute,min(date),max(date)) from library where student_id = " + str(studentId) + " group by date(date))"
            self.executer.execute(sql)
            sql = "SELECT sum(totaltime) FROM library_modify where student_id = " + str(studentId) 
            self.executer.execute(sql)
            student_LibraryTime = self.executer.fetchone()[0]
            if student_LibraryTime < self.level["A"]:
                LibraryTimeRank = "A"
            elif student_LibraryTime < self.level["B"]:
                LibraryTimeRank = "B"
            elif student_LibraryTime < self.level["C"]:
                LibraryTimeRank = "C"
            else:
                LibraryTimeRank = "D"
            
            sql = "update students set library_time_spand='" + LibraryTimeRank + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
            self.conn.commit()
        except:
            print(sql)
            pass
