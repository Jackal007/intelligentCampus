from Model import Student
from Tools import MyDataBase
from tqdm import tqdm
from a_FeatureCalculate.AvgDaysCostsCalculater import AvgDaysCostsCalculater
from a_FeatureCalculate.BalanceRankCalculater import BalanceRankCalculater
from a_FeatureCalculate.CardDaysCalculater import CardDaysCalculater
from a_FeatureCalculate.CardRechargeCalculater import CardRechargeCalculater
from a_FeatureCalculate.ConsumeTimes11_12Calculater import ConsumeTimes11_12Calculater
from a_FeatureCalculate.CostAmountCalculater import CostAmountCalculater
from a_FeatureCalculate.CostAverageDayDinnerHallCalculater import CostAverageDayDinnerHallCalculater
from a_FeatureCalculate.CostAverageDayLaundryRoomCalculater import CostAverageDayLaundryRoomCalculater
from a_FeatureCalculate.CostAverageDaySupermarketCalculater import CostAverageDaySupermarketCalculater
from a_FeatureCalculate.CostTimesDayDinnerHallCalculater import CostTimesDayDinnerHallCalculater
from a_FeatureCalculate.CostTimesDayLaundryRoomCalculater import CostTimesDayLaundryRoomCalculater
from a_FeatureCalculate.CostTimesDaySupermarketCalculater import CostTimesDaySupermarketCalculater
from a_FeatureCalculate.CostRateDinnerHallCalculater import CostRateDinnerHallCalculater
from a_FeatureCalculate.CostRateLaundryRoomCalculater import CostRateLaundryRoomCalculater
from a_FeatureCalculate.CostRateSupermarketCalculater import CostRateSupermarketCalculater
from a_FeatureCalculate.CostVarianceCalculater import CostVarianceCalculater
from a_FeatureCalculate.CosumeTimes0_25Calculater import CosumeTimes0_25Calculater
from a_FeatureCalculate.CountCost0_10Calculater import CountCost0_10Calculater
from a_FeatureCalculate.LibraryBorrowCalculater import LibraryBorrowCalculater
from a_FeatureCalculate.LibraryTimesCalculater import LibraryTimesCalculater
from a_FeatureCalculate.LibraryTimeSpandCalculater import LibraryTimeSpandCalculater
from a_FeatureCalculate.MaxCost7_8Calculater import MaxCost7_8Calculater
from a_FeatureCalculate.ScoreRankCalculater import ScoreRankCalculater
from a_FeatureCalculate.SubsidyCalculater import SubsidyCalculater
from a_FeatureCalculate.Time6_7CostsCalculater import Time6_7CostsCalculater
from a_FeatureCalculate.Time7_8CostsCalculater import Time7_8CostsCalculater
from a_FeatureCalculate.TotalDinnerCostsCalculater import TotalDinnerCostsCalculater
from a_FeatureCalculate.Avg_ChargeCaculater import Avg_ChargeCaculater
from a_FeatureCalculate.Below2_5_RankCalculater import Below2_5_RankCalculater
from a_FeatureCalculate.Below10_RankCalculater import Below10_RankCalculater
from a_FeatureCalculate.Num_Of_1000Calculater import Num_Of_1000Calculater
from a_FeatureCalculate.Num_Of_2000Calculater import Num_Of_2000Calculater
from a_FeatureCalculate.Num_Of_1500Calculater import Num_Of_1500Calculater
from a_FeatureCalculate.PropotionCalculater1000 import PropotionCalculater1000
from a_FeatureCalculate.PropotionCalculater2000 import PropotionCalculater2000
from a_FeatureCalculate.PropotionCalculater1500 import PropotionCalculater1500
from a_FeatureCalculate.scorerank_divided_by_stunum import scorerank_divided_by_stunum
from a_FeatureCalculate.Stu_Num_Calculater import Stu_Num_Calculater

Student = Student.Student
AvgDaysCostsCalculater = AvgDaysCostsCalculater()          
Below10_RankCalculater=Below10_RankCalculater()       
BalanceRankCalculater = BalanceRankCalculater()                  
CardDaysCalculater = CardDaysCalculater()               
CardRechargeCalculater = CardRechargeCalculater()                   
ConsumeTimes11_12Calculater = ConsumeTimes11_12Calculater()                      
CostAmountCalculater = CostAmountCalculater()                 
CostAverageDayDinnerHallCalculater = CostAverageDayDinnerHallCalculater()                
CostAverageDayLaundryRoomCalculater = CostAverageDayLaundryRoomCalculater()              
CostAverageDaySupermarketCalculater = CostAverageDaySupermarketCalculater()                     
CostTimesDayDinnerHallCalculater = CostTimesDayDinnerHallCalculater()                    
CostTimesDayLaundryRoomCalculater = CostTimesDayLaundryRoomCalculater()                  
CostTimesDaySupermarketCalculater = CostTimesDaySupermarketCalculater()                       
CostRateDinnerHallCalculater = CostRateDinnerHallCalculater()                    
CostRateLaundryRoomCalculater = CostRateLaundryRoomCalculater()                  
CostRateSupermarketCalculater = CostRateSupermarketCalculater()    
CostVarianceCalculater = CostVarianceCalculater()                 
CosumeTimes0_25Calculater = CosumeTimes0_25Calculater()                    
CountCost0_10Calculater = CountCost0_10Calculater()                    
LibraryBorrowCalculater = LibraryBorrowCalculater()                    
LibraryTimesCalculater = LibraryTimesCalculater()                   
LibraryTimeSpandCalculater = LibraryTimeSpandCalculater()                       
MaxCost7_8Calculater = MaxCost7_8Calculater()                 
ScoreRankCalculater = ScoreRankCalculater()              
SubsidyCalculater = SubsidyCalculater()           
Time6_7CostsCalculater = Time6_7CostsCalculater()                 
Time7_8CostsCalculater = Time7_8CostsCalculater()                 
TotalDinnerCostsCalculater = TotalDinnerCostsCalculater()                      
Avg_ChargeCaculater = Avg_ChargeCaculater()                      
Below2_5_RankCalculater = Below2_5_RankCalculater()                       
Num_Of_1000Calculater = Num_Of_1000Calculater()                       
Num_Of_2000Calculater = Num_Of_2000Calculater()                       
Num_Of_1500Calculater = Num_Of_1500Calculater()                       
PropotionCalculater1000 = PropotionCalculater1000()                       
PropotionCalculater2000 = PropotionCalculater2000()                       
PropotionCalculater1500 = PropotionCalculater1500()                       
scorerank_divided_by_stunum = scorerank_divided_by_stunum()                       
Stu_Num_Calculater = Stu_Num_Calculater()

calculater = [
#             Stu_Num_Calculater,
#             Num_Of_1000Calculater,
#             Num_Of_2000Calculater,
#             Num_Of_1500Calculater,
            ScoreRankCalculater,
            Below10_RankCalculater,
            Time6_7CostsCalculater,
            Time7_8CostsCalculater,
            TotalDinnerCostsCalculater,
            AvgDaysCostsCalculater,
            BalanceRankCalculater,
            CardDaysCalculater,
            CardRechargeCalculater,
            ConsumeTimes11_12Calculater,
            CostAmountCalculater,
            CostAverageDayDinnerHallCalculater,
            CostAverageDayLaundryRoomCalculater,
            CostAverageDaySupermarketCalculater,
 
            CostRateDinnerHallCalculater,
            CostRateLaundryRoomCalculater,
            CostRateSupermarketCalculater,
             
            CostTimesDayDinnerHallCalculater,
            CostTimesDayLaundryRoomCalculater,
            CostTimesDaySupermarketCalculater,
            CostVarianceCalculater,
            CosumeTimes0_25Calculater,
            CountCost0_10Calculater,
            LibraryBorrowCalculater,
            LibraryTimesCalculater,
            LibraryTimeSpandCalculater,
            MaxCost7_8Calculater,
            Avg_ChargeCaculater,
            Below2_5_RankCalculater,
                         
            PropotionCalculater1000,
            PropotionCalculater2000,
            PropotionCalculater1500,
            scorerank_divided_by_stunum,
            SubsidyCalculater,
            ]

# calculater = [SubsidyCalculater]

def calculate():
    db = MyDataBase.MyDataBase("train")
    conn = db.getConn()
    executer = db.getExcuter()
    
    sql = "delete from students"
    executer.execute(sql)
    sql = "delete from students_rank"
    executer.execute(sql)
    sql = "delete from library_modify"
    executer.execute(sql)
    
    sql = "select student_id from score"
    executer.execute(sql)
    studentIds = executer.fetchall()
    db.close()
     
    for i in tqdm(studentIds):
        i = i[0]
        student = Student(studentId=i)
        student.calculate(calculater)
         
    for i in calculater:
        i.setLevel()
     
    for i in tqdm(studentIds):
        i = i[0]
        student = Student(studentId=i)
        student.calculate(calculater)
     
    for i in calculater:
        i.afterCalculate()

if __name__ == '__main__':
    calculate()
