# 🛒 Superstore Sales Dashboard
 
An interactive sales analytics dashboard built with **Streamlit**, **PostgreSQL**, and **Python** — visualizing key business KPIs and trends from a Superstore dataset.
 
---
 
## 📊 Features
 
- **KPI Metrics** — Total Sales, Total Profit, Profit Margin, and Average Delivery Delay
- **Sales by Region** — Bar chart comparing revenue across regions
- **Sales by Category** — Bar chart breaking down sales per product category
- **Top 10 Products** — Horizontal bar chart of best-selling products
- **Sales Trend** — Line chart showing daily sales over time
 
---
 
## 🗂️ Project Structure
 
```
├── app.py          # Streamlit dashboard — main entry point
├── kpis.py         # KPI calculations and data groupings
├── queries.py      # SQL query to extract data from PostgreSQL
├── database.py     # Database connection via SQLAlchemy
└── Charts.ipynb    # Exploratory notebook for chart prototyping
```
 
---
 
## 🛠️ Tech Stack
 
| Layer        | Technology              |
|-------------|-------------------------|
| Frontend     | Streamlit               |
| Visualization| Matplotlib, Seaborn     |
| Backend      | Python 3                |
| Database     | PostgreSQL              |
| ORM / Query  | SQLAlchemy, pandas      |
 
---
 
## ⚙️ Setup & Installation
 
### 1. Clone the repository
 
```bash
git clone https://github.com/your-username/superstore-dashboard.git
cd superstore-dashboard
```
 
### 2. Install dependencies
 
```bash
pip install -r requirements.txt
```
 
**Required packages:**
```
streamlit
pandas
sqlalchemy
psycopg2-binary
matplotlib
seaborn
```
 
### 3. Configure the database
 
Make sure PostgreSQL is running and a database named `superstore_db` exists. Update the connection string in `database.py` and `queries.py` if needed:
 
```python
engine = create_engine("postgresql://your_user:your_password@localhost:5432/superstore_db")
```
 
The database should have the following tables:
- `orders` — order dates, ship dates, delivery delay
- `order_details` — sales, profit, profit ratio
- `products` — category, sub-category, product name
- `customers` — customer name, location reference
- `locations` — region
 
### 4. Run the dashboard
 
```bash
streamlit run app.py
```
 
Then open your browser at `http://localhost:8501`.
 
---
 
## 📸 Dashboard Preview
 
> KPI cards + bar/line charts rendered interactively in the browser.
 
---
 
## 📁 Data Source
 
Based on the [Superstore Sales dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) — a fictional retail dataset commonly used for business intelligence practice.
 
---
 
## 🙌 Contributing
 
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.
 
---
 
## 📄 License
 
[MIT](LICENSE)
