def binary_to_decimal(binary_string):
    """Converts a binary string to its decimal equivalent."""
    decimal_value = 0
    for i in range(len(binary_string)):
        digit = binary_string[-(i + 1)]  # Access digits from right to left
        if digit == '1':
            decimal_value += 2**i
        elif digit != '0':
            return "Invalid input. Please enter a valid binary number (0s and 1s only)."
    return decimal_value

# Get user input
binary_input = input("Enter a binary number: ")

# Convert and print the result
decimal_result = binary_to_decimal(binary_input)
print("Decimal equivalent:", decimal_result)
