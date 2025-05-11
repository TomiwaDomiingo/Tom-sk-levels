n = int(input("Enter a positive number: "))

while n < 1:
    print("Please enter a positive number:")
    n = int(input())
for countdown in range(n, 0, -1):
    print(countdown)
print("Blast Off!")