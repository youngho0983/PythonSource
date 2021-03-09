#SQLite:내장 데이터베이스 (응용 프로그램에 넣어서 사용.)
import sqlite3
from datetime import datetime

#sqlite 버전 확인
print(sqlite3.version)

# 날짜/시간 생성
now =datetime.now()
print(now)

nowDateTime =now.strftime("%Y -%m -%d %H : %M : %S")
print(nowDateTime)



