import matplotlib.pyplot as plt


months = ['Jan','Feb','Mar','Apr','May','Jun']
profit = [2000, 3500, 2800, 4200, 5100, 6000]


plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(months, profit, marker='o', color='steelblue', label ='Profit')
ax.fill_between(months, profit, alpha=0.2,color='steelblue',)
ax.set_title('Monthly Profit')
ax.set_xlabel('Month')
ax.set_ylabel('Profit (₹)')
ax.grid(True)
plt.show()
