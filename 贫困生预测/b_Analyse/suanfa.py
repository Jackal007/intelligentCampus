from sklearn import linear_model
import DataCarer
from numpy import *
from Tools import MyDataBase
from sklearn import tree
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.naive_bayes import GaussianNB



def createTrainDataSet():
    dataSet = DataCarer.createTrainDataSet()
    DataCarer.transform(dataSet)
    return mat(dataSet)

def createTestDataSet():
    students, dataSet = DataCarer.createTestDataSet()
    DataCarer.transform(dataSet)
    return students, dataSet

# dataSet = createTrainDataSet()
clf0 = tree.DecisionTreeClassifier()
clf1 = ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
clf2 = svm.SVC()
clf3 = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
clf4 = SGDClassifier(loss="hinge", penalty="l2")
clf5 = NearestCentroid()
gnb = GaussianNB()
algorithm = [clf0, clf1,clf2,clf4,clf5,gnb]
algorithmName = ['tree', 'ExtraTreesClassifier','SVC','SGDClassifier','NearestCentroid','GaussianNB']
for i in range(len(algorithm)):
    dataSet = mat(createTrainDataSet())
    X = dataSet[:, :-1]
    Y = dataSet[:, -1]
#     if i == 3:
#         scaler = StandardScaler()  
#         # Don't cheat - fit only on training data
#         scaler.fit(X)  
#         X_train = scaler.transform(X)  
#         # apply same transformation to test data
#         X_test = scaler.transform(Y)  

    algorithm[i].fit(X, Y)
    students, dataSet = createTestDataSet()
    X = dataSet
    result = algorithm[i].predict(X)
    DataCarer.saveResult(students, result, algorithmName[i])
    print(result)



