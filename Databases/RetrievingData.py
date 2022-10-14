import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rtha1209",
  database="PracticeDB"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Employee")

myresult = mycursor.fetchall()


for x in myresult:
  print(x)

print("\n")
mycursor.execute("SELECT * FROM Employee where address = 'delhi'")
res = mycursor.fetchall()

for data in res:
    print(data)


print("\n")
mycursor.execute("SELECT * FROM Employee ORDER BY name")
res1 = mycursor.fetchall()

for dat in res1:
    print(dat)

print("\n")
mycursor.execute("UPDATE Employee SET name= 'rohitha' WHERE id = 3")
mydb.commit()
res3 = mycursor.fetchall()

for da in res3:
    print(da)