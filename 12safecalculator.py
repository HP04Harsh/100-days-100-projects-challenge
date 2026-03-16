print("🔢 Safe Calculator")

try:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        raise ValueError("Invalid operator")

    print("Result:", result)

except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero!")

except ValueError as e:
    print("❌ Error:", e)

except Exception:
    print("❌ Something went wrong!")