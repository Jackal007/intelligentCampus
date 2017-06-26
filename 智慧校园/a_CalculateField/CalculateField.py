'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import os
# os.system("StudentScore.py")

def painStudent():
    os.system('python a_CalculateField/CalculateScore.py')
    os.system('python a_CalculateField/CalculateCostAmount.py')
#     os.system('python a_CalculateField/CalculateCostAverage.py')
#     os.system('python a_CalculateField/CalculateCostRate.py')
    os.system('python a_CalculateField/CalculateLibraryBorrow.py')
    os.system('python a_CalculateField/CalculateLibraryTimes.py')
    os.system('python a_CalculateField/CalculateLibraryTimeSpand.py')
    os.system('python a_CalculateField/CalculateBalanceRank.py')
    os.system('python a_CalculateField/CalculateSubsidy.py')
    
if __name__ == '__main__':
#     print("painStudent")
    painStudent()
