'''
Created on 2017年7月22日
高斯过程
@author: zhenglongtian
'''
from Classifiers.SingleModels import SingleClassifier
from sklearn import gaussian_process

class GaussianProcesses(SingleClassifier.SingleClassifier):
    def __init__(self):
        SingleClassifier.SingleClassifier.__init__(self)
        # weak classifier
        self.clf = gaussian_process.GaussianProcess(theta0=1e-2, thetaL=1e-4, thetaU=1e-1)
