from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import CostTimes_level

class CostTimesCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CostTimesCalculater")
        # 对每一个学生统计其消费次数
        studentId = self.student.getStudentId()
        sql = "select count(*) from card where student_id=" + str(studentId)
        self.executer.execute(sql)

        costTimes = self.executer.fetchone()[0]
        costTimes = self.classify(costTimes, CostTimes_level)
        
        sql = "update students set cost_times='" + costTimes + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return costTimes