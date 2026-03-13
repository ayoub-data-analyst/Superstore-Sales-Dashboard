import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

from database import load_data
from queries import query
from kpis import *

df = load_data(query)

## streamlite dashboard

st.title("Superstore Sales Dashboard")

st.write("Interactive dashboard to analyze sales performance.")

## KPIs

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total profit", f"${total_profit:,.0f}")
col3.metric("Profit margin", f"{profit_margin:.2f}%")
col4.metric("Avg Delivery Delay ", f"{avg_delivery:.2f} days")

## Charts

# sales by region
fig, ax = plt.subplots()

sales_region = sales_region.reset_index()

sns.barplot(data=sales_region, x="region", y="sales", color="green", ax=ax)

ax.set_title("Sales by Region")

st.pyplot(fig)

# sales by category
fig, ax = plt.subplots()

sales_category = sales_category.reset_index()

sns.barplot(data=sales_category, x="category", y="sales", color="blue", ax=ax)

ax.set_title("Sales by Category")

st.pyplot(fig)

# top 10 products

fig, ax = plt.subplots()

top_10_products = top_10_products.reset_index()

sns.barplot(data=top_10_products, x="sales", y="product_name", color="yellow", ax=ax)

ax.set_title("Top 10 Products")

st.pyplot(fig)

# avr delivery delay

fig, ax = plt.subplots()

sales_trend = sales_trend.reset_index()

sns.lineplot(data=sales_trend, x="order_date", y="sales", ax=ax)

ax.set_title("Sales Trend")

st.pyplot(fig)