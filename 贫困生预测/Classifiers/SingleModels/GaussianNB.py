'''
Created on 2017年7月22日

@author: zhenglongtian
'''
from Classifiers.SingleModels import SingleClassifier
from sklearn.naive_bayes import GaussianNB

class GaussianNB(SingleClassifier.SingleClassifier):
    def __init__(self):
        SingleClassifier.SingleClassifier.__init__(self)
        #weak classifier
        self.clf=GaussianNB()
