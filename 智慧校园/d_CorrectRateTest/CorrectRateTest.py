import pymysql
from numpy import empty

conn = pymysql.connect("localhost", "root", "root", "intelligentCampusTrain")
cur = conn.cursor()


fr = open("result.txt", 'r')
content = [inst.strip('\n').split(',') for inst in fr.readlines()]

correct = 0
total = len(content)
for ins in content :
    student_id = ins[0]
    presume = ins[1]
    sql = "select stipend from subsidy where student_id = " + student_id
    cur.execute(sql)
    real = cur.fetchone()[0]
    if presume == real :
        correct = correct + 1
            
cur.close()
conn.commit()
conn.close()


print(total)
print(correct)
print(correct / total)
