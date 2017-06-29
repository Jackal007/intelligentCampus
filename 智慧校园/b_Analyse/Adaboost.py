from numpy import *
from Model import Student
from test.test_audioop import datas

Student = Student.Student
students = {"A":[], "B":[], "C":[], "D":[]}
students_copy = []
labels = ['score', 'cost_amount', 'cost_avg_superMarket', 'cost_avg_dinnerHall', 'cost_supermarket_rate', 'cost_dinner_rate', 'cost_times', 'library_borrow', 'library_times', 'library_time_spand', 'balance_rank']
 
def loadDataSet(): 
    from Tools import MyDataBase 
    db = MyDataBase.MyDataBase()
    conn = db.getConn()
    executer = db.getExcuter()
    
    # 从这边读取到所有学生的id
    sql = "select student_id,score,cost_amount,cost_avg_superMarket,cost_avg_dinnerHall,cost_supermarket_rate,cost_dinnerhall_rate,cost_times,library_borrow,library_times,library_time_spand,balance_rank,subsidy from students"
    executer.execute(sql)
    for i in executer.fetchall():
        student = Student(i)
        students[student.getSubsidy()].append(student)
        students_copy.append(student)
    
def getDataSet(ABCD):
    dataSet = []
    labelSet = []
    student_t = []
    for i in range(len(students_copy)):
        student=students_copy[i]
        if student.getStudentId() != -1:
            student_t.append(i)
            dataSet.append([student.getScore(), student.getCost_amount(), student.getCost_avg_superMarket(), student.getCost_avg_dinnerHall(), student.getCost_supermarket_rate(), student.getCost_dinnerhall_rate(), student.getCost_times(), student.getLibrary_borrow(), student.getLibrary_times(), student.getLibrary_time_spand(), student.getBalance_rank(), student.getSubsidy()])
            labelSet.append(2 * int(student.getSubsidy() == ABCD) - 1)
    return student_t, dataSet

def getTrainDataSet(ABCD):
    dataSet = []
    labelSet = []
    for i in ABCD:
        for student in students[i]:
            dataSet.append([student.getScore(), student.getCost_amount(), student.getCost_avg_superMarket(), student.getCost_avg_dinnerHall(), student.getCost_supermarket_rate(), student.getCost_dinnerhall_rate(), student.getCost_times(), student.getLibrary_borrow(), student.getLibrary_times(), student.getLibrary_time_spand(), student.getBalance_rank(), student.getSubsidy()])
            labelSet.append(2 * int(student.getSubsidy() == ABCD) - 1)
    return dataSet, labelSet

'''
因为adaboost做的是二分类，所以这里要把ABCD四类分成 3个分类器来做
'''
def treesClassifier_A_BCD(dataSet):
    # 分 A 和其他的
    import Trees
    myTree = Trees.createTree(dataSet, labels)
    retArray = ones((shape(dataSet)[0], 1))
    result = []
    for data in dataSet:
        temp = Trees.classify(myTree, labels, data)
        if temp == "A":
            result.append([1.0])
        else:
            result.append([-1.0])
    retArray[mat(result)[:, 0] == -1.0] = -1.0
    return retArray

def treesClassifier_B_CD(dataSet):
    # 除了A外的分 B 和其他的
    import Trees
    myTree = Trees.createTree(dataSet, labels)
    retArray = ones((shape(dataSet)[0], 1))
    result = []
    for data in dataSet:
        temp = Trees.classify(myTree, labels, data)
        if temp == "B":
            result.append([1.0])
        else:
            result.append([-1.0])
    retArray[mat(result)[:, 0] == -1.0] = -1.0
    return retArray

def treesClassifier_C_D(dataSet):
    # 除了A、B外的分 C 和 D
    import Trees
    myTree = Trees.createTree(dataSet, labels)
    retArray = ones((shape(dataSet)[0], 1))
    result = []
    for data in dataSet:
        temp = Trees.classify(myTree, labels, data)
        if temp == "C":
            result.append([1.0])
        else:
            result.append([-1.0])
    retArray[mat(result)[:, 0] == -1.0] = -1.0
    return retArray
 
def buildTreeClassifier(classifier, dataArr, classLabels, D):
    '''
    D是错误权值计算要用到的加权数，分类器和adaboost交互的地方
    '''
    dataMatrix = mat(dataArr)
    predictedVals = classifier(dataArr)  # predictedVals保存分类器的预测结果
#     classifier={}
    labelMat = mat(classLabels).T
    m, n = shape(dataMatrix)  # m表示有几行数据，n表示有几个特征
    clasEst = mat(zeros((m, 1)))  # 分类结果，类别标签
    errArr = mat(ones((m, 1)))
    errArr[predictedVals == labelMat] = 0
    weightedError = D.T * errArr  # calc total error multiplied by D
    error = weightedError
    clasEst = predictedVals.copy()
    classifier = {}
    return classifier, error, clasEst

def adaBoostTrain(classifier, dataArr, classLabels, numIt=1):
    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m, 1)) / m)  # init D to all equal
    aggClassEst = mat(zeros((m, 1)))  # 储存分类结果
    for i in range(numIt):
        classify, error, classEst = buildTreeClassifier(classifier, dataArr, classLabels, D)  # build Stump
        # 计算一些东西
        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16)))  # calc alpha, throw in max(error,eps) to account for error=0
        classify['alpha'] = alpha  
        weakClassArr.append(classify)  # store Stump Params in Array
        expon = multiply(-1 * alpha * mat(classLabels).astype('float64').T, classEst)  # exponent for D calc, getting messy
        D = multiply(D, exp(expon))  # Calc New D for next iteration
        D = D / D.sum()
        # calc training error of all classifiers, if this is 0 quit for loop early (use break)
        aggClassEst += alpha * classEst
        # print ("aggClassEst: ",aggClassEst.T)
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggErrors.sum() / m
#         print ("total error: ", errorRate)
        if errorRate == 0.0: break
    return weakClassArr, aggClassEst
  
def adaClassify(classify,datSet, classifierArr):
    dataMatrix = mat(datSet)
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m, 1)))  # 储存分类结果
    for i in range(len(classifierArr)):
        classEst = classify(datSet)  # call classify
        aggClassEst += classifierArr[i]['alpha'] * classEst  # 计算分类结果，每个弱分类器的权值不一样，大家算好后加在一起就是结果
    return sign(aggClassEst)  # 因为是一个浮点数，而结果是1或者-1，所以需要调用sign函数

if __name__ == '__main__':
    
    loadDataSet()
    with open("../d_CorrectRateTest/results.txt", 'w')as f:
        dataSet, labelSet = getTrainDataSet("ABCD")
        weakClassArr, aggClassEst = adaBoostTrain(treesClassifier_A_BCD, dataSet, labelSet)
        
        student_t, dataSet = getDataSet("A")
        result = adaClassify(treesClassifier_A_BCD,dataSet, weakClassArr)
         
        for i in range(len(student_t)):
            r = int(result[i][0, 0])
            if r == 1:
                f.write(str(students_copy[student_t[i]].getStudentId()) + ",0\n")
                students_copy[student_t[i]].setStudentId(-1)
        
        dataSet, labelSet = getTrainDataSet("BCD")
        weakClassArr, aggClassEst = adaBoostTrain(treesClassifier_B_CD, dataSet, labelSet)
          
        student_t, dataSet = getDataSet("B")
        result = adaClassify(treesClassifier_B_CD,dataSet, weakClassArr)
         
        for i in range(len(student_t)):
            r = int(result[i][0, 0])
            if r == 1:
                f.write(str(students_copy[student_t[i]].getStudentId()) + ",1000\n")
                students_copy[student_t[i]].setStudentId(-1)
        
        dataSet, labelSet = getTrainDataSet("CD")
        weakClassArr, aggClassEst = adaBoostTrain(treesClassifier_C_D, dataSet, labelSet)
        
        student_t, dataSet = getDataSet("C")
        print(len(student_t))
        print(len(dataSet))
        result = adaClassify(treesClassifier_C_D,dataSet, weakClassArr)
         
        for i in range(len(student_t)):
            r = int(result[i][0, 0])
            if r == 1:
                f.write(str(students_copy[student_t[i]].getStudentId()) + ",1500\n")
            elif r == -1:
                f.write(str(students_copy[student_t[i]].getStudentId()) + ",2000\n")
