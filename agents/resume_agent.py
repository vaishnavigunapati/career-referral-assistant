# agents/resume_agent.py

import fitz  # PyMuPDF
from langchain_huggingface import HuggingFaceEmbeddings

# ✅ Parse PDF resume
def parse_resume(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

# ✅ Embed resume text using HuggingFace
def embed_resume(text):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings.embed_query(text)
