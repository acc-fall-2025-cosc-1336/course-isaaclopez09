from decisions import numerical_grade_to_letter_grade

def main():
    print("       MAIN MENU")
    print("1 - Letter grade using if")
    print("2 - Letter grade using switch")
    print("3 - Exit")

    selection = input("Enter selection here: ")
    if selection == "1":
        numerical_grade = input("Enter numerical grade: ")
        numerical_grade_to_letter_grade(numerical_grade)



main()