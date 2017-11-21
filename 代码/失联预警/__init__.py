print('鎺ヤ笅鏉ヤ负浣犲垪鍑哄彲鑳藉け鑱旂殑瀛︾敓')


# 涓嬮潰鏄竴浜涘彲鑳藉浜庡け鑱旂姸鎬佺殑瑙勫垯锛屽彧瑕佺鍚堝叾涓殑5鏉★紝灏辫鏄庝粬澶辫仈浜�
# 鍦ㄨ繖娈垫椂闂翠腑绠楁櫄
timeSlot = "BETWEEN '01:00:00' AND '04:00:00"
# 鍦ㄥ闈㈠緢鏅氱殑娆℃暟锛岄珮浜庤繖涓鏁板氨涓嶅ソ
StayOutLateTimes = "5"
# 涓�涓湀record_type鏈巿鏉冭秴杩�5娆�
wrong_time_sql = "SELECT\
    DISTINCT(student_num)\
FROM\
    (\
        SELECT\
            student_num,\
            count(record_type = '鏈巿鏉�') AS wrong_time,\
            DATE_FORMAT(record_time, '%Y-%m') AS MONTH\
        FROM\
            dorm_entrance\
        GROUP BY\
            student_num,\
            MONTH\
    ) t\
WHERE\
    wrong_time >= 130"
# 瓒呰繃2鐐瑰嚭瀹胯垗锛�#骞朵笖瓒呰繃1涓皬鏃舵病鍥炴潵
m_out_1_not_in_sql = "SELECT DISTINCT\
    (student_num)\
FROM\
    dorm_entrance\
WHERE\
    in_out = '鍑洪棬'\
AND DATE_FORMAT(record_time, '%H:%i') BETWEEN '02:00'\
AND '04:30'"
# 瓒呰繃2鐐规墠鍥炲鑸嶆鏁拌秴杩�3娆�
over_2_in_3_times_sql = "SELECT\
    *\
FROM\
    (\
        SELECT\
            student_num,\
            COUNT(*) AS times\
        FROM\
            dorm_entrance\
        WHERE\
            in_out = '杩涢棬'\
        AND DATE_FORMAT(record_time, '%H:%i') BETWEEN '02:00'\
        AND '04:30'\
        GROUP BY\
            student_num\
    ) t\
WHERE\
    times > 3"
# 鍦ㄥ伐浣滄棩鍦ㄥ鏃堕棿瓒呰繃48灏忔椂
#
 
