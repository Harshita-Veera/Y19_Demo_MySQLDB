# Creating Table
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="root", database="klu_cse")

if (conn):
    print("Connection Successful")
else:
    print("Connection Failed")

cur = conn.cursor()

try:
    dbs = cur.execute("create table student(sno integer(10) primary key, sname varchar(20), branch varchar(3))")
    print("Table Created Successfully")
except:
    conn.rollback()

cur.close()
conn.close()
