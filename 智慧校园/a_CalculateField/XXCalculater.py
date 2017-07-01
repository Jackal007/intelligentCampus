from Tools import *

class XXCalculater:

    def __init__(self, level):
        # levels about the weight
        self.level = level
        self.db = MyDataBase.MyDataBase()
        self.conn = self.db.getConn()
        self.executer = self.db.getExcuter()
                
    def setStudent(self, student):
        self.student = student

    def calculate(self):
        pass  
    
    def afterCalculate(self):
        self.db.close()

if __name__ == '__main__':
    print('a father')
