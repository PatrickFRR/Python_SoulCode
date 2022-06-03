from pymongo import collection

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.mbtst.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    return client['soul_code_data']
    
dbname = get_database()
collection_name = dbname["itens_soulcode"]

# Consultando itens do banco de dados
# detalhes_itens = collection_name.find()

# Consultado apenas um iten do banco de dados  por especificações 
# detalhes_itens = collection_name.find({"categoria":"Online"})

# Consultado itens do banco de dados  por especificações  com valores lógicos and ou or
# detalhes_itens = collection_name.find({"$and" : [{"categoria":"Online"}, {"categoria":"Físico"}]})

# Consultado itens do banco de dados utilizando regex, ou seja, começando com Mi
detalhes_itens = collection_name.find({"nome_item":{"$regex":"^Mi"}})

for item in detalhes_itens:
    print(item)