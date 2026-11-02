from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import models

# Tworzy tabele w bazie (jeśli nie istnieją)
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
def create_item(name: str, price: float, rarity: str = None, db: Session = Depends(get_db)):
    new_item = models.Item(name=name, price=price, rarity=rarity)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item