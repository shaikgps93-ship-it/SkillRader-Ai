import sqlite3

# Create database
conn = sqlite3.connect("database.db")

print("database.db created successfully!")

conn.close()