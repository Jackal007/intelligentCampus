from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
import DataCarer
from sklearn import tree
from numpy import *
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
import DataCarer
from numpy import *
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectFromModel, SelectKBest, chi2
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier, VotingClassifier, AdaBoostClassifier
from sklearn import tree
from sklearn import svm
from sklearn.svm import LinearSVC 
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

def createTrainDataSet():
    dataSet = DataCarer.createTrainDataSet()
    DataCarer.transform(dataSet)
    return mat(dataSet)

def createTestDataSet():
    students, dataSet = DataCarer.createTestDataSet()
    DataCarer.transform(dataSet)
    return students, dataSet

# get train data and test data
dataSet = mat(createTrainDataSet())
X_train, Y_train = dataSet[:, :-1], dataSet[:, -1]
students, dataSet = createTestDataSet()
X_test = dataSet

# weak classifiers
clf0 = tree.DecisionTreeClassifier()
clf1 = ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
clf2 = svm.SVC(probability=True)
clf4 = SGDClassifier(alpha=0.0001, average=False, class_weight=None, epsilon=0.1,
        eta0=0.0, fit_intercept=True, l1_ratio=0.15,
        learning_rate='optimal', loss='modified_huber', n_iter=5, n_jobs=1,
        penalty='l2', power_t=0.5, random_state=None, shuffle=True,
        verbose=0, warm_start=False)
clf6 = RandomForestClassifier(random_state=1)
clf7 = GaussianNB()

# stronger classifier
clf0 = AdaBoostClassifier(base_estimator=clf0, learning_rate=1, n_estimators=110, algorithm='SAMME')
clf1 = AdaBoostClassifier(base_estimator=clf1, learning_rate=1, n_estimators=50, algorithm='SAMME')
clf2 = AdaBoostClassifier(base_estimator=clf2, learning_rate=1, n_estimators=1, algorithm='SAMME')
clf4 = AdaBoostClassifier(base_estimator=clf4, learning_rate=1, n_estimators=1, algorithm='SAMME')
clf6 = AdaBoostClassifier(base_estimator=clf6, learning_rate=1, n_estimators=150, algorithm='SAMME')
clf7 = AdaBoostClassifier(base_estimator=clf7, learning_rate=1, n_estimators=150, algorithm='SAMME')
dataset = mat(createTrainDataSet()) 

clf0.fit(X_train,Y_train)
fetureSelection = SelectFromModel(clf0,prefit=True)

print(fetureSelection.get_support(indices=True)) #display importance of each variables

# from sklearn import datasets
# from sklearn.feature_selection import RFE
# from sklearn.linear_model import LogisticRegression
#  
# def createTrainDataSet():
#     dataSet = DataCarer.createTrainDataSet()
#     DataCarer.transform(dataSet)
#     return mat(dataSet)
#   
# dataset = mat(createTrainDataSet())
#   
# X = dataset[:, :-1]
# Y = dataset[:, -1]
# model = LogisticRegression() # build logistic regression model
# rfe = RFE(model,20) # limit number of variables to three
# rfe = rfe.fit(X,Y)
# print(rfe.support_) 
# print(rfe.ranking_)

