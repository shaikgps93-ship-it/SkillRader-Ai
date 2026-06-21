import sqlite3
import pandas as pd


def get_jobs_data():
    conn = sqlite3.connect("database.db")

    df = pd.read_sql(
        "SELECT * FROM jobs",
        conn
    )

    conn.close()

    return df