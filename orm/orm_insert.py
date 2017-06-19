import mysql.connector
from datetime import date

conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)

cur = conn.cursor()
# insert data
# cur.execute('insert into user (name, birthday) values (%s, %s)', ['Asoka', date(1990, 3, 22)])
# cur.execute('insert into user (name,birthday) values (%s, %s)', ['Asoka',date(1993, 8, 9)])
cur.execute('insert into user (name,birthday) values (%s, %s)', ['CraneJen', date(1993, 3, 22)])

conn.commit()

# cur.close()
# conn.close()
