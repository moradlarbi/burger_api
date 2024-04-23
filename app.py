from pymongo import MongoClient
from fastapi import FastAPI
from Burger import Burger
from typing import List
client = MongoClient('mongodb://burger-mongodb-1:27017/')
db = client['burger']
collection = db['burger']

app = FastAPI()
@app.get("/burgers", response_model=List[Burger])
def get_burgers():
    burgers = collection.find()
    return list(burgers)

@app.post("/burgers", response_model=Burger)
def create_burger(burger: Burger):
    burger_id = collection.insert_one(burger.dict()).inserted_id
    return burger
