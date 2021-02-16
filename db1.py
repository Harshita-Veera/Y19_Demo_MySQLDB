'''
steps to connect the python application woth MySQL database:
------------------------------------------------------------

s1: import mysql.connector module.
s2: u need to create connection object.
s3: Create cursor object.
s4: execute the query

step1:
------
import mysql.connector

step 2:
-------
connection_object = mysql.connector.connect(host="",user="",passwd="")
'''
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="root")

if (conn):
    print("Connection Successful")
else:
    print("Connection Failed")

cur = conn.cursor()

try:
    dbs = cur.execute("show databases")
except:
    conn.rollback()

for i in cur:
    print(i)

cur.close()
conn.close()