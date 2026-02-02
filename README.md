
# 🤖 Smart Resume Screener (AI-Powered Resume Matching)

Smart Resume Screener is an **AI-powered resume screening web application** built using **Streamlit**, **HuggingFace sentence embeddings**, and **OpenRouter LLMs**.
It automatically evaluates multiple resumes against a given Job Description and ranks candidates based on **semantic relevance**, not keyword matching.

This project simulates how modern **ATS (Applicant Tracking Systems)** work using **NLP + AI reasoning**.

---

## ✨ Key Features

- 📄 Upload multiple resumes (PDF format)
- 📝 Paste any Job Description
- 🧠 Semantic similarity scoring using embeddings
- 📊 Resume ranking with percentage match
- 🤖 AI-generated HR-style reasoning (2 sentences per candidate)
- ⚡ Fast, simple, and interactive Streamlit UI

---

## 🧠 How the System Works

### 1️⃣ Job Description Processing
- User pastes the Job Description
- JD text is converted into an embedding vector using HuggingFace

### 2️⃣ Resume Processing
- User uploads multiple PDF resumes
- Text is extracted using PyPDF2
- Each resume is converted into an embedding vector

### 3️⃣ Similarity Scoring
- Cosine similarity is calculated between:
  - Job Description embedding
  - Resume embedding
- Score is converted into **percentage (0–100%)**

### 4️⃣ AI Reasoning
- A snippet of JD + Resume is sent to an LLM via OpenRouter
- LLM generates a **2-sentence HR-style explanation**

---

## 🧮 Scoring Logic

```python
score = cosine_similarity(jd_vector, resume_vector)
final_score = round(score * 100, 2)
```

### Score Interpretation
| Score Range | Meaning |
|------------|--------|
| 80–100% | Excellent fit |
| 60–80% | Good match |
| 40–60% | Partial match |
| <40% | Low relevance |

---

## 🏗️ Tech Stack

- Streamlit
- HuggingFace (`all-MiniLM-L6-v2`)
- Scikit-learn
- OpenRouter (LangChain)
- PyPDF2
- Python 3.9+

---

## 📂 Project Structure

```
Smart-Resume-Screener/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml
```

---

## 🔐 API Key Setup

Create `.streamlit/secrets.toml`:

```toml
OPENROUTER_API_KEY = "your_openrouter_api_key_here"
```

---

## 📦 Installation

```bash
git clone https://github.com/sarthakdahiya8/Smart-Resume-Screener.git
cd Smart-Resume-Screener
pip install -r requirements.txt
streamlit run app.py
```

## ⚠️ Limitations

- Scanned resumes not supported
- Very long resumes embedded as single block
- LLM output depends on model availability

---

## 🔮 Future Improvements

- Resume chunking
- Skill extraction
- OCR support
- CSV export
- Role-based scoring

---

## 👤 Author

**Sarthak Dahiya**  
GitHub: https://github.com/sarthakdahiya8

---

⭐ If you like this project, give it a star on GitHub!
