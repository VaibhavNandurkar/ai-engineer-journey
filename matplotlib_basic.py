import matplotlib.pyplot as plt

months  = ['Jan','Feb','Mar','Apr','May','Jun']
revenue = [120000,145000,98000,167000,189000,210000]

fig, ax = plt.subplots(figsize = (10,5))
colors = ['gold' if v==max(revenue) else 'steelblue' for v in revenue]
bars = ax.bar(months, revenue, color=colors)
for i, v in enumerate(revenue):
    ax.text(i, v+1500, f'{v:,}', ha = 'center', fontsize = 9)
ax.set_title('Monthly Revenue (peak highlighted)')
ax.set_xlabel('Month')
ax.set_ylabel('Revenue (INR)')
ax.grid(axis ='y', alpha=0.4 )
plt.tight_layout()
plt.show()