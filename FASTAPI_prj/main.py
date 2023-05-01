from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = {}


class ItemModel(BaseModel):
    name: str
    desc: str


@app.post('/')
def create(item: ItemModel):
    db[item.name] = item.desc
    return {'item': item}