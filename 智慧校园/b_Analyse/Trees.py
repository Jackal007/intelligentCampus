import random
import operator
import DataSetCreater
from math import log
from Model import Student
from Tools import treePlotter

students = []
Student = Student.Student

def createTrainDataSet():
    st,dataSet, labels = DataSetCreater.createTrainDataSet()
    return dataSet, labels

def createTestDataSet():
    students,dataSet, labels = DataSetCreater.createTestDataSet()
    return students,dataSet, labels

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

def randomClass() :  # 随机生成一个'A'~'D'之间的字符并返回
    classlabels = chr(random.randint(0, 3) + ord('A'))
    return classlabels


def classify(inputTree, featLabels, testVec):
    firstSides = list(inputTree.keys())

    firstStr = firstSides[0]  # 挑选首选特征
    print("###first= " + firstStr + "###")
    # firstStr = inputTree.keys()[0]
    #  print(firstStr)
    #  print(featLabels)
    secondDict = inputTree[firstStr]  # 这时secondDict的内容就是决策树按照名称为 firstStr 的特征分类后的结果
    featIndex = featLabels.index(firstStr)  # 找到该特征处于第几列，赋值给featIndex
    print(featIndex)
    new_item = 1  # 标记当前的待分类记录是不是以前从未出现的情况（包括各节点所包含的key的组合），0表示假，1表示真
    for key in secondDict.keys() :
        if testVec[featIndex] == key:
            new_item = 0
            if isinstance(secondDict[key], dict):
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    if new_item == 1:
        return randomClass()

    return classLabel  # classLabel表示最后的分类类型


def createTree(dataSet, labels):
    tlabels = labels[:]
    classList = [example[-1] for example in dataSet]
#     print(classList)
    try:
        if classList.count(classList[0]) == len(classList):
            return classList[0]  # stop splitting when all of the classes are equal
    except:
        return "A"
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

def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename, 'rb')
    return pickle.load(fr)

def Train():
    myDat, labels = createTrainDataSet()
    myTree = createTree(myDat, labels)
    storeTree(myTree, 'dtress.txt')
#     treePlotter.createPlot(myTree)

def Test():
    students,myDat, labels = createTestDataSet()
    myTree = grabTree('dtress.txt')
    #     将结果写入文件
    with open('../d_CorrectRateTest/results.txt', 'w')as f:
        for student in students :
            temp = classify(myTree, labels, student.getAll())
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

if __name__ == '__main__':
    Train()
    Test()

