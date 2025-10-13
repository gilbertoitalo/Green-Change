# Green Change


# 🌱 MVP  Green Change – Hackathon PUC Minas 2025

**ODS 13 – Ação Contra a Mudança Global do Clima**  
Produto mínimo viável que calcula a emissão evitada de CO₂ em recargas de veículos elétricos e gera créditos de carbono tokenizados (NFTs).  

---

## 🚀 Sobre o Projeto

O **Green Change** é uma solução que visa incentivar o uso de energia limpa e a redução das emissões de CO₂ através da **tokenização de créditos de carbono**.  
Cada recarga de veículo elétrico é transformada em **créditos digitais** (NFTs), que poderão ser usados no futuro como benefícios sustentáveis ou investimentos verdes.

**Proposta:**  
- Calcular o CO₂ evitado por recarga.  
- Gerar créditos de carbono equivalentes.  
- Registrar os créditos simbolicamente na blockchain.  
- Permitir que o usuário visualize suas recargas e créditos no app.

---

## 🧩 Arquitetura do MVP

Frontend (Streamlit)
↓
API (FastAPI - Python)
↓
Leads CSV / Cálculo de CO₂
↓
Blockchain (NFT simbólico - testnet)


---

## ⚙️ Funcionalidades

### 🔹 Back-end (FastAPI)
- `/simulate`: calcula energia (kWh), CO₂ evitado e créditos de carbono.  
- `/lead`: armazena leads com dados e créditos gerados em `data/leads.csv`.  
- Documentação automática via Swagger:  


### 🔹 Front-end (Streamlit)
- Interface simples com 3 telas:
1. **Home** – apresentação do projeto e ODS 13.  
2. **Simulador** – cálculo de CO₂ e créditos via API.  
3. **Carteira (Wallet)** – visualização simbólica dos créditos.  

### 🔹 Blockchain (conceitual)
- Mint de NFT representando os créditos gerados (testnet).  
- Registro do **TX hash** documentado em `blockchain/CONTRACTS.md`.  

---

## 🧮 Exemplo de uso da API

### Endpoint `/simulate`
**Request**
```json
{
"distance_km": 100,
"vehicle_type": "ev",
"kwh_per_100km": 15
}


{
  "distance_km": 100.0,
  "kwh": 15.0,
  "co2_kg": 3.24,
  "credits": 0.00324
}


📜 Licença

Este projeto foi desenvolvido para fins acadêmicos e educacionais no contexto do Hackathon PUC Minas 2025 – Desafio ODS 13.
© 2025 – Todos os direitos reservados à equipe.