from pymongo import MongoClient, collection

def get_database():
    from pymongo import MongoClient
    import pymongo 
    
    # Endereço de conexão ao bando de dados 
    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.mbtst.mongodb.net/?retryWrites=true&w=majority" 

    # Conectando ao banco de dados
    client = MongoClient(CONNECTION_STRING)

    print("Concectado com sucesso...")
    # Retorno da base de dados para verificar conexão
    return client['sample_airbnb']

get_database()
