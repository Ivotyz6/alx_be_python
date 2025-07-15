#prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))    
#prompt the user for their monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))
#calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses 
#calculate the projrcted savings in 12 months
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
#display the projected savings
print(f"Your projected savings in 12 months is: ${projected_savings:.2f}")      
