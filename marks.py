# Validate marks and show message
marks = float(input("Enter marks (0-100): "))
if 0 <= marks <= 100:
    print("Marks are valid:", marks)
else:
    print("Invalid marks entered.")
