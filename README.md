# ================================================================
# 🤖 Smart Resume Screener (AI-Powered)
# ================================================================
#
# An AI-powered resume screening web application built using:
# - Streamlit (UI)
# - HuggingFace Embeddings (semantic similarity)
# - OpenRouter LLMs (AI reasoning via LangChain)
#
# This application automatically evaluates resumes against a
# Job Description and ranks candidates based on semantic relevance.
#
# ---------------------------------------------------------------
# 📌 KEY FEATURES
# ---------------------------------------------------------------
# ✔ Upload multiple resumes (PDF format)
# ✔ Paste any Job Description
# ✔ Semantic similarity scoring (no keyword matching)
# ✔ AI-generated HR-style reasoning (2 sentences)
# ✔ Ranked candidate list with progress bar
#
# ---------------------------------------------------------------
# 🧠 AI & NLP PIPELINE
# ---------------------------------------------------------------
#
# 1️⃣ Job Description Processing
#    - User pastes job description text
#    - Text is converted into a dense vector embedding
#
# 2️⃣ Resume Processing
#    - PDFs are uploaded
#    - Text is extracted page-by-page using PyPDF2
#    - Each resume is embedded using HuggingFace
#
# 3️⃣ Similarity Scoring
#    - Cosine similarity is computed between:
#         Job Description embedding
#         Resume embedding
#    - Score is scaled to 0–100%
#
# 4️⃣ AI Reasoning
#    - JD snippet + Resume snippet are sent to an LLM
#    - LLM generates a strict 2-sentence justification
#    - Mimics real HR screening explanations
#
# ---------------------------------------------------------------
# 📊 SCORING METHODOLOGY
# ---------------------------------------------------------------
#
# Cosine Similarity Formula:
#   similarity = cos(θ) = (A · B) / (||A|| ||B||)
#
# Final Score:
#   final_score = round(similarity * 100, 2)
#
# Typical Score Interpretation:
#   80–100% → Excellent fit
#   60–80%  → Good match
#   40–60%  → Partial match
#   <40%    → Low relevance
#
# ---------------------------------------------------------------
# 🏗️ TECH STACK
# ---------------------------------------------------------------
#
# Frontend        : Streamlit
# Embeddings      : HuggingFace (all-MiniLM-L6-v2)
# Similarity      : scikit-learn (cosine similarity)
# LLM             : OpenRouter (via LangChain)
# PDF Parsing     : PyPDF2
# Language        : Python 3.9+
#
# ---------------------------------------------------------------
# 📂 PROJECT STRUCTURE
# ---------------------------------------------------------------
#
# Smart-Resume-Screener/
# ├── app.py
# ├── requirements.txt
# ├── README.md
# ├── .gitignore
# └── .streamlit/
#     └── secrets.toml   (API keys, NOT committed)
#
# ---------------------------------------------------------------
# 🔐 API KEY SETUP (OpenRouter)
# ---------------------------------------------------------------
#
# Create a file:
#   .streamlit/secrets.toml
#
# Add:
#   OPENROUTER_API_KEY = "your_openrouter_api_key_here"
#
# ⚠️ Never push secrets.toml to GitHub
#
# ---------------------------------------------------------------
# ☁️ DEPLOYMENT (Streamlit Cloud)
# ---------------------------------------------------------------
#
# 1. Push code to GitHub
# 2. Go to https://streamlit.io/cloud
# 3. Click "New App"
# 4. Select:
#      - Repository
#      - Branch: main
#      - File: app.py
# 5. Add secrets in App Settings
# 6. Deploy 🚀
#
# ---------------------------------------------------------------
# ⚠️ LIMITATIONS
# ---------------------------------------------------------------
#
# - Scanned resumes (images) are not supported
# - Very long resumes are embedded as one block
# - LLM responses depend on model availability
#
# ---------------------------------------------------------------
# 🔮 FUTURE IMPROVEMENTS
# ---------------------------------------------------------------
#
# - Resume chunking for higher accuracy
# - Skill extraction and weighting
# - OCR support for scanned PDFs
# - CSV export of results
# - Role-based scoring logic
#
# ---------------------------------------------------------------
# 👤 AUTHOR
# ---------------------------------------------------------------
#
# Name   : Sarthak Dahiya
# GitHub : https://github.com/sarthakdahiya8
#
# ---------------------------------------------------------------
# ⭐ If you find this project useful, consider giving it a star!
# ================================================================
