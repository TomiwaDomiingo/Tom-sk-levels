num = int(input("Enter a five-digit integer: "))
result = is_palindrome(num)

if result == True:
     print(f"{num} is a palindrome.")
elif result == False:
     print(f"{num} is not a palindrome.")
else:
     print(result)

except ValueError:
    print("Invalid input. Please enter a valid integer.")



if not (10000 <= number <= 99999):
        return "Please enter a five-digit number."

    digit1 = number // 10000
    digit2 = (number // 1000) % 10
    digit3 = (number // 100) % 10
    digit4 = (number % 100) // 10
    digit5 = number % 10

    if digit1 == digit5 and digit2 == digit4:
        return True
    else:
        return False

