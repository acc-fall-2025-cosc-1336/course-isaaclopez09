from lists import get_p_distance, get_p_distance_matrix

def main():
    running = True
    while running:
        print("MAIN MENU")
        print("1 - Get P distance matrix")
        print("2 - Exit")
        selection = input("Enter selection here: ")
        if selection == "1":
            list1 = []
            running = True
            while running:
                user_input = input("Enter DNA list or 'done' when finished: ")
                if user_input =="done":
                    break
                list1.append(user_input.split())
            matrix = get_p_distance_matrix(list1)
            print("P-distance Matrix:")
            for row in matrix:
                print(row)
            print()


        elif selection == "2":
            print("Exiting program")
            break
        else:
            print("Invalid option, try again.")
            print("")

if __name__ == '__main__':
    main()