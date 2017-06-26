class Student:
    def __init__(self, info):
        self.studentId = info[0]
        self.score = info[1]
        self.cost_amount = info[2]
        self.cost_avg_superMarket = info[3]
        self.cost_avg_dinnerHall = info[4]
        self.cost_supermarket_rate = info[5]
        self.cost_dinnerhall_rate = info[6]
        self.cost_times = info[6]
        self.library_borrow = info[7]
        self.library_times = info[8]
        self.library_time_spand = info[9]
        self.balance_rank = info[10]
        self.subsidy = info[11]
    
    def getStudentId(self):
        return self.studentId
    
    def setStudentId(self, studentId): 
        self.studentId = studentId
    
    def getScore(self):
        return self.score
    
    def setScore(self, score): 
        self.score = score
    
    def getStudent_id(self): 
        return self.student_id
    
    def setStudent_id(self, student_id): 
        self.student_id = student_id
    
    def getCost_avg_dinnerHall(self): 
        return self.cost_avg_dinnerHall
    
    def setCost_avg_dinnerHall(self, cost_avg_dinnerHall): 
        self.cost_avg_dinnerHall = cost_avg_dinnerHall
    
    def getCost_avg_superMarket(self): 
        return self.cost_avg_superMarket
    
    def setCost_avg_superMarket(self, cost_avg_superMarket): 
        self.cost_avg_superMarket = cost_avg_superMarket
    
    def getCost_amount(self): 
        return self.cost_amount
    
    def setCost_amount(self, cost_amount): 
        self.cost_amount = cost_amount
    
    def getLibrary_borrow(self): 
        return self.library_borrow
    
    def setLibrary_borrow(self, library_borrow): 
        self.library_borrow = library_borrow
    
    def getBalance_rank(self): 
        return self.balance_rank
    
    def setBalance_rank(self, balance_rank): 
        self.balance_rank = balance_rank
    
    def getLibrary_times(self): 
        return self.library_times
    
    def setLibrary_times(self, library_times): 
        self.library_times = library_times
    
    def getLibrary_time_spand(self): 
        return self.library_time_spand
    
    def setLibrary_time_spand(self, library_time_spand): 
        self.library_time_spand = library_time_spand
    
    def getCost_supermarket_rate(self): 
        return self.cost_supermarket_rate
    
    def setCost_supermarket_rate(self, cost_supermarket_rate): 
        self.cost_supermarket_rate = cost_supermarket_rate
    
    def getCost_dinnerhall_rate(self): 
        return self.cost_dinnerhall_rate
    
    def setCost_dinnerhall_rate(self, cost_dinnerhall_rate): 
        self.cost_dinnerhall_rate = cost_dinnerhall_rate
    
    def getCost_times(self): 
        return self.cost_times
    
    def setCost_times(self, cost_times): 
        self.cost_times = cost_times
    
    def getSubsidy(self): 
        return self.subsidy
    
    def setSubsidy(self, subsidy): 
        self.subsidy = subsidy