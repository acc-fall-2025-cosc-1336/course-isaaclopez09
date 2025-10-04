def get_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
    
def sum_odd_numbers(n):
    total_sum = 0
    current_number = 1

    while current_number <= n:
        if current_number % 2 != 0:  
            total_sum += current_number
        current_number += 1
    return total_sum