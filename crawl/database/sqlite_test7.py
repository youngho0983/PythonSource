# SQLite:내장 데이터베이스 (응용 프로그램에 넣어서 사용.)
import sqlite3
from datetime import datetime

# database 생성 & 연결 의 의미
conn = sqlite3.connect("./crawl/database/test.db")

# Corsor 획득
cursor = conn.cursor()

now = datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")

# sql = "select * from users where id =?"
# cursor.execute(sql ,(3,))


# sql="select * from users where id = %s "
# cursor.execute(sql % 4)

# param={"id" :5}
# sql="select * from users where id = :id "
# cursor.execute(sql , param)

param = (3,5)
sql ="select * from users where id in (?,?)"
cursor.execute(sql,param)
print(cursor.fetchall())

# cursor.execute(sql)
# print("first : " , cursor.fetchone())
# print("third : " , cursor.fetchmany(size=3))
# print("second : " , cursor.fetchall())

# for row in cursor.fetchall():
#     print(row)
temp=cursor.fetchone()

print(temp)

conn.close()
