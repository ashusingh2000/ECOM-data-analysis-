import numpy as np
import matplotlib.pyplot as plt
import csv

# create an empty list to store transactions
transactions = []

# function to add a transaction
def add_transaction(transaction):
    transactions.append(transaction)
    print(f"Transaction added: {transaction}")

    # write transaction to CSV file
    with open('transactions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([transaction['amount'], transaction['month']])


# function to calculate total balance
def calculate_balance():
    balance = 0
    for transaction in transactions:
        balance += transaction['amount']
    return balance

# function to generate a balance report
def generate_report():
    # calculate total balance
    balance = calculate_balance()

    # calculate monthly expenses
    expenses = []
    for i in range(1, 13):
        monthly_expenses = sum([transaction['amount'] for transaction in transactions if transaction['amount'] < 0 and transaction['month'] == i])

        expenses.append(monthly_expenses)
    if not expenses:
        print("No expenses to plot.")
    else:
        # print balance report
        print(f"\nCurrent balance: {balance}")
        print(f"Total income: {sum([transaction['amount'] for transaction in transactions if transaction['amount'] > 0])}")

        print(f"Total expenses: {sum([transaction['amount'] for transaction in transactions if transaction['amount'] < 0])}")

        print(f"Average monthly expenses: {np.mean(expenses)}")

    # plot monthly expenses
        months = np.arange(1, 13)
        plt.plot(months, expenses,"r^--")
        plt.title("Monthly Expenses")
        plt.xlabel("Month")
        plt.ylabel("Expenses")
        xs=[1,2,3,4,5,6,7,8,9,10,11,12]
        bins=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        plt.xticks(xs,bins)
        plt.figure(figsize=(5,1))
        
        plt.show()

    
      





# main program loop
while True:
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. Generate Report")
    
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter transaction amount: "))
        month = int(input("Enter transaction month (1-12): "))
        transaction = {'amount': amount, 'month': month}
        add_transaction(transaction)
    elif choice == "2":
        generate_report()
        
       
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.") 

