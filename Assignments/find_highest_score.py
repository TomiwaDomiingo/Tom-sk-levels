def find_highest_score():
    num_of_students = int(input("Enter the number of students: "))
    highest_score = 0
    highest_score_name = ""

    for i in range(1, num_of_students + 1):
        name = input(f"Enter student {i} name: ")
        score = int(input(f"Enter student {i} score: "))

        while score < 0 or score > 1000:
            print("Invalid score. Please enter a score between 0 and 1000.")
            score = int(input(f"Enter student {i} score: "))

        if score > highest_score:
            highest_score = score
            highest_score_name = name

    print(f"The student with the highest score is: {highest_score_name} with a score of {highest_score}")

find_highest_score()
