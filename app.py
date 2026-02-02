import streamlit as st
import pandas as pd
import PyPDF2
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.messages import HumanMessage
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# --- Configuration ---
st.set_page_config(page_title="Smart Resume Screener (OpenRouter Edition)", layout="wide")

# --- Helper Functions ---

def extract_text_from_pdf(uploaded_file):
    """Extracts text from a uploaded PDF file using PyPDF2."""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        st.error(f"Error reading {uploaded_file.name}: {e}")
        return ""

def calculate_similarity_score(jd_embedding, resume_embedding):
    """Calculates cosine similarity between JD and Resume embeddings."""
    jd_vec = np.array(jd_embedding).reshape(1, -1)
    res_vec = np.array(resume_embedding).reshape(1, -1)
    score = cosine_similarity(jd_vec, res_vec)[0][0]
    return round(score * 100, 2)

def generate_reasoning(jd_text, resume_text, score, llm):
    """Uses LLM (via OpenRouter) to generate a short justification."""
    
    # Truncate to safe limits (OpenRouter models vary in context window)
    jd_snippet = jd_text[:2000]
    resume_snippet = resume_text[:2000]
    
    prompt = f"""
    You are an expert HR AI Assistant. 
    Job Description Snippet: "{jd_snippet}..."
    Candidate Resume Snippet: "{resume_snippet}..."
    
    The calculated semantic match score is {score}%.
    
    Task: Provide a strict 2-sentence summary justifying this score.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

# --- Main Application Logic ---

def main():
    st.title("🤖 Smart Resume Screener")
    st.caption("Powered by OpenRouter & HuggingFace")

    # 1. API Key Check
    if "OPENROUTER_API_KEY" not in st.secrets:
        st.error("OpenRouter API Key not found. Please set `OPENROUTER_API_KEY` in .streamlit/secrets.toml")
        st.stop()
    
    api_key = st.secrets["OPENROUTER_API_KEY"]

    # 2. Sidebar / Inputs
    with st.sidebar:
        st.header("Upload Data")
        jd_input = st.text_area("Paste Job Description:", height=300)
        uploaded_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)
        analyze_btn = st.button("Analyze Candidates")

    # 3. Processing
    if analyze_btn:
        if not jd_input:
            st.warning("Please enter a Job Description.")
            return
        if not uploaded_files:
            st.warning("Please upload at least one resume.")
            return

        with st.spinner("Initializing AI Models..."):
            try:
                # A. Embeddings (Local & Free)
                # 'all-MiniLM-L6-v2' is a lightweight, high-performance model suitable for CPUs
                embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

                # B. LLM (OpenRouter)
                # We use ChatOpenAI but point it to OpenRouter's URL
                llm = ChatOpenAI(
                    model="openai/gpt-3.5-turbo", # You can change this to "mistralai/mistral-7b-instruct" etc.
                    openai_api_key=api_key,
                    openai_api_base="https://openrouter.ai/api/v1",
                    temperature=0.5,
                    default_headers={"HTTP-Referer": "http://localhost:8501", "X-Title": "Resume Screener"}
                )

                # Embed Job Description
                st.write("Encoding Job Description...")
                jd_embedding = embeddings.embed_query(jd_input)
                
                results_list = []

                # Process Resumes
                progress_bar = st.progress(0)
                for idx, file in enumerate(uploaded_files):
                    resume_text = extract_text_from_pdf(file)
                    if not resume_text:
                        continue 

                    # Embed & Score
                    resume_embedding = embeddings.embed_query(resume_text)
                    score = calculate_similarity_score(jd_embedding, resume_embedding)

                    # Generate Reasoning
                    reasoning = generate_reasoning(jd_input, resume_text, score, llm)

                    results_list.append({
                        "Name": file.name,
                        "Match Score": score,
                        "AI Reasoning": reasoning
                    })
                    
                    # Update progress
                    progress_bar.progress((idx + 1) / len(uploaded_files))

                # 4. Output Display
                if results_list:
                    df = pd.DataFrame(results_list)
                    df = df.sort_values(by="Match Score", ascending=False)
                    
                    df_display = df.copy()
                    #df_display["Match %"] = df_display["Match Score"].apply(lambda x: f"{x:.2f}%")

                    #df_display["Match Score"] = df_display["Match Score"].apply(lambda x: f"{x:.2f}%")

                    st.success("Analysis Complete!")
                    st.dataframe(
                        df_display,
                        column_config={
                            "Name": st.column_config.TextColumn("Candidate"),
                            "Match Score": st.column_config.ProgressColumn("Match %", format="%.2f", min_value=0, max_value=100),
                            "AI Reasoning": st.column_config.TextColumn("AI Analysis", width="large")
                        },
                        use_container_width=True
                    )
                else:
                    st.info("No valid text found in documents.")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()