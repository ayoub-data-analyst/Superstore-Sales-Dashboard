from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine("postgresql://postgres:12341234@localhost:5432/superstore_db")

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("Connection successful")
  
def load_data(query):
    df = pd.read_sql(query, engine)
    return df