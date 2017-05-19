import MyDataBase

class StudentSubsidy:

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
        sql="select  * from subsidy"
        self.executer.execute(sql)
        students =self.executer.fetchall()
        for student in students:

            student_id=student[0]
            subsidy=student[1]

            weight=1
            if int(subsidy)==0:
                weight*=0
            else:
                weight*=1

            sql="insert into students(student_id,can) values('"+str(student_id)+"',"+str(weight)+")"
            try:
                self.executer.execute(sql)
            except e:
                print(e)

        self.conn.commit()
        self.db.close()

if __name__=='__main__':
    t=StudentSubsidy(10,20,30,40)
    t.calculate()
