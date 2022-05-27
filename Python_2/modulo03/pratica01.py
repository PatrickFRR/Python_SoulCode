import mysql.connector

#função criar data base
def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE sistema_escolar_soul_on")
    print("Database criada com sucesso!")

#chamando a função criar data base
# create_database()

#Transformando função mysql e mycursor em variável global
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema_escolar_soul_on"
)
mycursor = mydb.cursor()

#função criar tabela
def create_table():
    mycursor.execute("CREATE TABLE alunos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), matricula VARCHAR(255), turma VARCHAR(255))")
    print("Tabela criada com sucesso!")

#chamando a função criar tabela
# create_table()

#função inserir dados 
def insert_data():
    sql = "INSERT INTO alunos (nome, matricula, turma) VALUE (%s, %s, %s)"
    val = [
        ('José Lima', 'MAT90551', 'BCW22'),
        ('Carlos Augusto', 'MAT90552', 'BCW22'),
        ('Lívia Lima', 'MAT90553', 'BCW22'),
        ('Sandra Gomes', 'MAT90554', 'BCW23'),
        ('João Augusto', 'MAT90555', 'BCW23'),
        ('Breno Lima', 'MAT90556', 'BCW24'),
        ('José Vinícius', 'MAT90557', 'BCW25')
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "linha(s) inserida(s)")

#chamando a função inserir dados
# insert_data()

#Função listar dados
def select_data():
    #Lista todos os alunos
    #mycursor.execute("SELECT * FROM alunos")
    #Lista apenas alunos da turma BCW23
    #mycursor.execute("SELECT nome, matricula FROM alunos WHERE turma = 'BCW23'")
    #Lista de alunos que possuem Lima como sobrenome
    mycursor.execute("SELECT nome FROM alunos WHERE nome LIKE '%Lima%'")

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

#Chamando a função listar dados
# select_data()

#Função atualizar dados
def change_class():
    sql = "UPDATE alunos SET turma = 'BCW25' WHERE id = '2'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "linha(s) alterada(s). ")

#chamando a função atualizar dados
# change_class()

#Função deletar dados
def delete_item():
    sql = "DELETE FROM alunos WHERE id = '7'"
    mycursor.execute(sql)
    mydb.commit()

    print(mycursor.rowcount, "linha(s) deletada(s). ")

#Chamando a função deletar dados
# delete_item()