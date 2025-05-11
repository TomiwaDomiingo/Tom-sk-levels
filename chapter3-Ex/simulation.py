# Simulate a simple medical diagnosis
print("What is your problem?")
input()  # Ignore user's input

print("Have you had this problem before (yes or no)?")
answer = input().lower()

    if answer == "yes":
    print("Well, you have it again.")
    elif answer == "no":
    print("Well, you have it now.")
    else:
    print("Please answer yes or no.")