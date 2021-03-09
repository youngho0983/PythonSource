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
#     select * from users
# """
# sql="""select * from users where id=%s"""
# cursor.execute(sql % 1)
# print(cursor.fetchone())

cursor1 =conn.cursor(pymysql.cursors.DictCursor)
cursor1.execute("select * from users where id in(%s , %s)" %(1,5))

for row in cursor1.fetchall():
    print(row["username"])
# print(cursor.fetchmant(size=2))
# print(cursor.fetchall())
conn.commit()
conn.close()
