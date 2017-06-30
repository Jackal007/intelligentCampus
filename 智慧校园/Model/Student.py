from a_CalculateField import *

class Student:
    def __init__(self, info):
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
    
    def getStudentId(self):
        return self.studentId
    
    def setStudentId(self, studentId): 
        self.studentId = studentId
    
    def getScore(self):
        return self.score
    
    def setScore(self, score): 
        r = ScoreRankCalculater.ScoreRankCalculater(self, MyConfig.Score_level).calculate()
        self.score = r
    
    def getCost_amount(self): 
        return self.cost_amount
    
    def setCost_amount(self, cost_amount): 
        r = CostAmountCalculater.CostAmountCalculater(self, MyConfig.CostAmount_level)
        self.cost_amount = r
    
    def getCost_avg_dinnerHall(self): 
        return self.cost_avg_dinnerHall
    
    def setCost_avg_dinnerHall(self, cost_avg_dinnerHall): 
        r = CostDinnerHallAverageCalculater.CostDinnerHallAverageCalculater(self, MyConfig.AverageCost_level)
        self.cost_avg_dinnerHall = r
    
    def getCost_avg_superMarket(self): 
        return self.cost_avg_superMarket
    
    def setCost_avg_superMarket(self, cost_avg_superMarket): 
        r = CostSuperMarketAverageCalculater.CostSuperMarketAverageCalculater(self, MyConfig.AverageCost_level)
        self.cost_avg_superMarket = r
    
    def getLibrary_borrow(self): 
        return self.library_borrow
    
    def setLibrary_borrow(self, library_borrow): 
        self.library_borrow = library_borrow
    
    def getBalance_rank(self): 
        return self.balance_rank
    
    def setBalance_rank(self, balance_rank):
        r = BalanceRankCalculater.BalanceRankCalculater(self, MyConfig.BalanceRank_level) 
        self.balance_rank = r
    
    def getLibrary_times(self): 
        return self.library_times
    
    def setLibrary_times(self, library_times): 
        r = LibraryTimesCalculater.LibraryTimesCalculater(self, MyConfig.LibraryTimes_level)
        self.library_times = r
    
    def getLibrary_time_spand(self): 
        return self.library_time_spand
    
    def setLibrary_time_spand(self, library_time_spand): 
        self.library_time_spand = library_time_spand
    
    def getCost_supermarket_rate(self): 
        return self.cost_supermarket_rate
    
    def setCost_supermarket_rate(self, cost_supermarket_rate): 
        r = CostSuperMarketRateCalculater.CostSuperMarketRateCalculater(self, MyConfig.CostRate_level)
        self.cost_supermarket_rate = r
    
    def getCost_dinnerhall_rate(self): 
        return self.cost_dinnerhall_rate
    
    def setCost_dinnerhall_rate(self, cost_dinnerhall_rate):
        r = CostDinnerHallRateCalculater.CostDinnerHallRateCalculater(self, MyConfig.CostRate_level) 
        self.cost_dinnerhall_rate = r
    
    def getCost_times(self): 
        return self.cost_times
    
    def setCost_times(self, cost_times): 
        self.cost_times = cost_times
    
    def getSubsidy(self): 
        return self.subsidy
    
    def setSubsidy(self, subsidy): 
        self.subsidy = subsidy
