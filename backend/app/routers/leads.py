from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from ..storage import save_lead, calc_co2_and_credits

router = APIRouter(prefix="/lead", tags=["lead"])

class LeadReq(BaseModel):
    km: float | None = None
    kwh: float | None = None
    email: EmailStr

@router.post("")
def create_lead(req: LeadReq):
    if not req.email:
        raise HTTPException(status_code=400, detail="email required")
    co2_kg, credits = (None, None)
    if req.km or req.kwh:
        co2_kg, credits = calc_co2_and_credits(req.km, req.kwh)
    save_lead(req.email, req.km, req.kwh, co2_kg, credits)
    return {"ok": True, "email": req.email, "co2_kg": co2_kg, "credits": credits}
