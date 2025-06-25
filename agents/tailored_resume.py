import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_tailored_resume(resume_text, job_description):
    prompt = f"Rewrite this resume to align with the following job description.\n\nResume:\n{resume_text[:2000]}\n\nJob Description:\n{job_description[:2000]}"

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
        return f"⚠️ Failed to tailor resume. {str(e)}"
