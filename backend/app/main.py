from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import engine, Base

from .auth.routers import router as auth_router
from .users.routers import router as users_router
from .profiles.routers import router as profiles_router
from .admin.routers import router as admin_router

app = FastAPI(title="ZERO TRACE - Phase 1")

# CORS - adjust origins in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create tables (DEV only). In production use alembic migrations
@app.on_event("startup")
async def startup():
    # Importing Base to ensure models are registered
    Base.metadata.create_all(bind=engine.sync_engine)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(profiles_router, prefix="/profiles", tags=["profiles"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])

@app.get("/")
async def root():
    return {"message": "ZERO TRACE - Phase 1 API"}
