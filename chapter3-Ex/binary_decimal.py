def binary_to_decimal(binary_number):
  
decimal_value = 0
power = 0
while binary_number > 0:
        
digit = binary_number % 10
        
binary_number //= 10
       
decimal_value += digit * (2 ** power)
       
power += 1
return decimal_value

# test:
binary = 1101
decimal = binary_to_decimal(binary)
print(f"The decimal equivalent of {binary} is {decimal}")