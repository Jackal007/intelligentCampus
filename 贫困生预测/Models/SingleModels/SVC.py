'''
Created on 2017年7月22日

@author: zhenglongtian
'''
from Models.SingleModels import SingleClassifier
from sklearn import svm

class ExtraTrees(SingleClassifier):
    def __init__(self):
        #weak classifier
        self.clf=svm.SVC(probability=True)
# 