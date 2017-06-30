# -*- coding: utf-8 -*-

from math import log
from Tools import treePlotter
import operator
import pymysql

def calcShannonEnt(dataSet):
    """
    输入：数据集
    输出：数据集的香农熵
    描述：计算给定数据集的香农熵
    """
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    """
    输入：数据集，选择维度，选择值
    输出：划分数据集
    描述：按照给定特征划分数据集；去除选择维度中等于选择值的项
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    """
    输入：数据集
    输出：最好的划分维度
    描述：选择最好的数据集划分维度
    """
    numFeatures = len(dataSet[0]) - 1
    bestGini = 999999.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        gini = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            subProb = len(splitDataSet(subDataSet, -1, 'N')) / float(len(subDataSet))
            gini += prob * (1.0 - pow(subProb, 2) - pow(1 - subProb, 2))
        if (gini < bestGini):
            bestGini = gini
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    """
    输入：分类类别列表
    输出：子节点的分类
    描述：数据集已经处理了所有属性，但是类标签依然不是唯一的，
          采用多数判决的方法决定该子节点的分类
    """
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1))
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    """
    输入：数据集，特征标签
    输出：决策树
    描述：递归构建决策树，利用上述的函数
    """
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        # 类别完全相同，停止划分
        return classList[0]
    if len(dataSet[0]) == 1:
        # 遍历完所有特征时返回出现次数最多的
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    # 得到列表包括节点所有的属性值
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def classify(inputTree, featLabels, testVec):
    """
    输入：决策树，分类标签，测试数据
    输出：决策结果
    描述：跑决策树
    """
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    classLabel = 'N'
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel

def classifyAll(inputTree, featLabels, testDataSet):
    """
    输入：决策树，分类标签，测试数据集
    输出：决策结果
    描述：跑决策树
    """
    classLabelAll = []
    for testVec in testDataSet:
        classLabelAll.append(classify(inputTree, featLabels, testVec))
    return classLabelAll

def storeTree(inputTree, filename):
    """
    输入：决策树，保存文件路径
    输出：
    描述：保存决策树到文件
    """
    import pickle
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    """
    输入：文件路径名
    输出：决策树
    描述：从文件读取决策树
    """
    import pickle
    fr = open(filename, 'rb')
    return pickle.load(fr)

def createDataSet():
    """
    outlook->  0: sunny | 1: overcast | 2: rain
    temperature-> 0: hot | 1: mild | 2: cool
    humidity-> 0: high | 1: normal
    windy-> 0: false | 1: true
    """
    dataSet = []
    db = pymysql.connect("localhost", "root", "root", "intelligentCampustrain")
    cursor = db.cursor()
    sql = "select score,cost_amount,cost_avg_superMarket,cost_avg_dinnerHall,cost_supermarket_rate,cost_dinnerhall_rate,cost_times,library_borrow,library_times,library_time_spand,balance_rank,subsidy from students"
    cursor.execute(sql)
    students = cursor.fetchall()
    for student in students:
        score = student[0]
        cost_amount = student[1]
        cost_avg_superMarket = student[2]
        cost_avg_dinnerHall = student[3]
        cost_supermarket_rate = student[4]
        cost_dinnerhall_rate = student[5]
        cost_times = student[6]
        library_borrow = student[7]
        library_times = student[8]
        library_time_spand = student[9]
        balance_rank = student[10]
        subsidy = student[11]
        data = [score, cost_amount, cost_avg_superMarket, cost_avg_dinnerHall, cost_supermarket_rate, cost_dinnerhall_rate, cost_times, library_borrow, library_times, library_time_spand, balance_rank, subsidy]
        dataSet.append(data)
    # labels = ['outlook', 'temperature', 'humidity', 'windy']
    labels = ['score', ' cost_amount', ' cost_avg_superMarket', ' cost_avg_dinnerHall', ' cost_supermarket_rate', ' cost_dinnerhall_rate', ' cost_times', ' library_borrow', ' library_times', ' library_time_spand', 'balance_rank', 'subsidy', ]
    print(dataSet)
    return dataSet, labels

def createTestSet():
    """
    outlook->  0: sunny | 1: overcast | 2: rain
    temperature-> 0: hot | 1: mild | 2: cool
    humidity-> 0: high | 1: normal
    windy-> 0: false | 1: true
    """
    # testSet = [[0, 1, 0, 0],
    #            [0, 2, 1, 0],
    #            [2, 1, 1, 0],
    #            [0, 1, 1, 1],
    #            [1, 1, 0, 1],
    #            [1, 0, 1, 0],
    #            [2, 1, 0, 1]]
    dataSet = []
    db = pymysql.connect("localhost", "root", "root", "intelligentCampustrain")
    cursor = db.cursor()
    sql = "select score,cost_amount,cost_avg_superMarket,cost_avg_dinnerHall,cost_supermarket_rate,cost_dinnerhall_rate,cost_times,library_borrow,library_times,library_time_spand,balance_rank,subsidy from students"
    cursor.execute(sql)
    students = cursor.fetchall()
    for student in students:
        score = student[0]
        cost_amount = student[1]
        cost_avg_superMarket = student[2]
        cost_avg_dinnerHall = student[3]
        cost_supermarket_rate = student[4]
        cost_dinnerhall_rate = student[5]
        cost_times = student[6]
        library_borrow = student[7]
        library_times = student[8]
        library_time_spand = student[9]
        balance_rank = student[10]
        subsidy = student[11]
        data = [score, cost_amount, cost_avg_superMarket, cost_avg_dinnerHall, cost_supermarket_rate, cost_dinnerhall_rate, cost_times, library_borrow, library_times, library_time_spand, balance_rank, subsidy]
        dataSet.append(data)
    return dataSet

def main():
    dataSet, labels = createDataSet()
    labels_tmp = labels[:]  # 拷贝，createTree会改变labels
    desicionTree = createTree(dataSet, labels_tmp)
    storeTree(desicionTree, 'classifierStorage.txt')
    desicionTree = grabTree('classifierStorage.txt')
    print('desicionTree:\n', desicionTree)
    treePlotter.createPlot(desicionTree)
    testSet = createTestSet()
    print('classifyResult:\n', classifyAll(desicionTree, labels, testSet))

if __name__ == '__main__':
    main()
