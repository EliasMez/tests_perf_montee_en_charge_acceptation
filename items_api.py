from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()

# Modèle de données pour le corps de la requête POST
class Item(BaseModel):
    name: str
    description: str = None

# Données fictives pour simuler une base de données
items_db = [Item(name="Produit initial", description="Description du produit initial")]

# Endpoint pour ajouter un nouvel élément à la base de données
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

# Endpoint pour récupérer tous les éléments de la base de données
@app.get("/items/", response_model=list[Item])
def read_items():
    return items_db

