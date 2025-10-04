from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator
from ..services.carbon_calc import calculate_co2_credits
from ..services.mint_service import MintService
from web3 import Web3

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

@field_validator("to_address")
def validate_address(cls, v:str) -> str:
    # is_adress -> web3 v6; isAddress -> v5
    is_addr = getattr(Web3, "is_address", None) or getattr(Web3, "isAddress")
    if not is_addr(v):
            # 422 por padrão (validação do corpo)
            raise ValueError("Invalid Ethereum address")

        # Normaliza para checksum (v6: to_checksum_address; v5: toChecksumAddress)
    to_checksum = getattr(Web3, "to_checksum_address", None) or getattr(Web3, "toChecksumAddress")
    return to_checksum(v)


    
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

