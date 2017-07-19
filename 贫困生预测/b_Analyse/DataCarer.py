from Model import Student
from Tools import MyDataBase

'''
used to deal with the data
'''
Student = Student.Student
def createTrainDataSet():
    '''
    get train data
    '''
    db = MyDataBase.MyDataBase("train")
    conn, executer = db.getConn(), db.getExcuter()
    # get all the students
    executer.execute("select * from students_rank_copy")
    dataSet = []
    for i in executer.fetchall():
        student = Student(studentId=i[0],attributes=list(i[1:-1]), subsidy=i[-1])
        dataSet.append(student.getAll())
    # 处理数据不平衡问题
    # 统计每种类别的个数
    classCount = {'A':0, 'B':0, 'C':0, 'D':0}
    for i in dataSet:
        classCount[(isinstance(i[-1], int) and str(chr(ord('A') + i[-1] - 1))) or str(i[-1])] += 1
    classCount_result = sorted(classCount.items(), key=lambda asd:asd[1], reverse=False)
    flag = True
    while flag:
        flag = False
        for i in classCount_result[:-1]:
            if i[1] > 0 and 4 * i[1] < classCount_result[-1][1]:
                flag = True
                type = i[0]
                temp = []
                for student in dataSet :
                    if ((isinstance(student[-1], int) and str(chr(ord('A') + student[-1] - 1))) or str(student[-1])) == type:
                        t = student[:]
                        temp.append(t)
                        classCount[type] += 1
                dataSet.extend(temp)
                classCount_result = sorted(classCount.items(), key=lambda asd:asd[1], reverse=False)
    conn.close();executer.close()
    transform(dataSet)
    return dataSet
    
def createTestDataSet():
#     '''
#     get test data
#     '''
#     db = MyDataBase.MyDataBase("test")
#     conn, executer = db.getConn(), db.getExcuter()
#     # get all the students
#     executer.execute("select * from students_rank")
#     students, dataSet = [], []
#     for i in executer.fetchall():
#         student = Student(studentId=i[0],attributes=i[1:-1])
#         students.append(student)
#         dataSet.append(student.getAll()[0:-1])
#     conn.close();executer.close()
#     transform(dataSet)
#     return students, dataSet
    '''
    get test data
    '''
    db = MyDataBase.MyDataBase("test")
    conn, executer = db.getConn(), db.getExcuter()
    # get all the students
    executer.execute("select * from students_rank")
    dataSet = []
    students = []
    for i in executer.fetchall():
        student = Student(studentId=i[0],attributes=list(i[1:-1]), subsidy=i[-1])
        dataSet.append(student.getAll())
        students.append(student)
    # 处理数据不平衡问题
    # 统计每种类别的个数
    classCount = {'A':0, 'B':0, 'C':0, 'D':0}
    for i in dataSet:
        classCount[(isinstance(i[-1], int) and str(chr(ord('A') + i[-1] - 1))) or str(i[-1])] += 1
    classCount_result = sorted(classCount.items(), key=lambda asd:asd[1], reverse=False)
    flag = True
    for i in range(len(classCount)):
        print(str(chr(ord('A')+i)),".......",classCount[str(chr(ord('A')+i))])
    while flag:
        flag = False
        for i in classCount_result[:-1]:
            if i[1] > 0 and 4 * i[1] < classCount_result[-1][1]:
                flag = True
                type = i[0]
                tempdateSet = []
                tempstudent = []
                for student in students :
                    if ((isinstance(student[-1], int) and str(chr(ord('A') + student[-1] - 1))) or str(student[-1])) == type:
                        t = student[:]
                        tempdateSet.append(t[1:])
                        tempstudent.append(t[:])
                        classCount[type] += 1
                dataSet.extend(tempdateSet)
                students.extend(tempstudent)
                classCount_result = sorted(classCount.items(), key=lambda asd:asd[1], reverse=False)
    conn.close();executer.close()
#     print(type(students))
    for i in range(len(students)):
#         students[i]=student[i]
        dataSet[i]=dataSet[i][:-1]
    transform(dataSet)
    return students, dataSet

def transform(dataSet):
    '''
    transfrom data to good one
    '''
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
                
def saveResult(students, results, filename):
    '''
    save the result to a file
    '''
    with open('../d_CorrectRateTest/' + filename + '.csv', 'w')as f:
        #提交到网上要求的第一行
#         f.write("studentid,subsidy\n")
        temp = ""
        for student, result in zip(students, results):
            if result == 1:
                temp = 0
            elif result == 2:
                temp = 1000
            elif result == 3:
                temp = 1500
            elif result == 4:
                temp = 2000
            else:
                print("!!!!!!!!!!!!!")
              
            f.write(str(student.getStudentId()) + "," + str(temp) + "\n")