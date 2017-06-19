import mysql.connector
from mysql.connector import errorcode

# connect mysql with key word
"""
config = {
    'user': 'root',
    'host': '127.0.0.1',
    'password': 'password',
    'database': 'test',
}

conn = mysql.connector.connect(**config)
conn.close()
"""

# to handle connection errors
try:
    conn = mysql.connector.connect(
        user='root',
        host='127.0.0.1',
        password='password',
        database='test'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password!')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Database does not exist!')
    else:
        print(err)
else:
    conn.close()
