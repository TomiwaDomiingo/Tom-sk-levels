
print("Enter  loan amount:")
principal = float(input())

print("Enter the annual interest rate:")
interest_rate = float(input())

print("Enter the loan duration in years:")
duration = int(input())

monthly_rate = interest_rate / 12
number_of_payments = duration * 12
monthly_payment = principal * (monthly_rate * (1 + monthly_rate)number_of_payments) / ((1 + monthly_rate)number_of_payments - 1)

print("Your monthly mortgage payment is:", monthly_payment)
