// API Configuration
const API_BASE_URL = 'http://localhost:8000/api';

// API Functions for all endpoints

/**
 * Generate brand names
 * @param {string} keywords - Keywords for brand generation
 * @param {string} industry - Industry category
 * @param {string} tone - Brand tone
 * @returns {Promise<Object>} API response
 */
async function generateBrandNames(keywords, industry, tone) {
    try {
        // Prepare payload matching BrandNameRequest
        // keywords can be string (comma separated) or array
        const keywordList = Array.isArray(keywords)
            ? keywords
            : keywords.split(',').map(k => k.trim()).filter(k => k);

        const response = await fetch(`${API_BASE_URL}/brand/generate-name`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                industry: industry,
                keywords: keywordList.length ? keywordList : ["general"],
                style: tone,
                target_audience: "general", // Default
                context: ""
            })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();

        // Map backend 'suggestions' to 'response' for main.js handling
        return {
            success: data.success,
            response: data.suggestions
        };
    } catch (error) {
        console.error('Error generating brand names:', error);
        throw error;
    }
}

/**
 * Generate logo prompt
 * @param {string} brandName - Brand name
 * @param {string} industry - Industry category
 * @param {string} keywords - Keywords/Values for logo
 * @returns {Promise<Object>} API response
 */
async function generateLogo(brandName, industry, keywords) {
    try {
        const response = await fetch(`${API_BASE_URL}/logo/prompt`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                brand_name: brandName,
                industry: industry,
                brand_values: keywords, // Mapping keywords to brand_values
                style: "modern", // Default
                icon_preferences: "",
                colors: ""
            })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();

        return {
            success: data.success,
            response: data.prompts, // Map 'prompts' to 'response'
            image_url: data.image_url // Pass image URL
        };
    } catch (error) {
        console.error('Error generating logo:', error);
        throw error;
    }
}

/**
 * Edit logo using AI text commands
 * @param {string} imageBase64 - Current logo as base64 (without data:image prefix)
 * @param {string} editPrompt - What changes to make, e.g., "make the background blue"
 * @param {number} strength - How much to change (0.0 = subtle, 1.0 = major)
 * @returns {Promise<Object>} API response with edited image
 */
async function editLogo(imageBase64, editPrompt, strength = 0.7) {
    try {
        const response = await fetch(`${API_BASE_URL}/logo/edit`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                image_base64: imageBase64,
                edit_prompt: editPrompt,
                strength: strength
            })
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return {
            success: data.success,
            image_url: data.image_url,
            edit_applied: data.edit_applied
        };
    } catch (error) {
        console.error('Error editing logo:', error);
        throw error;
    }
}

/**
 * Generate marketing content
 * @param {string} brandName - Brand name
 * @param {string} description - Brand description
 * @param {string} tone - Content tone
 * @param {string} contentType - Type of content
 * @returns {Promise<Object>} API response
 */
async function generateContent(brandName, description, tone, contentType) {
    try {
        const response = await fetch(`${API_BASE_URL}/content/generate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                brand_name: brandName,
                brand_description: description,
                content_type: contentType,
                target_audience: "General Audience", // Default
                tone: tone
            })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();

        return {
            success: data.success,
            content: data.content, // main.js checks for 'content'
            response: data.content
        };
    } catch (error) {
        console.error('Error generating content:', error);
        throw error;
    }
}

/**
 * Get design system (colors)
 * @param {string} brandName - Brand name
 * @param {string} tone - Brand tone
 * @param {string} industry - Industry category
 * @returns {Promise<Object>} API response
 */
async function getDesignSystem(brandName, tone, industry) {
    try {
        const response = await fetch(`${API_BASE_URL}/design/palette`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                brand_name: brandName,
                industry: industry,
                brand_personality: tone, // Mapping tone to personality
                target_audience: "General",
                mood: tone
            })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();

        return {
            success: data.success,
            response: data.recommendations // Map 'recommendations' to 'response'
        };
    } catch (error) {
        console.error('Error getting design system:', error);
        throw error;
    }
}

/**
 * Analyze sentiment of review
 * @param {string} review - Customer review text
 * @returns {Promise<Object>} API response
 */
async function analyzeSentiment(review) {
    try {
        const response = await fetch(`${API_BASE_URL}/sentiment/analyze`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                text: review,
                context: "Customer Review"
            })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();

        return {
            success: data.success,
            response: data.analysis // Map 'analysis' to 'response'
        };
    } catch (error) {
        console.error('Error analyzing sentiment:', error);
        throw error;
    }
}

/**
 * Chat with AI branding assistant
 * @param {string} message - User message
 * @returns {Promise<Object>} API response
 */
async function chatWithAI(message) {
    try {
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: message,
                conversation_history: [], // Not maintaining history in frontend yet
                business_context: ""
            })
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();

        return {
            success: data.success,
            response: data.response
        };
    } catch (error) {
        console.error('Error chatting with AI:', error);
        throw error;
    }
}

// Export functions if using modules (optional)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        generateBrandNames,
        generateLogo,
        generateContent,
        getDesignSystem,
        analyzeSentiment,
        chatWithAI
    };
}
