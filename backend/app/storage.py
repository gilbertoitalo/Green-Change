import csv, time
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
LEADS_CSV = DATA_DIR / "leads.csv"

def save_lead(email, km, kwh, co2_kg, credits):
    header = ["timestamp", "email", "km", "kwh", "co2_kg", "credits_tCO2"]
    exists = LEADS_CSV.exists()
    with LEADS_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(header)
        writer.writerow([int(time.time()), email, km or "", kwh or "", co2_kg or "", credits or ""])

def calc_co2_and_credits(km=None, kwh=None):
    if km is None and kwh is None:
        raise ValueError("Provide km or kwh")
    if km is None:
        km = float(kwh) * 6.0  # 6 km por kWh
    co2_kg = float(km) * 0.18  # 180 g CO₂/km
    credits = co2_kg / 1000.0  # 1 crédito = 1 tCO₂
    return round(co2_kg, 3), round(credits, 6)
