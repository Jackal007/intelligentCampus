'''
Created on 2017年7月22日

@author: zhenglongtian
'''
from Classifiers.SingleModels import SingleClassifier
from sklearn.ensemble import RandomForestClassifier

class ExtraTrees(SingleClassifier):
    def __init__(self):
        #weak classifier
        self.clf=RandomForestClassifier(random_state=1)
# 