from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

items: List[Item] = []

@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to the FastAPI example"}

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for idx, existing in enumerate(items):
        if existing.id == item_id:
            items[idx] = item
            return item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    items = [it for it in items if it.id != item_id]
    return {"message": "Item deleted"}
