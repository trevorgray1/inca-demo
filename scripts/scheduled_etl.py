import sched
import time
import subprocess

def run_etl():
    # Run the ETL script as a subprocess
    print("Running ETL pipeline...")
    subprocess.run(["python", "scripts/run_etl.py"])

# Schedule the ETL to run every 5 minutes
schedule.every(5).minutes.do(run_etl)

print("scheduler started - ETL will run every 5 minutes. press Ctrl+C to stop.")
run_etl()  # Run immediately on start

while True:
    schedule.run_pending()
    time.sleep(1)   