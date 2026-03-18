# BrandCraft

BrandCraft is a simple GenAI-powered branding platform tailored for startups and small businesses. It helps you generate brand names, marketing content, color palettes, and more using AI.

## 🚀 Features

- **Brand Name Generator**: Get creative names for your business.
- **Content Creator**: Generate engaging social posts, emails, and taglines.
- **Branding Chatbot**: An AI assistant for your brand strategies.
- **Design System Generator**: Find the perfect color palette.
- **Sentiment Analysis**: Analyze customer feedback easily.

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, FastAPI
- **AI Integration**: Groq API (LLaMA-3)

## 💻 How to Run Locally

### 1. Setup the Backend
Open a terminal and navigate to the `backend` folder (if it exists):
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Open the .env file and paste your GROQ_API_KEY inside it.
uvicorn app.main:app --reload --port 8000
```

### 2. Setup the Frontend
Simply open the `index.html` file located in the `frontend` folder in your browser. No extra setup is required


