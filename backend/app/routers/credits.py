from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from ..services.carbon_calc import calculate_co2_credits
from ..services.mint_service import MintService

router = APIRouter(prefix="/credits", tags=["credits"])
mint_svc = MintService()

class SimulateReq(BaseModel):
    distance_km: float = Field(..., gt=0)

class SimulateRes(BaseModel):
    distance_km: float
    co2_credits_kg: float

class MintReq(BaseModel):
    to_address: str = Field(..., description="Wallet do usuário (0x...)")
    distance_km: float = Field(..., gt=0)

@router.post("/simulate", response_model=SimulateRes)
def simulate(req: SimulateReq):
    co2 = calculate_co2_credits(req.distance_km)
    return SimulateRes(distance_km=req.distance_km, co2_credits_kg=co2)

@router.post("/mint")
def mint(req: MintReq):
    try:
        co2 = calculate_co2_credits(req.distance_km)
        result = mint_svc.mint(req.to_address, co2)
        return {
            "mode": result.mode,
            "tx_hash": result.tx_hash,
            "token_id": result.token_id,
            "explorer": result.explorer,
            "co2_credits_kg": co2
        }
    except Exception as e:
        raise HTTPException(500, f"Mint falhou: {e}")
