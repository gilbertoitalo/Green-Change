import logging
logger = logging.getLogger(__name__)

COMBUSTION_EMISSIONS_FACTOR = 0.25  # kg CO2/km
EV_EMISSIONS_FACTOR = 0.05          # kg CO2/km

def calculate_co2_credits(distance_km: float) -> float:
    """Créditos de CO2 evitados ao usar EV vs combustão."""
    credits = distance_km * (COMBUSTION_EMISSIONS_FACTOR - EV_EMISSIONS_FACTOR)
    logger.info(f"Calculated {credits:.2f} kg CO2 credits for {distance_km} km")
    return round(credits, 2)
