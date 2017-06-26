from Tools import MyDataBase
from Model import Student

Student=Student.Student
db = MyDataBase.MyDataBase()
conn = db.getConn()
executer = db.getExcuter()
 
sql = "select student_id,score,cost_amount,cost_avg_superMarket,cost_avg_dinnerHall,cost_supermarket_rate,cost_dinnerhall_rate,cost_times,library_borrow,library_times,library_time_spand,balance_rank,subsidy from students"
executer.execute(sql)
students = []
for i in executer.fetchall():
    students.append(Student(i))
    
