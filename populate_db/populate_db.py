from pymongo import MongoClient
from Burger import Burger

client = MongoClient('mongodb://burger-mongodb-1:27017/')
db = client['burger']
collection = db['burger']

def populate_db():
    n = 20
    for i in range(n):
        name = "Burger" + str(i)
        burger = Burger(prix=15, description=name, list_allergene=["lait", "oeuf"], cuisson="saignant", unite=10000)
        burger_id = collection.insert_one(burger.dict()).inserted_id
    

if __name__ == '__main__':
    populate_db()