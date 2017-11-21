print('接下来为你列出可能失联的学生')

# 下面是一些可能处于失联状态的规则，只要符合其中的5条，就说明他失联了
# 在这段时间中算晚
timeSlot = "BETWEEN '01:00:00' AND '04:00:00"
# 在外面很晚的次数，高于这个次数就不好
StayOutLateTimes = "5"
# 超过1点出宿舍，#并且超过1个小时没回来
m_out_1_not_in_sql = "SELECT DISTINCT(student_num) FROM dorm_entrance WHERE in_out = '出门' AND DATE_FORMAT(record_time, '%H:%i') BETWEEN '01:00' AND '04:30'"
# 超过1点才回宿舍次数超过3次
over_2_in_3_times_sql = "SELECT * FROM ( SELECT student_num,COUNT(*) AS times FROM dorm_entrance WHERE in_out = '进门' AND DATE_FORMAT(record_time, '%H:%i') BETWEEN '01:00' AND '04:30' GROUP BY student_num ) t WHERE times > 3"
# 在工作日在外时间超过48小时
#
# 一个月record_type未授权超过120次
wrong_time_sql = "SELECT DISTINCT(student_num) FROM (SELECT student_num,count(record_type = '未授权') AS wrong_time,DATE_FORMAT(record_time, '%Y-%m') AS MONTH FROM dorm_entrance GROUP BY student_num,MONTH) t WHERE wrong_time >= 100"

 
