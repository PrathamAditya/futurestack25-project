# FutureStack GenAI Hackathon Project

This project is a **full-stack AI-powered Resume and Interview Evaluator** built for the FutureStack GenAI Hackathon.  
It uses **FastAPI (Python)** for the backend and **React** for the frontend.  
The system parses resumes, enriches job descriptions using Exa, evaluates resume-to-job-fit using Cerebras LLaMA models, and generates + evaluates interview questions.

---

## Features

- Resume parsing (PDF/DOCX) using PyMuPDF & python-docx
- Job description enrichment using Exa API
- Smart comparison between resume and JD
- AI-generated interview questions
- Real-time candidate answer evaluation with scoring and feedback
- Clean, responsive frontend with animated gradient UI

---

## 🏗 Tech Stack

**Frontend**

- React (Bootstrap, CSS)
- Environment-based API URLs

**Backend**

- FastAPI + Uvicorn
- PyMuPDF, python-docx for parsing
- Cerebras LLaMA for AI analysis
- Exa for web enrichment
- dotenv for env management

**Containerization**

- Docker for backend and frontend
- Docker Compose for local orchestration

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/futurestack25-project.git
cd futurestack25-project
```

### 2. Backend Setup

```bash
cd backend
cp .env.example .env   # fill in your API keys
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs on **http://127.0.0.1:8000**

### 3. Frontend Setup

```bash
cd frontend
cp .env.example .env
npm install
npm start
```

Frontend runs on **http://localhost:3000**

---

## Running with Docker

### Build & Run Backend

```bash
cd backend
docker build -t futurestack-backend .
docker run -p 8000:8000 --env-file .env futurestack-backend
```

### Run Full Stack with Docker Compose

```bash
docker compose up --build
```

---

## API Endpoints (Backend)

| Endpoint                       | Method | Description                                  |
| ------------------------------ | ------ | -------------------------------------------- |
| `/upload-resume`               | POST   | Upload resume + job description for analysis |
| `/interview/generate-advanced` | POST   | Generate interview questions                 |
| `/interview/evaluate`          | POST   | Evaluate candidate answers                   |

Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Environment Variables

Create a `.env` file in both `backend/` and `frontend/` directories.

### Backend `.env`

```
CEREBRAS_API_KEY=your_key_here
EXA_API_KEY=your_key_here
```

### Frontend `.env`

```
REACT_APP_BACKEND_URL=http://127.0.0.1:8000
REACT_APP_ENV=development
```

---

## 📝 Project Structure

```
futurestack25-project/
│
├── backend/
│   ├── main.py
│   ├── resume_parser.py
│   ├── exa_tool.py
│   ├── interview_tool.py
│   ├── cerebras_client.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── App.js
│   ├── public/
│   ├── Dockerfile
│   └── .env
│
└── docker-compose.yml
```

---

## 🚀 Deployment

- Ensure `.env.production` is set for both frontend and backend.
- Build Docker images and push to container registry (e.g., Docker Hub, Azure Container Registry).
- Deploy using your cloud platform of choice (e.g., Render, Azure App Service, Fly.io).

---
