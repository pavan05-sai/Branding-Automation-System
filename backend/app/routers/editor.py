"""
AI Logo Editor Router
Edit logos using text commands with Stability AI image-to-image.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import get_settings
import base64
import httpx

router = APIRouter()
settings = get_settings()


class EditLogoRequest(BaseModel):
    """Request model for AI logo editing."""
    image_base64: str  # The current logo as base64 (without data:image prefix)
    edit_prompt: str   # What changes to make, e.g., "make the background blue"
    strength: float = 0.7  # How much to change (0.0 = no change, 1.0 = complete change)


class EditLogoResponse(BaseModel):
    """Response model for AI logo editing."""
    success: bool
    image_url: str
    edit_applied: str


@router.post(
    "/logo/edit",
    response_model=EditLogoResponse,
    summary="Edit Logo with AI",
    description="Edit a logo using text commands. Describe what changes you want."
)
async def edit_logo(request: EditLogoRequest):
    """
    Edit logo using Stability AI image-to-image.
    
    Example prompts:
    - "Make the background blue"
    - "Add a coffee cup icon"
    - "Make it more minimalist"
    - "Change colors to red and gold"
    """
    try:
        if not settings.stability_api_key:
            raise HTTPException(status_code=500, detail="Stability AI API key not configured")
        
        print(f"🎨 Editing logo with prompt: {request.edit_prompt}")
        
        # Decode the input image
        try:
            image_bytes = base64.b64decode(request.image_base64)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid base64 image data")
        
        # Stability AI image-to-image endpoint
        api_url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image"
        
        # Prepare the multipart form data
        files = {
            "init_image": ("logo.png", image_bytes, "image/png"),
        }
        
        data = {
            "text_prompts[0][text]": f"professional logo, {request.edit_prompt}, vector art, clean design, high quality",
            "text_prompts[0][weight]": "1",
            "text_prompts[1][text]": "blurry, low quality, distorted, ugly, bad art",
            "text_prompts[1][weight]": "-1",
            "cfg_scale": "7",
            "samples": "1",
            "steps": "30",
            "image_strength": str(1 - request.strength),  # Stability uses inverse: 0 = full change
        }
        
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {settings.stability_api_key}",
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                api_url,
                headers=headers,
                files=files,
                data=data,
                timeout=60.0
            )
            
            if response.status_code == 200:
                result = response.json()
                edited_image = result["artifacts"][0]["base64"]
                image_url = f"data:image/png;base64,{edited_image}"
                print(f"✅ Logo edited successfully")
                
                return EditLogoResponse(
                    success=True,
                    image_url=image_url,
                    edit_applied=request.edit_prompt
                )
            else:
                error_text = response.text[:300] if response.text else "Unknown error"
                print(f"⚠️ Stability AI Error {response.status_code}: {error_text}")
                raise HTTPException(
                    status_code=500,
                    detail=f"Image editing failed: {error_text}"
                )
                
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Edit Exception: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Logo editing failed: {str(e)}"
        )
