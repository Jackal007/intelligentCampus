import pymysql
from numpy import empty

conn = pymysql.connect("localhost", "root", "root", "intelligentCampustest")
cur = conn.cursor()


fr = open("results_ExtraTreesClassifier.csv", 'r')
content = [inst.strip('\n').split(',') for inst in fr.readlines()]

correct = 0
correct0=0
total = 0
#total = len(content)
for ins in content :
    student_id = ins[0]
    presume = int(ins[1])
    sql = "select subsidy from students_rank where student_id = " + student_id
    cur.execute(sql)
    real = str(cur.fetchone()[0])
    print(real)
    if real=='1':
        real=0
    elif real=='2':
        real=1000
    elif real=='3':
        real=1500
    elif real=='4':
        real=2000
    if real is not None :
        total+=1
        if presume == real:         
            correct +=  1
        if (presume == 0 and real ==0) or(presume != 0 and real !=0):
            correct0 +=  1
cur.close()
conn.commit()
conn.close()


print(total)

print(correct)
print(correct / total)
# print(correct0)
# print(correct0 / total)
