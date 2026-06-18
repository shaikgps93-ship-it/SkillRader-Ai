import sqlite3
import pandas as pd
import logging
import os
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
CSV_FILE = "jobs.csv"
DB_FILE = "database.db"
TABLE_NAME = "jobs"


def load_data():
    """Load data from CSV file into SQLite database."""
    try:
        # Check if CSV file exists
        if not Path(CSV_FILE).exists():
            logger.error(f"CSV file not found: {CSV_FILE}")
            return False
        
        logger.info(f"Reading data from {CSV_FILE}...")
        df = pd.read_csv(CSV_FILE)
        logger.info(f"Loaded {len(df)} records from CSV")
        
        # Connect to database
        logger.info(f"Connecting to database: {DB_FILE}...")
        with sqlite3.connect(DB_FILE) as conn:
            # Load data into jobs table
            df.to_sql(
                TABLE_NAME,
                conn,
                if_exists="replace",
                index=False
            )
            logger.info(f"Successfully loaded data into '{TABLE_NAME}' table")
        
        logger.info("Data loading completed successfully!")
        return True
        
    except pd.errors.EmptyDataError:
        logger.error(f"CSV file is empty: {CSV_FILE}")
        return False
    except pd.errors.ParserError as e:
        logger.error(f"Error parsing CSV file: {e}")
        return False
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = load_data()
    exit(0 if success else 1)
