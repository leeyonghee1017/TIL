# 1. 데이타 입력

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='sqldb')
cur = conn.cursor()

sql = "insert into usertbl(userid, name, birthyear, addr) values('KKK', 'KIM', 1991, 'SL');"

cur.execute(sql)
conn.commit()
conn.close()
