# Determine exam result using nested ifs and elifs
maths = float(input("Enter marks in Math (0-100): "))
science = float(input("Enter marks in Science (0-100): "))
english = float(input("Enter marks in English (0-100): "))
# quick validation
if not (0 <= maths <= 100 and 0 <= science <= 100 and 0 <= english <= 100):
    print("One or more marks invalid")
else:
    # if any subject less than passing mark
    if maths < 33 or science < 33 or english < 33:
        print("Result: Fail (one or more subjects below passing)")
    else:
        total = maths + science + english
        percent = total / 3
        if percent >= 75:
            print("Result: A grade")
        elif percent >= 60:
            print("Result: B grade")
        elif percent >= 50:
            print("Result: C grade")
        else:
            print("Result: Pass")
