import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# ✅ Load and print SERPAPI key (only partial for safety)
SERP_API_KEY = os.getenv("SERP_API_KEY")
print("🔐 Using SERP_API_KEY:", SERP_API_KEY[:6] + "..." if SERP_API_KEY else "❌ None loaded")

def search_jobs(job_title, location):
    query = f"{job_title} in {location}"
    
    params = {
        "engine": "google_jobs",
        "q": query,
        "hl": "en",
        "api_key": SERP_API_KEY
    }

    # ✅ Send request to SerpAPI
    response = requests.get("https://serpapi.com/search", params=params)

    if response.status_code != 200:
        print("❌ Failed to fetch jobs from SerpAPI")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return []

    data = response.json()
    jobs = data.get("jobs_results", [])
    
    filtered_jobs = []
    seen = set()

    for job in jobs:
        title = job.get("title", "").strip()
        company = job.get("company_name", "").strip()
        location = job.get("location", "").strip()
        url = job.get("apply_options", [{}])[0].get("link") or job.get("link") or job.get("share_link")
        jd = job.get("description", "")
        posted_at = job.get("detected_extensions", {}).get("posted_at", "").lower()

        # Skip duplicates
        unique_key = f"{title}|{company}|{location}"
        if unique_key in seen or not url:
            continue
        seen.add(unique_key)

        # Skip old jobs (more than 1 day ago)
        if "day" in posted_at:
            try:
                days = int(posted_at.split()[0])
                if days > 1:
                    continue
            except:
                continue
        elif "hour" not in posted_at and "today" not in posted_at:
            continue

        filtered_jobs.append({
            "title": title,
            "company_name": company,
            "location": location,
            "url": url,
            "description": jd,
            "posted_at": posted_at
        })

    print(f"✅ Found {len(filtered_jobs)} recent jobs.")
    return filtered_jobs


a=input("enter a number1:")
b= input("enter a number2:")
print("sum of two number is:",a+b)
