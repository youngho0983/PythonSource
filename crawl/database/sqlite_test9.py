# SQLite:내장 데이터베이스 (응용 프로그램에 넣어서 사용.)
import sqlite3
from datetime import datetime

# database 생성 & 연결 의 의미
conn = sqlite3.connect("./crawl/database/test.db")

# Corsor 획득
cursor = conn.cursor()

now = datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")


# sql ="delete from users where id=?"
# cursor.execute(sql,(3,))
deleted_num = cursor.execute("delete from users").rowcount
cursor.execute("select * from users ")
print(cursor.fetchall())
conn.commit()
conn.close()
