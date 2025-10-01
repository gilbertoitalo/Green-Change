import os, uuid, logging
from typing import Literal, Optional
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class MintResult(BaseModel):
    mode: Literal["mock","onchain"]
    tx_hash: str
    token_id: str
    explorer: Optional[str] = None

class MintService:
    def __init__(self):
        # Comuta entre mock e onchain por env (por padrão mock)
        self.mode = os.getenv("MINT_MODE", "mock").lower()
        # Placeholders para onchain
        self.eth_rpc_http = os.getenv("ETH_RPC_HTTP")
        self.contract_address = os.getenv("CONTRACT_ADDRESS")
        self.chain_id = int(os.getenv("CHAIN_ID", "11155111"))

    def mint(self, to_address: str, co2_kg: float) -> MintResult:
        if self.mode == "mock":
            token_int = uuid.uuid4().int & ((1 << 256) - 1)
            token_id = str(token_int)
            tx_hash = f"0xMockTxHash{token_id}"
            logger.info(f"[MOCK] Mint -> to={to_address} co2={co2_kg}kg token_id={token_id} tx={tx_hash}")
            return MintResult(mode="mock", tx_hash=tx_hash, token_id=token_id)

        # --- FUTURO: ONCHAIN ---
        # from web3 import Web3
        # carregar ABI, assinar tx, enviar, etc.
        # tx_hash = ...
        # token_id = ...
        # explorer = f"https://sepolia.etherscan.io/tx/{tx_hash}"
        # return MintResult(mode="onchain", tx_hash=tx_hash, token_id=str(token_id), explorer=explorer)

        raise RuntimeError("MINT_MODE inválido ou onchain não implementado.")
