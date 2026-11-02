from fastapi import FastAPI
from search_skins import fetch_items
import json
from pathlib import Path
CACHE_FILE = Path("items.json")
app = FastAPI()

@app.get("/skins")
def show_skins():
    if CACHE_FILE.exists():
        data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        print("wczytano z pliku")
    else:
        data = fetch_items()
        CACHE_FILE.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        print("zapisano do pliku")

    # return data[:20]
    names = [items["market_hash_name"] for items in data]
    return names[:50]












# http://localhost:8000
# http://localhost:8000/docs