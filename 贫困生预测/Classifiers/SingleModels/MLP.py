'''
Created on 2017年7月22日

@author: zhenglongtian
'''
from Classifiers.SingleModels import SingleClassifier
from sklearn import ExtraTreesClassifier

class ExtraTrees(SingleClassifier):
    def __init__(self):
        #weak classifier
        self.clf=ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
# 