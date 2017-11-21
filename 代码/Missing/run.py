'''
Created on 2017年11月20日

@author: qfWu
'''
from Tools.MyDataBase import MyDataBase
from __init__ import m_out_1_not_in_sql
from __init__ import over_2_in_3_times_sql
from __init__ import wrong_time_sql

db = MyDataBase("软件学院")
conn = db.getConn()
executer = db.getExcuter()

m_out_1_not_in_students = list()
executer.execute(m_out_1_not_in_sql)
data = executer.fetchall()
for i in data:
    m_out_1_not_in_students.append(i[0])
    
over_2_in_3_times_students = list()
executer.execute(over_2_in_3_times_sql)
data = executer.fetchall()
for i in data:
    over_2_in_3_times_students.append(i[0])
    
wrong_time_students = list()
executer.execute(wrong_time_sql)
data = executer.fetchall()
for i in data:
    wrong_time_students.append(i[0])

the_students = set(m_out_1_not_in_students).intersection(set(over_2_in_3_times_students)).intersection(set(wrong_time_students))
print(the_students)
