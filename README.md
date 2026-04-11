# 🚀 Django Smart Mentor (Fullstack RAG System)

An intelligent AI assistant designed to help developers master Django. The system uses **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware answers based on official Django 6.0 documentation, effectively eliminating AI hallucinations.

## 🌟 Project Overview

This is a fullstack application that scrapes, processes, and serves technical knowledge through a modern web interface. All AI computations are performed locally to ensure data privacy and zero API costs.

### Key Features:

- **Phase 1: RAG Engine** – Custom scraper (BeautifulSoup4) and semantic search using `SentenceTransformers`.
- **Phase 2: FastAPI Backend** – High-performance REST API with Pydantic schemas and CORS integration.
- **Phase 3: React Frontend** – Modern UI built with Vite, featuring **Markdown rendering** and **Syntax Highlighting** for code blocks.
- **Hardware Acceleration** – Heavy vector operations optimized for **NVIDIA CUDA (RTX 4060)**.

## 📁 Project Structure

```text
django-smart-mentor/
├── src/                # Core AI Logic (Embeddings & RAG)
├── backend/            # FastAPI Server & Schemas
├── frontend/           # React (Vite) Web Application
├── data/               # Knowledge base (Scraped CSV files)
└── requirements.txt    # Python dependencies
```

## 🚀 Getting Started

**1. Prerequisites**

- Install Ollama and pull the model: ollama pull llama3.2:3b

- Ensure you have Node.js and Python 3.10+ installed.

- (Optional) NVIDIA GPU with CUDA drivers for hardware acceleration.

**2. Backend Setup**

Clone the repository

       git clone https://github.com/Plutoteo0/django-smart-mentor

       cd django-smart-mentor

       # Install dependencies
       pip install -r requirements.txt

       # Run the FastAPI server
       cd backend
       python main.py

**Backend runs at http://127.0.0.1:8000**

**3. Frontend Setup**

       Open a new terminal:

       cd frontend
       npm install
       npm run dev

**Frontend runs at http://localhost:5173**

## 📈 Roadmap & Development

- Scraper & RAG Core Logic
- FastAPI REST API Integration
- React Web Interface with Markdown Support
- Mobile App (React Native - Planned)
- Vector Database migration (ChromaDB/FAISS - Planned)

# Developed by Plutoteo0

## Student at WSB Merito University in Wrocław. Focused on Python, AI/ML, and Modern Web Systems.
