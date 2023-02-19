import pymongo


dosare_de_urmarit = {"clienti":[{
                     "nume_client":"Ion",
                     "nr_dosar":"18-2p/o-2352-15112013",
                     "data_inregistrare":"2023-11-15",
                     "data_informare":""},
                     {"nume_client":"Ana",
                     "nr_dosar":"20-1-7892-03072013",
                     "data_inregistrare":"2023-11-18",
                     "data_informare":""
                     }]}

MongoT_Client= "mongodb://localhost:27017/"
MongoT_Database = "sda_practic"
MongoT_Collection = "docs_clients"

Mongo_client = pymongo.MongoClient(MongoT_Client)
Mongo_mydb = Mongo_client[MongoT_Database]
#Important: In MongoDB, a database is not created until it gets content!
Mongo_mycol = Mongo_mydb[MongoT_Collection]

Mongo_mycol.insert_one(dosare_de_urmarit)

