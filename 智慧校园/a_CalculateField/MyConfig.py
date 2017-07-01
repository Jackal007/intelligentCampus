from Tools import MyDataBase
db = MyDataBase.MyDataBase()
conn = db.getConn()
executer = db.getExcuter()


###### thread config ######
threadN = 10
Subsidy_level = {"A":0, "B":1000, "C":1500, "D": 2000}
Score_level = {"A":293, "B":879, "C":1465, "D": 2931}
LibraryBorrow_level = {"A":8, "B":20, "C":43, "D": 424}
LibraryTimes_level = {"A":62, "B":168, "C":352, "D": 2964}
LibraryTimeSpand_level = {"A":90, "B":120, "C":150, "D": 180}
BalanceRank_level = {"A":110.0, "B":157.5, "C":250.0, "D": 2313.0}
CostAmount_level = {"A":6003.13, "B":8912.93, "C":11138.1, "D": 28700.05}
AverageCost_level = {"A":6.29041, "B":7.623881, "C":9.593506, "D": 703.76}
CostDinnerHallRate_level = {"A":0.15, "B":0.3, "C":0.45, "D": 0.6}
CostSuperMarketRate_level={"A":0.2, "B":0.4, "C":0.6, "D": 0.8}
CostTimes_level = {"A":840, "B":1255, "C":1571, "D": 4878}
CostType_level = {"A":10, "B":20, "C":30, "D": 40}

if __name__ == '__main__':
    ###### level config ######
    '''
    奖学金额
    '''
    A = 0
    B = 1000
    C = 1500
    D = 2000
    Subsidy_level = {"A":A, "B":B, "C": C, "D": D}
    print('Subsidy_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
    '''
    成绩排名
    '''
    sql = "select max(rank) from score"
    executer.execute(sql)
    studentNum = executer.fetchone()[0]
    A = int(studentNum * 0.1)
    B = int(studentNum * 0.3)
    C = int(studentNum * 0.5)
    D = int(studentNum * 1)
    Score_level = {"A":A, "B":B, "C":C, "D": D}
    print('Score_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
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
    LibraryBorrow_level = {"A":A, "B": B, "C": C, "D":D}
    print('LibraryBorrow_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
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
    LibraryTimes_level = {"A":A, "B": B, "C": C, "D":D}
    print('LibraryTimes_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
    '''
    在图书馆时长
    '''
    A = 90
    B = 120
    C = 150
    D = 180
    LibraryTimeSpand_level = {"A":90, "B": 120, "C":150, "D": 180}
    print('LibraryTimeSpand_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
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
    BalanceRank_level = {"A":A, "B": B, "C": C, "D":D}
    print('BalanceRank_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
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
    CostAmount_level = {"A":A, "B": B, "C":C, "D": D}
    print('CostAmount_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
    '''
    平均花费
    '''
    sql = "select avg(deal_cost) as c from card group by student_id order by c"
    executer.execute(sql)
    AverageCosts = executer.fetchall()
    A = AverageCosts[int(len(AverageCosts) * 0.25)][0]
    B = AverageCosts[int(len(AverageCosts) * 0.5)][0]
    C = AverageCosts[int(len(AverageCosts) * 0.75)][0]
    D = AverageCosts[int(len(AverageCosts) * 1) - 1][0]
    AverageCost_level = {"A":A, "B": B, "C":C, "D": D}
    print('AverageCost_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
    '''
    食堂消费/总消费比例
    '''
    A = 0.1
    B = 0.2
    C = 0.3
    D = 0.4
    CostDinnerHallRate_level = {"A":A, "B": B, "C":C, "D": D}
    print('CostRate_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
    '''
    超市消费/总消费比例
    '''
    A = 0.25
    B = 0.5
    C = 0.75
    D = 1
    CostSuperMarketRate_level = {"A":A, "B":B, "C":C, "D": D}
    print('CostRate_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
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
    CostTimes_level = {"A":A, "B": B, "C": C, "D":D}
    print('CostTimes_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
    '''
    消费类型
    '''
    A = 10
    B = 20
    C = 30
    D = 40
    CostType_level = {"A":10, "B":20, "C": 30, "D":40}
    print('CostType_level = {"A":' + str(A) + ', "B":' + str(B) + ', "C":' + str(C) + ', "D": ' + str(D) + '}')
    
