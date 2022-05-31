from pymongo import collection

def get_database():
    from pymongo import MongoClient

    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.mbtst.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso...")
    return client['soul_code_data']
    
dbname = get_database()
collection_name = dbname["itens_soulcode"]

# Consultas por filtro valor 
#detalhes_itens = collection_name.distinct("nome_item")
#detalhes_itens = collection_name.find({"categoria":"Físico"}).limit(1)
detalhes_itens = collection_name.find({}, {"nome_item", "desconto_maximo"}).skip(2)
for item in detalhes_itens:
    print(item)

