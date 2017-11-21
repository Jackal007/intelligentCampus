# from _overlapped import NULL
class Student:
    def __init__(self, studentId, attributes=None, subsidy="1"):
        self.studentId = studentId
        try:
            self.attributes = list(attributes)
        except:
            pass
        self.subsidy = subsidy
        
    def calculate(self, calculater):
        for i in calculater:
            i.setStudent(self)
            i.calculate()
        
    def rankit(self, calculater):
        for i in calculater:
            i.setStudent(self)
            i.rankit()
        
    def getAll(self):
        (self.attributes).append(self.subsidy)
        return self.attributes
    
    def setStudentId(self, studentId): 
        self.studentId = studentId
    
    def getStudentId(self):
        return self.studentId
