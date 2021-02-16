'''
#DATABASE CREATION:
#-------------------
import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
)
mycursor=mydb.cursor()

mycursor.execute("create database HOSPITAL")
mycursor.execute("show databases")
for x in mycursor:
    print(x)
'''
'''
#TABLE CREATION FOR HOSPITAL
import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
    database='HOSPITAL'
)
mycursor=mydb.cursor()

mycursor.execute("create table hospital(hospital_id int not null primary key,hospital_name text not null,bed_count int)")
mycursor.execute("show tables")
for x in mycursor:
    print(x)
'''
'''
#Table Creation For Doctor 
import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
    database='HOSPITAL'
)
mycursor=mydb.cursor()

mycursor.execute("create table doctor(doctor_id int not null primary key,"
                 "doctor_name text not null,hospital_id int not null,salary int not null)")
mycursor.execute("show tables")
for x in mycursor:
    print(x)
'''
'''
#Insertion of values in hospital
import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
    database='hospital'
)


mycursor=mydb.cursor()

sql="insert into hospital(hospital_id,hospital_name,bed_count) values (%s ,%s ,%s)"
val=[
    ("1", "Apolla hospital", "200"),
    ("2", "Surya hospital", "400"),
    ("3", "Trimula hospital", "1000"),
    ("4", "Venkataswara hospital", "100"),
    ("5", "Global hospital", "50"),
    ("6", "Mims hospital", "500"),
    ("7", "Johns hospital", "100"),
    ("8", "NRI hospital", "100"),
    ("9", "NRI Queen hospital", "150"),
    ("10", "V.E.R hospital", "50")
]
mycursor.executemany(sql, val)
mydb.commit()
print("record was inserted.")

mycursor.execute("select * from hospital")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

'''
'''
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database='hospital'
)
mycursor = mydb.cursor()
'''
'''
mycursor.execute(
    "create table doctor(doctor_id int not null primary key,doctor_name text not null,hospital_id int not null,salary int not null)")
mycursor.execute("show tables")
for x in mycursor:
    print(x)
'''
'''
sql = "insert into doctor(doctor_id,doctor_name,hospital_id,salary) values (%s ,%s ,%s ,%s)"
val = [
    ("101", "Ram", "1", "40000"),
    ("102", "Krishna", "2", "20000"),
    ("103", "Sampath", "3", "25000"),
    ("104", "Sai", "4", "28000"),
    ("105", "Nandan", "5", "30000"),
    ("106", "Harshita", "6", "40000"),
    ("107", "Charani", "7", "32000"),
    ("108", "Jayanth", "8", "50000"),
    ("109", "Preethi", "9", "45000"),
    ("110", "Pranesh", "10", "35000"),
    ("111", "Taruni", "7", "25000"),
    ("112", "Lalitha", "4", "40000")
]
mycursor.executemany(sql, val)
mydb.commit()
print("record was inserted.")


mycursor.execute("select * from doctor")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
    database='hospital'
)
mycursor=mydb.cursor()
sql="select * from hospital where hospital_name='Global hospital'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
#order by
import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
    database='hospital'
)
mycursor=mydb.cursor()
sql="select * from hospital order by hospital_name"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
'''
'''
#DELETE
import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
    database='hospital'
)
mycursor=mydb.cursor()
sql="delete from hospital where hospital_id='3'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record deleted")
'''
'''
#DROP TABLE
import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
    database='hospital'
)
mycursor=mydb.cursor()
sql="drop table doctor"
mycursor.execute(sql)
'''
'''
#UPDATE
import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
    database='hospital'
)

mycursor=mydb.cursor()
sql="update hospital set hospital_id='4' where hospital_id='2'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record updated successfully")
'''
import mysql.connector
mydb=mysql.connector.connect (
    host="localhost",
    user="root",
    password="root",
    database='hospital'
)
mycursor=mydb.cursor()
mycursor.execute("select * from hospital limit 4")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)