def find_two_largest(numbers):
if len(numbers) < 2:
    return None
if numbers[0] > numbers[1]:
        largest = numbers[0]
        second_largest = numbers[1]
    else:
        largest = numbers[1]
        second_largest = numbers[0]
        
    for number in numbers[2:]:
    if number > largest:
            second_largest = largest
            largest = number
    elif number > second_largest:
            second_largest = number
            
    return (largest, second_largest)

# test
numbers = [5, 2, 8, 1, 9, 4, 7, 3, 6, 10]
result = find_two_largest(numbers)

if result:
    print("The two largest numbers are:", result)
else:
    print("Not enough numbers in the list.")

