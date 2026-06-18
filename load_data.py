import sqlite3
import pandas as pd

# Read CSV
df = pd.read_csv("jobs.csv")

# Connect database
conn = sqlite3.connect("database.db")

# Load data into jobs table
df.to_sql(
    "jobs",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Data loaded successfully!")