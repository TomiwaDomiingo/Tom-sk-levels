n = int(input("Enter a positive integer: "))

while n < 1:
    print("Please enter a positive integer:")
    n = int(input())
for countdown in range(n, 0, -1):
    print(countdown)
print("Blast Off!")