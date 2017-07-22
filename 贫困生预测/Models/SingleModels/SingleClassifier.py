'''
Created on 2017年7月22日
 
@author: zhenglongtian
'''
import DataCarer
from numpy import *
from Tools import DataCarer
from sklearn.ensemble import AdaBoostClassifier
from AccuracyValidation import OfflineValidation
 
class SingleClassifier():
    def __init__(self):
        # weak classifier
        self.clf = None
         
    def getBeastOne(self, name):
        from sklearn.externals import joblib
        # if it has already generated
        try:
            clf = joblib.load(name + '.pkl')
            return clf
        except:
            pass
        # get train data and test data
        dataSet = mat(DataCarer.createTrainDataSet())
        X_train, Y_train = dataSet[:, :-1], dataSet[:, -1]
        students, dataSet = DataCarer.createTestDataSet()
        X_test = dataSet
         
        # search for the best loop time 
        bestAccuracyRate, n_estimators = 0, 1
        for i in range(2, 200):
            sclf = AdaBoostClassifier(base_estimator=self.clf, learning_rate=1, n_estimators=i, algorithm='SAMME')
            sclf.fit(X_train, Y_train)
            DataCarer.saveResult(students, sclf.predit(X_test), 'temp')
            
            # the accuracy is the criteria
            accuracyRate = OfflineValidation.getAccuracy('temp')
            if accuracyRate > bestAccuracyRate:
                bestAccuracyRate = accuracyRate
                n_estimators = i
        
        # save the classifier as a dump
        clf = joblib.dump(name + '.pkl')
        
        return AdaBoostClassifier(base_estimator=self.clf, learning_rate=1, n_estimators=n_estimators, algorithm='SAMME')
