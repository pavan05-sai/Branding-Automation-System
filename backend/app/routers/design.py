"""
Design System / Color Palette Router
API endpoint for generating design recommendations.
"""

from fastapi import APIRouter, HTTPException
from app.schemas.models import DesignRequest, DesignResponse, ErrorResponse
from app.services.ai_service import get_ai_service
from app.config import get_settings

router = APIRouter()
settings = get_settings()


@router.post(
    "/design/palette",
    response_model=DesignResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Generate Color Palette",
    description="Generate color palette and design system recommendations for your brand."
)
async def generate_palette(request: DesignRequest):
    """
    Generate design system recommendations.
    
    - **brand_name**: Your brand name
    - **industry**: Industry or niche
    - **brand_personality**: Brand personality traits
    - **target_audience**: Target audience description
    - **mood**: Desired mood/feeling
    - **existing_colors**: Any existing brand colors to consider
    
    Returns:
    - Primary color palette with HEX/RGB values
    - Secondary/accent colors
    - Neutral colors
    - Color psychology explanation
    - Typography recommendations
    - Usage examples
    """
    try:
        ai_service = get_ai_service()
        recommendations = ai_service.generate_color_palette(
            brand_name=request.brand_name,
            industry=request.industry,
            brand_personality=request.brand_personality,
            target_audience=request.target_audience,
            mood=request.mood,
            existing_colors=request.existing_colors
        )
        
        return DesignResponse(
            success=True,
            recommendations=recommendations,
            model_used=settings.model_name
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Design generation failed: {str(e)}"
        )
