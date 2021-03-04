import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",                        #create a connection to mysql using mysql connector that we imported.
  password="myexam123",
  port=8080,
  database="mydb"
)

print(mydb)

mycursor=mydb.cursor()
mycursor.execute("use mydb")
# mycursor.execute("create table office (id int,officename varchar(200))")
mycursor.execute("select * from employee")
data=mycursor.fetchall()
for x in data:
    print(x)
mycursor.execute("insert into office values(%s,%s)",(2,"Microsoft"))
mydb.commit()
mycursor.execute("select version()")
data=mycursor.fetchone()
print(data)