# smoke_test.py
import os, sys
# garante que a raiz (onde está a pasta "backend") está no sys.path
sys.path.insert(0, os.path.abspath("."))

from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

# 1) Testa rota raiz
r = client.get("/")
print("GET /", r.status_code, r.json())

# 2) Testa simulação
r = client.post("/credits/simulate", json={"distance_km": 100})
print("POST /credits/simulate", r.status_code, r.json())

# 3) (opcional) Testa lead
r = client.post("/lead", json={"email":"teste@ex.com","km":120})
print("POST /lead", r.status_code, r.json())
