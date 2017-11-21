'''
Created on 2017年7月22日
 
@author: zhenglongtian
'''
from Tools import DataCarer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
 
class SingleClassifier():
    def __init__(self):
        # weak classifier
        self.clf = None
        # get train data
        self.X, self.Y = DataCarer.createTrainDataSet()
         
    def getBestOne(self, name):
        # if the classifier has already generated
        try:
            from sklearn.externals import joblib
            clf = joblib.load(name + '.pkl')
            return clf
        except:
            pass
         
        # if the classifier is not exists
        # search for the best loop time 
        bestAccuracyRate, n_estimators = 0, 1
        for loopTimes in range(2, 200):
            
            sclf = AdaBoostClassifier(base_estimator=self.clf, learning_rate=1, n_estimators=loopTimes, algorithm='SAMME')
            
            # cross validation to get the score
            X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y, test_size=0.1, random_state=0)
            sclf.fit(X_train, Y_train)
            accuracyRate = sclf.score(X_test, Y_test)
            
            if accuracyRate > bestAccuracyRate:
                bestAccuracyRate = accuracyRate
                n_estimators = loopTimes
        
        # save the classifier as a dump
        joblib.dump(sclf, name + '.pkl')
        
        return AdaBoostClassifier(base_estimator=self.clf, learning_rate=1, n_estimators=n_estimators, algorithm='SAMME')
