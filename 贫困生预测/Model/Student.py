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
#         self.setAll(attributes=attributes, subsidy=attributes[-1])
        
    def setAll(self, attributes=NULL, subsidy="A"):
        if attributes != NULL:
            self.attributes = {
                'student_id':attributes[0],
                'score':attributes[1],
                'cost_amount':attributes[2],
                'cost_variance':attributes[3],
                'cost_avg_day_superMarket':attributes[4],
                'cost_avg_day_laundryroom':attributes[5],
                'cost_avg_day_dinnerHall':attributes[6],
                'cost_rate_supermarket':attributes[7],
                'cost_rate_laundryroom':attributes[8],
                'cost_rate_dinnerhall':attributes[9],
                'cost_times_day_supermarket':attributes[10],
                'cost_times_day_dinnerhall':attributes[11],
                'cost_times_day_laundry':attributes[12],
                'cost_times':attributes[13],
                'library_borrow':attributes[14],
                'library_times':attributes[15],
                'library_time_spand':attributes[16],
                'balance_rank':attributes[17],
                'card_days':attributes[18],
                'time6_7costs':attributes[19],
                'time7_8costs':attributes[20],
                'totaldinnercosts':attributes[21],
                'avgdayscosts':attributes[22],
                'consumetimes11_12':attributes[23],
                'consumetimes0_25':attributes[24],
                'countcost0_10':attributes[25],
                'cardrecharge':attributes[26],
                'maxcost7_8':attributes[27]
                }
        self.attributes['subsidy'] = subsidy
            
    def getAll(self):
        all = list(self.attributes.values())
        return [self.attributes['costAmount'], self.attributes['costAvgSuperMarket'], \
                self.attributes['costAvgDinnerHall'], \
                self.attributes['costTimes'], \
                self.attributes['balanceRank'], self.attributes['subsidy'], ]

    
    def setStudentId(self, studentId): 
        self.attributes['studentId'] = studentId
    
    def getStudentId(self):
        return self.attributes['studentId']
