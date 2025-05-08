#--------------------Task 1 --------------------------------

n = int(input("Enter a number : "))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

result = factorial(n)
print(f"factorial of {n} is : ", result)


# ---------------------------Task 2 ----------------------------

import math

num = float(input("Enter a number: "))

if num <= 0:
    print("Square root and natural logarithm are only defined for positive numbers.")
else:
    square_root = math.sqrt(num)
    log_result = math.log(num)
    sine_result = math.sin(num) 
    
    print(f"Square Root is: {square_root}")
    print(f"Natural Logarithm (base e) is: {log_result}")
    print(f"Sine (in radians) is: {sine_result}")



