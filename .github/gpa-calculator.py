print("Welcome to the Overly Verbose GPA Calculator!")


while True:
    num = input("How many classes are you in? (at least 5): ")
    if num.isdigit():
        num_classes = int(num)
        if num_classes >= 5:
            break
        else:
            print("Please enter a number that is 5 or more.")
    else:
        print("Unfortunately, that is not a valid number. Please try again.")


grades = []

for i in range(num_classes):
    while True:
        grade_input = input(f"Enter grade {i + 1} (0.0 - 4.0): ")
        try:
            grade = float(grade_input)
            if 0.0 <= grade <= 4.0:
                grades.append(grade)
                break
            else:
                print("Grade must be between 0.0 and 4.0.")
        except ValueError:
            print("Please enter a valid number like 3.5 or 4.0.")


total = sum(grades)
count = len(grades)
gpa = round(total / count, 2)

print(f"\n Your current GPA is: {gpa} (from {count} classes)")

print("\nLet's look at your semesters!")

while True:
    semester_choice = input("Check which semester?\n1. First half\n2. Second half\nEnter 1 or 2: ")
    if semester_choice in ["1", "2"]:
        break
    else:
        print("Please enter either 1 or 2.")

half = count // 2
if semester_choice == "1":
    semester_grades = grades[:half]
    label = "First"
else:
    semester_grades = grades[half:]
    label = "Second"

semester_gpa = round(sum(semester_grades) / len(semester_grades), 2)

print(f"\n{label} semester GPA: {semester_gpa}")
print(f"Overall GPA: {gpa}")

if semester_gpa > gpa:
    print("Nice job! You are improving! Keep up the good work!")
elif semester_gpa < gpa:
    print("It looks like you are slipping a little. Time to start focusing a bit more!")
else:
    print("Your GPA is very steady.")


while True:
    goal_input = input("\nWhat is your goal GPA? (0.0 - 4.0): ")
    try:
        goal = float(goal_input)
        if 0.0 <= goal <= 4.0:
            break
        else:
            print("Please enter a goal GPA between 0.0 and 4.0.")
    except ValueError:
        print("That’s not a valid number. Try again.")

if gpa >= goal:
    print(f"\nCongrats! Your current GPA of {gpa} already meets or exceeds your goal of {goal}!")
else:
    print(f"\nLet's see if you can reach your goal GPA of {goal} by changing just one grade to 4.0...")

    found_solution = False
    for i in range(len(grades)):
        original_grade = grades[i]
        if original_grade == 4.0:
            continue
        hypothetical = grades.copy()
        hypothetical[i] = 4.0
        new_gpa = round(sum(hypothetical) / count, 2)
        if new_gpa >= goal:
            if not found_solution:
                print("\n There is good news! You can reach your goal GPA by improving just ONE grade:")
                found_solution = True
            print(f"- If you raise your grade in class {i + 1} from {original_grade} to 4.0, your GPA would be {new_gpa}")

    if not found_solution:
        print("\nYou will need to improve more than one grade to hit your goal GPA.")
        print("It is time for you to lock in and start studying more!")

print("\nThank you for using the Overly Verbose GPA Calculator! Goodbye!")