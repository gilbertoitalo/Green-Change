from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from .routers import credits, leads, root



app = FastAPI(title="Carbon Token MVP - Simulator API")
app.include_router(credits.router)  # credits/simulate
app.include_router(leads.router)   # /Lead
app.include_router(root.router)  # GET /
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



