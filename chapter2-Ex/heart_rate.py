age = int(input("Please enter your age in: "))

max_heart_rate = 220 - age

lower_target_heart_rate = 0.50 * max_heart_rate
upper_target_heart_rate = 0.85 * max_heart_rate

print("Your maximum heart rate is:", max_heart_rate, "beats per minute")
print("Your target heart rate range is between", lower_target_heart_rate, "and", upper_target_heart_rate, "beats per minute")
