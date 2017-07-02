from Model import Student
from Tools import MyDataBase


Student = Student.Student
def createDataSet():
    db = MyDataBase.MyDataBase()
    conn, executer = db.getConn(), db.getExcuter()
    # get all the students
    sql = "select student_id,score,cost_amount,cost_avg_superMarket,cost_avg_dinnerHall,cost_supermarket_rate,cost_dinnerhall_rate,cost_times,library_borrow,library_times,library_time_spand,balance_rank,subsidy from students"
    executer.execute(sql)
    students,dataSet  = [], []
    for i in executer.fetchall():
        student = Student(i)
        students.append(student)
        dataSet.append(student.getAll())
    labels = ['score', 'cost_amount', 'cost_avg_superMarket', 'cost_avg_dinnerHall', 'cost_supermarket_rate', 'cost_dinner_rate', 'cost_times', 'library_borrow', 'library_times', 'library_time_spand', 'balance_rank']
    conn.close()
    return dataSet, labels
