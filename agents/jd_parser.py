import requests
from bs4 import BeautifulSoup

def extract_jd(url):
    try:
        html = requests.get(url, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()
    except:
        return ""