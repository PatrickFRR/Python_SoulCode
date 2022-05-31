from pymongo import collection

def get_database():
    from pymongo import MongoClient

    # Endereço de conexão ao bando de dados 
    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.mbtst.mongodb.net/?retryWrites=true&w=majority"
    
    # Conectando ao banco de dados
    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    # Retornando base de dados criada
    return client['soul_code_data']
    
dbname = get_database()

# Criando a coleção do banco de dados
collection_name = dbname["itens_soulcode"]

# Criando documentos 
item_1 = {
    "_id":"SC001",
    "nome_item":"Livro",
    "desconto_maximo":"10%",
    "REF":"RRGSFF001",
    "preco": 340,
    "categoria":"Físico"
}

item_2 = {
    "_id":"SC002",
    "nome_item":"Camera",
    "desconto_maximo":"15%",
    "REF":"RRGSJ001S4",
    "preco": 540,
    "categoria":"Físico"
}

item_3 = {
    "nome_item":"Microfone",
    "desconto_maximo":"12%",
    "REF":"RRGSJ0FRSW7854R",
    "preco": 300,
    "categoria":"Físico"
}

item_4 = {
    "nome_item":"Aula Remota",
    "desconto_maximo":"19%",
    "REF":"RRGS844W7854R",
    "preco": 400,
    "categoria":"Online"
}

item_5 = {
    "_id":"SC005",
    "nome_item":"Apostila",
    "desconto_maximo":"19%"
}

#Inserindo Documentos
# Inserindo mais de um item automáticamente
# collection_name.insert_many([item_1,item_2,item_3])
# Inserindo um item por vez
collection_name.insert_one(item_4) 
collection_name.insert_one(item_5)
print("Dados inseridos!")