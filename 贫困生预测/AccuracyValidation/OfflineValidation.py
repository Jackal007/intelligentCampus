'''
测试准确率
'''
from Tools import DataCarer
from sklearn.model_selection import train_test_split

def getAccuracy(filename):
    X, Y = DataCarer.createTrainDataSet()
    X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.4, random_state=0)
    return correct / total
