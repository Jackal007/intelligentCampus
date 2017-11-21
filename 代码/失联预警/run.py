'''
Created on 2017年11月20日

@author: qfWu
'''
from Tools.MyDataBase import MyDataBase
import wrong_time_sql

db = MyDataBase("软件学院")
conn = db.getConn()
executer = db.getExcuter()

executer.execute(wrong_time_sql)
data = executer.fetchall()

for i in data:
    print(i)
