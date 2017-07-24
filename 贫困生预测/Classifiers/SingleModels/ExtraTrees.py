'''
Created on 2017年7月22日

@author: zhenglongtian
'''
from Classifiers.SingleModels import SingleClassifier
from sklearn.ensemble import ExtraTreesClassifier

class ExtraTrees(SingleClassifier.SingleClassifier):
    def __init__(self):
        SingleClassifier.SingleClassifier.__init__(self)
        # weak classifier
        self.clf = ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
