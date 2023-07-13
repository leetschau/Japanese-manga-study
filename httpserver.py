from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from manga_ocr import MangaOcr
from PIL import Image

app = FastAPI()
mocr = MangaOcr()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/snapshots/")
async def get_snapshot(shot: UploadFile = File(...)):
    res = f'Len of Snapshot: {len(shot.filename)}'
    image = Image.open(shot.file)
    text = mocr(image)
    print(text)
    return {res}


@app.get("/")
async def root():
    return {"message": "Hello Chao"}


@app.post("/items/")
async def create_item(item: Item):
    print(item)
    return item
