from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
import DataCarer
from sklearn import tree
from numpy import *
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
 
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

# from sklearn import datasets
# from sklearn.feature_selection import RFE
# from sklearn.linear_model import LogisticRegression
#  
# def createTrainDataSet():
#     dataSet = DataCarer.createTrainDataSet()
#     DataCarer.transform(dataSet)
#     return mat(dataSet)
#   
# dataset = mat(createTrainDataSet())
#   
# X = dataset[:, :-1]
# Y = dataset[:, -1]
# model = LogisticRegression() # build logistic regression model
# rfe = RFE(model,20) # limit number of variables to three
# rfe = rfe.fit(X,Y)
# print(rfe.support_) 
# print(rfe.ranking_)

