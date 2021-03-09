import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="biguser1",
    password="12345",
    db="bigdata",
    charset="utf8",
)


cursor=conn.cursor()

sql="""
    insert into users(username, email,phone,website)
    values(%s,%s,%s,%s)
"""
userList=(
    ("Lee","lee@naver.com","010-1231-1221","lee.com"),
    ("choi","choi@naver.com","010-1231-4521","choi.com"),
    ("yoo","yoo@naver.com","010-1231-9921","yoo.com"),

)
cursor.executemany(sql,userList)

sql="select * from users"
cursor.execute(sql)
print(cursor.fetchall())
conn.commit()
conn.close()
