'''
Created on 2017Äê6ÔÂ26ÈÕ

@author: qfWu
'''
from Tools import MyDataBase

db = MyDataBase.MyDataBase()
conn = db.getConn()
executer = db.getExcuter()

sql = "select student_id, from score"
executer.execute(sql)
students = []
for i in executer.fetchall():
    students.append(i[0])