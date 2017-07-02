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
    
    def setCalculater(self, calculater):
        self.ScoreRankCalculater = calculater[0]
        self.ScoreRankCalculater.setStudent(self)
        self.CostAmountCalculater = calculater[1]
        self.CostAmountCalculater.setStudent(self)
        self.CostDinnerHallAverageCalculater = calculater[2]
        self.CostDinnerHallAverageCalculater.setStudent(self)
        self.CostSuperMarketAverageCalculater = calculater[3]
        self.CostSuperMarketAverageCalculater.setStudent(self)
        self.LibraryBorrowCalculater = calculater[4]
        self.LibraryBorrowCalculater.setStudent(self)
        self.BalanceRankCalculater = calculater[5]
        self.BalanceRankCalculater.setStudent(self)
        self.LibraryTimesCalculater = calculater[6]
        self.LibraryTimesCalculater.setStudent(self)
        self.LibraryTimeSpandCalculater = calculater[7]
        self.LibraryTimeSpandCalculater.setStudent(self)
        self.CostSuperMarketRateCalculater = calculater[8]
        self.CostSuperMarketRateCalculater.setStudent(self)
        self.CostDinnerHallRateCalculater = calculater[9]
        self.CostDinnerHallRateCalculater.setStudent(self)
        self.CostTimesCalculater = calculater[10]
        self.CostTimesCalculater.setStudent(self)
        self.SubsidyCalculater = calculater[11]
        self.SubsidyCalculater.setStudent(self)
    
    def getStudentId(self):
        return self.studentId
    
    def setStudentId(self, studentId): 
        self.studentId = studentId
    
    def getScore(self):
        return self.score
    
    def setScore(self): 
        self.score = self.ScoreRankCalculater.calculate()
    
    def getCost_amount(self): 
        return self.cost_amount
    
    def setCost_amount(self): 
        self.cost_amount = self.CostAmountCalculater.calculate()
    
    def getCost_avg_dinnerHall(self): 
        return self.cost_avg_dinnerHall
    
    def setCost_avg_dinnerHall(self): 
        self.cost_avg_dinnerHall = self.CostDinnerHallAverageCalculater.calculate()
    
    def getCost_avg_superMarket(self): 
        return self.cost_avg_superMarket
    
    def setCost_avg_superMarket(self): 
        self.cost_avg_superMarket = self.CostSuperMarketAverageCalculater.calculate()
    
    def getLibrary_borrow(self): 
        return self.library_borrow
    
    def setLibrary_borrow(self): 
        self.library_borrow = self.LibraryBorrowCalculater.calculate()
    
    def getBalance_rank(self): 
        return self.balance_rank
    
    def setBalance_rank(self):
        self.balance_rank = self.BalanceRankCalculater .calculate()
    
    def getLibrary_times(self): 
        return self.library_times
    
    def setLibrary_times(self): 
        self.library_times = self.LibraryTimesCalculater.calculate()
    
    def getLibrary_time_spand(self): 
        return self.library_time_spand
    
    def setLibrary_time_spand(self):
        self.library_time_spand = self.LibraryTimeSpandCalculater.calculate()
    
    def getCost_supermarket_rate(self): 
        return self.cost_supermarket_rate
    
    def setCost_supermarket_rate(self): 
        self.cost_supermarket_rate = self.CostSuperMarketRateCalculater.calculate()
    
    def getCost_dinnerhall_rate(self): 
        return self.cost_dinnerhall_rate
    
    def setCost_dinnerhall_rate(self):
        self.cost_dinnerhall_rate = self.CostDinnerHallRateCalculater.calculate()
    
    def getCost_times(self): 
        return self.cost_times
    
    def setCost_times(self): 
        self.cost_times = self.CostTimesCalculater.calculate()
    
    def getSubsidy(self): 
        return self.subsidy
    
    def setSubsidy(self): 
        self.subsidy = self.SubsidyCalculater.calculate()

    def setAll(self):
        self.setScore()
        self.setLibrary_borrow()
        self.setLibrary_time_spand()
        self.setLibrary_times()
        self.setSubsidy()
        self.setCost_times()
        self.setCost_amount()
        self.setBalance_rank()
        self.setCost_avg_dinnerHall()
        self.setCost_supermarket_rate()
        self.setCost_dinnerhall_rate()
        self.setCost_supermarket_rate()
        
    def getAll(self):
        return [self.getScore(), \
                self.getCost_amount(), \
                self.getCost_avg_superMarket(), self.getCost_avg_dinnerHall(), \
                self.getCost_supermarket_rate(), self.getCost_dinnerhall_rate(), \
                self.getCost_times(), \
                self.getLibrary_borrow(), self.getLibrary_times(), self.getLibrary_time_spand(), \
                 self.getBalance_rank(), \
                 self.getSubsidy()]
