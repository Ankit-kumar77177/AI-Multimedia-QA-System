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
