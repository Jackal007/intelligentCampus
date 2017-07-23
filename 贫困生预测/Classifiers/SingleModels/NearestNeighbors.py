'''
Created on 2017年7月22日
随机梯度下降
@author: zhenglongtian
'''
from Classifiers.SingleModels import SingleClassifier
from sklearn.neighbors import NearestNeighbors

class ExtraTrees(SingleClassifier):
    def __init__(self):
        # weak classifier
        algorithms = ['brute', 'ball_tree', 'kd_tree']
        self.clf = NearestNeighbors(n_neighbors=2, algorithm=algorithms[0])
# 
