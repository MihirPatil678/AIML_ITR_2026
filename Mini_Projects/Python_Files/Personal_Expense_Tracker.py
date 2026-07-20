# Project 3 - Personal Expense Tracker

expenses = []  # List Of All Expenses
monthly_budget = float(input("Enter Monthly Budget (Rs.):"))

def add_expense():
    description = input("Enter Description:")
    category = input("Enter Category (Food/Travel/Bills/Entertainment/Other):")
    amount = float(input("Enter Amount (Rs.):"))
    date = input("Enter Date (DD/MM/YYYY):")

    expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)

    total = 0
    for e in expenses:
        total += e["amount"]

    print("Expense Added!")
    print("Total Spent So Far: Rs.", total)

def view_expenses():
    if len(expenses) == 0:
        print("No Expenses Recorded.")
        return

    for i in range(len(expenses)):
        e = expenses[i]
        print(f"{i+1}. {e['date']} | {e['category']} | Rs.{e['amount']} | {e['description']}")

def category_summary():
    if len(expenses) == 0:
        print("No Expenses To Show.")
        return

    summary = {}

    for e in expenses:
        cat = e["category"]

        if cat in summary:
            summary[cat] += e["amount"]
        else:
            summary[cat] = e["amount"]

    print("\n*** Category Summary ***")

    for cat in summary:
        print(f"{cat}: Rs. {summary[cat]:.2f}")

def budget_report():
    total = 0

    for e in expenses:
        total += e["amount"]

    remaining = monthly_budget - total
    percent_used = (total / monthly_budget) * 100

    print("\n*** Budget Report ***")
    print(f"Total Spent: Rs. {total:.2f}")
    print(f"Budget: Rs. {monthly_budget:.2f}")
    print(f"Remaining: Rs. {remaining:.2f}")
    print(f"Used: {percent_used:.2f}%")

    if percent_used >= 100:
        print("WARNING: Budget Exceeded!")
    elif percent_used >= 80:
        print("WARNING: You Have Used 80% Of Your Budget!")

# Main Menu Loop
while True:
    print("\n*** PERSONAL EXPENSE TRACKER ***")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")

    choice = input("Enter Choice:")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category_summary()
    elif choice == "4":
        budget_report()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice.")