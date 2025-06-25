import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_cover_letter(resume_text, job_title, job_description, tone="Professional"):
    prompt = f"""
Write a short, {tone.lower()} cover letter for the job '{job_title}'.\n\nResume:\n{resume_text[:2000]}\n\nJob Description:\n{job_description[:2000]}\n\n3 paragraphs max. Emphasize enthusiasm and fit.
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        res = requests.post(GROQ_URL, headers=headers, json=body)
        res.raise_for_status()
        return res.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ Failed to generate cover letter. {str(e)}"
