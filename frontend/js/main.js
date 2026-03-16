
// =================================
// TAB NAVIGATION (Dashboard)
// =================================

function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    if (tabButtons.length === 0) return; // Not on dashboard page

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabName = button.getAttribute('data-tab');

            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            // Add active class to clicked button and corresponding content
            button.classList.add('active');
            const activeTab = document.getElementById(`${tabName}-tab`);
            if (activeTab) {
                activeTab.classList.add('active');
            }
        });
    });
}

// =================================
// BRAND NAME GENERATOR
// =================================

function initBrandGenerator() {
    const generateBtn = document.getElementById('generateBrandBtn');
    if (!generateBtn) return;

    generateBtn.addEventListener('click', async () => {
        const keywords = document.getElementById('brandKeywords').value.trim();
        const industry = document.getElementById('brandIndustry').value;
        const tone = document.getElementById('brandTone').value;
        const outputDiv = document.getElementById('brandOutput');

        if (!keywords) {
            outputDiv.innerHTML = '<div class="error-message">Please enter keywords</div>';
            return;
        }

        // Show loading
        generateBtn.disabled = true;
        outputDiv.innerHTML = '<div class="loading-text"><span class="loading"></span> Generating brand names...</div>';

        try {
            const result = await generateBrandNames(keywords, industry, tone);

            // Display results
            let html = '<h3>Generated Brand Names:</h3><ul>';

            if (result.brand_names && Array.isArray(result.brand_names)) {
                result.brand_names.forEach(name => {
                    html += `<li>${name}</li>`;
                });
                html += '</ul>';
            } else if (result.response) {
                // Parse Markdown
                html += `<div class="markdown-content">${marked.parse(result.response)}</div>`;
            }

            outputDiv.innerHTML = html;
        } catch (error) {
            outputDiv.innerHTML = `<div class="error-message">Error: ${error.message}. Make sure the backend is running.</div>`;
        } finally {
            generateBtn.disabled = false;
        }
    });
}

// =================================
// LOGO GENERATOR
// =================================

function initLogoGenerator() {
    const generateBtn = document.getElementById('generateLogoBtn');
    if (!generateBtn) return;

    generateBtn.addEventListener('click', async () => {
        const brandName = document.getElementById('logoName').value.trim();
        const industry = document.getElementById('logoIndustry').value.trim();
        const keywords = document.getElementById('logoKeywords').value.trim();
        const outputDiv = document.getElementById('logoOutput');

        if (!brandName || !industry || !keywords) {
            outputDiv.innerHTML = '<div class="error-message">Please fill in all fields</div>';
            return;
        }

        // Show loading
        generateBtn.disabled = true;
        outputDiv.innerHTML = '<div class="loading-text"><span class="loading"></span> Generating logo prompt...</div>';

        try {
            const result = await generateLogo(brandName, industry, keywords);

            // Display results
            let html = '<h3>Your Generated Logo:</h3>';

            if (result.image_url) {
                window.currentLogoUrl = result.image_url;
                html += `<div class="logo-preview" style="text-align: center; margin-bottom: 20px;">
                    <img id="currentLogoImage" src="${result.image_url}" 
                         alt="Generated Logo" 
                         style="max-width: 100%; max-height: 400px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
                </div>`;
                html += `<div style="background: #1a1a2e; border-radius: 12px; padding: 20px; margin-top: 20px; border: 1px solid rgba(255,255,255,0.1);">
                    <h4 style="margin: 0 0 15px 0; color: #fff;">🎨 Edit with AI</h4>
                    <p style="color: #aaa; margin-bottom: 15px; font-size: 14px;">Describe changes: "make background blue", "add coffee cup", "make minimalist"</p>
                    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                        <input type="text" id="editPromptInput" placeholder="Describe your edit..." style="flex: 1; min-width: 200px; padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.05); color: #fff;">
                        <select id="editStrength" style="padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.2); background: #1a1a2e; color: #fff;"><option value="0.5">Subtle</option><option value="0.7" selected>Normal</option><option value="0.9">Major</option></select>
                        <button id="applyEditBtn" style="background: linear-gradient(135deg, #9333ea, #7c3aed); padding: 12px 24px; border-radius: 8px; border: none; color: #fff; cursor: pointer; font-weight: 600;">✨ Apply Edit</button>
                    </div>
                    <div id="editStatus" style="margin-top: 10px; color: #aaa; font-size: 13px;"></div>
                </div>`;
                populateMockups(result.image_url, brandName);
            } else {
                html += '<p>No image generated.</p>';
            }
            outputDiv.innerHTML = html;
            if (document.getElementById('applyEditBtn')) {
                document.getElementById('applyEditBtn').addEventListener('click', handleLogoEdit);
            }
        } catch (error) {
            outputDiv.innerHTML = `<div class="error-message">Error: ${error.message}. Make sure the backend is running.</div>`;
        } finally {
            generateBtn.disabled = false;
        }
    });
}

// Handle AI logo editing
async function handleLogoEdit() {
    const editPrompt = document.getElementById('editPromptInput').value.trim();
    const editStrength = document.getElementById('editStrength').value;
    const editStatus = document.getElementById('editStatus');
    const applyEditBtn = document.getElementById('applyEditBtn');
    const currentLogoImage = document.getElementById('currentLogoImage');

    if (!editPrompt) { editStatus.innerHTML = '<span style="color:#ef4444;">Please describe what changes you want.</span>'; return; }
    if (!window.currentLogoUrl) { editStatus.innerHTML = '<span style="color:#ef4444;">No logo to edit.</span>'; return; }

    let imageBase64 = window.currentLogoUrl.startsWith('data:') ? window.currentLogoUrl.split(',')[1] : window.currentLogoUrl;

    try {
        applyEditBtn.disabled = true;
        applyEditBtn.textContent = '⏳ Editing...';
        editStatus.innerHTML = '<span class="loading"></span> AI is editing your logo...';

        const result = await editLogo(imageBase64, editPrompt, parseFloat(editStrength));

        if (result.success && result.image_url) {
            currentLogoImage.src = result.image_url;
            window.currentLogoUrl = result.image_url;
            const brandName = (document.getElementById('logoBrandName') || document.getElementById('brandName') || {}).value || 'Brand';
            populateMockups(result.image_url, brandName);
            editStatus.innerHTML = `<span style="color:#22c55e;">✓ Applied: "${result.edit_applied}"</span>`;
            document.getElementById('editPromptInput').value = '';
        } else {
            editStatus.innerHTML = '<span style="color:#ef4444;">Edit failed. Please try again.</span>';
        }
    } catch (error) {
        editStatus.innerHTML = `<span style="color:#ef4444;">Error: ${error.message}</span>`;
    } finally {
        applyEditBtn.disabled = false;
        applyEditBtn.textContent = '✨ Apply Edit';
    }
}

// Populate merchandise mockups with logo
function populateMockups(logoUrl, brandName) {
    const mockupContainer = document.getElementById('mockupPreviews');
    if (!mockupContainer) return;

    // Show the mockup container
    mockupContainer.style.display = 'block';

    // Business card logo
    const businessCardLogo = document.getElementById('businessCardLogo');
    if (businessCardLogo) {
        businessCardLogo.style.backgroundImage = `url('${logoUrl}')`;
    }

    // Update brand name on card
    const cardBrandName = document.getElementById('cardBrandName');
    if (cardBrandName) {
        cardBrandName.textContent = brandName;
    }

    // Signage logo
    const signageLogo = document.getElementById('signageLogo');
    if (signageLogo) {
        signageLogo.style.backgroundImage = `url('${logoUrl}')`;
    }
}


// =================================
// CONTENT GENERATOR
// =================================

function initContentGenerator() {
    const generateBtn = document.getElementById('generateContentBtn');
    if (!generateBtn) return;

    generateBtn.addEventListener('click', async () => {
        const brandName = document.getElementById('contentBrandName').value.trim();
        const description = document.getElementById('contentDescription').value.trim();
        const tone = document.getElementById('contentTone').value;
        const contentType = document.getElementById('contentType').value;
        const outputDiv = document.getElementById('contentOutput');

        if (!brandName || !description) {
            outputDiv.innerHTML = '<div class="error-message">Please enter brand name and description</div>';
            return;
        }

        // Show loading
        generateBtn.disabled = true;
        outputDiv.innerHTML = '<div class="loading-text"><span class="loading"></span> Generating content...</div>';

        try {
            const result = await generateContent(brandName, description, tone, contentType);

            // Display results
            let html = '<h3>Generated Content:</h3>';

            if (result.content) {
                html += `<div class="markdown-content">${marked.parse(result.content)}</div>`;
                // Populate social previews
                populateSocialPreviews(brandName, result.content);
            } else if (result.response) {
                html += `<div class="markdown-content">${marked.parse(result.response)}</div>`;
                populateSocialPreviews(brandName, result.response);
            }

            outputDiv.innerHTML = html;
        } catch (error) {
            outputDiv.innerHTML = `<div class="error-message">Error: ${error.message}. Make sure the backend is running.</div>`;
        } finally {
            generateBtn.disabled = false;
        }
    });
}

// Populate social media preview cards
function populateSocialPreviews(brandName, content) {
    const previewContainer = document.getElementById('socialPreviews');
    if (!previewContainer) return;

    // Show the preview container
    previewContainer.style.display = 'block';

    // Get first initial for avatar
    const initial = brandName.charAt(0).toUpperCase();

    // Instagram
    const instaAvatar = document.getElementById('instaAvatar');
    if (instaAvatar) instaAvatar.textContent = initial;

    const instaBrandName = document.getElementById('instaBrandName');
    if (instaBrandName) instaBrandName.textContent = brandName;

    const instaName = document.getElementById('instaName');
    if (instaName) instaName.textContent = brandName;

    const instaCaption = document.getElementById('instaCaption');
    if (instaCaption) {
        // Truncate for Instagram preview (max 125 chars for preview)
        const truncated = content.length > 125 ? content.substring(0, 125) + '... more' : content;
        instaCaption.textContent = truncated;
    }

    // LinkedIn
    const linkedinAvatar = document.getElementById('linkedinAvatar');
    if (linkedinAvatar) linkedinAvatar.textContent = initial;

    const linkedinBrandName = document.getElementById('linkedinBrandName');
    if (linkedinBrandName) linkedinBrandName.textContent = brandName;

    const linkedinCaption = document.getElementById('linkedinCaption');
    if (linkedinCaption) {
        // LinkedIn shows more text
        const truncated = content.length > 300 ? content.substring(0, 300) + '...' : content;
        linkedinCaption.textContent = truncated;
    }
}


// =================================
// DESIGN SYSTEM GENERATOR
// =================================

function initDesignGenerator() {
    const generateBtn = document.getElementById('generateDesignBtn');
    if (!generateBtn) return;

    generateBtn.addEventListener('click', async () => {
        const brandName = document.getElementById('designBrandName').value.trim();
        const tone = document.getElementById('designTone').value.trim();
        const industry = document.getElementById('designIndustry').value.trim();
        const outputDiv = document.getElementById('designOutput');

        if (!brandName || !tone || !industry) {
            outputDiv.innerHTML = '<div class="error-message">Please fill in all fields</div>';
            return;
        }

        // Show loading
        generateBtn.disabled = true;
        outputDiv.innerHTML = '<div class="loading-text"><span class="loading"></span> Generating design system...</div>';

        try {
            const result = await getDesignSystem(brandName, tone, industry);

            // Display results
            let html = '<h3>Design System Recommendations:</h3>';

            if (result.response) {
                html += `<div class="markdown-content">${marked.parse(result.response)}</div>`;
            }

            outputDiv.innerHTML = html;
        } catch (error) {
            outputDiv.innerHTML = `<div class="error-message">Error: ${error.message}. Make sure the backend is running.</div>`;
        } finally {
            generateBtn.disabled = false;
        }
    });
}

// =================================
// SENTIMENT ANALYZER
// =================================

function initSentimentAnalyzer() {
    const analyzeBtn = document.getElementById('analyzeSentimentBtn');
    if (!analyzeBtn) return;

    analyzeBtn.addEventListener('click', async () => {
        const review = document.getElementById('sentimentReview').value.trim();
        const outputDiv = document.getElementById('sentimentOutput');

        if (!review) {
            outputDiv.innerHTML = '<div class="error-message">Please enter a customer review</div>';
            return;
        }

        // Show loading
        analyzeBtn.disabled = true;
        outputDiv.innerHTML = '<div class="loading-text"><span class="loading"></span> Analyzing sentiment...</div>';

        try {
            const result = await analyzeSentiment(review);

            // Display results
            let html = '<div class="sentiment-result">';

            if (result.sentiment) {
                const sentimentClass = result.sentiment.toLowerCase();
                html += `<span class="sentiment-badge sentiment-${sentimentClass}">${result.sentiment}</span>`;
            }

            if (result.confidence) {
                html += `<p><strong>Confidence:</strong> ${(result.confidence * 100).toFixed(2)}%</p>`;
            }

            html += '</div>';

            if (result.improved_review) {
                html += `<h3>Improved Review:</h3><p>${result.improved_review}</p>`;
            } else if (result.response) {
                html += `<h3>Analysis:</h3><div class="markdown-content">${marked.parse(result.response)}</div>`;
            }

            outputDiv.innerHTML = html;
        } catch (error) {
            outputDiv.innerHTML = `<div class="error-message">Error: ${error.message}. Make sure the backend is running.</div>`;
        } finally {
            analyzeBtn.disabled = false;
        }
    });
}

// =================================
// AI CHAT
// =================================

function initChat() {
    const sendBtn = document.getElementById('sendChatBtn');
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');

    if (!sendBtn || !chatInput || !chatMessages) return;

    // Handle send button click
    sendBtn.addEventListener('click', sendMessage);

    // Handle Enter key press
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    async function sendMessage() {
        const message = chatInput.value.trim();

        if (!message) return;

        // Add user message to chat
        addChatMessage('user', message);

        // Clear input
        chatInput.value = '';

        // Disable send button
        sendBtn.disabled = true;

        // Add loading indicator
        const loadingId = 'loading-' + Date.now();
        addChatMessage('assistant', '<span class="loading"></span> Thinking...', loadingId);

        try {
            const result = await chatWithAI(message);

            // Remove loading message
            const loadingMsg = document.getElementById(loadingId);
            if (loadingMsg) {
                loadingMsg.remove();
            }

            // Add AI response
            if (result.response) {
                addChatMessage('assistant', marked.parse(result.response));
            }
        } catch (error) {
            // Remove loading message
            const loadingMsg = document.getElementById(loadingId);
            if (loadingMsg) {
                loadingMsg.remove();
            }

            addChatMessage('assistant', `Error: ${error.message}. Make sure the backend is running.`);
        } finally {
            sendBtn.disabled = false;
            chatInput.focus();
        }
    }

    function addChatMessage(role, content, id = null) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `chat-message ${role}`;
        if (id) messageDiv.id = id;

        const roleLabel = role === 'user' ? 'You' : 'AI Assistant';
        messageDiv.innerHTML = `<strong>${roleLabel}:</strong> ${content}`;

        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

// =================================
// EVENT LISTENERS
// =================================

document.addEventListener('DOMContentLoaded', () => {

    // Get Started button (index.html)
    const getStartedBtn = document.getElementById('getStartedBtn');
    if (getStartedBtn) {
        getStartedBtn.addEventListener('click', () => {
            window.location.href = 'branding.html';
        });
    }

    // Initialize dashboard features (branding.html)
    initTabs();
    initBrandGenerator();
    initLogoGenerator();
    initContentGenerator();
    initDesignGenerator();
    initSentimentAnalyzer();
    initChat();
});
