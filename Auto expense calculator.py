def auto_expense_calculator():
    print("🔢 Auto Expense Calculator Based on Income\n")

    try:
        income = float(input("Enter your monthly income (₹): "))

        fixed_rent = int(input("\nEnter Your Monthly House Rent Amount (₹): "))
        fixed_groceries = int(input("\nEnter Your Monthly Groceries Amount (₹): "))
        fixed_bills = int(input("\nEnter Your Monthly Bill Amount (₹): "))

        remaining_income = income - (fixed_rent + fixed_groceries + fixed_bills)

        if remaining_income <= 8000:
            print("\n⚠️ Warning: Your remaining budget is too low (₹ {:.2f})".format(remaining_income))
            print("💡 Please try to reduce your fixed monthly expenses.\n")
            return

        expenses = {
            "Miscellaneous ": 0.60,
            "Emergency Fund": 0.10,
            "Investment    ": 0.0932
        }

        print("\n📊 Estimated Monthly Expenses Breakdown:")
        print(f"  - Rent             : ₹ {fixed_rent:.2f}")
        print(f"  - Groceries        : ₹ {fixed_groceries:.2f}")
        print(f"  - Bills            : ₹ {fixed_bills:.2f}")
        total = fixed_rent + fixed_groceries + fixed_bills

        for item, percent in expenses.items():
            amount = remaining_income * percent
            total += amount
            print(f"  - {item}   : ₹ {amount:.2f}")

        print(f"\n      Total          : ₹ {total:.2f}")
        if total > income:
            print("⚠️ Warning: Your expenses exceed your income!")

        savings = income - total
        print(f"✅ Your Savings      : ₹ {savings:.2f}\n")

    except ValueError:
        print("❌ Please enter a valid number.")

auto_expense_calculator() 