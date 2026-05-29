import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    product TEXT, region TEXT, amount REAL
)""")

rows = [
    (1,"Laptop","North",80000),(2,"Phone","South",45000),
    (3,"Laptop","South",75000),(4,"Phone","North",50000),
    (5,"Tablet","North",30000),(6,"Tablet","South",28000),
    (7,"Laptop","North",92000),(8,"Phone","South",41000)
]
cur.executemany("INSERT INTO sales VALUES (?,?,?,?)", rows)
conn.commit()

cur.execute("""
        SELECT product, SUM(amount) AS total
        FROM sales
        GROUP BY product
    """)
for row in cur.fetchall():
    print(f"{row[0]}: {row[1]:.0f}")

cur.execute("""
        SELECT region, COUNT(*) AS num_sales 
        FROM sales 
        GROUP BY region
    """)    
for row in cur.fetchall():
    print(f"{row[0]}: {row[1]} sales")

cur.execute("""
        SELECT product, SUM(amount) AS total
        FROM sales
        GROUP BY product
        HAVING SUM(amount) > 150000
    """)
for row in cur.fetchall():
    print(f"{row[0]}: {row[1]:.0f}")

cur.execute("""
        SELECT product, region, amount
        FROM sales
        WHERE amount > (SELECT AVG(amount) FROM sales)
        ORDER BY amount DESC
    """)
for row in cur.fetchall():
    print(row)

cur.execute("CREATE INDEX idx_region ON sales(region)")
cur.execute("""
        EXPLAIN QUERY PLAN
        SELECT * FROM sales WHERE region = 'North'
    """)
print(cur.fetchall())

cur.execute("""
        SELECT product, SUM(amount) AS total
        FROM sales 
        GROUP BY region
        HAVING SUM(amount) > (
            SELECT AVG(region_total)
            FROM(
                SELECT SUM(amount) AS region_total
                FROM sales GROUP BY region
            )
        )
    """)
for row in cur.fetchall():
    print(f"{row[0]}: {row[1]:.0f}")
conn.close()    
