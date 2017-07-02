from Model import Student
from Tools import MyDataBase
from tqdm import tqdm
from a_CalculateField import MyConfig
from a_CalculateField import ScoreRankCalculater
from a_CalculateField import CostAmountCalculater
from a_CalculateField import CostDinnerHallAverageCalculater
from a_CalculateField import CostSuperMarketAverageCalculater
from a_CalculateField import LibraryBorrowCalculater
from a_CalculateField import BalanceRankCalculater
from a_CalculateField import LibraryTimesCalculater
from a_CalculateField import LibraryTimeSpandCalculater
from a_CalculateField import CostSuperMarketRateCalculater
from a_CalculateField import CostDinnerHallRateCalculater
from a_CalculateField import CostTimesCalculater
from a_CalculateField import SubsidyCalculater


Student = Student.Student

db = MyDataBase.MyDataBase()
executer = db.getExcuter()

sql = "select student_id from score"
executer.execute(sql)
studentIds = executer.fetchall()
students = []

ScoreRankCalculater = ScoreRankCalculater.ScoreRankCalculater(MyConfig.Score_level)
CostAmountCalculater = CostAmountCalculater.CostAmountCalculater(MyConfig.CostAmount_level)
CostDinnerHallAverageCalculater = CostDinnerHallAverageCalculater.CostDinnerHallAverageCalculater(MyConfig.AverageDinnerHallCost_level)
CostSuperMarketAverageCalculater = CostSuperMarketAverageCalculater.CostSuperMarketAverageCalculater(MyConfig.AverageSuperMarketCost_level)
LibraryBorrowCalculater = LibraryBorrowCalculater.LibraryBorrowCalculater(MyConfig.LibraryBorrow_level)
BalanceRankCalculater = BalanceRankCalculater.BalanceRankCalculater(MyConfig.BalanceRank_level)
LibraryTimesCalculater = LibraryTimesCalculater.LibraryTimesCalculater(MyConfig.LibraryTimes_level)
LibraryTimeSpandCalculater = LibraryTimeSpandCalculater.LibraryTimeSpandCalculater(MyConfig.LibraryTimeSpand_level) 
CostSuperMarketRateCalculater = CostSuperMarketRateCalculater.CostSuperMarketRateCalculater(MyConfig.CostSuperMarketRate_level)
CostDinnerHallRateCalculater = CostDinnerHallRateCalculater.CostDinnerHallRateCalculater(MyConfig.CostDinnerHallRate_level)
CostTimesCalculater = CostTimesCalculater.CostTimesCalculater(MyConfig.CostTimes_level)
SubsidyCalculater = SubsidyCalculater.SubsidyCalculater(MyConfig.Subsidy_level)
calculater = [ScoreRankCalculater, CostAmountCalculater, CostDinnerHallAverageCalculater, CostSuperMarketAverageCalculater, LibraryBorrowCalculater, \
            BalanceRankCalculater, LibraryTimesCalculater, LibraryTimeSpandCalculater, LibraryTimeSpandCalculater, \
            CostSuperMarketRateCalculater, CostDinnerHallRateCalculater, CostTimesCalculater, SubsidyCalculater]

for i in tqdm(studentIds):
    print()
    i = i[0]
    student = Student([])
    student.setStudentId(i)
    student.setAll(calculater)

for i in calculater:
    i.afterCalculate()
