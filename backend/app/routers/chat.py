"""
Branding Chatbot Router
API endpoint for conversational branding consultation.
"""

from fastapi import APIRouter, HTTPException
from app.schemas.models import ChatRequest, ChatResponse, ErrorResponse
from app.services.ai_service import get_ai_service
from app.config import get_settings

router = APIRouter()
settings = get_settings()


@router.post(
    "/chat",
    response_model=ChatResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Branding Consultant Chat",
    description="Interactive AI branding consultant for business analytics and strategy guidance."
)
async def chat(request: ChatRequest):
    """
    Chat with the AI branding consultant.
    
    - **message**: Your question or message
    - **conversation_history**: Previous messages for context (optional)
    - **business_context**: Your business context (optional)
    
    The AI consultant can help with:
    - Brand strategy and positioning
    - Market analysis insights
    - Competitive positioning
    - Startup branding advice
    - Marketing strategy recommendations
    """
    try:
        ai_service = get_ai_service()
        
        # Convert conversation history to dict format
        history = [
            {"role": msg.role, "content": msg.content}
            for msg in request.conversation_history
        ] if request.conversation_history else []
        
        response = ai_service.chat(
            message=request.message,
            conversation_history=history,
            business_context=request.business_context
        )
        
        return ChatResponse(
            success=True,
            response=response,
            model_used=settings.model_name
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Chat failed: {str(e)}"
        )
