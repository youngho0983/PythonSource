# SQLite:내장 데이터베이스 (응용 프로그램에 넣어서 사용.)
import sqlite3
from datetime import datetime

# database 생성 & 연결 의 의미
conn = sqlite3.connect("./crawl/database/test.db")

# Corsor 획득
cursor = conn.cursor()

now = datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")

userList = (
    (3, "Hong", "hong@naver.com", "hong.com", nowDateTime),
    (4, "Cho", "cho@naver.com", "cho.com", nowDateTime),
    (5, "Yoo", "yoo@naver.com", "yoo.com", nowDateTime),
)
sql = "insert into users values(?,?,?,?,?)"
cursor.executemany(sql, userList)
conn.commit()
conn.close()
