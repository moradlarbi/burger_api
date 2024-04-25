from pymongo import MongoClient
from fastapi import FastAPI
from Burger import Burger
from typing import List
from bson import ObjectId

client = MongoClient('mongodb://burger-mongodb-1:27017/')
db = client['burger']
collection = db['burger']

app = FastAPI()
@app.get("/burgers", response_model=List[dict])  
def get_burgers():
    burgers = list(collection.find()) 
    for burger in burgers:
        burger["_id"] = str(burger["_id"]) 
    return burgers

@app.get("/burgers/{burger_id}", response_model=Burger)
def get_burger_by_id(burger_id: str):
    burger = collection.find_one({"_id": ObjectId(burger_id)})
    if not burger:
        raise HTTPException(status_code=404, detail="Burger not found")
    return burger

@app.put("/burgers/{burger_id}", response_model=Burger)
def update_burger(burger_id: str, burger: Burger):
    updated_result = collection.find_one_and_update(
        {"_id": ObjectId(burger_id)},
        {"$set": burger.dict(exclude={"_id"})},
        return_document=True
    )
    if not updated_result:
        raise HTTPException(status_code=404, detail="Burger not found")
    return updated_result

@app.delete("/burgers/{burger_id}", response_model=dict)
def delete_burger(burger_id: str):
    delete_result = collection.delete_one({"_id": ObjectId(burger_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Burger not found")
    return {"message": "Burger deleted"}

@app.post("/burgers", response_model=Burger)
def create_burger(burger: Burger):
    burger_id = collection.insert_one(burger.dict()).inserted_id
    return burger
