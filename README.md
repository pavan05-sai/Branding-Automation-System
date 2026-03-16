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
Simply open the `index.html` file located in the `frontend` folder in your browser. No extra setup is required!

---

## 📌 How to Push This Project to GitHub

Follow these step-by-step commands to upload your project to GitHub. Open your terminal in the root folder (`BrandingAutomationSystem`) and type these commands:

### Step 1: Initialize Git
```bash
git init
```

### Step 2: Add Your Files
This prepares all your project files to be saved.
```bash
git add .
```

### Step 3: Commit Your Changes
This saves your changes locally with a message.
```bash
git commit -m "Initial commit: Added BrandCraft project"
```

### Step 4: Create a New Repository on GitHub
1. Go to [GitHub](https://github.com) and log in.
2. Click the **+** icon in the top right corner and select **New repository**.
3. Name your repository (e.g., `BrandCraft`).
4. **Do NOT** check the box "Add a README file" because you already have one!
5. Click **Create repository**.

### Step 5: Link Your Local Project to GitHub
Copy the link from your new GitHub repository and link it. Replace the link below with your actual GitHub link:
```bash
git remote add origin YOUR_GITHUB_REPOSITORY_LINK_HERE
```
*(Example: `git remote add origin https://github.com/yourusername/BrandCraft.git`)*

### Step 6: Push Code to GitHub
Finally, push your code to GitHub:
```bash
git branch -M main
git push -u origin main
```

🎉 That's it! Your project is now live on GitHub.
