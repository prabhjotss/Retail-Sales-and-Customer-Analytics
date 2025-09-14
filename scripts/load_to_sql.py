import os
import pandas as pd
from sqlalchemy import create_engine

# ---- Find project root and data folder automatically ----
base_dir = os.path.dirname(os.path.dirname(__file__))   # project1 folder ka path
data_dir = os.path.join(base_dir, "data")

engine = create_engine("sqlite:///retail.db")  # SQLite DB

# ---- Read CSVs from data folder ----
sales = pd.read_csv(os.path.join(data_dir, "sales.csv"), parse_dates=['order_date'])
customers = pd.read_csv(os.path.join(data_dir, "customers.csv"))

sales.to_sql("sales", engine, if_exists="replace", index=False)
customers.to_sql("customers", engine, if_exists="replace", index=False)

print("Data loaded into retail.db")
