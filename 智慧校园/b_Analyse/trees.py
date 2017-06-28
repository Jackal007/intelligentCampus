'''
Created on Oct 12, 2010
Decision Tree Source Code for Machine Learning in Action Ch. 3
@author: Peter Harrington
'''
from Model import Student
from math import log
import operator
import treePlotter
from Tools import MyDataBase

students = []
Student = Student.Student
def createDataSet():
    db = MyDataBase.MyDataBase()
    conn = db.getConn()
    executer = db.getExcuter()
    # get all the students
    sql = "select student_id,score,cost_amount,cost_avg_superMarket,cost_avg_dinnerHall,cost_supermarket_rate,cost_dinnerhall_rate,cost_times,library_borrow,library_times,library_time_spand,balance_rank,subsidy from students"
    executer.execute(sql)
    dataSet = []
    for i in executer.fetchall():
        student = Student(i)
        students.append(student)
        dataSet.append([student.getScore(), student.getCost_amount(), student.getCost_avg_superMarket(), student.getCost_avg_dinnerHall(), student.getCost_supermarket_rate(), student.getCost_dinnerhall_rate(), student.getCost_times(), student.getLibrary_borrow(), student.getLibrary_times(), student.getLibrary_time_spand(), student.getBalance_rank(),student.getSubsidy()])
    labels = ['score', 'cost_amount', 'cost_avg_superMarket', 'cost_avg_dinnerHall', 'cost_supermarket_rate', 'cost_dinner_rate', 'cost_times', 'library_borrow', 'library_times', 'library_time_spand', 'balance_rank']
    # change to discrete values
    print(len(dataSet))
    return dataSet, labels

"""计算香农熵"""
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:  # the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)  # log base 2
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  # chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0;
    bestFeature = 0
    for i in range(numFeatures):  # iterate over all the features
        featList = [example[i] for example in dataSet]  # create a list of all the examples of this feature
        uniqueVals = set(featList)  # get a set of unique values
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy  # calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):  # compare this to the best gain so far
            bestInfoGain = infoGain  # if better than current best, set to best
            bestFeature = i
    return bestFeature  # returns an integer


def majorityCnt(classList):
#     print("民主投票")
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    tlabels=labels[:]
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]  # stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1:  # stop splitting when there are no more features in dataSet
#         print("民主投票")
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = tlabels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (tlabels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        
        subLabels = tlabels[:]  # copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def classify(inputTree, featLabels, testVec):
    firstSides = list(inputTree.keys())
#     print("***********", firstSides, "*************")
    firstStr = firstSides[0]  # 挑选首选特征
    secondDict = inputTree[firstStr]  # 这时secondDict的内容就是决策树按照名称为 firstStr 的特征分类后的结果
    featIndex = featLabels.index(firstStr)  # 找到该特征处于第几列，赋值给featIndex
    key = testVec[featIndex]  # 获得待分类的记录该特征的具体值

#     print("-----------------------------------------------------")
#     print("特征名为：", firstStr, "特征的列数为：", featIndex, "----特征值为：", key)
#     print("有效特征值包括：", list(secondDict.keys()))
#     print("-----------------------------------------------------")

    valueOfFeat = secondDict[key]

    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else:
        classLabel = valueOfFeat
    return classLabel  # classLabel表示最后的分类类型

def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)


myDat, labels = createDataSet()
myTree = createTree(myDat, labels)
# treePlotter.createPlot(myTree)
 
f = open('../d_CorrectRateTest/results.txt', 'w')
for student in students :
    temp = classify(myTree, labels, [student.getScore(), student.getCost_amount(), student.getCost_avg_superMarket(), student.getCost_avg_dinnerHall(), student.getCost_supermarket_rate(), student.getCost_dinnerhall_rate(), student.getCost_times(), student.getLibrary_borrow(), student.getLibrary_times(), student.getLibrary_time_spand(), student.getBalance_rank()])
    if temp == "A":
        temp = 0
    elif temp == "B":
        temp = 1000
    elif temp == "C":
        temp = 1500
    elif temp == "D":
        temp = 2000
    else:
        print("!!!!!!!!!!!!!")
     
    f.write(str(student.getStudentId()) + "," + str(temp) + "\n")
 
f.close()
