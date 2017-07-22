'''
测试准确率
'''
import pymysql

def getAccuracy(filename):
    conn = pymysql.connect("localhost", "root", "root", "intelligentCampustest")
    cur = conn.cursor()
    
    fr = open('../AccuracyValidation/results' + filename + ".csv", 'r')
    content = [inst.strip('\n').split(',') for inst in fr.readlines()]
    
    correct = total = 0
    for ins in content :
        student_id = ins[0]
        presume = int(ins[1])
        sql = "select subsidy from students where student_id = " + student_id
        cur.execute(sql)
        real = str(cur.fetchone()[0])
        if real is not None :
            total += 1
            if presume == real:         
                correct += 1
    cur.close();conn.commit();conn.close()
    return correct / total
