import json
import csv
import os

FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(FILE):
        with open('FILE', 'r') as f:
            return json.load(f)
    return []
    
def save_expenses(expenses):
    with open(FILE, 'w') as f:
        json.dump(expenses , f, indent = 2)    

def add_expense(expenses, date, category, amount, note):
    expense = {
        'date' : date,
        'category': category,
        'amount' : amount,
        'note' : note
    }        
    expenses.append(expense)
    save_expenses(expenses)
    print('Expense added.')
    return expenses

def print_summary(expenses):
    totals = {}
    for e in expenses:
        cat = e['category']
        totals[cat] = totals.get(cat, 0) + e['amount']
    print("\n--- Expense Summary ---")    
    for cat, total in totals.items():
        print(f'{cat}: ₹{total:.2f}')
    print(f'Total : ₹{sum(totals.values()):.2f}')    

def export_csv(expenses):
    csv_filename = 'expenses.csv'
    with open(FILE, 'w', newline ='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'category' , 'amount', 'note'])
        writer.writeheader()
        writer.writerows(expenses) 
    print("Exported to expenses.csv.")

expenses = load_expenses()
expenses = add_expense(expenses, '2026-05-28', 'Food', 150, 'Lunch')
expenses = add_expense(expenses, '2026-05-28', 'Transport', 50, 'Auto')    
expenses = add_expense(expenses, '2026-05-29', 'Food', 200, 'Dinner')
print_summary(expenses)
export_csv(expenses)

def filter_by_category(expenses, category):
    return [e for e in expenses if e['category'].lower() == category.lower()]
food_expenses = filter_by_category(expenses, 'food')
print(food_expenses)

