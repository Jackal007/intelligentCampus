import DataCarer
from numpy import *
from sklearn import tree
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import svm
from sklearn.svm import LinearSVC 
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import  AdaBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

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
clf3 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf4 = SGDClassifier(loss="hinge", penalty="l2")
clf5 = NearestCentroid()
clf6 = RandomForestClassifier(random_state=1)
clf7 = GaussianNB()

# stronger classifier
clf0 = AdaBoostClassifier(base_estimator=clf0, learning_rate=1, n_estimators=100, algorithm='SAMME')
clf1 = AdaBoostClassifier(base_estimator=clf1, learning_rate=1, n_estimators=100, algorithm='SAMME')
clf2 = AdaBoostClassifier(base_estimator=clf2, learning_rate=1, n_estimators=1, algorithm='SAMME')
clf3 = AdaBoostClassifier(base_estimator=clf3, learning_rate=1, n_estimators=100, algorithm='SAMME')
clf4 = AdaBoostClassifier(base_estimator=clf4, learning_rate=1, n_estimators=100, algorithm='SAMME')
clf5 = AdaBoostClassifier(base_estimator=clf5, learning_rate=1, n_estimators=100, algorithm='SAMME')
clf6 = AdaBoostClassifier(base_estimator=clf6, learning_rate=1, n_estimators=100, algorithm='SAMME')
clf7 = AdaBoostClassifier(base_estimator=clf7, learning_rate=1, n_estimators=100, algorithm='SAMME')

# final classifier
finalClassifier = VotingClassifier(estimators=[
       ('0', clf0), ('1', clf1), ('2', clf2),  ('6', clf7), ('7', clf7)],
       voting='soft',weights=[1,3,3,1,1])

# feature selection 
fetureSelection = SelectFromModel(clf1)

clf = Pipeline([
#   ('feature_selection', SelectKBest(chi2, k=2)),
  ('feature_selection', fetureSelection),
  ('classification', finalClassifier)
])
clf.fit(X_train, Y_train)
result = clf.predict(X_test)

# result=ada_real.predict(X_test)
DataCarer.saveResult(students, result, "result")


