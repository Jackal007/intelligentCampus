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
    labels = ['cost_amount', 'cost_avg_dinnerHall','cost_avg_superMarket', 'cost_rate_dinnerhall',  'cost_rate_supermarket', 'cost_times',  'balance_rank', 'subsidy']
    classCount={'A':0,'B':0,'C':0,'D':0}
    for i in dataSet:
        classCount[i[-1]]+=1
    classCount_result=sorted(classCount.items(),key =lambda asd:asd[1], reverse = False)
    print("===============================",classCount_result)
    flag=True
    while flag:
        flag=False
        for i in classCount_result[:-1]:
            if 16*i[1]< classCount_result[-1][1]:
                flag=True
                type =i[0]
                temp =[]
                for student in dataSet :
                    if student[-1] ==type:
                        temp.append(student)
                        classCount[type]+=1
                dataSet.extend(temp)
                
              
                classCount_result=sorted(classCount.items(),key =lambda asd:asd[1], reverse = False)
                print("===============================",classCount_result)
            
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
    labels = ['cost_amount', 'cost_avg_dinnerHall', 'cost_avg_superMarket', 'cost_rate_dinnerhall', 'cost_rate_supermarket', 'cost_times',  'balance_rank']
    conn.close()
    executer.close()
    return students, dataSet, labels

