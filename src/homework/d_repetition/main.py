from repetition import get_factorial, sum_odd_numbers


print("MAIN MENU")
print("1 - Factorial")
print("2 - Sum odd numbers")
print("3 - exit")
selection = input("Enter selection here: ")
if selection == "1":
        input_number = int(input("Enter any positive number: "))
        if 0 <= input_number:

            factorial = get_factorial(input_number)
            print(f"The factorial of {input_number} is: {factorial}")
        else:
            print("Number entered must be positive")