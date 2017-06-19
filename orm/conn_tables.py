import mysql.connector
from mysql.connector import errorcode


DB_name = 'test'

TABLES = {}

TABLES['employees'] = (
    "CREATE TABLE employees ("
    "emp_no int(11) NOT NULL AUTO_INCREMENT,"
    "birth_date date NOT NULL,"
    "first_name varchar(14) NOT NULL,"
    "last_name varchar(10) NOT NULL,"
    "gender enum('M', 'F') NOT NULL,"
    "PRIMARY KEY(emp_no)"
    ") ENGINE=InnoDB")

TABLES['departments'] = (
    "CREATE TABLE departments ("
    "dept_no char(4) NOT NULL,"
    "dept_name varchar(40) NOT NULL,"
    "PRIMARY KEY (dept_no),"
    "UNIQUE KEY dept_name (dept_name)"
    ") ENGINE=InnoDB")

TABLES['salaries'] = (
    "CREATE TABLE salaries ("
    "emp_no int(11) NOT NULL,"
    "salary int(11) NOT NULL,"
    "from_date date NOT NULL,"
    "to_date date NOT NULL,"
    "PRIMARY KEY (emp_no, from_date),"
    "KEY (emp_no),"
    "CONSTRAINT salaries_ibfk_1 FOREIGN KEY (emp_no)"
    "REFERENCES employees (emp_no) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

conn = mysql.connector.connect(
    user='root',
    password='password',
    host='127.0.0.1',
)
cur = conn.cursor()


# create database
def create_database(cur):
    try:
        cur.execute(
            "CREATE DATABASE {dbname} DEFAULT CHARACTER SET 'utf8'".format(dbname=DB_name)
        )
    except mysql.connector.Error as err:
        print('Failed creating database: (err)'.format(err=err))
        exit(1)


try:
    conn.database = DB_name
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cur)
        conn.database = DB_name
    else:
        print(err)
        exit(1)

# create tables
for name, ddl in TABLES.items():
    # print(name)
    # print(ddl)
    try:
        print('Creating table {name}:'.format(name=name), end='')
        cur.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('{name} already exists'.format(name=name))
        else:
            print(err.msg)
    else:
        print('OK')

cur.close()
conn.close()
