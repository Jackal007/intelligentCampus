import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "intelligentcampustrain")
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT \
       student_id, \
       date(deal_date),\
       sum(deal_cost) \
       FROM   \
        card\
        GROUP BY \
        student_id, \
        date(deal_date) "
# try:
# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print(len(results))
for row in results:
   studentid = int(row[0])
   date = row[1]
   date_cost = float(row[2])
   sql = " insert into card_2 values(" + str(studentid) + ",'" + str(date) + "'," + str(date_cost) + ")"
   cursor.execute(sql)
   
   print('.')
   # 打印结果`

# except:
#    print ("Error: unable to fecth data")
db.commit()
# 关闭数据库连接
db.close()
