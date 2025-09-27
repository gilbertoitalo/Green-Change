
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from .storage import save_lead, calc_co2_and_credits

app = FastAPI(title="Carbon Credits MVP - Simulator API")

class SimReq(BaseModel):
    km: float | None = None
    kwh: float | None = None
    email: EmailStr | None = None

@app.post("/simulate")
def simulate(req: SimReq):
    try:
        co2_kg, credits = calc_co2_and_credits(req.km, req.kwh)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"co2_kg": co2_kg, "credits_tCO2": credits}

@app.post("/lead")
def lead(req: SimReq):
    if not req.email:
        raise HTTPException(status_code=400, detail="email required")
    co2_kg, credits = None, None
    if req.km or req.kwh:
        co2_kg, credits = calc_co2_and_credits(req.km, req.kwh)
    save_lead(req.email, req.km, req.kwh, co2_kg, credits)
    return {"ok": True}

