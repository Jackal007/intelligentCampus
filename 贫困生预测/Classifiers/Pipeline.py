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
from sklearn.feature_selection import RFE
from sklearn.feature_selection import f_regression
import AccuracyTest.CorrectRateTest as CorrectRateTest

def createTrainDataSet():
    dataSet = DataCarer.createTrainDataSet()
    DataCarer.transform(dataSet)
    return mat(dataSet)

def createTestDataSet():
    students, dataSet = DataCarer.createTestDataSet()
    DataCarer.transform(dataSet)
    return students, dataSet

# get train data and test data
X_train, Y_train = DataCarer.createTrainDataSet()
students, dataSet = DataCarer.createTestDataSet()
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

# final classifier
finalClassifier = VotingClassifier(estimators=[
       ('0', clf0),('1', clf1),('2', clf2),('4', clf4),('6', clf6),],
       voting='soft',
       weights=[1,3,1,1,3])

# feature selection 
fetureSelection = SelectFromModel(clf0)
anova_filter = SelectKBest(f_regression, k=10)
clf = Pipeline([
#   ('feature_selection', SelectKBest(chi2, k=2)),
  ('anova_filter', anova_filter),
  ('classification', finalClassifier)
])
k=37

outfile=open("outFile",'w')
print(len(X_train))
print(len(X_test))
while(k>0):
    clf.set_params(anova_filter__k=k)
    clf.fit(X_train, Y_train)
    result = clf.predict(X_test)
    
    # result=ada_real.predict(X_test)
    DataCarer.saveResult(students, result, str("result"+str(k)))

    outfile.write(str(str(k)+"___"+str(CorrectRateTest.CorrectRate(str("result"+str(k))))))
    outfile.write("\n")
    k=k-1
# print(anova_filter.get_support(indices))
# print(anova_filter.scores_)

