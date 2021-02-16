# Update Operation
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="0000", database="klu_cse")

if (conn):
    print("Connection Successful")
else:
    print("Connection Failed")

cur = conn.cursor()

try:
    cur.execute("update student set sname='Siddharth Verma' where sno=190032121")
    conn.commit()
    print("Record Updated Successfully")
except:
    conn.rollback()
print(cur.rowcount, "Records Updated")

cur.close()
conn.close()