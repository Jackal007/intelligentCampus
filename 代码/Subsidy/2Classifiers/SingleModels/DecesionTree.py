'''
Created on 2017年7月22日

@author: zhenglongtian
'''
from Classifiers.SingleModels import SingleClassifier
from sklearn import tree

class DecesionTree(SingleClassifier.SingleClassifier):
    def __init__(self):
        SingleClassifier.SingleClassifier.__init__(self)
        # weak classifier
        self.clf = tree.DecisionTreeClassifier()
