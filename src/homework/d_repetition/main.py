from repetition import get_factorial, sum_odd_numbers


def main():
    print("MAIN MENU")
    print("1 - Factorial")
    print("2 - Sum odd numbers")
    print("3 - exit")
    selection = input("Enter selection here: ")
    if selection == "1":
        input_number = int(input("Enter number between 0 and 10: "))
        if input_number < 0:
            print("Number entered must be greater than 0, please enter another number")

        elif 10 < input_number:
            print("Number cant be over 10, please enter another number")
    
        else:
            factorial = get_factorial(input_number)
            print(f"The factorial of {input_number} is: {factorial}")
    
    elif selection == "2":
        input_number = int(input("Enter a number between 0 and 100: "))
        if input_number < 0:
            print("entered number must be greater than 0, please enter another number")
    
        elif 100 < input_number:
            print("entered number cant be over 100, please enter another number")
    
        else: 
            sum = sum_odd_numbers(input_number)
            print(f"the sum of odd numbers up {input_number} is {sum} ")

    elif selection == '3':
        print("Exiting the program.")

    else:
        print("invalid entry, please select 1,2,or 3")

main()