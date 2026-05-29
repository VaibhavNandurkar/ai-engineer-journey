import sqlite3
import pandas as pd


conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer TEXT, product TEXT,
    quantity INTEGER, price REAL, month TEXT
)""")
rows = [
    (1,"Alice","Laptop",1,80000,"Jan"),(2,"Bob","Phone",2,45000,"Jan"),
    (3,"Alice","Tablet",1,30000,"Feb"),(4,"Charlie","Laptop",1,80000,"Feb"),
    (5,"Bob","Laptop",1,80000,"Mar"),(6,"Charlie","Phone",3,45000,"Mar"),
    (7,"Alice","Phone",1,45000,"Mar"),(8,"Charlie","Tablet",2,30000,"Jan")
]
cur.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?)", rows)
conn.commit()

df = pd.read_sql('SELECT * FROM orders',conn)
print(df)
print(df.shape)

df['revenue'] = df['quantity'] * df['price']

df['discount'] = df['revenue'] * 0.10 * (df['quantity'] >= 2)
df['final_price'] = df['revenue'] - df['discount']

print(f"Total:", df['revenue'].sum())
print(df.groupby('customer')['revenue'].sum())
print("Top customer:", df.groupby('customer')['revenue'].sum().idxmax())

df_high = df[df['revenue'] > 60000].sort_values('revenue', ascending = False)
print(df_high[['customer', 'product', 'product','revenue']])

df_jan = pd.read_sql("SELECT * FROM orders WHERE month = 'jan'", conn)
print(df_jan)

df.to_sql('orders_enriched',conn,if_exists='replace',index=False)
df_check = pd.read_sql("SELECT * FROM orders_enriched", conn)
print(df_check.columns.tolist())

sql_result = pd.read_sql(
    "SELECT month, SUM(revenue) AS total FROM orders_enriched GROUP BY month",
    conn
)
pandas_result = df.groupby('month')['revenue'].sum().reset_index()
pandas_result.columns = ['month', 'total']
print(sql_result)
print(pandas_result)
conn.close()