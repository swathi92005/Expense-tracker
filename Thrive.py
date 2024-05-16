#Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more informa
# Initialize income, expenses, and debt
income = float(input("Enter your income for this month: "))
balance = income
debt = 0.0

# Initialize an empty list to store expenses
expenses = []

def add_expense():
    """Add a new expense."""
    global balance, debt
    description = input("Enter a brief description of the expense: ")
    try:
        amount = float(input("Enter the expense amount: "))
    except ValueError:
        print("Invalid input. Please enter a valid numeric amount.")
        return

    if amount < 0:
        print("Expense amount cannot be negative.")
        return

    if balance >= amount:
        balance -= amount
        expenses.append((description, amount))
        print(f"Expense '{description}' added successfully! Remaining balance: ${balance:.2f}")
    else:
        print(f"Insufficient balance! You are in debt.")
        debt += amount
        print(f"Debt accumulated: ${debt:.2f}")

def remove_expense():
    """Remove an existing expense."""
    global balance
    if not expenses:
        print("No expenses to remove.")
        return

    description = input("Enter the description of the expense to remove: ")
    for desc, amt in expenses:
        if desc == description:
            balance += amt
            expenses.remove((desc, amt))
            print(f"Expense '{desc}' removed successfully! New balance: ${balance:.2f}")
            break
    else:
        print("Expense not found.")

def update_expense():
    """Update an existing expense."""
    global balance
    if not expenses:
        print("No expenses to update.")
        return

    description = input("Enter the description of the expense to update: ")
    for i, (desc, amt) in enumerate(expenses):
        if desc == description:
            try:
                new_description = input("Enter the updated description: ")
                new_amount = float(input("Enter the updated expense amount: "))
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
                return

            if new_amount < 0:
                print("Expense amount cannot be negative.")
                return

            balance += amt - new_amount
            expenses[i] = (new_description, new_amount)
            print(f"Expense '{new_description}' updated successfully! New balance: ${balance:.2f}")
            break
    else:
        print("Expense not found.")

def check_balance():
    """Calculate and display the total balance."""
    total_balance = balance + debt
    print(f"Total balance: ${balance:.2f}")
    print(f"Debt accumulated: ${debt:.2f}")
    print(f"Total balance (including debt): ${total_balance:.2f}")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. Update Expense")
        print("4. List Expenses")
        print("5. Check Balance")
        print("6. Exit")
        choice = input("Enter your choice (1-6 or -1 to exit): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            remove_expense()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            for desc, amt in expenses:
                print(f"{desc} | ${amt:.2f}")
        elif choice == "5":
            check_balance()
        elif choice == "6" or choice == "-1":
            print("Exiting Expense Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1-6 or enter -1 to exit.")

if __name__ == "__main__":
    main()



