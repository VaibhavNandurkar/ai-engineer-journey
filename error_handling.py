                                # Error Handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

print(safe_divide(10, 2))
print(safe_divide(5, 0))

                                #Read Number
def read_number(value):
    try:
        result = int(value) 
        return result                              
    except:
        print( "Error: '<value>' is not a valid number.")
        result = None
    else:
        print("Conversion successful!")
    finally:
        print("Attempt Completed") 
    return result

print(read_number(42))
print(read_number("Hello!"))

                                    #Bank Account

class InsufficientFundError(Exception):
    pass
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount    
        print(f"Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundError(
                f"Cannot withdraw  ₹{amount}. Balance is only {self.balance}."
            )
        self.balance -= amount
        print(f"Withdrew ₹{amount}. Balance: ₹{self.balance}.") 

account = BankAccount(500) 
account.deposit(200) 
try:
    account.withdraw(800)
except InsufficientFundError as e:
    print("Transaction Failed: {e}")     
  

              