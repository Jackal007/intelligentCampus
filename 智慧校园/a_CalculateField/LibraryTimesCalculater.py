from a_CalculateField import XXCalculater

class LibraryTimesCalculater(XXCalculater.XXCalculater):
    def calculate(self):
        print("LibraryTimesCalculater")
        
        try:
            studentId = self.student.getStudentId()
            sql="select count(student_id) from library where student_id="+str(studentId)
            self.executer.execute(sql)
            t=studyTimes=self.executer.fetchone()[0]
            if studyTimes<self.level["A"]:
                studyTimes="A"
            elif studyTimes<self.level["B"]:
                studyTimes="B"
            elif studyTimes<self.level["C"]:
                studyTimes="C"
            else:
                studyTimes="D"
            sql="update students set library_times='"+studyTimes+"' where student_id="+str(studentId)
            self.executer.execute(sql)
            self.conn.commit()
        except:
            print(sql)
            pass
        return t