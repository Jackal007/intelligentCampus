from FeatureCalculate import Student
from Tools import MyDataBase
from tqdm import tqdm
from FeatureCalculate.AvgDaysCostsCalculater import AvgDaysCostsCalculater
from FeatureCalculate.BalanceRankCalculater import BalanceRankCalculater
from FeatureCalculate.CardDaysCalculater import CardDaysCalculater
from FeatureCalculate.CardRechargeCalculater import CardRechargeCalculater
from FeatureCalculate.ConsumeTimes11_12Calculater import ConsumeTimes11_12Calculater
from FeatureCalculate.CostAmountCalculater import CostAmountCalculater
from FeatureCalculate.CostAverageDayDinnerHallCalculater import CostAverageDayDinnerHallCalculater
from FeatureCalculate.CostAverageDayLaundryRoomCalculater import CostAverageDayLaundryRoomCalculater
from FeatureCalculate.CostAverageDaySupermarketCalculater import CostAverageDaySupermarketCalculater
from FeatureCalculate.CostTimesDayDinnerHallCalculater import CostTimesDayDinnerHallCalculater
from FeatureCalculate.CostTimesDayLaundryRoomCalculater import CostTimesDayLaundryRoomCalculater
from FeatureCalculate.CostTimesDaySupermarketCalculater import CostTimesDaySupermarketCalculater
from FeatureCalculate.CostRateDinnerHallCalculater import CostRateDinnerHallCalculater
from FeatureCalculate.CostRateLaundryRoomCalculater import CostRateLaundryRoomCalculater
from FeatureCalculate.CostRateSupermarketCalculater import CostRateSupermarketCalculater
from FeatureCalculate.CostVarianceCalculater import CostVarianceCalculater
from FeatureCalculate.CosumeTimes0_25Calculater import CosumeTimes0_25Calculater
from FeatureCalculate.CountCost0_10Calculater import CountCost0_10Calculater
from FeatureCalculate.LibraryBorrowCalculater import LibraryBorrowCalculater
from FeatureCalculate.LibraryTimesCalculater import LibraryTimesCalculater
from FeatureCalculate.LibraryTimeSpandCalculater import LibraryTimeSpandCalculater
from FeatureCalculate.MaxCost7_8Calculater import MaxCost7_8Calculater
from FeatureCalculate.ScoreRankCalculater import ScoreRankCalculater
from FeatureCalculate.SubsidyCalculater import SubsidyCalculater
from FeatureCalculate.Time6_7CostsCalculater import Time6_7CostsCalculater
from FeatureCalculate.Time7_8CostsCalculater import Time7_8CostsCalculater
from FeatureCalculate.TotalDinnerCostsCalculater import TotalDinnerCostsCalculater
from FeatureCalculate.Avg_ChargeCaculater import Avg_ChargeCaculater
from FeatureCalculate.Below2_5_RankCalculater import Below2_5_RankCalculater
from FeatureCalculate.Below10_RankCalculater import Below10_RankCalculater
from FeatureCalculate.Num_Of_1000Calculater import Num_Of_1000Calculater
from FeatureCalculate.Num_Of_2000Calculater import Num_Of_2000Calculater
from FeatureCalculate.Num_Of_1500Calculater import Num_Of_1500Calculater
from FeatureCalculate.PropotionCalculater1000 import PropotionCalculater1000
from FeatureCalculate.PropotionCalculater2000 import PropotionCalculater2000
from FeatureCalculate.PropotionCalculater1500 import PropotionCalculater1500
from FeatureCalculate.scorerank_divided_by_stunum import scorerank_divided_by_stunum
from FeatureCalculate.Stu_Num_Calculater import Stu_Num_Calculater
from FeatureCalculate.Time7_8Consume_Avg import Time7_8Consume_Avg


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
Time7_8Consume_Avg = Time7_8Consume_Avg()

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
            Time7_8Consume_Avg
            ]

# calculater = [SubsidyCalculater]

def calculate():
    db = MyDataBase.MyDataBase("train")
    conn = db.getConn()
    executer = db.getExcuter()

    
    sql = "select student_id from score"
    executer.execute(sql)
    studentIds = executer.fetchall()
    db.close()
     
#     for i in tqdm(studentIds):
#         i = i[0]
#         student = Student(studentId=i)
#         student.calculate(calculater)
           
    for i in calculater:
        i.setLevel()
      
    for i in tqdm(studentIds):
        i = i[0]
        student = Student(studentId=i)
        student.rankit(calculater)
     
    for i in calculater:
        i.afterCalculate()

if __name__ == '__main__':
    calculate()
