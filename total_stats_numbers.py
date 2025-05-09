numbers = []

for i in range(4):
    while True:
        try:
        num = int(input(f"Enter integer {i + 1}: "))
        numbers.append(num)
        break 
        except ValueError:
        print("Invalid input. Please enter an integer.")

total = sum(numbers)

average = total / 4

product = 1
for num in numbers:
    product *= num


smallest = min(numbers)
largest = max(numbers)


print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")