import sys
import os
import schedule
import time
import subprocess

def run_etl():
    print("Running ETL pipeline...")
    subprocess.run(
        [sys.executable, "-m", "scripts.run_etl"],
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

schedule.every(5).minutes.do(run_etl)

print("scheduler started - ETL will run every 5 minutes. press Ctrl+C to stop.")
run_etl()  # Run once at start

while True:
    schedule.run_pending()
    time.sleep(1)