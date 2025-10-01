from fastapi import FastAPI 

from .routers import credits, leads, root



app = FastAPI(title="Carbon Token MVP - Simulator API")
app.include_router(credits.router)  # credits/simulate
app.include_router(leads.router)   # /Lead
app.include_router(root.router)  # GET /



