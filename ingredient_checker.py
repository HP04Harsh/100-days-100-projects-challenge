# ingredient_checker.py

# Recipe ingredients (tuple - fixed)
recipe = ("tomato", "onion", "salt", "oil", "chili")

# Convert recipe tuple to set
recipe_set = set(recipe)

# User ingredients input
user_input = input("Enter ingredients you have (comma separated): ")

# Convert input to set
user_ingredients = set(user_input.lower().split(","))

# Check missing ingredients
missing = recipe_set - user_ingredients

print("\nRecipe Ingredients:", recipe_set)
print("Your Ingredients:", user_ingredients)

if missing:
    print("Missing Ingredients:", missing)
else:
    print("You have all ingredients! You can cook the dish.")