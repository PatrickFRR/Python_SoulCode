import mysql.connector

db =  mysql.connector.connect(host="212.1.211.51", user="u948493795_rootx", passwd="Soulcodeacademy1#", db="u948493795_library") 

cursor = db.cursor()
cursor.execute('SELECT * FROM `tblbooks`')
numrows = int(cursor.rowcount) 
linhas = cursor.fetchall() 
print("Número total de registros encontrados: ", numrows) 
print("\nMostrando resultados...") 


for linha in linhas: 
    print("-", linha[0]) 
    print('-', linha[1])