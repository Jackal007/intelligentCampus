'''
Created on 2017年7月22日
支持向量机
@author: zhenglongtian
'''
from Classifiers.SingleModels import SingleClassifier
from sklearn import svm

class SVC(SingleClassifier.SingleClassifier):
    def __init__(self):
        SingleClassifier.SingleClassifier.__init__(self)
        # weak classifier
        self.clf = svm.SVC(probability=True)
        # 这边可以设权值来处理数据不平衡问题
        self.weight = [1, 2, 3, ]
# 
