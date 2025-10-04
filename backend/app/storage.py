import csv, time
from pathlib import Path
from .services.carbon_calc import calculate_co2_credits, km_from_kwh


DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
LEADS_CSV = DATA_DIR / "leads.csv"

def save_lead(email, km, kwh, co2_kg, credits):
    header = ["timestamp","email","km","kwh","co2_kg","credits_tCO2"]
    exists = LEADS_CSV.exists()
    with LEADS_CSV.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not exists:
            w.writerow(header)
        w.writerow([int(time.time()), email, km or "", kwh or "", co2_kg or "", credits or ""])



def calc_co2_and_credits(km=None, kwh=None):
    if km is None and kwh is None:
        raise ValueError("Provide km or kwh")
    if km is None:
        km = km_from_kwh(float(kwh)) # Convert kWh to km using the service function
    co2_kg = calculate_co2_credits(float(km))  
    credits_tco2 = round(co2_kg / 1000.0, 4) 
    return co2_kg, credits_tco2
