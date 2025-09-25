from output import get_tip_ammount, get_sales_tax


def reciept_main():
    meal_ammount = float(input("Enter meal ammount: "))
    tip_rate = float(input("Enter tip rate: "))
    sale_tax = get_sales_tax(meal_ammount)
    tip_ammount = get_tip_ammount(meal_ammount, tip_rate)

    print("Meal Ammount", meal_ammount)
    print("sales Tax", sale_tax)
    print("Tip Ammount", tip_ammount)
    print("Total", meal_ammount + sale_tax + tip_ammount)
    
reciept_main()