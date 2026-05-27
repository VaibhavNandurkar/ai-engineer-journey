import pandas as pd

months   = ['Jan','Jan','Jan','Feb','Feb','Feb','Mar','Mar','Mar',
            'Apr','Apr','Apr','May','May','May','Jun','Jun','Jun']
products = ['Laptop','Phone','Tablet'] * 6
regions  = ['North','South','West'] * 6
units    = [30,50,20,35,60,25,40,55,30,28,70,22,45,65,35,50,80,40]
prices   = [55000,20000,15000] * 6

sales = pd.DataFrame({
    'months': months, 'products': products, 'regions': regions,
    'units_sold': units, 'prices_per_unit': prices
})
print(sales.head(6))
print(sales.shape)
sales['revenue'] = sales['units_sold'] * sales['prices_per_unit']
print(sales)
print("Total Revenue: Rs.", sales['revenue'].sum())
month_order = ['Jan','Feb','Mar','Apr','May','Jun']
monthly = sales.groupby('months')['revenue'].sum().reindex(month_order)
print("MOnthly Revenue:",monthly)
product_revenue = sales.groupby('products')['revenue'].sum().sort_values(ascending=False)
print("Revenue by Product:")
print(product_revenue)
print("Top Product:",product_revenue.idxmax())
region_stats = sales.groupby('regions').agg({'revenue':'sum','units_sold':'sum'})
print("Region Stats:", region_stats)
high_months = monthly[monthly> monthly.mean()]
print("Above average months:", high_months)
print("Best monts:", monthly.idxmax())
def print_dashboard():
    print(f"=" * 40)
    print("    SALES DASHBOARD SUMMARY")
    print(f"=" * 40)
    print(f"Total Revenue     : Rs. {sales['revenue'].sum():,}")
    print(f"Best Month        : {monthly.idxmax()} ")
    print(f"Top Product       : {product_revenue.idxmax()}")
    print(f"Top Region Revenue: {region_stats['revenue'].idxmax()}")
    print(f"Above-avg Months  : {list(high_months.index)}")
    print(f"=" * 40)
print_dashboard()    