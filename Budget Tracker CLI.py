class Transaction:
    def __init__(self, t_type, amount, category, note):
        self.t_type = t_type
        self.amount = amount
        self.category = category
        self.note = note

    def __str__(self):
        return f"[{self.t_type}] {self.category} — ₹{self.amount} ({self.note})" 


class BudgetTracker:
    def __init__(self, filename):
        self.filename = filename
        self.transactions = []

    def add_income(self, amount, category, note):
        t = Transaction("income", amount, category, note)
        self.transactions.append(t)
        print("Income added.")

    def add_expense(self, amount, category, note):
        t = Transaction("expense", amount, category, note)
        self.transactions.append(t)
        print("Expense added.")


    def show_summary(self):
        incomes = [t.amount for t in self.transactions if t.t_type == "income"]
        expenses = [t.amount for t in self.transactions if t.t_type == "expense"]
        total_income = sum(incomes)
        total_expenses = sum(expenses)
        balance = total_income - total_expenses
        print("--- Budget Summary ---")
        print(f"Total Income:   ₹{total_income}")
        print(f"Total Expenses: ₹{total_expenses}")
        print(f"Balance:        ₹{balance}")
    
    def save_to_file(self):
        with open(self.filename, 'w') as f:
            for t in self.transactions: 
                f.write(f"{t.t_type},{t.amount},{t.category},{t.note}\n")
        print(f"Data saved to budget.txt") 

    def load_from_file(self):
        self.transactions = []
        with open(self.filename, 'r') as f:
            for line in f.readlines():
                t_type, amount, category, note = line.strip().split(',')
                t = Transaction(t_type, int(amount), category, note)
                self.transactions.append(t)
        print(f"Loaded {len(self.transactions)} transactions.")

    def show_all(self):
        if not self.transactions:
            print("No transactions yet.")
            return 
        print("--- All Transactions ---")   
        for i, t in enumerate(self.transactions, start=1):
            print(f"{i}. {t}")
def main():
    bt = BudgetTracker("budget.txt")
    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add income")
        print("2. Add expense")
        print("3. Show all transactions")
        print("4. Show summary")
        print("5. Save")
        print("6. Load")
        print("7. Exit")
        choice = input("Choose: ")
        if choice == "1":
            amount = int(input("Amount: "))
            category = input("Category: ")
            note = input("Note: ")    
            bt.add_income(amount, category, note)
        elif choice == "2":
            amount = int(input("Amount: "))
            category = input("Category: ")
            note = input("Note: ")
            bt.add_expense(amount, category, note)
        elif choice == "3":
            bt.show_all()
        elif choice == "4":
            bt.show_summary()
        elif choice == "5":
            bt.save_to_file()
        elif choice == "6":
            bt.load_from_file()
        elif choice == "7":
            print("Goodbye!")
            break    
if __name__ == "__main__":
    main()


