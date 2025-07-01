# 🚀 AI-Powered Career Referral Assistant

An intelligent Gradio app that:
- 🧠 Parses resumes
- 🧩 Matches them to recent job openings
- ✉️ Generates personalized referral messages
- 📄 Creates tailored resumes and cover letters
- 💼 Uses Groq and SerpAPI to fetch jobs and generate content

---

## 🌐 Live Demo (Once Deployed)
👉 [Click here to try it out](https://huggingface.co/spaces/YOUR_USERNAME/career-referral-assistant)

---

## 🧾 Features

✅ Resume Parsing  
✅ Job Matching (last 24 hours, filtered by location & title)  
✅ Groq LLM-based Referral Message Generation  
✅ Tailored Resume + Cover Letter Creation  
✅ PDF Download Support  
✅ Clean Gradio UI

---

## 📁 Project Structure

```
career-referral-assistant/
│
├── app.py                   # Main Gradio app
├── requirements.txt         # Python dependencies
├── agents/
│   ├── resume_agent.py
│   ├── job_scraper.py
│   ├── jd_parser.py
│   ├── matcher.py
│   ├── message_generator.py
│   ├── tailored_resume.py
│   ├── cover_letter_generator.py
│   └── pdf_exporter.py
├── database/
│   └── db.py
```

---



Create a file called `requirements.txt`:

```txt
gradio
requests
python-dotenv
groq
sentence-transformers
langchain
```

---

---

## 📌 Notes

- Gradio will auto-detect `app.py` and run `iface.launch()`
- The app avoids long Groq prompts by truncating long resumes or JDs
- Errors like “Invalid API key” mean secrets weren’t set correctly

---

## 👨‍💻 Author

Made with ❤️ by Vaishnavi reddy

---

## 📃 License

MIT – free to use, modify, and deploy
