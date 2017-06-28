import pymysql
from numpy import empty

conn = pymysql.connect("localhost", "root", "root", "intelligentCampusTrain")
cur = conn.cursor()


fr = open("results.txt", 'r')
content = [inst.strip('\n').split(',') for inst in fr.readlines()]

correct = 0
total = 0
#total = len(content)
for ins in content :
    student_id = ins[0]
    presume = int(ins[1])
    sql = "select stipend from subsidy where student_id = " + student_id
    cur.execute(sql)
    real = (int)(cur.fetchone()[0])
    if real!=empty :
        total+=1
        if presume == real:         
            correct = correct + 1
            
cur.close()
conn.commit()
conn.close()


print(total)

print(correct)
print(correct / total)
