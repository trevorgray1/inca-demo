# load.py: Load data into SQL database

import os
import yaml
from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Load DB config from config/config.yaml
def get_database_url():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config.get('database_url', 'sqlite:///blockchain_data.db')

# SQLAlchemy setup
Base = declarative_base()

class PriceData(Base):
    __tablename__ = 'price_data'
    id = Column(String, primary_key=True)
    symbol = Column(String)
    price_usd = Column(Float)
    market_cap_usd = Column(Float)
    volume_24h_usd = Column(Float)
    change_24h_pct = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

def load_data(processed_data):
    """
    Store processed data in the SQL database using SQLAlchemy.
    Args:
        processed_data (dict): Output from process_data().
    """
    if not processed_data:
        print("No data to store.")
        return

    db_url = get_database_url()
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)  # Create table if not exists
    Session = sessionmaker(bind=engine)
    session = Session()

    # Use timestamp+symbol as unique id for simplicity
    now = datetime.utcnow()
    row_id = f"{processed_data['symbol']}_{now.isoformat()}"
    price_row = PriceData(
        id=row_id,
        symbol=processed_data['symbol'],
        price_usd=processed_data['price_usd'],
        market_cap_usd=processed_data['market_cap_usd'],
        volume_24h_usd=processed_data['volume_24h_usd'],
        change_24h_pct=processed_data['change_24h_pct'],
        timestamp=now
    )
    session.add(price_row)
    session.commit()
    print(f"Stored data in DB: {price_row}")
    session.close()
