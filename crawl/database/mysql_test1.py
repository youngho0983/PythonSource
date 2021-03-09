import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="biguser1",
    password="12345",
    db="bigdata",
    charset="utf8",
)

print(conn)

cursor=conn.cursor()

sql="""
    create table IF NOT exists users(
        id int(11) not null auto_increment,
        username varchar(20),
        email varchar(100),
        phone varchar(100),
        website varchar(100),
        regdate timestamp Default current_timeStamp,
        primary key(id)
    )
"""
cursor.execute(sql)
conn.commit()
conn.close()
