from tqdm import tqdm
import threading
import CalculateXX
from MyConfig import CostAmount_level as level
from MyConfig import threadN

class CalculateCostAmount(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateCostAmount")
        # 对每一个学生统计其消费金额的情况
        def smallCalculate(students):
            try:
                for studentId in tqdm(students):
                        sql = "select sum(deal_cost) from card where student_id=" + str(studentId) 
                        self.executer.execute(sql)
                        deal_cost = self.executer.fetchone()[0]
                        weight = "D"
                        if int(deal_cost) < self.level["A"]:
                            weight = "A"
                        elif int(deal_cost) < self.level["B"]:
                            weight ="B"
                        elif int(deal_cost) < self.level["C"]:
                            weight = "C"
            
                        sql = "update students set cost_amount='" + str(weight) + "' where student_id=" + str(studentId)
                        self.executer.execute(sql)
            except:
                pass
            self.conn.commit()
            
        # slice students to many slices
        students=[]
        stepSize=int(len(self.students)/threadN)
        for i in range(threadN):
            students.append(self.students[i*stepSize:(i+1)*stepSize])
        students.append(self.students[threadN*stepSize:])
        #set them to run in mulity threads
        threads=[]
        for i in range(threadN+1):
            threads.append(threading.Thread(smallCalculate(students[i])))
        for t in threads:
            t.setDaemon(True)
            t.start()
        t.join()
        self.db.close()

if __name__ == '__main__':
    t=CalculateCostAmount(level)
    t.calculate()
