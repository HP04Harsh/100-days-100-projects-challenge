# notes_app.py

filename = "notes.txt"

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        note = input("Write your note: ")

        with open(filename, "a") as file:
            file.write(note + "\n")

        print("Note saved!")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                print("\nYour Notes:")
                print(file.read())
        except FileNotFoundError:
            print("No notes found!")

    elif choice == "3":
        print("Exiting app...")
        break

    else:
        print("Invalid choice!")
        