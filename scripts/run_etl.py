# Entry point for running the ETL pipeline
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from etl.fetch import fetch_data
from etl.process import process_data
from etl.load import load_data

if __name__ == "__main__":
    raw_data = fetch_data()
    print("Fetched data:", raw_data)  # Show what was fetched for learning
    processed_data = process_data(raw_data)
    load_data(processed_data)
