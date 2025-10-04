import logging
import math
import os
logger = logging.getLogger(__name__)

# Fatores (podem ser sobrepostos via .env)
COMBUSTION_KG_PER_KM = float(os.getenv("COMBUSTION_KG_PER_KM", "0.25"))
EV_KG_PER_KM         = float(os.getenv("EV_KG_PER_KM", "0.05"))
KM_PER_KWH           = float(os.getenv("KM_PER_KWH", "6.0"))

DELTA_KG_PER_KM = COMBUSTION_KG_PER_KM - EV_KG_PER_KM  # 0.20 por padrão

def _ensure_non_negative(x: float, name: str):
    if x is None or math.isnan(x) or x < 0:
        raise ValueError(f"{name} must be a non-negative number")

def km_from_kwh(kwh: float) -> float:
    """Converte kWh dirigidos/carregados para km equivalentes."""
    _ensure_non_negative(kwh, "kWh")
    return round(kwh * KM_PER_KWH, 3)     # kg CO2/km

def calculate_co2_credits(distance_km: float) -> float:
    """
    Retorna CO₂ evitado (em kg) ao usar EV vs combustão.
    distance_km: distância em km (não-negativo)
    """
    _ensure_non_negative(distance_km, "distance_km")
    co2 = distance_km * DELTA_KG_PER_KM
    logger.info(
        "CO2=%.2f kg para %.2f km (comb=%.3f, ev=%.3f, Δ=%.3f kg/km)",
        co2, distance_km, COMBUSTION_KG_PER_KM, EV_KG_PER_KM, DELTA_KG_PER_KM
    )
    return round(co2, 2)
