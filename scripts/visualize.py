import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from etl.load import get_database_url, PriceData
from sqlalchemy.orm import sessionmaker

# Connect to DB and load data
db_url = get_database_url()
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
rows = session.query(PriceData).order_by(PriceData.timestamp).all()
session.close()

# Convert to DataFrame
data = [{
    'timestamp': row.timestamp,
    'price_usd': row.price_usd,
    'market_cap_usd': row.market_cap_usd,
    'volume_24h_usd': row.volume_24h_usd,
    'change_24h_pct': row.change_24h_pct
} for row in rows]
df = pd.DataFrame(data)

# Plot
st.title('Bitcoin Price Data')
st.line_chart(df.set_index('timestamp')['price_usd'])
st.line_chart(df.set_index('timestamp')['market_cap_usd'])
st.line_chart(df.set_index('timestamp')['volume_24h_usd'])