from Tools import MyLog
from Tools import MyDataBase

class XXCalculater:

    def __init__(self):
        # levels about the weight
        self.db = MyDataBase.MyDataBase()
        self.conn = self.db.getConn()
        self.executer = self.db.getExcuter()
                
    def setStudent(self, student):
        self.student = student
    
    def classify(self, param, level):
        if param:
            if param < level["A"]:
                param = "A"
            elif param < level["B"]:
                param = "B"
            elif param < level["C"]:
                param = "C"
            else:
                param = "D"
        else:
            param = "A"
        return param
        
    @MyLog.myException
    def calculate(self):
        pass  
    
    def afterCalculate(self):
        self.db.close()

if __name__ == '__main__':
    print('a father')
