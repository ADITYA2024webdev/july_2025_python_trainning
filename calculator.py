
try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
            result = num1 + num2
    elif operator == '-':
            result = num1 - num2
    elif operator == '*':
            result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator. Please use +, -, *, or /.")

    print(f"The result is: {result}")


except Exception as e:
    print(f"An unexpected error occurred: {e}")




