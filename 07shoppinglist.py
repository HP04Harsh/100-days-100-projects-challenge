shopping_list = []

while True:

    item = input("Add item (or type 'done'): ")

    if item.lower() == "done":
        break

    shopping_list.append(item)

print("\n🛒 Your Shopping List:")

for item in shopping_list:
    print("-", item)