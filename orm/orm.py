import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    user='root',
    password='password',
    database='test',
    use_unicode=True)
cur = conn.cursor()

# insert a table
cur.execute('DROP TABLE user')
cur.execute(
    'CREATE TABLE user (id int unsigned primary key auto_increment, name varchar(20), birthday date)')

# insert data
# cur.execute('insert into user (name, birthday) values (%s %s)', ['Asoka', date(1990-3-22)])
# cur.execute(
#    'insert into user (name,birthday) values (%s, %s)', [
#        'Asoka','1990-3-22'])
