import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rtha1209",
  database="PracticeDB"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO Employee(name, salary, address) VALUES ('amisha', 45000,'banglore')")
mydb.commit()

