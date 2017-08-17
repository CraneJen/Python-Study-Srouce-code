# import mysql.connector
import psycopg2
from config import DATABASES
# from psycopg2 import connect


# mysql
# db_name = 'mysql'
# config = DATABASES[db_name]
# conn = mysql.connector.connect(**config)

# postgres
dbname = 'postgres'
conf = DATABASES[dbname]
tablename = 'test'
# cnn = psycopg2.connect(**conf)
# cur = cnn.cursor()
# tbname = 'test'
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, name varchar(80), num int, birthday date);")
# cur.execute("INSERT INTO test (name,num,birthday) VALUES('Jim',2016001,'2016-06-15');")
# cur.execute("INSERT INTO test (name,num,birthday) VALUES('Tom',2016003,'2016-06-13');")
# cur.execute("SELECT * FROM test;")
# print(cur.statusmessage)
# # cur.fetchall()
# record = cur.fetchmany(1)
# print(record)

# cnn.commit()
# cur.close()
# cnn.close()


def getDb(**conf):
    def getCursor(func):
        def __call(*args, ** kwargs):
            conn = psycopg2.connect(**conf)
            cur = conn.cursor()
            ret = func(cur, *args, **kwargs)
            conn.commit()
            conn.close()
            return ret
        return __call

    class TrackDB(object):

        def __init__(self):
            pass

        # create table if not exists
        @staticmethod
        @getCursor
        def init(conn):
            conn.execute(
                "CREATE TABLE IF NOT EXISTS {} (id serial PRIMARY KEY, name varchar(80), num int, birthday date);".format(tablename)
            )

        # insert data
        @staticmethod
        @getCursor
        def insertdata(conn, name, num, birthday):
            conn.execute(
                "INSERT INTO {}(name,num,birthday) VALUES('{}',{},'{}');".format(tablename, name, num, birthday)
            )

        @staticmethod
        @getCursor
        def searchall(conn):
            conn.execute(
                "SELECT * FROM test;"
            )
            return conn.fetchall()

    obj = TrackDB()
    obj.init()
    return obj


getdb = getDb(**conf)
getdb.insertdata('Jack', 89, '1990-04-22')
print(getdb.searchall())
