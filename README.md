# AI Multimedia Q&A System

An AI-powered full-stack web application that allows users to upload PDF, audio, and video files and interact with them using an intelligent chatbot.

The system uses Whisper for transcription, FAISS vector search for semantic retrieval, and FastAPI + React for backend/frontend integration.

---

# Features

- Upload PDF documents
- Upload audio files (.mp3, .wav)
- Upload video files (.mp4)
- AI-powered question answering
- Automatic content summarization
- Timestamp extraction from audio/video
- Semantic vector search using FAISS
- MongoDB Atlas chat history storage
- React frontend UI
- FastAPI backend API
- Whisper transcription support

---

# Tech Stack

## Frontend
- React.js
- Axios
- Vite

## Backend
- FastAPI
- Python
- Whisper AI
- FAISS
- Sentence Transformers
- MongoDB Atlas
- PyMuPDF
- MoviePy

---

# Project Structure

```bash
AI-Multimedia-QA-System/
│
├── backend/
│   ├── app/
│   ├── uploads/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md

# Installation

## Clone Repository

```bash
git clone https://github.com/Ankit-kumar77177/AI-Multimedia-QA-System.git
```

```bash
cd AI-Multimedia-QA-System
```

---

# Backend Setup

```bash
cd backend
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# Frontend Setup

Open new terminal:

```bash
cd frontend
```

## Install Dependencies

```bash
npm install
```

## Run Frontend

```bash
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /upload | Upload multimedia files |
| POST | /chat | Ask AI questions |
| GET | /summary | Generate summary |
| GET | /timestamps | Extract timestamps |
| GET | / | Backend health check |

# OUTPUT IMAGES
# FOR Backend
![image alt](https://github.com/Ankit-kumar77177/AI-Multimedia-QA-System/blob/main/Screenshot%202026-05-08%20224441.png?raw=true)

# FOR Frontend
![image alt](https://github.com/Ankit-kumar77177/AI-Multimedia-QA-System/blob/main/Screenshot%202026-05-08%20224542.png?raw=true)

# FOR Video Uploding and get Summery By AI 
![image alt](https://github.com/Ankit-kumar77177/AI-Multimedia-QA-System/blob/main/Screenshot%202026-05-08%20224324.png?raw=true)

# FOR AI Chart
![image alt](https://github.com/Ankit-kumar77177/AI-Multimedia-QA-System/blob/main/Screenshot%202026-05-08%20223513.png?raw=true)

# FOR PDF Uploding and get Summery By AI
![image alt](https://github.com/Ankit-kumar77177/AI-Multimedia-QA-System/blob/main/Screenshot%202026-05-08%20223922.png?raw=true)
