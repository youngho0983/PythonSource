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

sql ="""
    delete from users where id=%s

"""
cursor.execute(sql % 4)

cursor1 = conn.cursor(pymysql.cursors.DictCursor)
cursor1.execute("select * from users")

for row in cursor1.fetchall():
    print(row)

conn.commit()
conn.close()
