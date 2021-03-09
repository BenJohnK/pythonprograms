import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # create a connection to mysql using mysql connector that we imported.
    password="myexam123",
    port=8080,
    database="mydb"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("use mydb")
# mycursor.execute("create table office (id int,officename varchar(200))")
# mycursor.execute("select * from employee")
# data = mycursor.fetchall()
# for x in data:
#     print(x)
# mycursor.execute("insert into office values(%s,%s)", (2, "Microsoft"))
# mycursor.executemany("insert into office values(%s,%s)", [(5, "Qb"), (6, "Suyati")])
# print(mycursor)
# print("Inserted",mycursor.rowcount,"records")
# mydb.commit()
# mycursor.execute("select version()")
# data = mycursor.fetchone()
# print(data)
# mycursor.execute("select * from office")
# data=mycursor.fetchall()
# for x in data:
#   print(x)

# mycursor.execute("update office set officename='new_office' where id=5")
#
# mydb.commit()

# f=open("data_file","r")
# for lines in f:
#     word=lines.rstrip("\n").split(",")
#     mycursor.execute("insert into office values(%s,%s)",(word[0],word[1]))
#
# mydb.commit()
# f.close()

#created employees table

# mycursor.execute("create table employees (eid int, ename varchar(80), desig varchar(80), sal int)")

# f=open("employee_details","r")
# count=0
# for lines in f:
#     if count==0:
#         count=1
#         continue
#     word=lines.rstrip("\n").split(" ")
#     try:
#      mycursor.execute("insert into employees values(%s,%s,%s,%s)",(word[0],word[1],word[2],word[3]))
#     except:
#      pass
#
# mydb.commit()
# mycursor.execute("select * from employees")
# data=mycursor.fetchall()
# for x in data:
#     print(x)

mycursor.execute("select ename from employees where sal=(select max(sal) from employees)")
data=mycursor.fetchone()
for x in data:
    print(x)





