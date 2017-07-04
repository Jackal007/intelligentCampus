from Tools import MyDataBase

db = MyDataBase.MyDataBase("train")
conn = db.getConn()
executer = db.getExcuter()

def saveConfig(name, level):
    levels = {"A":level[0], "B":level[1], "C":level[2], "D": level[3]}
    print(name + "=" + str(levels))
    with open('Myconfig.py', 'a')as f:
        f.write('\n' + name + '=' + str(levels))

def Subsidy_levelConfig():
        '''
        奖学金额
        '''
        A = 0
        B = 1000
        C = 1500
        D = 2000
        saveConfig("Subsidy_level", [A, B, C, D])

def Score_levelConfig():
        '''
        成绩排名
        '''
        sql = "select max(rank) from score"
        executer.execute(sql)
        studentNum = executer.fetchone()[0]
        A = int(studentNum * 0.25)
        B = int(studentNum * 0.5)
        C = int(studentNum * 0.5)
        D = int(studentNum * 1)
        saveConfig("Score_level", [A, B, C, D])
        
def LibraryBorrow_levelConfig():
        '''
        借阅书籍数
        '''
        sql = "select COUNT(*) as c from borrow group by student_id order by c"
        executer.execute(sql)
        LibraryBorrows = executer.fetchall()
        A = LibraryBorrows[int(len(LibraryBorrows) * 0.25)][0]
        B = LibraryBorrows[int(len(LibraryBorrows) * 0.5)][0]
        C = LibraryBorrows[int(len(LibraryBorrows) * 0.75)][0]
        D = LibraryBorrows[int(len(LibraryBorrows) * 1) - 1][0]
        saveConfig("LibraryBorrow_level", [A, B, C, D])

def LibraryTimes_levelConfig():
        '''
        图书馆次数
        '''
        sql = "select COUNT(*) as c from library group by student_id order by c"
        executer.execute(sql)
        LibraryTimes = executer.fetchall()
        A = LibraryTimes[int(len(LibraryTimes) * 0.25)][0]
        B = LibraryTimes[int(len(LibraryTimes) * 0.5)][0]
        C = LibraryTimes[int(len(LibraryTimes) * 0.75)][0]
        D = LibraryTimes[int(len(LibraryTimes) * 1) - 1][0]
        saveConfig("LibraryTimes_level", [A, B, C, D])

def LibraryTimeSpand_levelConfig():
        '''
        在图书馆时长
        '''
        A = 90
        B = 120
        C = 150
        D = 180
        saveConfig("LibraryTimeSpand_level", [A, B, C, D])

def BalanceRank_levelConfig():
        '''
        卡内平均余额
        '''
        sql = "select (min(balance)+max(balance))/2 as a from card group by student_id order by a"
        executer.execute(sql)
        BalanceRanks = executer.fetchall()
        A = BalanceRanks[int(len(BalanceRanks) * 0.25)][0]
        B = BalanceRanks[int(len(BalanceRanks) * 0.5)][0]
        C = BalanceRanks[int(len(BalanceRanks) * 0.75)][0]
        D = BalanceRanks[int(len(BalanceRanks) * 1) - 1][0]
        saveConfig("BalanceRank_level", [A, B, C, D])

def CostAmount_levelConfig():
        '''
        消费金额
        '''
        sql = "select sum(deal_cost) as c from card group by student_id order by c"
        executer.execute(sql)
        CostAmounts = executer.fetchall()
        A = CostAmounts[int(len(CostAmounts) * 0.25)][0]
        B = CostAmounts[int(len(CostAmounts) * 0.5)][0]
        C = CostAmounts[int(len(CostAmounts) * 0.75)][0]
        D = CostAmounts[int(len(CostAmounts) * 1) - 1][0]
        saveConfig("CostAmount_level", [A, B, C, D])

def CostAverageDinnerHall_levelConfig():
        '''
        食堂平均花费
        '''
        sql = "select avg(deal_cost) as c from card where deal_way='dinnerhall' group by student_id order by c"
        executer.execute(sql)
        AverageCosts = executer.fetchall()
        A = AverageCosts[int(len(AverageCosts) * 0.25)][0]
        B = AverageCosts[int(len(AverageCosts) * 0.5)][0]
        C = AverageCosts[int(len(AverageCosts) * 0.75)][0]
        D = AverageCosts[int(len(AverageCosts) * 1) - 1][0]
        saveConfig("CostAverageDinnerHall_level", [A, B, C, D])
        
def CostAverageLaundryRoom_levelConfig():
        '''
        洗衣房平均花费
        '''
        sql = "select avg(deal_cost) as c from card where deal_way='laundryroom' group by student_id order by c"
        executer.execute(sql)
        AverageCosts = executer.fetchall()
        A = AverageCosts[int(len(AverageCosts) * 0.25)][0]
        B = AverageCosts[int(len(AverageCosts) * 0.5)][0]
        C = AverageCosts[int(len(AverageCosts) * 0.75)][0]
        D = AverageCosts[int(len(AverageCosts) * 1) - 1][0]
        saveConfig("CostAverageLaundryRoom_level", [A, B, C, D])
        
def CostAverageSupermarket_levelConfig():
        '''
        超市平均花费
        '''
        sql = "select avg(deal_cost) as c from card where deal_way='supermarket' group by student_id order by c"
        executer.execute(sql)
        AverageCosts = executer.fetchall()
        A = AverageCosts[int(len(AverageCosts) * 0.25)][0]
        B = AverageCosts[int(len(AverageCosts) * 0.5)][0]
        C = AverageCosts[int(len(AverageCosts) * 0.75)][0]
        D = AverageCosts[int(len(AverageCosts) * 1) - 1][0]
        saveConfig("CostAverageSupermarket_level", [A, B, C, D])
        
def CostRateDinnerHall_levelConfig():
        '''
        食堂消费/总消费比例
        '''
        A = 0.1
        B = 0.2
        C = 0.3
        D = 0.4
        saveConfig("CostRateDinnerHall_level", [A, B, C, D])
        
def CostRateSuperMarket_levelConfig():
        '''
        超市消费/总消费比例
        '''
        A = 0.25
        B = 0.5
        C = 0.75
        D = 1
        saveConfig("CostRateSuperMarket_level", [A, B, C, D])

def CostRateLaundryRoom_levelConfig():
        '''
        洗衣房消费/总消费比例
        '''
        A = 0.05
        B = 0.1
        C = 0.2
        D = 0.4
        saveConfig("CostRateLaundryRoom_level", [A, B, C, D])
        
def CostTimes_levelConfig():
        '''
        消费次数
        '''
        sql = "select COUNT(*) as c from card group by student_id order by c"
        executer.execute(sql)
        CostTimes = executer.fetchall()
        A = CostTimes[int(len(CostTimes) * 0.25)][0]
        B = CostTimes[int(len(CostTimes) * 0.5)][0]
        C = CostTimes[int(len(CostTimes) * 0.75)][0]
        D = CostTimes[int(len(CostTimes) * 1) - 1][0]
        saveConfig("CostTimes_level", [A, B, C, D])
        
def CostType_levelConfig():
        '''
        消费类型[周一]
        '''
        A = 10
        B = 20
        C = 30
        D = 40
        saveConfig("CostType_level", [A, B, C, D])

def config():
    Subsidy_levelConfig()
    Score_levelConfig()
    LibraryBorrow_levelConfig()
    LibraryTimes_levelConfig()
    LibraryTimeSpand_levelConfig()
    BalanceRank_levelConfig()
    CostAmount_levelConfig()
    CostAverageDinnerHall_levelConfig()
    CostAverageLaundryRoom_levelConfig()
    CostAverageSupermarket_levelConfig()
    CostRateDinnerHall_levelConfig()
    CostRateLaundryRoom_levelConfig()
    CostRateSuperMarket_levelConfig()
    CostTimes_levelConfig()
    CostType_levelConfig()

if __name__ == '__main__':
    config()



Subsidy_level={'A': 0, 'B': 1000, 'C': 1500, 'D': 2000}
Score_level={'A': 733, 'B': 1466, 'C': 1466, 'D': 2933}
LibraryBorrow_level={'A': 8, 'B': 19, 'C': 42, 'D': 426}
LibraryTimes_level={'A': 28, 'B': 81, 'C': 171, 'D': 1485}
LibraryTimeSpand_level={'A': 90, 'B': 120, 'C': 150, 'D': 180}
BalanceRank_level={'A': 110.0, 'B': 158.5, 'C': 250.0, 'D': 2200.0}
CostAmount_level={'A': 6083.54, 'B': 8904.05, 'C': 11105.1, 'D': 30275.2}
CostAverageDinnerHall_level={'A': 3.855575, 'B': 4.499582, 'C': 5.42988, 'D': 153.55}
CostAverageLaundryRoom_level={'A': 1.28, 'B': 2.28, 'C': 3.235, 'D': 23.5}
CostAverageSupermarket_level={'A': 5.88, 'B': 7.635392, 'C': 10.04717, 'D': 171.199997}
CostRateDinnerHall_level={'A': 0.1, 'B': 0.2, 'C': 0.3, 'D': 0.4}
CostRateLaundryRoom_level={'A': 0.05, 'B': 0.1, 'C': 0.2, 'D': 0.4}
CostRateSuperMarket_level={'A': 0.25, 'B': 0.5, 'C': 0.75, 'D': 1}
CostTimes_level={'A': 837, 'B': 1246, 'C': 1566, 'D': 4159}
CostType_level={'A': 10, 'B': 20, 'C': 30, 'D': 40}