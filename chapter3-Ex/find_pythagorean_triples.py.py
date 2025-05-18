number_limit = int(input("Enter the limit for the range: "))
for side1 in range(1, number_limit +1): 
	for side2 in range(1, number_limit +1):
		for hypotenuse in range(1, number_limit +1):
            # Check if the Pythagorean theorem holds
			if side1 + side2 == hypotenuse**2:
                # Print the Pythagorean triple
				print(side1, side2, hypotenuse)
