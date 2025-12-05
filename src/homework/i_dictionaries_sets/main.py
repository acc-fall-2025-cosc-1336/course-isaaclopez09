from dictionary import add_inventory, remove_inventory_widget

def main():
    Widgets = {}
    running = True
    while running:
        print("CURRENT INVENTORY")
        for entry in Widgets:
            print(entry, Widgets[entry])
        print("")
        print("INVENTORY MENU")
        print("1 - Add or Update Item")
        print("2 - Delete item")
        print("3 - Exit")
        selection = input("Enter selection here: ")
        if selection == "1":
            
            item_name = input("Enter item name: ")
            item_quantity = int(input("enter item ammount: "))
            print("")
            add_inventory(Widgets, item_name, item_quantity)
        elif selection == "2":
            item_name = input("Enter item you wish to delete: ")
            print("")
            results = remove_inventory_widget(Widgets, item_name)
            print(results)
            print("")
        elif selection == "3":
            print("Exiting program")
            break
        else:
            print("Invalid option, try again.")
            print("")

if __name__ == '__main__':
    main()
