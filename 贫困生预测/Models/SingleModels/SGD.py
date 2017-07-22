'''
Created on 2017年7月22日

@author: zhenglongtian
'''
from Models.SingleModels import SingleClassifier
from sklearn.linear_model import SGDClassifier

class ExtraTrees(SingleClassifier):
    def __init__(self):
        #weak classifier
        self.clf=SGDClassifier(alpha=0.0001, average=False, class_weight=None, epsilon=0.1,
        eta0=0.0, fit_intercept=True, l1_ratio=0.15,
        learning_rate='optimal', loss='modified_huber', n_iter=5, n_jobs=1,
        penalty='l2', power_t=0.5, random_state=None, shuffle=True,
        verbose=0, warm_start=False)
# 