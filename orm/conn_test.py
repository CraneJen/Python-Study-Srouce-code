import mysql.connector
from config import DATABASES
import psycopg2
# from psycopg2 import connect


# mysql
# db_name = 'mysql'
# config = DATABASES[db_name]
# conn = mysql.connector.connect(**config)

# postgres
dbname = 'postgres'
conf = DATABASES[dbname]
cnn = psycopg2.connect(**conf)
cur = cnn.cursor()
# tbname = 'test'
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, name varchar(80), num int, birthday date);")
# cur.execute("INSERT INTO test (name,num,birthday) VALUES('Jim',2016001,'2016-06-15');")
# cur.execute("INSERT INTO test (name,num,birthday) VALUES('Tom',2016003,'2016-06-13');")
cur.execute("SELECT * FROM test;")
print(cur.statusmessage)
# cur.fetchall()
record = cur.fetchmany(1)
print(record)

cnn.commit()
cur.close()
cnn.close()
