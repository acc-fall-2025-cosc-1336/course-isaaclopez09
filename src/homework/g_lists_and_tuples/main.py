from lists import get_lowest_list_value, get_highest_list_value

def main():
    running = True
    while running:
        print("MAIN MENU")
        print("1 - Show the list low /high values")
        print("2 - Exit")
        selection = input("Enter selection here: ")
        if selection == "1":
            values = []
            keep_going = "y"
            running = True
            while running:
                value = input("Enter a list value: ")
                try:
                    values.append(float(value))
                except ValueError:
                    print("Error, please enter a number")
                    continue
                if len(values) >= 3:
                    keep_going = input("Do you want to enter another value? (y/n): ").lower()
                    print("")
                    if keep_going != "y":
                        break
            if len(values) > 0:
                low = get_lowest_list_value(values)
                high = get_highest_list_value(values)
                
                print(f"Lowest value: {low}")
                print(f"Highest value: {high}")
                print("")
            
        elif selection == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid option, try again.")
            print("")

if __name__ == '__main__':
    main()