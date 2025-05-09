n = 1
 if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


print(f"Factorial of 10: {factorial(10)}")
print(f"Factorial of 20: {factorial(20)}")
print(f"Factorial of 30: {factorial(30)}")
print(f"Factorial of 100: {factorial(100)}")
print(f"Factorial of 170: {factorial(170)}") # Largest factorial that can be computed in Python without overflow.
print(f"Factorial of 171: {factorial(171)}") # Overflow occurs, which leads to an incorrect value.

