while True:
    try:
        initial_investment = float(input("Enter the initial investment amount: "))
        if initial_investment >= 0:
            break 
        else:
            print("Please enter a valid investment amount.")

annual_interest_rate = 0.07

print("Year\tInvestment Value")

for year in range(1, 31):
    investment_value = initial_investment * (1 + annual_interest_rate) ** year
    print(f"{year}\t\t${investment_value:,.2f}")