from sklearn import tree
from numpy import *
import DataSetCreater
from Model import Student
import Output

def createTrainDataSet():
    dataSet = DataSetCreater.createTrainDataSet()
    DataSetCreater.transform(dataSet)
    return mat(dataSet)

def createTestDataSet():
    students, dataSet = DataSetCreater.createTestDataSet()
    DataSetCreater.transform(dataSet)
    return students, dataSet

dataSet = createTrainDataSet()

X = dataSet[:, :-1]
Y = dataSet[:, -1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

students, dataSet = createTestDataSet()

X = dataSet
result = clf.predict(X)
print(result)

Output.output(students, result)
