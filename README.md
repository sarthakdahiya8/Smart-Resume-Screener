# 🤖 Smart Resume Screener (AI-Powered)

An AI-powered resume screening web application built using **Streamlit**, **HuggingFace embeddings**, and **OpenRouter (LLMs)** that evaluates resumes against a job description and ranks candidates based on semantic relevance.

This project demonstrates how modern ATS systems use **semantic similarity + LLM reasoning** instead of traditional keyword matching.

---

## 📌 Features

### ✅ Core Functionality
- Upload multiple resumes (PDF format)
- Paste any Job Description
- Automatic resume parsing and ranking
- AI-generated HR-style justification for each candidate

### 🧠 AI Capabilities
- Semantic similarity (not keyword-based)
- HuggingFace sentence embeddings (local & free)
- LLM-powered reasoning via OpenRouter
- Context-aware ranking

### 📊 UI Features
- Clean Streamlit interface
- Progress bar for relevance score
- Ranked candidate table
- AI analysis for each resume

---

## 🏗️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Frontend | Streamlit |
| Embeddings | HuggingFace (`all-MiniLM-L6-v2`) |
| Similarity | Cosine Similarity (scikit-learn) |
| LLM | OpenRouter (LangChain) |
| PDF Parsing | PyPDF2 |
| Language | Python 3.9+ |

---

## 📂 Project Structure
Smart-Resume-Screener/
│
├── app.py # Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore
└── .streamlit/
└── secrets.toml # API keys (NOT committed)

---

## 🚀 How It Works

### 1️⃣ Job Description Processing
- User pastes job description
- Text is converted into an embedding vector

### 2️⃣ Resume Processing
- PDF resumes are uploaded
- Text is extracted using PyPDF2
- Each resume is embedded using HuggingFace

### 3️⃣ Similarity Scoring
- Cosine similarity is calculated between:
  - Job Description embedding
  - Resume embedding
- Score is normalized to **0–100%**

### 4️⃣ AI Reasoning
- Resume + JD snippets are sent to an LLM
- The LLM generates a **2-sentence HR justification**

### 5️⃣ Output
- Candidates are ranked by relevance
- Displayed with a progress bar and AI explanation

---
