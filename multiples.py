print("checking for multiples")

number = int(input("Enter a number: "))

divisor = int(input("Enter a divisor"))

if number % divisor == 0:
	print(f"{number} is a multiple of {divisor}")
else:
	print(f"{number} is not a multiple of {divisor}")
	