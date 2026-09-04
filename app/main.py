from fastapi import FastAPI
from app.core.config import settings
from app.api.health import router as health_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="LeafClub - University Club Management System Backend API",
    version="0.1.0",
    debug=settings.DEBUG,
)

app.include_router(health_router)


@app.get("/", include_in_schema=False)
def root():
    return {
        "message": f"Welcome to {settings.PROJECT_NAME} API",
        "docs": "/docs",
        "health": "/health",
    }
