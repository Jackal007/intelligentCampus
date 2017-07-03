from Tools import MyDataBase

db = MyDataBase.MyDataBase()
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
        A = 0.25
        B = 0.5
        C = 0.75
        D = 1
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

Subsidy_level = {'A': 0, 'B': 1000, 'C': 1500, 'D': 2000}
Score_level = {'A': 732, 'B': 1465, 'C': 1465, 'D': 2931}
LibraryBorrow_level = {'A': 8, 'B': 20, 'C': 43, 'D': 424}
LibraryTimes_level = {'A': 62, 'B': 168, 'C': 352, 'D': 2964}
LibraryTimeSpand_level = {'A': 90, 'B': 120, 'C': 150, 'D': 180}
BalanceRank_level = {'A': 110.0, 'B': 157.5, 'C': 250.0, 'D': 2313.0}
CostAmount_level = {'A': 6003.13, 'B': 8912.93, 'C': 11138.1, 'D': 28700.05}
CostAverageDinnerHall_level = {'A': 3.85589, 'B': 4.502174, 'C': 5.40595, 'D': 37.766668}
CostAverageLaundryRoom_level = {'A': 1.283333, 'B': 2.322439, 'C': 3.257143, 'D': 30.0}
CostAverageSupermarket_level = {'A': 5.848889, 'B': 7.588235, 'C': 9.951852, 'D': 211.199997}
CostRateDinnerHall_level = {'A': 0.1, 'B': 0.2, 'C': 0.3, 'D': 0.4}
CostRateLaundryRoom_level = {'A': 0.25, 'B': 0.5, 'C': 0.75, 'D': 1}
CostRateSuperMarket_level = {'A': 0.25, 'B': 0.5, 'C': 0.75, 'D': 1}
CostTimes_level = {'A': 840, 'B': 1255, 'C': 1571, 'D': 4878}
CostType_level = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
