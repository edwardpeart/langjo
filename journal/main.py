from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from journal.api.routers import entries
from contextlib import asynccontextmanager
from .db.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"stats": "ok"}

app.include_router(entries.router, prefix="/entries", tags=["entries"])
"""
app.include_router(vocab.router)
app.include_router(stats.router)
"""

