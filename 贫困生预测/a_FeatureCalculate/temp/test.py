from Model import Student
from Tools import MyDataBase
from tqdm import tqdm
from a_FeatureCalculate.modifying.Time7_8Consume_Avg import Time7_8Consume_Avg

Student = Student.Student
Time7_8Consume_Avg = Time7_8Consume_Avg()                       

calculater = [Time7_8Consume_Avg]

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
