number_layers = int(input("Enter the number of layers you want to approximate: ")) 
e_approx = 0
factorial = 1 
for number in range(0, number_layers): 
    e_approx = e_approx + (1 / factorial)
    print(f"For Term {number + 1} (1/{number}): {1 / factorial:.10f}")
    print(f"increasing sum: {e_approx:.10f}")
    if number > 0: 
        factorial = factorial * (number + 1)
print({e_approx})
