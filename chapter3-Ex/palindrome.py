def is_palindrome(number):
    number_str = str(number)
    return len(number_str)== 5 and number_str == number_str[::-1]
number = int(input('Enter a fiv3 digit number:'))

if is_palindrome(number):
    print('it is a palindrome')
else:
    print('it is not a palindrome')    