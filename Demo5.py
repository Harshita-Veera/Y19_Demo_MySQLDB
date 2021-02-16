# Delete Operation
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="0000", database="klu_cse")

if (conn):
    print("Connection Successful")
else:
    print("Connection Failed")

cur = conn.cursor()

try:
    cur.execute("delete from student where sno=190030001")
    conn.commit()
    print("Record Deleted Successfully")
except:
    conn.rollback()
print(cur.rowcount, "Records Deleted")

cur.close()
conn.close()