'''
一个使用sklearn的小例子
'''
from sklearn import datasets
from sklearn import svm
import DataSetCreater

digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100.)

print(clf.gamma )

clf.fit(digits.data[:-1], digits.target[:-1])

r = clf.predict(digits.data[-1:])

print(r)
