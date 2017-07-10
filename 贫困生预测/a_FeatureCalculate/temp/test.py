from Model import Student
from Tools import MyDataBase
from tqdm import tqdm
from a_FeatureCalculate.modifying.Below10_RankCalculater import Below10_RankCalculater

Student = Student.Student
Below10_RankCalculater = Below10_RankCalculater()                       

calculater = [Below10_RankCalculater]

def calculate():
    db = MyDataBase.MyDataBase("train")
    conn = db.getConn()
    executer = db.getExcuter()
    
    sql = "select student_id from score"
    executer.execute(sql)
    studentIds = executer.fetchall()
    db.close()
    students = []
     
    for i in tqdm(studentIds):
        i = i[0]
        student = Student()
        student.setStudentId(i)
        student.calculate(calculater)
        
    for i in calculater:
        i.setLevel()
    
    for i in tqdm(studentIds):
        i = i[0]
        student = Student()
        student.setStudentId(i)
        student.rankit(calculater)
    
    for i in calculater:
        i.afterCalculate()

if __name__ == '__main__':
    calculate()
