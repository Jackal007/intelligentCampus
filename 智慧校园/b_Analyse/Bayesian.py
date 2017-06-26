from Tools import MyDataBase
from Model import Student

# def classfiy(o):
#     if o == "A":
#         return 1
#     elif o == "B":
#         return 2
#     else:
#         return 3

Student = Student.Student
db = MyDataBase.MyDataBase()
conn = db.getConn()
executer = db.getExcuter()

# get all the students
sql = "select student_id,score,cost_amount,cost_avg_superMarket,cost_avg_dinnerHall,cost_supermarket_rate,cost_dinnerhall_rate,cost_times,library_borrow,library_times,library_time_spand,balance_rank,subsidy from students"
executer.execute(sql)
students = []
for i in executer.fetchall():
    students.append(Student(i))

def testData():
    salt = 0.15
    # 
    subsidy = {"A":0, "B":0, "C":0, "D": 0}  
    score = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    cost_amount = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    cost_avg_superMarket = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    cost_avg_dinnerHall = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    cost_supermarket_rate = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    cost_dinnerhall_rate = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    cost_times = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    library_borrow = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    library_times = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    library_time_spand = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    balance_rank = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
    
    for student in students:
        subsidy[student.getSubsidy()] = subsidy[student.getSubsidy()] + 1
        score[student.getScore()][student.getSubsidy()] = score[student.getScore()][student.getSubsidy()] + 1  
        cost_amount[student.getCost_amount()][student.getSubsidy()] = cost_amount[student.getCost_amount()][student.getSubsidy()] + 1 
        cost_avg_superMarket[student.getCost_avg_superMarket()][student.getSubsidy()] = cost_avg_superMarket[student.getCost_avg_superMarket()][student.getSubsidy()] + 1 
        cost_avg_dinnerHall[student.getCost_avg_dinnerHall()][student.getSubsidy()] = cost_avg_dinnerHall[student.getCost_avg_dinnerHall()][student.getSubsidy()] + 1 
        cost_supermarket_rate[student.getCost_supermarket_rate()][student.getSubsidy()] = cost_supermarket_rate[student.getCost_supermarket_rate()][student.getSubsidy()] + 1 
        cost_dinnerhall_rate[student.getCost_dinnerhall_rate()][student.getSubsidy()] = cost_dinnerhall_rate[student.getCost_dinnerhall_rate()][student.getSubsidy()] + 1 
        cost_times[student.getCost_times()][student.getSubsidy()] = cost_times[student.getCost_times()][student.getSubsidy()] + 1  
        library_borrow[student.getLibrary_time_spand()][student.getSubsidy()] = library_borrow[student.getLibrary_time_spand()][student.getSubsidy()] + 1 
        library_times[student.getLibrary_times()][student.getSubsidy()] = library_times[student.getLibrary_times()][student.getSubsidy()] + 1
        library_time_spand[student.getLibrary_time_spand()][student.getSubsidy()] = library_time_spand[student.getLibrary_time_spand()][student.getSubsidy()] + 1
        balance_rank[student.getBalance_rank()][student.getSubsidy()] = balance_rank[student.getBalance_rank()][student.getSubsidy()] + 1 
    for i in ["A", "B", "C", "D"]:
        # �޷���ȡ��ѧ��ĸ���
        # ��ȡ1000��ѧ��ĸ���
        # ��ȡ1500��ѧ��ĸ���
        # ��ȡ2000��ѧ��ĸ���
        P_subsidy[i] = subsidy[i] / len(students);
    for i in ["A", "B", "C", "D"]:
        for j in ["A", "B", "C", "D"]:
            P_score[j][i] = float(score[i][j]) / float(subsidy[i][j]) + salt
            P_cost_amount[j][i] = float(cost_amount[i][j]) / float(subsidy[i][j]) + salt
            P_cost_avg_superMarket[j][i] = float(cost_avg_superMarket[i][j]) / float(subsidy[i][j]) + salt
            P_cost_avg_dinnerHall[j][i] = float(cost_avg_dinnerHall[i][j]) / float(subsidy[i][j]) + salt
            P_cost_supermarket_rate[j][i] = float(cost_supermarket_rate[i][j]) / float(subsidy[i][j]) + salt
            P_cost_dinnerhall_rate[j][i] = float(cost_dinnerhall_rate[i][j]) / float(subsidy[i][j]) + salt
            P_cost_times[j][i] = float(cost_times[i][j]) / float(subsidy[i][j]) + salt
            P_library_borrow[j][i] = float(library_borrow[i][j]) / float(subsidy[i][j]) + salt
            P_library_times[j][i] = float(library_times[i][j]) / float(subsidy[i][j]) + salt
            P_library_time_spand[j][i] = float(library_time_spand[i][j]) / float(subsidy[i][j]) + salt
            P_balance_rank[j][i] = float(balance_rank[i][j]) / float(subsidy[i][j]) + salt
     
def Analyse_test(studentId, score, cost_amount, cost_avg_superMarket, cost_avg_dinnerHall, cost_supermarket_rate, cost_dinnerhall_rate, cost_times, library_borrow, library_times, library_time_spand, balance_rank):
    t_subsidy = {"A":1, "B":1, "C":1, "D": 1}
    for i in ["A", "B", "C", "D"]:
        t_subsidy[i] = t_subsidy[i] * P_score[score][i]\
        *P_cost_amount[cost_amount][i] * P_cost_avg_superMarket[cost_avg_superMarket][i] * P_cost_avg_dinnerHall[cost_avg_dinnerHall][i] * \
        P_cost_supermarket_rate[cost_supermarket_rate] * P_cost_dinnerhall_rate[cost_dinnerhall_rate][i] * P_cost_times[cost_times][i] * \
        P_library_borrow[library_borrow][i] * P_library_times[library_times][i] * P_library_time_spand[library_time_spand][i] * \
        P_balance_rank[balance_rank][i]
    
    max = tag = 0;
    for i in ["A", "B", "C", "D"]:
        if P_subsidy[i] > max:
            tag = i
            max = P_subsidy[i]
    
    if tag == "A": 
        print (studentId, " 0")
    elif tag == "B": 
        print (studentId, " 1000")
    elif tag == "C": 
        print (studentId, " 1500")
    elif tag == "D": 
        print (studentId, " 2000")

def analyse():
    for student in students:
        Analyse_test(student.getstudentdent_id(), student.getBalance_rank(), student.getBook_borrow(), student.getScore(), student.getCost_amount(), student.getLibrary_time_spand(), student.getLibrary_times())

# ����
P_score = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_cost_amount = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_cost_avg_superMarket = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_cost_avg_dinnerHall = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_cost_supermarket_rate = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_cost_dinnerhall_rate = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_cost_times = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_library_borrow = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_library_times = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_library_time_spand = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_balance_rank = {"A":{"A":0, "B":0, "C":0, "D": 0}, "B": {"A":0, "B":0, "C":0, "D": 0}, "C":{"A":0, "B":0, "C":0, "D": 0}, "D": {"A":0, "B":0, "C":0, "D": 0}}
P_subsidy = {"A":0, "B":0, "C":0, "D": 0}

testData()
analyse()
