from Model import Student
from Tools import MyDataBase


Student = Student.Student
def createTrainDataSet():
#     abs(BaseExceptionC)
    db = MyDataBase.MyDataBase("train")
    conn, executer = db.getConn(), db.getExcuter()
    # get all the students
    sql = "select student_id,score,cost_amount,cost_avg_dinnerHall,cost_avg_laundryroom,cost_avg_superMarket,cost_rate_dinnerhall,cost_rate_laundryroom,cost_rate_supermarket,cost_times,library_borrow,library_times,library_time_spand,balance_rank,subsidy from students"
    executer.execute(sql)
    dataSet = []
    for i in executer.fetchall():
        student = Student(attributes=i, subsidy=i[-1])
        dataSet.append(student.getAll())
#     labels = ['score', 'cost_amount', 'cost_avg_dinnerHall', 'cost_avg_laundryroom', 'cost_avg_superMarket', 'cost_rate_dinnerhall', 'cost_rate_laundryroom', 'cost_rate_supermarket', 'cost_times', 'library_borrow', 'library_times', 'library_time_spand', 'balance_rank', 'subsidy']
    labels = ['cost_amount', 'cost_avg_dinnerHall', 'cost_avg_superMarket', 'cost_rate_dinnerhall',  'cost_rate_supermarket', 'cost_times',  'balance_rank', 'subsidy']
    conn.close()
    executer.close()
    return dataSet, labels
    
def createTestDataSet():
    db = MyDataBase.MyDataBase("test")
    conn, executer = db.getConn(), db.getExcuter()
    # get all the students
    sql = "select student_id,score,cost_amount,cost_avg_dinnerHall,cost_avg_laundryroom,cost_avg_superMarket,cost_rate_dinnerhall,cost_rate_laundryroom,cost_rate_supermarket,cost_times,library_borrow,library_times,library_time_spand,balance_rank,subsidy from students"
    executer.execute(sql)
    students, dataSet = [], []
    for i in executer.fetchall():
        student = Student(attributes=i)
        students.append(student)
        dataSet.append(student.getAll()[0:-1])
#     labels = ['score', 'cost_amount', 'cost_avg_dinnerHall', 'cost_avg_laundryroom', 'cost_avg_superMarket', 'cost_rate_dinnerhall', 'cost_rate_laundryroom', 'cost_rate_supermarket', 'cost_times', 'library_borrow', 'library_times', 'library_time_spand', 'balance_rank']
    labels = ['cost_amount', 'cost_avg_dinnerHall', 'cost_avg_superMarket', 'cost_rate_dinnerhall',  'cost_rate_supermarket', 'cost_times',  'balance_rank']
    conn.close()
    executer.close()
    return students, dataSet, labels

