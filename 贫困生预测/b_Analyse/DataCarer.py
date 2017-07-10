from Model import Student
from Tools import MyDataBase


Student = Student.Student
def createTrainDataSet():
    db = MyDataBase.MyDataBase("train")
    conn, executer = db.getConn(), db.getExcuter()
    # get all the students
    sql = "select student_id,score,cost_amount,cost_variance,cost_avg_day_superMarket,cost_avg_day_laundryroom,cost_avg_day_dinnerHall,cost_rate_supermarket,cost_rate_laundryroom,cost_rate_dinnerhall,cost_times_day_supermarket,cost_times_day_dinnerhall,cost_times_day_laundry,cost_times,library_borrow,library_times,library_time_spand,balance_rank,card_days,time6_7costs,time7_8costs,totaldinnercosts,avgdayscosts,consumetimes11_12,consumetimes0_25,countcost0_10,cardrecharge,maxcost7_8,subsidy from students_rank"
    executer.execute(sql)
    dataSet = []
    for i in executer.fetchall():
        student = Student(attributes=i, subsidy=i[-1])
        dataSet.append(student.getAll())
    classCount = {'A':0, 'B':0, 'C':0, 'D':0}
    for i in dataSet:
#         print((isinstance(i[-1],int)))
#         print(str(chr(ord('A')+i[-1])))
#         print(str(i[-1]))
#         print((isinstance(i[-1],int) and str(chr(ord('A')+i[-1]-1))) or str(i[-1]))
        classCount[(isinstance(i[-1],int) and str(chr(ord('A')+i[-1]-1))) or str(i[-1])] += 1
    classCount_result = sorted(classCount.items(), key=lambda asd:asd[1], reverse=False)
#     print("===============================",classCount_result)
    flag = True
    while flag:
        flag = False
        for i in classCount_result[:-1]:
            if i[1]>0 and 4 * i[1] < classCount_result[-1][1]:
#                 print(i)
#                 print(classCount_result[-1][1])
                flag = True
                type = i[0]
                temp = []
                for student in dataSet :
                    if ((isinstance(student[-1],int) and str(chr(ord('A')+student[-1]-1))) or str(student[-1])) == type:
#                         print(type)
                        t=student[:]
                        temp.append(t)
                        classCount[type] += 1
                dataSet.extend(temp)
                classCount_result = sorted(classCount.items(), key=lambda asd:asd[1], reverse=False)
#                 print("===============================",classCount_result)
    conn.close()
    executer.close()
    transform(dataSet)
    return dataSet
    
def createTestDataSet():
    db = MyDataBase.MyDataBase("test")
    conn, executer = db.getConn(), db.getExcuter()
    # get all the students
    sql = "select * from students_rank"
    executer.execute(sql)
    students, dataSet = [], []
    for i in executer.fetchall():
        student = Student(attributes=i)
        students.append(student)
        dataSet.append(student.getAll()[0:-1])
#     labels = ['score', 'cost_amount', 'cost_avg_dinnerHall', 'cost_avg_laundryroom', 'cost_avg_superMarket', 'cost_rate_dinnerhall', 'cost_rate_laundryroom', 'cost_rate_supermarket', 'cost_times', 'library_borrow', 'library_times', 'library_time_spand', 'balance_rank']
    conn.close()
    executer.close()
    transform(dataSet)
    return students, dataSet

def transform(dataSet):
    for i in range(len(dataSet)):
        for j in range(len(dataSet[i])):
            if dataSet[i][j] == 'A':
                dataSet[i][j] = 1
            elif dataSet[i][j] == 'B':
                dataSet[i][j] = 2
            elif dataSet[i][j] == 'C':
                dataSet[i][j] = 3
            elif dataSet[i][j] == 'D':
                dataSet[i][j] = 4
                
def saveResult(students, result, algorithm):
    with open('../d_CorrectRateTest/results_' + algorithm + '.csv', 'w')as f:
#         f.write("studentid,subsidy\n")
        temp = ""
        for i in range(len(students)):
            if result[i] == 1:
                temp = 0
            elif result[i] == 2:
                temp = 1000
            elif result[i] == 3:
                temp = 1500
            elif result[i] == 4:
                temp = 2000
            else:
                print("!!!!!!!!!!!!!")
              
            f.write(str(students[i].getStudentId()) + "," + str(temp) + "\n")
    
