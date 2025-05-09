passes = 0  # Counter for passes
failures = 0  # Counter for failures

while True:
	user_input = input("Enter 1 or 2: ") 
    if user_input == '1':
        passes += 1
        print("Pass")
    elif user_input == '2':
        failures += 1
        print("Fail")
    else:
        print("Invalid input. Please enter 1 or 2.")
        continue   
    if passes + failures >= 5: 
        break 
print(f"Number of passes: {passes}")
print(f"Number of failures: {failures}")