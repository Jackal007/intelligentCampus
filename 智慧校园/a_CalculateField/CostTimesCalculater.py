from a_CalculateField import XXCalculater

class CostTimesCalculater(XXCalculater.XXCalculater):

    def calculate(self):
        
        print("CalculateLibraryBorrow")
        # 对每一个学生统计其消费次数
        for studentId in tqdm(self.students):
            sql = "select count(*) from card where student_id=" + str(studentId)
            self.executer.execute(sql)

            data = self.executer.fetchone()
            cost_times = data[0]
            weight = "D"
            if cost_times < self.level["A"]:
                weight ="A"
            elif cost_times < self.level["B"]:
                weight ="B"
            elif cost_times < self.level["C"]:
                weight = "C"
            try:
                sql = "update students set cost_times='" + str(weight) + "' where student_id=" + str(studentId)
                self.executer.execute(sql)
            except:
                print(sql)
        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateLibraryBorrow(level)
    t.calculate()
