# Insert Operation
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="root", database="klu_cse")

if (conn):
    print("Connection Successful")
else:
    print("Connection Failed")

cur = conn.cursor()

try:
    str = "insert into student values(%s, %s, %s)"
    rec = (190031422, "Rishikesh", "ME")
    dbs = cur.execute(str, rec)
    conn.commit()
    print("Record Inserted Successfully")
except:
    conn.rollback()
print(cur.rowcount, "Records Inserted")

cur.close()
conn.close()