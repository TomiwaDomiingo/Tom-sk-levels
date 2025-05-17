def multiply_without_symbol(firstNum, secondNum):

	multiply = 0 
	for numbers in range(secondNum):
		multiply = multiply + firstNum	
	#if (firstNum <= -1 and secondNum >= -100):
	
	#return f"invalid"	
	return multiply

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(multiply_without_symbol(number1, number2))



 



