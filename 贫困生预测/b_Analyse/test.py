'''
Created on 2017年7月4日

@author: qfWu
'''
from sklearn import datasets
digits = datasets.load_digits()
digits.images.shape

import matplotlib.pyplot as plt 
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r) 
plt.show()