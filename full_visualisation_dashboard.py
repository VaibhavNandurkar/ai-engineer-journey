import matplotlib.pyplot as plt
import pandas as pd

data = {
    'month':   ['Jan','Feb','Mar','Apr','May','Jun'],
    'revenue': [120000,145000,98000,167000,189000,210000],
    'costs':   [80000,95000,70000,110000,120000,140000],
    'units':   [15,18,12,21,24,27]
}
df = pd.DataFrame(data)
df['profit'] = df['revenue'] - df['costs']

products = ['Laptop','Phone','Tablet','Monitor','Keyboard']
prod_rev  = [247000,136000,58000,92000,31000]
regions   = ['North','South','East','West']
reg_rev   = [210000,185000,130000,95000]

fig, axes = plt.subplots(2, 2, figsize=(14,10))
fig.suptitle('Sales Dashboard — H1 2026', fontsize = 16, fontweight = 'bold')
ax = axes[0][0]
ax.plot(df['month'], df['revenue'], marker = 'o', color ='steelblue', label = 'Revenue')
ax.plot(df['month'], df['revenue'], marker = 's', color = 'coral', label = 'Costs')
ax.set_title('Revenue vs Costs')
ax.legend()
ax.grid(axis ='y', alpha=0.4)
ax = axes[0][1]
bars = ax.bar(products, prod_rev, color = 'teal')
for i, v in enumerate(prod_rev):
    ax.text(i, v+1500, f'{v:,}', ha ='center', fontsize=8)
ax.set_title('Revenue by Product')
ax.set_xticklabels(products, rotation = 45, ha='right')    
ax = axes[1][0]
colors = ['green' if p > 50000 else 'orange' for p in df['profit']]
ax.bar(df['month'], df['profit'], color = colors)
ax.set_title('Monthly Profit')
ax.grid(axis ='y', alpha=0.4)
ax = axes[1][1]
explode = [0.1,0,0,0]
ax.pie(reg_rev, labels = regions, autopct = '%1.1f%%', explode =explode, startangle = 140)
ax.set_title('Revenue by region')
plt.subplots_adjust(hspace=0.4, wspace=0.3) 
plt.savefig('sales_dashboard.png', dpi=150, bbox_inches='tight')
print('Dashboard saved.')
total = df['revenue'].sum()
profit = df['profit'].sum()
best = df.loc[df['profit'].idxmax(), 'month']
fig.text(0.5, 0.01,
        f"Total Revenue: {total:,} | Total Profit: {profit:,} | Best Month: {best}",
        ha ='center', fontsize = 10, color = '#444'
)
plt.tight_layout(rect=[0,0.04,1,1])
plt.savefig('sales_dashboard_final.png', dpi=150, bbox_inches='tight')
plt.show()