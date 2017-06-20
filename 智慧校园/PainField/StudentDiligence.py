import MyDataBase

class StudentDiligence:

    def __init__(self,level_1,level_2,level_3,level_4):
        # levels about the weight
        self.level_1=level_1
        self.level_2=level_2
        self.level_3=level_3
        self.level_4=level_4
        self.db=MyDataBase.MyDataBase()
        self.conn=self.db.getConn()
        self.executer=self.db.getExcuter()

    def calculate(self):
        sql="select  student_id from students order by score"
        self.executer.execute(sql)
        students = self.executer.fetchall()
        for student in students:
            student_id=student[0]

            sql="select count(student_id) from library where student_id='"+str(student_id)+"'"
            self.executer.execute(sql)
            data = self.executer.fetchall()
            total,num=0,0
            for row in data:
                study_time=row[0]
                weight=1
                if study_time<self.level_2:
                    weight*=self.level_1
                elif study_time<self.level_2:
                    weight*=self.level_2
                else:
                    weight*=self.level_3

                total+=weight
                num+=1
            try:
                weight=total/(num)
            except:
                weight=0

            sql="update students set diligence='"+str(weight)+"' where student_id='"+str(student_id)+"' "
            self.executer.execute(sql)
        self.conn.commit()
        self.db.close()

if __name__=='__main__':
    t=StudentDiligence(10,20,30,40)
    t.calculate()
