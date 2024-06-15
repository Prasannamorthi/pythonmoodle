Develop a Python program that safely performs division between two numbers provided by the user. Handle exceptions like division by zero and non-numeric inputs.

Input Format: Two lines of input, each containing a number.

Output Format: Print the result of the division or an error message if an exception occurs.


For example:

Input	Result
10
2
5.0
10
0
Error: Cannot divide or modulo by zero.
ten
5
Error: Non-numeric input provided.

def safe_division():
    try:
        num1 = float(input())
        num2 = float(input())

        result = num1 / num2

        print(result)

    except ZeroDivisionError:
        print("Error: Cannot divide or modulo by zero.")

    except ValueError:
        print("Error: Non-numeric input provided.")

safe_division()


