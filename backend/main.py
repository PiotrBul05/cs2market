from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import models

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