name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

birth_year = 2026 - age

print("\n------ USER PROFILE ------")
print(f"Hello {name} 👋")
print(f"You live in {city}")
print(f"You are {age} years old")
print(f"Your approximate birth year is {birth_year}")