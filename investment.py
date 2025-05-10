initial_investment = int(input('Enter the initial investment amount: '))
roi = 0
if initial_investment <= 0:    
    print("Please enter a non-negative investment amount.")
number_of_years = int(input('How long do you wish to invest for: '))
annual_interest_rate = int(input("Enter your rate: ")) / 100

for year in range(1, number_of_years +1):
    yearly_interest = initial_investment * annual_interest_rate 
    roi = initial_investment + yearly_interest
  
    print(f"{roi:.2f}")
    initial_investment = roi 
