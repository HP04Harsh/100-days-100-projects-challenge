class BudgetPlanner:
    def __init__(self):
        self.income = 0
        self.expenses = []

    def add_income(self, amount):
        self.income += amount
        print(f"✅ Income added: ₹{amount}")

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})
        print(f"💸 Expense added: {category} - ₹{amount}")

    def show_balance(self):
        total_expense = sum(exp["amount"] for exp in self.expenses)
        balance = self.income - total_expense
        print(f"\n💰 Total Income: ₹{self.income}")
        print(f"💸 Total Expenses: ₹{total_expense}")
        print(f"📊 Remaining Balance: ₹{balance}")

    def show_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        print("\n📋 Expense List:")
        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. {exp['category']} - ₹{exp['amount']}")

    def category_summary(self):
        summary = {}
        for exp in self.expenses:
            summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]
        
        print("\n📊 Category-wise Spending:")
        for category, amount in summary.items():
            print(f"{category}: ₹{amount}")


def main():
    planner = BudgetPlanner()

    while True:
        print("\n====== Personal Budget Planner ======")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Category Summary")
        print("5. Show Balance")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: ₹"))
            planner.add_income(amount)

        elif choice == "2":
            category = input("Enter category (Food, Rent, Travel, etc.): ")
            amount = float(input("Enter expense amount: ₹"))
            planner.add_expense(category, amount)

        elif choice == "3":
            planner.show_expenses()

        elif choice == "4":
            planner.category_summary()

        elif choice == "5":
            planner.show_balance()

        elif choice == "6":
            print("👋 Exiting... Stay financially smart!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()