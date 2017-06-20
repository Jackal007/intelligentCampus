import MyDataBase

class StudentRead:

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
        sql="select  student_id from score"
        self.executer.execute(sql)
        students = self.executer.fetchall()
        for student in students:
            student_id=student[0]
            sql="select count(student_id) from brrow where student_id='"+str(student_id)+"'"
            self.executer.execute(sql)

            total=0
            num=0
            data = self.executer.fetchall()
            for row in data:
                read_time=row[0]

                weight=1
                if read_time<self.level_1:
                    weight*=self.level_1
                elif read_time<self.level_2:
                    weight*=self.level_2
                else:
                    weight*=self.level_3

                total+=weight
                num+=1
            try:
                weight=total/(num)
            except:
                weight=0

            sql="update students set book='"+str(weight)+"' where student_id='"+str(student_id)+"' "
            self.executer.execute(sql)

if __name__=='__main__':
    t=StudentRead(10,20,30,40)
    t.calculate()
