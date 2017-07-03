from _overlapped import NULL
class Student:
    def __init__(self, attributes=NULL, subsidy="A"):
        self.attributes = {}
        if attributes != NULL:
            self.setAll(attributes, subsidy)
        
    def fetch(self, calculater):
        attributes = [self.getStudentId()]
        for i in calculater:
            i.setStudent(self)
            attributes.append(i.calculate())
        self.setAll(attributes=attributes, subsidy=attributes[-1])
        
    def setAll(self, attributes=NULL, subsidy="A"):
        if attributes != NULL:
            self.attributes = {
                'studentId':attributes[0],
                'score':attributes[1],
                'costAmount':attributes[2],
                'costAvgSuperMarket':attributes[3],
                'costAvgDinnerHall':attributes[4],
                'costAvgLaundry':attributes[5],
                'costSupermarketRate':attributes[6],
                'costDinnerhallRate':attributes[7],
                'costLaundryRate':attributes[8],
                'costTimes':attributes[9],
                'libraryBorrow':attributes[10],
                'libraryTimes':attributes[11],
                'libraryTimeSpand':attributes[12],
                'balanceRank':attributes[13],
                }
        self.attributes['subsidy'] = subsidy
            
    def getAll(self):
        all = list(self.attributes.values())
        return all[1:-1]

    
    def setStudentId(self, studentId): 
        self.attributes['studentId'] = studentId
    
    def getStudentId(self):
        return self.attributes['studentId']
