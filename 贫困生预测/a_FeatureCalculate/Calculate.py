from Model import Student
from Tools import MyDataBase
from tqdm import tqdm
from a_FeatureCalculate.AvgDaysCostsCalculater import AvgDaysCostsCalculater
from a_FeatureCalculate.BalanceRankCalculater import BalanceRankCalculater
# from a_FeatureCalculate.CardDaysCalculater import CardDaysCalculater
from a_FeatureCalculate.CardRechargeCalculater import CardRechargeCalculater
from a_FeatureCalculate.ConsumeTimes11_12Calculater import ConsumeTimes11_12Calculater
from a_FeatureCalculate.CostAmountCalculater import CostAmountCalculater
# from a_FeatureCalculate.CostAverageDayCalculater import CostAverageDayCalculater
# from a_FeatureCalculate.CostTimesDayCalculater import CostTimesDayCalculater
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

Student = Student.Student
AvgDaysCostsCalculater = AvgDaysCostsCalculater()                 
BalanceRankCalculater = BalanceRankCalculater()                  
# CardDaysCalculater = CardDaysCalculater()               
CardRechargeCalculater = CardRechargeCalculater()                   
ConsumeTimes11_12Calculater = ConsumeTimes11_12Calculater()                      
CostAmountCalculater = CostAmountCalculater()                 
# CostAverageDayCalculater = CostAverageDayCalculater()                     
# CostTimesDayCalculater = CostTimesDayCalculater()                 
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

# calculater = [ScoreRankCalculater,
#             AvgDaysCostsCalculater,
#             BalanceRankCalculater,
# #             CardDaysCalculater,
#             CardRechargeCalculater,
#             ConsumeTimes11_12Calculater,
#             CostAmountCalculater,
# #             CostAverageDayCalculater,
# #             CostTimesDayCalculater,
#             CostVarianceCalculater,
#             CosumeTimes0_25Calculater,
#             CountCost0_10Calculater,
#             LibraryBorrowCalculater,
#             LibraryTimesCalculater,
#             LibraryTimeSpandCalculater,
#             MaxCost7_8Calculater,
#             SubsidyCalculater,
#             Time6_7CostsCalculater,
#             Time7_8CostsCalculater,
#             TotalDinnerCostsCalculater,
#             ]

calculater = [ScoreRankCalculater]

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
    db.close()
    students = []
    
    for i in calculater:
        i.level = None
    
    for i in tqdm(studentIds):
        print()
        i = i[0]
        student = Student()
        student.setStudentId(i)
        student.fetch(calculater)
        
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
