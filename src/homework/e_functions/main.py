from void_func import display_payroll_check

def main():

    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    display_payroll_check(hours_worked, hourly_rate)

main()