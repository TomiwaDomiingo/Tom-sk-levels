def password_strength(password):
    length = len(password)
    if length < 8:
        return "Very Weak"
    elif length == 8:
        return "Weak"
    elif 8 < length <= 16:
        return "Strong"
    else: 
        return "Very Strong"

# prompts the user to enter the password
password = input("Enter your password: ")

# determine and display the strength
strength = password_strength(password)
print("Password Strength:", strength)
