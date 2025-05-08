print("number\tsquare\tcube")

for number in range(6):
    square = number * number  #Calculate the square
    cube = number * number * number  #Calculate the cube
    print(f"{number}\t{square}\t{cube}")  #Print the number, square, and cube, separated by tabs