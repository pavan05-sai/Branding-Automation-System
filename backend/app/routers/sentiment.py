"""
Sentiment Analysis Router
API endpoint for analyzing text sentiment.
"""

from fastapi import APIRouter, HTTPException
from app.schemas.models import SentimentRequest, SentimentResponse, ErrorResponse
from app.services.ai_service import get_ai_service
from app.config import get_settings

router = APIRouter()
settings = get_settings()


@router.post(
    "/sentiment/analyze",
    response_model=SentimentResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Analyze Sentiment",
    description="Analyze sentiment and emotional tone of text for brand and business insights."
)
async def analyze_sentiment(request: SentimentRequest):
    """
    Analyze text sentiment for brand insights.
    
    - **text**: The text to analyze (customer reviews, social mentions, feedback, etc.)
    - **context**: Context for analysis (helps improve accuracy)
    
    Returns:
    - Overall sentiment (Positive/Negative/Neutral/Mixed)
    - Emotional breakdown
    - Brand implications
    - Key phrases
    - Actionable recommendations
    """
    try:
        ai_service = get_ai_service()
        analysis = ai_service.analyze_sentiment(
            text=request.text,
            context=request.context
        )
        
        return SentimentResponse(
            success=True,
            analysis=analysis,
            model_used=settings.model_name
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Sentiment analysis failed: {str(e)}"
        )
