import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers") #Retorna todas as informações
mycursor.execute("SELECT name, address FROM customers")

#Percorre toda a lista e retornará todos os elementos
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

#retornará somente o primeiro elemento
myresult = mycursor.fetchone()
print(myresult)