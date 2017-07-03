from _overlapped import NULL
class Student:
    def __init__(self, studnetId, attributes=NULL, subsidy="A"):
        self.attributes = {}
        self.setAll(studnetId, attributes, subsidy)
        
    def fetch(self, calculater):
        attributes = []
        for i in calculater:
            i.setStudent(self)
            attributes.append(i.calculate())
        self.setAll(self.attributes['studnetId'], attributes)
        
    def setAll(self, studnetId, attributes=NULL, subsidy="A"):
        self.attributes['studnetId'] = studnetId
        if len(attributes) > 0:
            self.attributes = {
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
                'subsidy':"A",
                }
        if attributes[13]:
            self.attributes['subsidy'] = attributes[13]
            
    def getAll(self):
        return self.attributes.values()

    
    def setStudentId(self, studentId): 
        self.attributes['studentId'] = studentId
    
    def getStudentId(self):
        return self.attributes['studentId']
