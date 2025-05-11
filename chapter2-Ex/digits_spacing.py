number = int(input("Enter a five-digit number: "))

digit1 = number // 10000
remaining = number % 10000
digit2 = remaining // 1000
remaining = remaining % 1000
digit3 = remaining // 100
remaining = remaining % 100
digit4 = remaining // 10
digit5 = remaining % 10

print(digit1, "   ", digit2, "   ", digit3, "   ", digit4, "   ", digit5)