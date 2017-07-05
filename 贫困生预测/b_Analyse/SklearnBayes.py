from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from numpy import mat
from sklearn.ensemble import ExtraTreesClassifier
import DataSetCreater
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
clf = ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
# clf = BaggingClassifier(KNeighborsClassifier(),max_samples=0.5, max_features=0.5)
clf = clf.fit(X, Y)

students, dataSet, labels = createTestDataSet()

X = dataSet
result = clf.predict(X)

Output.output(students, result)

