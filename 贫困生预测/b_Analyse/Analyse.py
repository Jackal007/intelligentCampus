from sklearn import linear_model
import DataCarer
from numpy import *
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import  AdaBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectFromModel

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
rf = RandomForestClassifier()


algorithm = [clf0, clf1,clf4,clf5,gnb,rf,clf2]
algorithmName = ['tree', 'ExtraTreesClassifier','SGDClassifier','NearestCentroid','GaussianNB','RandomForestClassifier','SVC']
# for i in range(len(algorithm)):
#     print('-------------------',algorithmName[i],'------------')
#     dataSet = mat(createTrainDataSet())
#     X = dataSet[:, :-1]
#     Y = dataSet[:, -1]
# #     if i == 3:
# #         scaler = StandardScaler()  
# #         # Don't cheat - fit only on training data
# #         scaler.fit(X)  
# #         X_train = scaler.transform(X)  
# #         # apply same transformation to test data
# #         X_test = scaler.transform(Y)  
# 
#     algorithm[i].fit(X, Y)
#     if i == 5:
#         RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#             max_depth=None, max_features='auto', max_leaf_nodes=None,
#             min_samples_leaf=1, min_samples_split=2,
#             min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
#             oob_score=False, random_state=None, verbose=0,
#             warm_start=False)
#         
#     students, dataSet = createTestDataSet()
#     X = dataSet
#     result=list()
#     if i!=5:
#         result = algorithm[i].predict(X)
#     else :
#         resultOFrandom=algorithm[i].predict_proba(X)
#         for j in range(len(resultOFrandom)) :
#             index =0
#             max = 0
#             for m in range(len(resultOFrandom[j])) :
#                 if resultOFrandom[j][m]> max:
#                     index = m
#                     max = resultOFrandom[j][index]
#             print(j)
#             print(index)
#             result.append(index+1)
#         
#     DataCarer.saveResult(students, result, algorithmName[i])
#     print(result)

dataSet = mat(createTrainDataSet())
X = dataSet[:, :-1]
Y = dataSet[:, -1]
clf2.fit(X,Y)
ada_real=AdaBoostClassifier(base_estimator=clf2,learning_rate=1,n_estimators=100,algorithm='SAMME')
ada_real.fit(X,Y)
students, dataSet = createTestDataSet()
X = dataSet
result=ada_real.predict(X)
DataCarer.saveResult(students, result, "")
