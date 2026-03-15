# Safe Calculator using Exception Handling

def safe_calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            raise ValueError("Invalid operator!")

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers or operator.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("Unexpected error:", e)

# Run the calculator
safe_calculator()