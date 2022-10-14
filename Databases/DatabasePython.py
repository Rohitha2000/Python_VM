import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rtha1209",
  database="PracticeDB"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), salary INT , address VARCHAR(255))")

