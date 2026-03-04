
# Blockchain Data ETL Pipeline

This project extracts, processes, stores, and visualizes blockchain (cryptocurrency) data using Python. It is designed for learning and demonstration of ETL, scheduling, and dashboarding best practices.

## Project Structure
- `etl/`: ETL logic (fetch, process, load)
- `config/`: Configuration files (API keys, DB connection)
- `scripts/`: Entry-point scripts, scheduler, and visualization
- `requirements.txt`: Python dependencies
- `Dockerfile`: Containerization support
- `.gitignore`: Ignore sensitive/config files and build artifacts

## Features
- Fetches crypto price data (e.g., Bitcoin) from the CoinGecko API (no API key required)
- Processes and stores data in a local SQLite database using SQLAlchemy
- Schedules ETL runs every 5 minutes (or custom interval) with a Python scheduler
- Visualizes collected data with an interactive Streamlit dashboard

## Setup & Usage

### 1. Clone and Install Dependencies
```bash
git clone https://github.com/trevorgray1/inca-demo.git
cd inca-demo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Database (Optional)
Edit `config/config.yaml` to set your database URL. Default is SQLite:
```yaml
database_url: "sqlite:///blockchain_data.db"
```

### 3. Run the ETL Pipeline Manually
From the project root:
```bash
python -m scripts.run_etl
```

### 4. Schedule ETL Runs Automatically
To run the ETL every 5 minutes:
```bash
python -m scripts.scheduled_etl
```
Leave this running in a terminal to collect data over time.

### 5. Visualize Data with Streamlit
Install Streamlit if you haven't:
```bash
pip install streamlit
```
Then run:
```bash
streamlit run scripts/visualize.py
```
By default, the dashboard is available at `http://localhost:8501`. To access from other devices on your network, use:
```bash
streamlit run scripts/visualize.py --server.address=0.0.0.0
```
and open `http://<your-ip>:8501` in a browser.

## Troubleshooting
- If you see `ModuleNotFoundError: No module named 'etl'`, make sure you are running scripts with `python -m scripts.run_etl` from the project root, or add the following to the top of your script:
	```python
	import sys, os
	sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
	```
- For Streamlit, always run from the project root and add the above sys.path lines if needed.
- If you can't access the dashboard from another device, check your firewall and use `--server.address=0.0.0.0`.

## Extending the Project
- Collect data for more assets by modifying `etl/fetch.py` and `etl/process.py`.
- Add alerting (email, Slack) for price changes.
- Deploy with Docker or to the cloud (AWS, etc.).
- Build more advanced dashboards with Streamlit.

## Learning Goals
- Practice Python ETL, SQLAlchemy, and API integration
- Learn about scheduling and automation
- Explore data visualization with Streamlit
- Understand project structure and best practices

---
Created as a learning project inspired by real-world R&D and data engineering workflows.
