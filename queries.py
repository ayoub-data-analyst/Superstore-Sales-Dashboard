from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql+psycopg2://postgres:12341234@localhost:5432/superstore_db")

query = """
        SELECT 
            od.profit,
            od.profit_ratio,
            od.sales,

            l.region,

            p.category,
            p.sub_category,
            p.product_name,

            o.order_date,
            o.ship_date,
            o.delivery_delay,

            c.customer_name

        FROM orders o

        JOIN order_details od
            ON od.order_id = o.order_id
        JOIN products p
            ON p.product_id = od.product_id
        JOIN customers c
            ON c.customer_id = o.customer_id
        JOIN locations l
            ON l.location_id = c.location_id
"""

df = pd.read_sql(query, engine)

print(df.shape)