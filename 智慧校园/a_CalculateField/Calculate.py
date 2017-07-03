from Model import Student
from Tools import MyDataBase
from tqdm import tqdm
from a_CalculateField import ScoreRankCalculater
from a_CalculateField import BalanceRankCalculater
from a_CalculateField import CostAmountCalculater
from a_CalculateField import CostAverageDinnerHallCalculater
from a_CalculateField import CostAverageLaundryRoomCalculater
from a_CalculateField import CostAverageSuperMarketCalculater
from a_CalculateField import CostRateDinnerHallCalculater
from a_CalculateField import CostRateLaundryRoomCalculater
from a_CalculateField import CostRateSuperMarketCalculater
from a_CalculateField import CostTimesCalculater
from a_CalculateField import LibraryBorrowCalculater
from a_CalculateField import LibraryTimesCalculater
from a_CalculateField import LibraryTimeSpandCalculater
from a_CalculateField import SubsidyCalculater

Student = Student.Student
ScoreRankCalculater = ScoreRankCalculater.ScoreRankCalculater()
BalanceRankCalculater = BalanceRankCalculater.BalanceRankCalculater()
CostAmountCalculater = CostAmountCalculater.CostAmountCalculater()
CostAverageDinnerHallCalculater = CostAverageDinnerHallCalculater.CostAverageDinnerHallCalculater()
CostAverageLaundryRoomCalculater = CostAverageLaundryRoomCalculater.CostAverageLaundryRoomCalculater()
CostAverageSuperMarketCalculater = CostAverageSuperMarketCalculater.CostAverageSuperMarketCalculater()
CostRateDinnerHallCalculater = CostRateDinnerHallCalculater.CostRateDinnerHallCalculater()
CostRateLaundryRoomCalculater = CostRateLaundryRoomCalculater.CostRateLaundryRoomCalculater()
CostRateSuperMarketCalculater = CostRateSuperMarketCalculater.CostRateSuperMarketCalculater()
CostTimesCalculater = CostTimesCalculater.CostTimesCalculater()
LibraryBorrowCalculater = LibraryBorrowCalculater.LibraryBorrowCalculater()
LibraryTimesCalculater = LibraryTimesCalculater.LibraryTimesCalculater()
LibraryTimeSpandCalculater = LibraryTimeSpandCalculater.LibraryTimeSpandCalculater() 
SubsidyCalculater = SubsidyCalculater.SubsidyCalculater()
calculater = [ScoreRankCalculater, \
              CostAmountCalculater, \
              CostAverageDinnerHallCalculater, CostAverageLaundryRoomCalculater, CostAverageSuperMarketCalculater, \
              CostRateDinnerHallCalculater, CostRateLaundryRoomCalculater, CostRateSuperMarketCalculater, \
              CostTimesCalculater, \
              LibraryBorrowCalculater, LibraryTimesCalculater, LibraryTimeSpandCalculater,
              BalanceRankCalculater, ]#, \
             # SubsidyCalculater, ]

def calculate():
    db = MyDataBase.MyDataBase()
    conn = db.getConn()
    executer = db.getExcuter()
    
    sql = "delete from students"
    executer.execute(sql)
    sql = "delete from library_modify"
    executer.execute(sql)
    conn.commit()
    
    sql = "select student_id from score"
    executer.execute(sql)
    studentIds = executer.fetchall()
    students = []
    
    for i in tqdm(studentIds):
        print()
        i = i[0]
        student = Student()
        student.setStudentId(i)
        student.fetch(calculater)
    
    for i in calculater:
        i.afterCalculate()

if __name__=='__main__':
    calculate()