# Inserting Multiple Records
# executemany()
# Multiple records are provided as a LIST OF TUPLES
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="0000", database="klu_cse")

if (conn):
    print("Connection Successful")
else:
    print("Connection Failed")

cur = conn.cursor()

try:
    str = "insert into student values(%s, %s, %s)"
    rec = [(190032074, "Sai Teja", "ECE"), (190031536, "Sonu Kumar", "CSE"), (190030001, "Amit", "CE")]
    dbs = cur.executemany(str, rec)
    conn.commit()
    print("Record Inserted Successfully")
except:
    conn.rollback()
print(cur.rowcount, "Records Inserted")

cur.close()
conn.close()