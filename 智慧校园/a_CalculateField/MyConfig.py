from Tools import MyDataBase
db = MyDataBase.MyDataBase()
conn = db.getConn()
executer = db.getExcuter()

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
A = 100
B = 200
C = 300
D = 400
BalanceRank_level = {"A":100, "B":200, "C":300, "D":400}
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
xx消费/总消费比例
'''
A = 0.1
B = 0.2
C = 0.3
D = 0.4
CostRate_level = {"A":0.1, "B":0.2, "C":0.3, "D": 0.4}
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

###### thread config ######
threadN = 10
