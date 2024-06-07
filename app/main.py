from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth

app = FastAPI(
    title="tarasovAuth",
    description="Plug-and-play authentication service",
    version="0.1.0",
    docs_url="/docs",
    redoc_url=None,
)

# CORS settings (optional, permissive for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}

