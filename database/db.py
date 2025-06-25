import sqlite3

DB_PATH = "logs/referral_logs.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            resume TEXT,
            job_title TEXT,
            location TEXT,
            best_match TEXT,
            job_url TEXT,
            referral TEXT,
            tailored_resume TEXT,
            cover_letter TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_user_log(resume, job_title, location, best_match, job_url, referral, tailored_resume, cover_letter):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (resume, job_title, location, best_match, job_url, referral, tailored_resume, cover_letter)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (resume, job_title, location, best_match, job_url, referral, tailored_resume, cover_letter))
    conn.commit()
    conn.close()

