from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from numpy import mat
from sklearn.ensemble import ExtraTreesClassifier
import DataSetCreater

def createTrainDataSet():
    dataSet, labels = DataSetCreater.createTrainDataSet()
    transform(dataSet)
    return mat(dataSet), labels

def createTestDataSet():
    students, dataSet, labels = DataSetCreater.createTestDataSet()
    transform(dataSet)
    return students, dataSet, labels

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

dataSet, labels = createTrainDataSet()

X = dataSet[:, :-1]
Y = dataSet[:, -1]
clf = ExtraTreesClassifier(n_estimators=10, max_depth=None,min_samples_split=2, random_state=0)
# clf = BaggingClassifier(KNeighborsClassifier(),max_samples=0.5, max_features=0.5)
clf = clf.fit(X, Y)

students, dataSet, labels = createTestDataSet()

X = dataSet
result = clf.predict(X)
print(result)

with open('../d_CorrectRateTest/results.txt', 'w')as f:
    for i in range(len(students)):
        temp=""
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
