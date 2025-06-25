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

## 🛠️ How to Deploy on Hugging Face Spaces

### Step 1: Upload the Code

1. Go to 👉 [https://huggingface.co/spaces](https://huggingface.co/spaces)
2. Click `Create new Space`
   - **Space SDK**: Gradio
   - **Name**: `career-referral-assistant`
   - **Visibility**: Public or Private
3. In the **Files and versions** tab, upload:
   - `app.py`
   - `requirements.txt`
   - `agents/` and `database/` folders

---

### Step 2: Add Secrets (Environment Variables)

Go to the **Settings → Secrets** tab in your Hugging Face Space and add:

| Key            | Value                                  |
|----------------|----------------------------------------|
| `GROQ_API_KEY` | `gsk_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` |
| `SERPAPI_KEY`  | `3b5d9aae1e53XXXXXXXXXXXXXXXXXXXXXXXXX` |

---

### Step 3: Define Your Requirements

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

### Step 4: Done ✅

Once your Space rebuilds:
- You’ll see a **public Gradio UI**
- Upload a resume → Enter job title + location → Get instant results

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
