from Tools import MyLog
from Tools import MyDataBase

class XXCalculater:

    def __init__(self):
        # levels about the weight
        self.db = MyDataBase.MyDataBase("train")
        self.conn = self.db.getConn()
        self.executer = self.db.getExcuter()
                
    def setStudent(self, student):
        self.student = student
        
    def setLevel(self):
        pass
    
    @MyLog.myException
    def calculate(self):
        pass  
    
    def classify(self, param):
        if param is None:
            return 0
        for i in range(len(self.level)):
            if float(param) <= float(self.level[i]):
                return i+1
        return len(self.level)+1
    
    def afterCalculate(self):
        self.db.close()

if __name__ == '__main__':
    print('a father')
