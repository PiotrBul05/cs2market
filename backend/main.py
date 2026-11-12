from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import models
from pydantic import BaseModel
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CS2 Market API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "CS2 Market API działa z bazą danych!"}

@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

@app.get("/test-list")
def test_list():
    skiny = [
        {"name": "AK-47 | Redline", "price": 25.5},
        {"name": "AWP | Asiimov", "price": 89.0},
        {"name": "M4A4 | Howl", "price": 1850.0}
    ]
    return skiny

@app.post("/items")
def create_item(
    name: str,
    price: float,
    rarity: str = None,
    market_hash_name: str = None,
    weapon: str = None,
    min_price: float = None,
    max_price: float = None,
    suggested_price: float = None,
    quantity: int = 0,
    currency: str = "USD",
    image_url: str = None,
    item_page: str = None,
    db: Session = Depends(get_db)
):
    new_item = models.Item(
        name=name,
        price=price,
        rarity=rarity,
        market_hash_name=market_hash_name or name,
        weapon=weapon,
        min_price=min_price,
        max_price=max_price,
        suggested_price=suggested_price,
        quantity=quantity,
        currency=currency,
        image_url=image_url,
        item_page=item_page
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

    class SkinIn(BaseModel):
    name: str
    price: float

@app.post("/test-receive")
def test_receive(skins: List[SkinIn]):
    # tu odbierasz listę obiektów
    names = [skin.name for skin in skins]
    total = sum(skin.price for skin in skins)
    
    return {
        "ile_skinow": len(skins),
        "nazwy": names,
        "suma_cen": total
    }