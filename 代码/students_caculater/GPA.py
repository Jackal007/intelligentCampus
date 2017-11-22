'''
Created on 2017年11月21日

@author: 95679
'''
import pymysql 

db = pymysql.connect("172.16.20.5", "root", "", "软件学院", charset='utf8')
cur = db.cursor()
print("connect ok")
sql = "select student_num,school_year from students"
cur.execute(sql)
e = cur.fetchall()
for i in e:
    stu_num = str(i[0])
    school_year = str(i[1])
    next_year = str(int(str(i[1]))+1)
    year1 = school_year + "/" +next_year+"-1"
    year2 = school_year + "/" +next_year+"-2"
    sql = "select GPA,course_credit from score where stu_num = "+stu_num+" and school_year = "+year1   
    print(sql)
    cur.execute(sql)
    stu1 = cur.fetchone()
    print(stu1)
    GPA1 = float(stu1[0])
    credit1 = int(stu1[1])
    sql = "select GPA,course_credit from score where stu_num = "+stu_num+" and school_year = "+year2
    cur.execute(sql)
    stu2 = cur.fetchone()
    GPA2 = float(stu2[0])
    credit2 = int(stu2[1])
    GPA = (GPA1*credit1+GPA2*credit2)/(credit1+credit2)
    print(GPA)
    cur.execute("update students set GPA = "+GPA+" where student_num = "+stu_num+" and school = "+school_year)
db.close()
print("ok")
