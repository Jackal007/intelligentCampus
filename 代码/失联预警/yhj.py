'''
Created on 2017Äê11ÔÂ21ÈÕ

@author: LENOVO
'''

#stu_in_activities
# sql="select DISTINCT Stu_num,Stu_name,Stu_type,Grade from stu_in_activities"
#         cursor.execute(sql)
#         result=cursor.fetchall()
#         #sql="select sum(Participation_score)/count(*),sum(Active_level)/count(*) as activity_avg_level,sum(Activity_num) as Activity_num from stu_in_activities group by Stu_num,"
#         for re in result:
#             #print(re[1])
#            count=2014
#            for i in range(4):
#                sql="insert into students(student_num,student_name,student_type,student_grade,school_year) values(%s,%s,%s,%s,%s)"
#                #print(re[0],re[1],re[2],re[3])
#                cursor.execute(sql,(re[0],re[1],re[2],re[3],int(count)))
#                #cursor.execute(sql)
#                count=count+1

#stu_in_activities
#update students set activity_last_time=0;
#update students set avg_hornorary_times=0;
#update students set hornorary_amount=0;
# sql="select Stu_num,DATE_FORMAT(Start_time, '%Y'),sum(time_to_sec(timediff(Finish_time,Start_time))) from stu_in_activities  group by stu_num,DATE_FORMAT(Start_time, '%Y')"
#         cursor.execute(sql)
#         result=cursor.fetchall()
#         print(result)
#         for re in result:
#             #sql="update students set activity_last_time="+double(re[2]+" where student_num='"+re[0]+"' and school_year='"+re[1]+"'"
#             #cursor.execute(sql,(double(re[2],re[0],re[1])))
#             sql="update students set activity_last_time=%s where student_num=%s and school_year=%s"
#             cursor.execute(sql,(double(re[2]),re[0],re[1]))
#         conn.commit()



#hornorary_title
#            sql="select student_num,sum(amount) as amount,grant_year,count(*) as times from hornorary_title where title_name!="" group by student_num,grant_year"
#            cursor.execute(sql)
#            result=cursor.fetchall()
#             #print(result)
#            for re in result:
#                sql="update students set hornorary_amount=%s,avg_hornorary_times=%s where student_num=%s and school_year=%s"
#                  #sql="update students set hornorary_amount=%s,avg_hornorary_times=%s where student_num=%s and school_year=%s"
#                cursor.execute(sql,(int(re[1]),int(re[3]),re[0],re[2]))
#                  #print(re[1])
#                  #cursor.execute(sql,(re[0],re[1],re[2],re[3],int(count)))
#            conn.commit()


#library_borrow
#  sql="select student_num,DATE_FORMAT(borrow_date, '%Y'),count(*) from library_borrow group by student_num,DATE_FORMAT(borrow_date, '%Y')"
#         cursor.execute(sql)
#         result=cursor.fetchall()
#         print(result)
#         sql="update students set borrow_times=0"
#         cursor.execute(sql)
#         for re in result:
#              sql="update students set borrow_times=%s where student_num=%s and school_year=%s"
#              cursor.execute(sql,(int(re[2]),re[0],re[1]))
#         conn.commit()