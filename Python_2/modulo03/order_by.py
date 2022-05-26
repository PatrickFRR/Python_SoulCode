import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

# sql = "SELECT name FROM customers ORDER BY name" #Ordenação alfabética crescente
sql = "SELECT name FROM  customers ORDER BY name DESC" #Ordenação alfanética decrescente

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
      print(x)