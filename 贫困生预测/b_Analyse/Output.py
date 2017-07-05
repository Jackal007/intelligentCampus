def output(students,result):
    n=len(students) #n代表结果的个数
    if n!=len(result):
        return
    with open('../d_CorrectRateTest/results.txt', 'w')as f:
        for i in range(n):
            temp=""
            if result[i] == 1:
                temp = 0
            elif result[i] == 2:
                temp = 1000
            elif result[i] == 3:
                temp = 1500
            elif result[i] == 4:
                temp = 2000
            else:
                print("!!!!!!!!!!!!!")
              
            f.write(str(students[i].getStudentId()) + "," + str(temp) + "\n")