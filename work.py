# Simple age check for work eligibility
age = int(input("Enter your age: "))
if age >= 18 and age <= 60:
    print("You are of working age.")
elif age < 18:
    print("You are too young for work.")
else:
    print("You may be retired or beyond typical working age.")
