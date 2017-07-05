from Model import Student
from Tools import MyDataBase
from tqdm import tqdm
# from a_CalculateField.ScoreRankCalculater import ScoreRankCalculater
from a_CalculateField.BalanceRankCalculater import BalanceRankCalculater

Student = Student.Student
# ScoreRankCalculater = ScoreRankCalculater()
BalanceRankCalculater = BalanceRankCalculater()
# CostAmountCalculater = CostAmountCalculater.CostAmountCalculater()
# CostAverageDayCalculater = CostAverageDayCalculater.CostAverageDayCalculater()
# CostRateCalculater = CostRateCalculater.CostRateCalculater()
# LibraryBorrowCalculater = LibraryBorrowCalculater.LibraryBorrowCalculater()
# LibraryTimesCalculater = LibraryTimesCalculater.LibraryTimesCalculater()
# LibraryTimeSpandCalculater = LibraryTimeSpandCalculater.LibraryTimeSpandCalculater() 
# SubsidyCalculater = SubsidyCalculater.SubsidyCalculater()

# calculater = [ScoreRankCalculater,BalanceRankCalculater,\
#               CostAmountCalculater,CostAverageDayCalculater,\
#               CostRateCalculater,LibraryBorrowCalculater,\
#               LibraryTimesCalculater,LibraryTimeSpandCalculater,\
#               SubsidyCalculater]

calculater = [BalanceRankCalculater]

def calculate():
    db = MyDataBase.MyDataBase()
    conn = db.getConn()
    executer = db.getExcuter()
    
#     sql = "delete from students"
#     executer.execute(sql)
#     sql = "delete from library_modify"
#     executer.execute(sql)
#     conn.commit()
    
    sql = "select student_id from score"
    executer.execute(sql)
    studentIds = executer.fetchall()
    students = []
    
    for i in calculater:
        i.setLevel()
    
    for i in tqdm(studentIds):
        print()
        i = i[0]
        student = Student()
        student.setStudentId(i)
        student.fetch(calculater)
    
    for i in calculater:
        i.afterCalculate()

if __name__ == '__main__':
    calculate()
