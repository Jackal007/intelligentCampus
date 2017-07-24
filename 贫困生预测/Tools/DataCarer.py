'''
Created on 2017年7月22日

@author: zhenglongtian
'''
from FeatureCalculate import Student
from Tools import MyDataBase
import random
from sklearn.neighbors import NearestNeighbors
from numpy import mat

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
    executer.execute("select * from students_rank")
    dataSet = []
    for i in executer.fetchall():
        student = Student(studentId=i[0], attributes=list(i[1:-1]), subsidy=i[-1])
        dataSet.append(student.getAll())
    conn.close();executer.close()
    dataSet = mat(dataSet)
    return dataSet[:, :-1], dataSet[:, -1]

def createValidateDataSet():
    '''
    get validate data
    '''
    db = MyDataBase.MyDataBase("validate")
    conn, executer = db.getConn(), db.getExcuter()
    # get all the students
    executer.execute("select * from students_rank")
    students,dataSet = [],[]
    for i in executer.fetchall():
        student = Student(studentId=i[0], attributes=list(i[1:-1]), subsidy=i[-1])
        dataSet.append(student.getAll())
        students.append(student)
    conn.close();executer.close()
    dataSet = mat(dataSet)
    return students,dataSet[:, :-1]
    
def DataImbalanceProcessing(dataSet):
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
            if i[1] > 0 and 20 * i[1] < classCount_result[-1][1]:
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
                
def saveResult(students, results, filename):
    '''
    save the result to a file
    '''
    with open('../AccuracyValidation/results/' + filename + '.csv', 'w')as f:
        # 提交到网上要求的第一行
        f.write("studentid,subsidy\n")
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
                print("it is weird")
              
            f.write(str(student.getStudentId()) + "," + str(temp) + "\n")
# class Smote:
#     def __init__(self, samples, N=10, k=5):
#         self.n_samples, self.n_attrs = samples.shape
#         self.N = N
#         self.k = k
#         self.samples = samples
#         self.newindex = 0
#        # self.synthetic=np.zeros((self.n_samples*N,self.n_attrs))
# 
#     def over_sampling(self):
#         N = int(self.N / 100)
#         self.synthetic = np.zeros((self.n_samples * N, self.n_attrs))
#         neighbors = NearestNeighbors(n_neighbors=self.k).fit(self.samples)
#         print 'neighbors', neighbors
#         for i in range(len(self.samples)):
#             nnarray = neighbors.kneighbors(self.samples[i].reshape(1, -1), return_distance=False)[0]
#             # print nnarray
#             self._populate(N, i, nnarray)
#         return self.synthetic
# 
# 
#     # for each minority class samples,choose N of the k nearest neighbors and generate N synthetic samples.
#     def _populate(self, N, i, nnarray):
#         for j in range(N):
#             nn = random.randint(0, self.k - 1)
#             dif = self.samples[nnarray[nn]] - self.samples[i]
#             gap = random.random()
#             self.synthetic[self.newindex] = self.samples[i] + gap * dif
#             self.newindex += 1
# a = np.array([[1, 2, 3], [4, 5, 6], [2, 3, 1], [2, 1, 2], [2, 3, 4], [2, 3, 4]])
# s = Smote(a, N=100)
# print s.over_sampling()
