from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
import DataCarer
from sklearn import tree
from numpy import *
from sklearn.linear_model import SGDClassifier

def createTrainDataSet():
    dataSet = DataCarer.createTrainDataSet()
    DataCarer.transform(dataSet)
    return mat(dataSet)

dataset = mat(createTrainDataSet())

X = dataset[:, :-1]
Y = dataset[:, -1]
model = ExtraTreesClassifier() # build extra tree model
model.fit(X,Y)
print(model.feature_importances_) #display importance of each variables

