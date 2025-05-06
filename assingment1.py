# ----------------------problem 1 --------------------------------------------------


# input() function gets input as a string, so we convert it to an integer using int().
num1 = int(input("Enter number first : "))

# Prompt the user to enter the second number and convert it to an integer.
num2 = int(input("Enter number Second : "))

# Perform addition of num1 and num2
Addition = num1 + num2

# Print the result of the addition
print("Addition of Two number is", Addition)

# Perform subtraction of num2 from num1
subtraction = num1 - num2

# Print the result of the subtraction
print("Subtraction of Two number is", subtraction)

# Perform multiplication of num1 and num2
multiplication = num1 * num2

# Print the result of the multiplication
print("Multiplication of Two number is", multiplication)

# Perform division of num1 by num2 (returns a float)
division = num1 / num2

# Print the result of the division
print("Division of Two number is", division)


# ---------------------------------------problem 2 --------------------------------------------------

# Ask the user to enter their first name using input()
first_name = input("Enter your first name : ")

# Ask the user to enter their last name using input()
last_name = input("Enter your last name : ")

# Combine the first name and last name into a full name using string concatenation
# Note: There is no space between them, so the names will appear stuck together unless we add one
full_name = first_name + last_name

# Print a welcome message using an f-string to include the full name
print(f"Hello, {full_name} Welcome to the pyhton program")

