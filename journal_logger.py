entry = input("Write your journal: ")

with open("journal.txt", "a") as file:
    file.write(entry + "\n")

print("Saved!")