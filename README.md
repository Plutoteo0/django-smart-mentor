# 🚀 Django Smart Mentor (RAG System)

An intelligent Django documentation assistant based on **RAG** (Retrieval-Augmented Generation) architecture. The system searches a local knowledge base and generates precise answers using the **Llama 3.2** model, effectively eliminating AI hallucinations.

## 🌟 Key Features

- **Custom Scraper**: Bespoke script parsing official Django documentation into logical sections (Topic, Content, Code).
- **Vector Search**: Utilizing Cosine Similarity and the `all-MiniLM-L6-v2` model for lightning-fast data retrieval.
- **Local LLM**: Full privacy and zero API costs by leveraging **Ollama** and the **Llama 3.2:3b** model.
- **GPU Acceleration**: Full CUDA support (optimized for NVIDIA RTX 4060).

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **AI Frameworks:** PyTorch, Sentence-Transformers
- **LLM Engine:** Ollama (Llama 3.2:3b)
- **Data Handling:** BeautifulSoup4, Pandas

## 📁 Project Structure

```text
django-smart-mentor/
├── data/               # Generated knowledge bases (.csv)
├── src/
│   ├── scraper.py      # Data extraction from ://djangoproject.com
│   ├── brain.py        # RAG Logic (Embeddings + LLM)
│   └── main.py         # Future API (FastAPI)
├── requirements.txt    # Project dependencies
└── .gitignore          # Git exclusion rules
```

## 🚀 Getting Started

- **Clone the repository**:

**bash**

git clone https://github.com/Plutoteo0/django-smart-mentor

cd django-smart-mentor

- **Install dependencies**

pip install -r requirements.txt

- **Prepare the Knowledge Base**

## In src/scraper.py, add the sections you want to scrape:

- urls = [ "https://djangoproject.com",
  "https://djangoproject.com",

Add more links here to expand the Mentor's knowledge...]

Then run the scrapper to generate the CSV file

### python src/scraper.py

## RUN THE MENTOR

**_Launch the main AI engine to start asking questions:_**

**_python src/brain.py_**

## 📈 Project Status

- [x] **Phase 1: Scraper & RAG Engine (CLI)**  
       _Core logic for data extraction, vector embeddings, and local LLM integration._
- [x] **Phase 2: Backend API (FastAPI)**  
       _Exposing the mentor's logic via a REST API for external applications._
- [ ] **Phase 3: Mobile Frontend (React Native)**  
       _A mobile interface for the AI mentor, built with Expo and React Native._
