from a_CalculateField import XXCalculater

class ScoreCalculater(XXCalculater.XXCalculater):

    def calculate(self):
        print("CalculateScore")

        studentId = self.student.getStudentId()
        sql = "select rank from score where student_id=" + studentId
        self.executer.execute(sql)
        t=scoreRank = self.executer().fetchone()
        if int(scoreRank) < self.level["A"]:
            scoreRank = "A"
        elif int(scoreRank) < self.level["B"]:
            scoreRank = "B"
        elif int(scoreRank) < self.level["C"]:
            scoreRank = "C"
        else:
            scoreRank = "D"

        sql = "insert into students(student_id,score) values('" + str(studentId) + "','" + scoreRank + "')" 
        try:
            self.executer.execute(sql)
            self.conn.commit()
        except:
            print(sql)
            continue
        
        self.db.close()
        return t