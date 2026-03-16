"""
Marketing Content Generator Router
API endpoint for generating marketing content.
"""

from fastapi import APIRouter, HTTPException
from app.schemas.models import ContentRequest, ContentResponse, ErrorResponse
from app.services.ai_service import get_ai_service
from app.config import get_settings

router = APIRouter()
settings = get_settings()


@router.post(
    "/content/generate",
    response_model=ContentResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Generate Marketing Content",
    description="Generate compelling marketing content including taglines, social posts, emails, and ad copy."
)
async def generate_content(request: ContentRequest):
    """
    Generate marketing content using AI.
    
    - **brand_name**: Your brand name
    - **brand_description**: Brief description of your brand
    - **content_type**: Type of content (tagline, social_post, email, ad_copy, landing_page, blog_intro)
    - **target_audience**: Who you're targeting
    - **tone**: Tone of voice (professional, casual, playful, etc.)
    - **key_message**: The main message to convey
    - **cta**: Call to action
    """
    try:
        ai_service = get_ai_service()
        content = ai_service.generate_marketing_content(
            brand_name=request.brand_name,
            brand_description=request.brand_description,
            content_type=request.content_type,
            target_audience=request.target_audience,
            tone=request.tone,
            key_message=request.key_message,
            cta=request.cta
        )
        
        return ContentResponse(
            success=True,
            content=content,
            content_type=request.content_type,
            model_used=settings.model_name
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate content: {str(e)}"
        )
