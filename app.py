import gradio as gr
from agents import (
    resume_agent,
    job_scraper,
    jd_parser,
    matcher,
    message_generator,
    tailored_resume,
    cover_letter_generator,
    pdf_exporter
)
from database import db
import os
from dotenv import load_dotenv

load_dotenv()
db.init_db()

def full_pipeline(resume_file, job_title, location, tone):
    try:
        resume_text = resume_agent.parse_resume(resume_file.name)
        resume_embed = resume_agent.embed_resume(resume_text)

        jobs = job_scraper.search_jobs(job_title, location)
        top_matches = []

        for job in jobs:
            job_url = job.get("url") or (job.get("apply_options", [{}])[0].get("link"))
            if not job_url:
                print("⚠️ Skipping job with missing URL:", job)
                continue

            jd = jd_parser.extract_jd(job_url)
            if not jd:
                print("⚠️ Skipping job with empty JD:", job_url)
                continue

            score = matcher.match(resume_embed, jd)
            top_matches.append({
                "score": score,
                "url": job_url,
                "title": job.get("title", "Untitled"),
                "jd": jd,
                "company": job.get("company_name", "Unknown")
            })

        # Sort and take top 3
        top_matches = sorted(top_matches, key=lambda x: x["score"], reverse=True)[:3]

        if not top_matches:
            return "⚠️ No suitable job matches found in the last 24 hours. Try again.", "", "", None, None

        # Use the best one for resume + message generation
        best_match = top_matches[0]

        referral_msg = message_generator.generate_referral(
            best_match["title"], resume_text, best_match["jd"], best_match["company"]
        )
        tailored = tailored_resume.generate_tailored_resume(resume_text, best_match["jd"])
        cover_letter = cover_letter_generator.generate_cover_letter(
            resume_text, best_match["title"], best_match["jd"], tone
        )

        db.save_user_log(resume_text, job_title, location, best_match["title"], best_match["url"],
                         referral_msg, tailored, cover_letter)

        resume_pdf_path = pdf_exporter.save_to_pdf(tailored, "tailored_resume")
        cover_letter_pdf_path = pdf_exporter.save_to_pdf(cover_letter, "cover_letter")

        job_links = "\n".join([
            f"🔗 [{job['title']} at {job['company']}]({job['url']})"
            for job in top_matches
        ])

        result_msg = (
            f"🎯 **Top Job Matches:**\n{job_links}\n\n"
            f"📩 **Referral Message (Based on Best Match):**\n{referral_msg}"
        )

        return result_msg, tailored, cover_letter, resume_pdf_path, cover_letter_pdf_path

    except Exception as e:
        return f"❌ Error: {str(e)}", "", "", None, None

# UI Design
custom_css = """
.gradio-container { background-color: #f6f9fc; font-family: 'Segoe UI', sans-serif; }
h1, h2, h3, .title { color: #1a73e8; }
textarea, input, .gr-button { border-radius: 10px !important; }
.gr-button { background: #1a73e8; color: white; font-weight: bold; padding: 10px 20px; border: none; }
.gr-button:hover { background: #0c58d3; }
"""

iface = gr.Interface(
    fn=full_pipeline,
    inputs=[
        gr.File(label="📄 Upload Your Resume (PDF)"),
        gr.Textbox(label="💼 Job Title"),
        gr.Textbox(label="🌍 Preferred Location"),
        gr.Radio(["Professional", "Friendly", "Persuasive"], label="✍️ Cover Letter Tone", value="Professional")
    ],
    outputs=[
        gr.Textbox(label="🧠 AI Referral Message & Top Job Matches", lines=12),
        gr.Textbox(label="📄 Tailored Resume", lines=10),
        gr.Textbox(label="📑 Cover Letter", lines=10),
        gr.File(label="⬇️ Download Tailored Resume"),
        gr.File(label="⬇️ Download Cover Letter")
    ],
    title="🚀 AI-Powered Career Referral Assistant",
    description="Find recent jobs, generate referral messages, and create tailored resumes & cover letters with AI!",
    theme="soft",
    css=custom_css
)

if __name__ == "__main__":
    iface.launch()
