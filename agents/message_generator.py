import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_referral(job_title, resume_text, job_description, company):
    resume_text = resume_text[:2000]
    job_description = job_description[:2000]

    prompt = f"""
You are an expert at writing short, effective referral messages.

🎯 Job Title: {job_title}
🏢 Company: {company}

📄 Candidate's Resume:
{resume_text}

📑 Job Description:
{job_description}

Write a short, human-like LinkedIn message to someone at {company}, asking for a referral for the {job_title} role. Keep it polite, concise, and professional.
"""

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content.strip()
        if not reply:
            return "⚠️ Empty response received. Please try again with a simpler resume or JD."
        return reply

    except Exception as e:
        return f"❌ Error generating referral message: {str(e)}"
