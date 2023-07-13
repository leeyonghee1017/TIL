# 2. 데이타 조회

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='sqldb')
cur = conn.cursor()

sql = "select userid, name, birthyear, addr from usertbl;"

cur.execute(sql)

while True:
    v_row =  cur.fetchone()

    if v_row == None:
        break
    
    print(v_row, v_row[0], v_row[1], v_row[2], v_row[3])
    
conn.close()
