monthly_income = int(input("Enter Your monthly income: "))
monthly_expenses = int(input("Enter your monthly total expenses: "))
monthly_savings = monthly_income - monthly_expenses
# print(monthly_savings)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are ", monthly_savings)
print("Projected savings after one year, with interest, is: ", projected_savings)
