from decisions import get_letter_grade

def main():
    print("       MAIN MENU")
    print("1 - Letter grade using if")
    print("2 - Letter grade using switch")
    print("3 - Exit")

    selection = input("Enter selection here: ")
    if selection == "1":
        numerical_grade = int(input("Enter a number between 0 and 100: "))
        if 0 <= numerical_grade <= 100:

            grade = get_letter_grade(numerical_grade)
            print(f"The letter grade using if is: {grade}")
        else:
            print("Numerical grade must be between 0 and 100")

    elif selection == "2":
        numerical_grade = int(input("Enter a number between 0 and 100: "))
        if 0 <= numerical_grade <= 100:

            grade = get_letter_grade(numerical_grade)
            print(f"The letter grade using switch is: {grade}")
        else:
            print("Numerical grade must be between 0 and 100")

    elif selection == '3':
        print("Exiting the program.")

    else:
        print("invalid entry, please select 1,2,or 3")

main()