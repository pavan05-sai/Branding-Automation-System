"""
BrandCraft AI Prompt Templates
Professional, structured prompts for branding and business analytics.
"""

# System prompt establishing AI persona
SYSTEM_PROMPT = """You are BrandCraft AI, an expert enterprise branding and business analytics consultant with 20+ years of experience helping startups, creators, and small businesses build powerful brand identities.

Your expertise includes:
- Brand strategy and positioning
- Market analysis and competitive insights
- Marketing psychology and consumer behavior
- Visual identity principles
- Startup growth strategies

Communication style:
- Professional yet approachable
- Data-driven and strategic
- Action-oriented recommendations
- Clear, structured responses
- Business-focused language

Always provide actionable, practical advice that can be immediately implemented."""


# Brand Name Generation Prompt
BRAND_NAME_PROMPT = """Generate creative, memorable brand name suggestions based on the following criteria:

Industry/Niche: {industry}
Keywords/Themes: {keywords}
Style Preference: {style}
Target Audience: {target_audience}
Additional Context: {context}

Requirements:
1. Generate exactly 5 unique brand name suggestions
2. Each name should be memorable, easy to pronounce, and domain-friendly
3. Consider trademark availability (avoid common words)
4. Mix different naming strategies (invented words, compounds, metaphors)

For each suggestion, provide:
- The brand name
- Pronunciation guide (if needed)
- Brief meaning/rationale (1-2 sentences)
- Suggested domain extensions

Format your response as a structured list."""


# Marketing Content Generation Prompt
MARKETING_CONTENT_PROMPT = """Create compelling marketing content based on the following brief:

Brand Name: {brand_name}
Brand Description: {brand_description}
Content Type: {content_type}
Target Audience: {target_audience}
Tone: {tone}
Key Message: {key_message}
Call to Action: {cta}

Requirements:
1. Create content that resonates with the target audience
2. Incorporate the brand voice consistently
3. Include emotional triggers and persuasive elements
4. Optimize for the specified content type
5. Make the call to action clear and compelling

Provide the final content with any relevant variations or A/B test alternatives."""


# Branding Chatbot System Prompt
CHAT_SYSTEM_PROMPT = """You are BrandCraft AI, an expert branding and business analytics consultant. You're having a conversation with a business owner seeking branding guidance.

Your role is to:
1. Understand their business goals and challenges
2. Provide strategic branding advice
3. Offer actionable recommendations
4. Help with brand positioning and identity decisions
5. Analyze market opportunities

Conversation guidelines:
- Ask clarifying questions when needed
- Provide specific, actionable advice
- Reference industry best practices
- Be encouraging but honest
- Keep responses focused and valuable

Remember previous context in the conversation to provide coherent, personalized advice."""


# Sentiment Analysis Prompt
SENTIMENT_ANALYSIS_PROMPT = """Analyze the sentiment and emotional tone of the following text for brand/business insights:

Text to Analyze:
"{text}"

Context: {context}

Provide a comprehensive analysis including:

1. **Overall Sentiment**: (Positive/Negative/Neutral/Mixed) with confidence score (0-100%)

2. **Emotional Breakdown**:
   - Primary emotions detected
   - Intensity levels (Low/Medium/High)

3. **Brand Implications**:
   - How this sentiment affects brand perception
   - Potential opportunities or risks

4. **Key Phrases**:
   - Highlight significant phrases and their emotional weight

5. **Recommendations**:
   - Actionable steps based on the sentiment analysis

Format the response in a clear, structured manner suitable for business decision-making."""


# Color Palette / Design System Prompt
DESIGN_PALETTE_PROMPT = """Create a professional color palette and design system recommendations for:

Brand Name: {brand_name}
Industry: {industry}
Brand Personality: {brand_personality}
Target Audience: {target_audience}
Mood/Feeling: {mood}
Existing Colors (if any): {existing_colors}

Provide a complete design recommendation including:

1. **Primary Color Palette** (3-5 colors):
   - HEX codes
   - RGB values
   - Color names
   - Usage guidelines (when to use each color)

2. **Secondary/Accent Colors** (2-3 colors):
   - Supporting colors for highlights and CTAs

3. **Neutral Colors**:
   - Background, text, and border colors

4. **Color Psychology**:
   - Why these colors work for the brand
   - Emotional associations

5. **Typography Recommendations**:
   - Suggested font pairings (heading + body)
   - Font characteristics that match the brand

6. **Usage Examples**:
   - Website header
   - Call-to-action buttons
   - Social media templates

Ensure colors are WCAG accessible and work well together."""


# Logo Prompt Generator
LOGO_PROMPT_GENERATION = """Generate detailed text-to-image prompts for logo design based on:

Brand Name: {brand_name}
Industry: {industry}
Brand Values: {brand_values}
Style Preference: {style}
Icon Preferences: {icon_preferences}
Colors to Incorporate: {colors}

Generate 3 different logo concept prompts, each with:

1. **Concept Name**: Brief title for the concept

2. **Detailed Prompt**: A comprehensive text-to-image prompt (50-100 words) that includes:
   - Logo style (minimalist, vintage, modern, geometric, etc.)
   - Key visual elements
   - Color specifications
   - Typography style
   - Composition and layout
   - Technical specifications (vector, clean lines, etc.)

3. **Rationale**: Why this concept works for the brand (2-3 sentences)

4. **Negative Prompt**: What to avoid in the generation

Format each concept clearly for easy use with AI image generators."""
