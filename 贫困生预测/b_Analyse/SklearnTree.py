from sklearn import tree
from numpy import *
import DataSetCreater
from Model import Student
import Output

def createTrainDataSet():
    dataSet, labels = DataSetCreater.createTrainDataSet()
    DataSetCreater.transform(dataSet)
    return mat(dataSet), labels

def createTestDataSet():
    students, dataSet, labels = DataSetCreater.createTestDataSet()
    DataSetCreater.transform(dataSet)
    return students, dataSet, labels

dataSet, labels = createTrainDataSet()

X = dataSet[:, :-1]
Y = dataSet[:, -1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

students, dataSet, labels = createTestDataSet()

X = dataSet
result = clf.predict(X)
print(result)

Output.output(students, result)
