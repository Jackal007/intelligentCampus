import MyDataBase

class StudentCost:

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
            sql="select * from card where student_id='"+str(student_id)+"'"
            self.executer.execute(sql)

            total=0
            num=0
            data = self.executer.fetchall()
            for row in data:
                print("get one line of student : "+str(student_id))
                deal_type=row[1]
                deal_site=row[2]
                deal_way=row[3]
                deal_date=row[4]
                deal_cost=row[5]
                deal_balance=row[6]

                weight=1
                if deal_cost<self.level_1:
                    weight*=self.level_1
                elif deal_cost<self.level_2:
                    weight*=self.level_2
                else:
                    weight*=self.level_3

                total+=weight
                num+=1
            try:
                weight=total/(num)
            except:
                weight=0

            sql="update students set spend='"+str(weight)+"' where student_id='"+str(student_id)+"' "
            self.executer.execute(sql)
        self.conn.commit()
        self.db.close()

if __name__=='__main__':
    t=StudentCost(10,20,30,40)
    t.calculate()
