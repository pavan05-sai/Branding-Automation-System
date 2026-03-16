"""
BrandCraft - GenAI-Powered Branding & Business Analytics Platform
Main FastAPI Application Entry Point
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import get_settings
from app.routers import brand, content, chat, sentiment, design, logo, users, export, editor

# Get settings
settings = get_settings()


# Initialize FastAPI application
app = FastAPI(
    title="BrandCraft API",
    description="GenAI-powered branding and business analytics platform for startups, creators, and small businesses.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(brand.router, prefix=settings.api_prefix, tags=["Brand"])
app.include_router(content.router, prefix=settings.api_prefix, tags=["Content"])
app.include_router(chat.router, prefix=settings.api_prefix, tags=["Chat"])
app.include_router(sentiment.router, prefix=settings.api_prefix, tags=["Sentiment"])
app.include_router(design.router, prefix=settings.api_prefix, tags=["Design"])
app.include_router(logo.router, prefix=settings.api_prefix, tags=["Logo"])
app.include_router(editor.router, prefix=settings.api_prefix, tags=["Editor"])
app.include_router(users.router, prefix=settings.api_prefix, tags=["Users"])
app.include_router(export.router, prefix=settings.api_prefix, tags=["Export"])


@app.get("/api/config", tags=["Config"])
async def get_public_config():
    """Returns public configuration for frontend."""
    return {}


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for monitoring."""
    return {
        "status": "healthy",
        "service": "BrandCraft API",
        "model": settings.model_name
    }


# Mount frontend static files (must be after API routes)
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "frontend")
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
