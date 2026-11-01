# Write a Python program to create a BankAccount class with attributes such as account 
# number, account holder name, account type, and balance. Use a constructor to initialize 
# the attributes and implement methods to deposit money, withdraw money, and display 
# the account details and current balance. Create one or more objects to demonstrate the 
# functionality. 


# Bank Account Management System

# Create BankAccount class
class BankAccount:

    # Constructor to initialize account details
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid deposit amount!")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount!")

    # Method to display account details
    def display(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Account Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Account Type:", self.acc_type)
        print("Current Balance: Rs.", self.balance)


# Create an object
account1 = BankAccount(1001, "Arun", "Savings", 5000)

# Display account details
account1.display()

# Deposit money
account1.deposit(2000)

# Withdraw money
account1.withdraw(1500)

# Display updated account details
account1.display()
