# Upload data

from database import load_data
from queries import query
import pandas as pd

df = load_data(query)

#  Data Preparation

df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.month_name()

# KPIs

df[["sales","profit","delivery_delay"]].describe().round(2)

total_sales = df["sales"].sum()

total_profit = df["profit"].sum()

profit_margin = (total_profit / total_sales) * 100

avg_delivery = df["delivery_delay"].mean()

# GROUP BY

sales_region = df.groupby("region")["sales"].sum().sort_values(ascending=False)

sales_category = df.groupby("category")["sales"].sum().sort_values(ascending=False)

top_10_products = df.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(10)

sales_trend = df.groupby("order_date")["sales"].sum()