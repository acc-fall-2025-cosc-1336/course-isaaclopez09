fica_rate = 0.0765
federal_tax_rate = 0.08

def get_gross_pay(hours_worked, hourly_rate):
   
    if hours_worked > 40:
        regular_pay = 40 * hourly_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours_worked * hourly_rate
    return gross_pay

def get_fica_tax(gross_pay):
   
    return gross_pay * fica_rate

def get_federal_tax(gross_pay):
   
    return gross_pay * federal_tax_rate