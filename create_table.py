import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    title TEXT,
    experience TEXT,
    salary TEXT,
    skills TEXT
)
""")

conn.commit()
conn.close()

print("Jobs table created successfully!")