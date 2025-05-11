num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

sum_of_numbers = num1 + num2 + num3
average = sum_of_numbers / 3
product = num1 * num2 * num3

smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

print("Sum:", sum_of_numbers)
print("Average:", average)
print("Product:", product)
print("Smallest:", smallest)
print("Largest:", largest)