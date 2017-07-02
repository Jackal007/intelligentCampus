class Student:
    def __init__(self, info):
        if len(info) > 0:
            self.studentId = info[0]
            self.score = info[1]
            self.cost_amount = info[2]
            self.cost_avg_superMarket = info[3]
            self.cost_avg_dinnerHall = info[4]
            self.cost_supermarket_rate = info[5]
            self.cost_dinnerhall_rate = info[6]
            self.cost_times = info[7]
            self.library_borrow = info[8]
            self.library_times = info[9]
            self.library_time_spand = info[10]
            self.balance_rank = info[11]
            self.subsidy = info[12]
            
    def setStudentId(self, studentId): 
       self.studentId = studentId
    
    def getStudentId(self):
        return self.studentId
    
    def getScore(self):
        return self.score
    
    def getCost_amount(self): 
        return self.cost_amount
    
    def getCost_avg_dinnerHall(self): 
        return self.cost_avg_dinnerHall
    
    def getCost_avg_superMarket(self): 
        return self.cost_avg_superMarket
    
    def getLibrary_borrow(self): 
        return self.library_borrow
    
    def getBalance_rank(self): 
        return self.balance_rank
    
    def getLibrary_times(self): 
        return self.library_times
    
    def getLibrary_time_spand(self): 
        return self.library_time_spand
    
    def getCost_supermarket_rate(self): 
        return self.cost_supermarket_rate
    
    def getCost_dinnerhall_rate(self): 
        return self.cost_dinnerhall_rate
    
    def getCost_times(self): 
        return self.cost_times
    
    def getSubsidy(self): 
        return self.subsidy
    
    def setAll(self, calculater):
        info = []
        for i in calculater:
            i.setStudent(self)
            info.append(i.calculate())
        self.score = info[0]
        self.cost_amount = info[1]
        self.cost_avg_superMarket = info[2]
        self.cost_avg_dinnerHall = info[3]
        self.cost_supermarket_rate = info[4]
        self.cost_dinnerhall_rate = info[5]
        self.cost_times = info[6]
        self.library_borrow = info[7]
        self.library_times = info[8]
        self.library_time_spand = info[9]
        self.balance_rank = info[10]
        self.subsidy = info[11]
        
    def getAll(self):
        return [self.getScore(), \
                self.getCost_amount(), \
                self.getCost_avg_superMarket(), self.getCost_avg_dinnerHall(), \
                self.getCost_supermarket_rate(), self.getCost_dinnerhall_rate(), \
                self.getCost_times(), \
                self.getLibrary_borrow(), self.getLibrary_times(), self.getLibrary_time_spand(), \
                self.getBalance_rank(), \
                self.getSubsidy()]
