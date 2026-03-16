"""
BrandCraft Pydantic Schemas
Request and Response models for clean API contracts.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


# ============== Brand Name Generator ==============

class BrandNameRequest(BaseModel):
    """Request model for brand name generation."""
    industry: str = Field(..., description="Industry or niche for the brand", min_length=2)
    keywords: List[str] = Field(..., description="Keywords or themes to incorporate", min_length=1)
    style: str = Field(
        default="modern",
        description="Naming style: modern, classic, playful, professional, etc."
    )
    target_audience: str = Field(default="general", description="Target audience description")
    context: str = Field(default="", description="Additional context or requirements")

    class Config:
        json_schema_extra = {
            "example": {
                "industry": "sustainable fashion",
                "keywords": ["eco", "style", "conscious"],
                "style": "modern",
                "target_audience": "millennials and Gen Z",
                "context": "Focus on minimalist, premium feel"
            }
        }


class BrandNameResponse(BaseModel):
    """Response model for brand name generation."""
    success: bool
    suggestions: str
    model_used: str


# ============== Marketing Content Generator ==============

class ContentRequest(BaseModel):
    """Request model for marketing content generation."""
    brand_name: str = Field(..., description="Brand name", min_length=1)
    brand_description: str = Field(..., description="Brief brand description", min_length=10)
    content_type: str = Field(
        ..., 
        description="Type of content: tagline, social_post, email, ad_copy, landing_page, blog_intro"
    )
    target_audience: str = Field(..., description="Target audience description")
    tone: str = Field(
        default="professional",
        description="Tone of voice: professional, casual, playful, authoritative, friendly"
    )
    key_message: str = Field(default="", description="Key message to convey")
    cta: str = Field(default="", description="Call to action")

    class Config:
        json_schema_extra = {
            "example": {
                "brand_name": "EcoThread",
                "brand_description": "Sustainable fashion brand using recycled materials",
                "content_type": "social_post",
                "target_audience": "Environmentally conscious millennials",
                "tone": "friendly",
                "key_message": "Fashion that doesn't cost the earth",
                "cta": "Shop now"
            }
        }


class ContentResponse(BaseModel):
    """Response model for content generation."""
    success: bool
    content: str
    content_type: str
    model_used: str


# ============== Branding Chatbot ==============

class ChatMessage(BaseModel):
    """Individual chat message."""
    role: str = Field(..., description="Message role: user or assistant")
    content: str = Field(..., description="Message content")


class ChatRequest(BaseModel):
    """Request model for branding chatbot."""
    message: str = Field(..., description="User's message", min_length=1)
    conversation_history: List[ChatMessage] = Field(
        default=[],
        description="Previous conversation messages for context"
    )
    business_context: str = Field(
        default="",
        description="Optional business context (industry, stage, goals)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "message": "I'm starting a tech startup focused on AI productivity tools. How should I approach branding?",
                "conversation_history": [],
                "business_context": "B2B SaaS, early stage, targeting enterprise clients"
            }
        }


class ChatResponse(BaseModel):
    """Response model for chatbot."""
    success: bool
    response: str
    model_used: str


# ============== Sentiment Analysis ==============

class SentimentRequest(BaseModel):
    """Request model for sentiment analysis."""
    text: str = Field(..., description="Text to analyze", min_length=10)
    context: str = Field(
        default="general brand feedback",
        description="Context for analysis (e.g., customer review, social mention)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "text": "I absolutely love the new product design! It's intuitive and beautiful. However, the shipping took longer than expected.",
                "context": "Customer product review"
            }
        }


class SentimentResponse(BaseModel):
    """Response model for sentiment analysis."""
    success: bool
    analysis: str
    model_used: str


# ============== Design System / Color Palette ==============

class DesignRequest(BaseModel):
    """Request model for design system recommendations."""
    brand_name: str = Field(..., description="Brand name", min_length=1)
    industry: str = Field(..., description="Industry or niche")
    brand_personality: str = Field(
        ..., 
        description="Brand personality traits (e.g., innovative, trustworthy, playful)"
    )
    target_audience: str = Field(..., description="Target audience description")
    mood: str = Field(
        default="professional",
        description="Desired mood/feeling: energetic, calm, luxurious, friendly, bold"
    )
    existing_colors: str = Field(
        default="",
        description="Any existing brand colors to consider"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "brand_name": "TechFlow",
                "industry": "SaaS / Productivity",
                "brand_personality": "innovative, reliable, modern",
                "target_audience": "Business professionals and teams",
                "mood": "professional yet approachable",
                "existing_colors": ""
            }
        }


class DesignResponse(BaseModel):
    """Response model for design recommendations."""
    success: bool
    recommendations: str
    model_used: str


# ============== Logo Prompt Generator ==============

class LogoPromptRequest(BaseModel):
    """Request model for logo prompt generation."""
    brand_name: str = Field(..., description="Brand name", min_length=1)
    industry: str = Field(..., description="Industry or niche")
    brand_values: str = Field(..., description="Core brand values")
    style: str = Field(
        default="modern minimalist",
        description="Logo style: minimalist, vintage, geometric, abstract, mascot, wordmark"
    )
    icon_preferences: str = Field(
        default="",
        description="Preferred icons or symbols (optional)"
    )
    colors: str = Field(
        default="",
        description="Preferred colors for the logo"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "brand_name": "NexGen Labs",
                "industry": "Biotech / Healthcare",
                "brand_values": "innovation, precision, trust",
                "style": "modern minimalist",
                "icon_preferences": "DNA helix, abstract molecules",
                "colors": "blue, white, silver accents"
            }
        }


class LogoPromptResponse(BaseModel):
    """Response model for logo prompts."""
    success: bool
    prompts: Optional[str] = None
    image_url: Optional[str] = None
    model_used: str


# ============== Error Response ==============

class ErrorResponse(BaseModel):
    """Standard error response."""
    success: bool = False
    error: str
    detail: Optional[str] = None
