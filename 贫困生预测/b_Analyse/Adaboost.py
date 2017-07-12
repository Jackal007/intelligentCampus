from sklearn import linear_model
import DataCarer
from numpy import mat
from sklearn import tree
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import  AdaBoostClassifier



def createTrainDataSet():
    dataSet = DataCarer.createTrainDataSet()
    DataCarer.transform(dataSet)
    return mat(dataSet)

def createTestDataSet():
    students, dataSet = DataCarer.createTestDataSet()
    DataCarer.transform(dataSet)
    return students, dataSet

clf0 = tree.DecisionTreeClassifier()
clf1 = ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
clf2 = svm.SVC()
clf3 = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
clf4 = SGDClassifier(loss="hinge", penalty="l2")
clf5 = NearestCentroid()
gnb = GaussianNB()
rf = RandomForestClassifier()

dataSet = mat(createTrainDataSet())
X = dataSet[:, :-1]
Y = dataSet[:, -1]
clf2.fit(X,Y)
ada_real=AdaBoostClassifier(base_estimator=clf2,learning_rate=1,n_estimators=100,algorithm='SAMME')
ada_real.fit(X,Y)
students, dataSet = createTestDataSet()
X = dataSet
result=ada_real.predict(X)
DataCarer.saveResult(students, result, "result")
