from web3 import Web3
import logging
import uuid

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Your Infura API key
INFURA_API_KEY = "3299ae9dabcc4f13962bbfc76ad2a5ca"

# Mock values
MOCK_USER_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678"

# Connect to Ethereum Sepolia testnet via Infura
w3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{INFURA_API_KEY}", request_kwargs={'timeout': 30}))

if w3.is_connected():
    logger.info(f"Connected to Ethereum Sepolia via Infura: {w3.provider.endpoint_uri}")
    latest_block = w3.eth.block_number
    logger.info(f"Latest block number: {latest_block}")
else:
    logger.warning("Failed to connect to Sepolia. Proceeding with mock data only.")

def calculate_co2_credits(distance_km: float) -> float:
    """Calculate CO2 credits for EV charging vs combustion vehicle."""
    COMBUSTION_EMISSIONS_FACTOR = 0.25  # kg CO2/km for gasoline car
    EV_EMISSIONS_FACTOR = 0.05  # kg CO2/km for EV (grid emissions)
    credits = distance_km * (COMBUSTION_EMISSIONS_FACTOR - EV_EMISSIONS_FACTOR)
    logger.info(f"Calculated {credits:.2f} kg CO2 credits for {distance_km} km")
    return round(credits, 2)

def mock_mint_carbon_credit_nft(co2_credits: float, user_address: str) -> str:
    """Simulate NFT minting locally."""
    token_id = int(uuid.uuid4().int & (1<<256)-1)
    logger.info(f"Mock NFT minted! Token ID: {token_id}, Owner: {user_address}, CO2 Credits: {co2_credits} kg")
    return f"0xMockTxHash{token_id}"

def main():
    try:
        distance_km = 100.0
        co2_credits = calculate_co2_credits(distance_km)
        logger.info(f"CO2 Credits Earned: {co2_credits} kg")

        tx_hash = mock_mint_carbon_credit_nft(co2_credits, MOCK_USER_ADDRESS)
        if tx_hash:
            logger.info(f"Mock NFT minted successfully! Tx Hash: {tx_hash}")
        else:
            logger.error("Mock NFT minting failed")
    except Exception as e:
        logger.error(f"Main execution failed: {e}")

if __name__ == "__main__":
    main()