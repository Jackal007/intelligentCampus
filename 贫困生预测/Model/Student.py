from _overlapped import NULL
class Student:
    def __init__(self, studentId, attributes=NULL, subsidy="A"):
        self.studentId = studentId
        self.attributes = attributes
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
        return self.attributes.append(self.subsidy)
    
    def setStudentId(self, studentId): 
        self.studentId = studentId
    
    def getStudentId(self):
        return self.studentId
