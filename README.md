# Problem 1: Basic Arithmetic Calculator

## 🔍 Description
This Python program performs basic arithmetic operations—addition, subtraction, multiplication, and division—on two numbers provided by the user.

---

## 📌 Functionality
- Takes two integer inputs from the user.
- Performs and displays the result of:
  - Addition
  - Subtraction
  - Multiplication
  - Division

---

## 🧠 Step-by-Step Explanation

1. **Input Collection**:
   - Prompts the user to enter the first number.
   - Prompts the user to enter the second number.
   - Both inputs are converted from string to integer using `int()`.

2. **Arithmetic Operations**:
   - **Addition**: Adds the two numbers using `+`.
   - **Subtraction**: Subtracts the second number from the first using `-`.
   - **Multiplication**: Multiplies the two numbers using `*`.
   - **Division**: Divides the first number by the second using `/`.

3. **Output**:
   - Each result is printed with a clear message using `print()`.

----------------------------------------------------------------------------
# Problem 2: Full Name Greeting

## 🔍 Description
This Python program asks the user to input their first and last name, combines them, and prints a personalized greeting message.

---

## 📌 Functionality
- Takes two string inputs from the user (first name and last name).
- Concatenates the names without a space.
- Displays a greeting message using the combined name.

---

## 🧠 Step-by-Step Explanation

1. **Input Collection**:
   - Prompts the user to enter their first name.
   - Prompts the user to enter their last name.
   - Inputs are collected as strings using `input()`.

2. **String Concatenation**:
   - Combines `first_name` and `last_name` using `+`.
   - Note: No space is added between them, so the names will appear directly joined (e.g., JohnDoe).

3. **Output**:
   - Displays a welcome message using an `f-string`.




# -----------------------------------------------Assignment 2 Task 1 --------------------------------------------------

# Assignment 1: Basic Python Program

## Objective  
Create a Python program that takes user input and checks whether the number is even or odd.

## Approach  
- Used `input()` to take user input.  
- Converted the input to an integer using `int()`.  
- Used modulus operator `%` to determine even or odd.  
- Displayed the result using `print()`.

## How to Run  
1. Open the `.py` file in any Python IDE or terminal.  
2. Run the script using:  
   ```bash
   python filename.py


# ----------------------------------------------Assignment 2 Task 2 ----------------------------------------------

# Assignment 1: Basic Python Program

## Objective  
Create a program that prints numbers from 1 to 50 and calculates their total sum.

## Approach  
- Used a `for` loop with `range()` to print numbers.  
- Used `sum()` to calculate the total of integers from 1 to 50.  
- Used `print()` to display each number and the final result.

## How to Run  
1. Open the `.py` file in any Python IDE or terminal.  
2. Run the script using:  
   ```bash
   python filename.py

# ----------------------------------------------- Assignment 3 Task 1 --------------------------------------------

# Assignment 1: Basic Python Program

## 🎯 Objective

Create a Python program that takes user input, performs calculations, and displays the result.

---

## 🧠 Approach

- Used `input()` to take user input from the console.
- Converted the input to an integer using `int()` for arithmetic operations.
- Implemented a recursive function to calculate the factorial.
- Used `print()` to display the final result to the user.

---

## 💻 How to Run

1. Open the `.py` file in any Python IDE (e.g., VS Code, PyCharm) or terminal.
2. Run the script using the following command:


# -------------------------------------------Assignment 3 Task 2 ----------------------------------------------------

# Assignment 1: Python Math Operations Program

## 🎯 Objective

Create a Python program that:
- Takes a number as input from the user
- Calculates and displays:
  - Square root of the number
  - Natural logarithm (log base e)
  - Sine of the number (in radians)

The program uses functions and exception handling to ensure safe and reusable code.

---

## 🧠 Approach

- Used `input()` and `float()` to take numeric input from the user.
- Wrapped calculations in a function: `calculate_operations(num)`.
- Used the `math` module to compute:
  - `math.sqrt()` for square root
  - `math.log()` for natural logarithm
  - `math.sin()` for sine
- Handled invalid inputs and domain errors using `try-except`.

---

## 💻 How to Run

1. Ensure Python 3.x is installed on your system.
2. Save the code in a file named `math_operations.py`.
3. Open a terminal and navigate to the file's location.
4. Run the script using:

#```bash
#python math_operations.py



# ------------------------------------------Assignment 4 Task 1 --------------------------------------------------------------

# Assignment: Read a Text File in Python

## Objective:
Create a program that reads and displays the contents of a text file line by line, with error handling if the file does not exist.

## Approach:
- Used `open()` with `"r"` mode to open a file named `sample.txt`.
- Iterated over each line in the file and printed it using `print()` and `strip()` to remove newline characters.
- Wrapped the file reading logic inside a `try-except` block to gracefully handle errors.
- Specifically handled the `FileNotFoundError` if `sample.txt` does not exist.
- Used a general `Exception` handler to catch any unexpected errors.
- Closed the file manually using `close()` after reading.

## How to Run:
1. Make sure there is a file named `sample.txt` in the same directory as the Python script (optional if testing file-not-found error).
2. Open the `.py` file in any Python IDE or terminal.
3. Run the script using `python filename.py`.
4. The content of the file (if found) will be printed line by line.
5. If the file does not exist, a friendly error message will be shown.






















# ------------------------------------------Assignment 4 Task 2 --------------------------------------------------------------
# Assignment 1: File Handling in Python

## Objective:
Create a program that:
- Takes user input and writes it to a file.
- Appends additional input to the same file.
- Reads and displays the content of the file.

## Approach:
- Used `input()` to take user input.
- Used `open()` with `"w"` mode to write initial input to `output.txt`.
- Used `open()` with `"a"` mode to append more text.
- Used `open()` with `"r"` mode to read and display the final contents.
- Handled file-related errors using `try-except` blocks for safe execution.

## How to Run:
1. Open the `.py` file in any Python IDE or terminal.
2. Run the script using `python filename.py`.
3. Enter the required text inputs when prompted.
4. Final content of the file will be displayed in the output.
