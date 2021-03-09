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

# sql="""
#     insert into users(username, email,phone,website)
#     values(%s,%s,%s,%s)
# """
sql="select * from users"
cursor.execute(sql)
print(cursor.fetchall())
# cursor.execute(sql,('park','park@naver.com','010-1234-4321','park.com'))

conn.commit()
conn.close()
