"""
BrandCraft Users API Router
Handles user sync and profile endpoints (no database - uses client-side storage).
"""

from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Optional

router = APIRouter(prefix="/users", tags=["Users"])


# ============ Schemas ============

class UserSync(BaseModel):
    """User data from normal Sign-In."""
    user_id: str
    email: EmailStr
    name: str
    picture: Optional[str] = None


class BrandVoice(BaseModel):
    """Brand personality settings."""
    personality: Optional[str] = None
    industry: Optional[str] = None
    target_audience: Optional[str] = None
    tone: Optional[str] = None


# ============ Endpoints ============

@router.post("/sync", response_model=dict)
async def sync_user(user_data: UserSync):
    """
    Sync user on login.
    Note: Database removed - user data is stored client-side in localStorage.
    """
    return {
        "status": "ok",
        "message": "User synced (client-side storage)",
        "is_new": False
    }


@router.get("/me")
async def get_current_user(user_id: str):
    """Get current user's profile."""
    # No database - return minimal success response
    # Frontend handles user data via localStorage
    return {
        "status": "ok",
        "message": "Use client-side storage for user data"
    }


@router.put("/me/brand-voice")
async def update_brand_voice(user_id: str, brand_voice: BrandVoice):
    """Update user's brand voice settings."""
    # No database - frontend handles this via localStorage
    return {"status": "ok", "message": "Brand voice updated (client-side)"}


@router.get("/me/brand-voice")
async def get_brand_voice(user_id: str):
    """Get user's brand voice settings."""
    return {"brand_voice": None}


@router.get("/me/generations")
async def get_generations(user_id: str, limit: int = 20):
    """Get user's generation history."""
    return {"generations": []}
