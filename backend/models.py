from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    
    # Podstawowe informacje
    name = Column(String, index=True, nullable=False)                  # np. "AK-47 | Redline"
    market_hash_name = Column(String, index=True, nullable=True)       # pełna nazwa z marketu
    weapon = Column(String, nullable=True)                             # np. "AK-47"
    rarity = Column(String, nullable=True)                             # Classified, Covert itd.
    
    # Ceny
    price = Column(Float, nullable=False)                              # aktualna / główna cena
    min_price = Column(Float, nullable=True)
    max_price = Column(Float, nullable=True)
    suggested_price = Column(Float, nullable=True)
    
    # Dodatkowe dane rynkowe
    quantity = Column(Integer, nullable=True, default=0)               # ile sztuk na rynku
    currency = Column(String, nullable=True, default="USD")
    
    # Linki i obrazek
    image_url = Column(String, nullable=True)
    item_page = Column(String, nullable=True)
    
    # Daty
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())