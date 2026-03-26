# Secure User Profile App
# Concept: Encapsulation (hiding sensitive data like password)

class User:
    def __init__(self, username, password, age):
        # public variable (anyone can access)
        self.username = username
        
        # private variables (encapsulation - should not be accessed directly)
        self.__password = password
        self.__age = age

    # method to safely view profile
    def view_profile(self):
        print("\n--- User Profile ---")
        print("Username:", self.username)
        
        # we never show real password 🙂
        print("Password:", "*" * len(self.__password))
        print("Age:", self.__age)

    # method to change password (controlled access)
    def change_password(self):
        old_pass = input("Enter current password: ")
        
        # check before allowing change
        if old_pass == self.__password:
            new_pass = input("Enter new password (min 6 chars): ")
            
            if len(new_pass) >= 6:
                self.__password = new_pass
                print("✅ Password updated successfully!")
            else:
                print("❌ Password too short!")
        else:
            print("❌ Wrong current password!")

    # method to change age (with validation)
    def change_age(self):
        try:
            new_age = int(input("Enter new age: "))
            
            if new_age > 0:
                self.__age = new_age
                print("✅ Age updated!")
            else:
                print("❌ Invalid age!")
        except:
            print("❌ Please enter a valid number!")


# ---- Main Program ----

print("=== Welcome to Secure Profile App ===")

# creating a user (you can change values here)
user = User("harsh123", "mypassword", 22)

while True:
    print("\nWhat do you want to do?")
    print("1. View Profile")
    print("2. Change Password")
    print("3. Change Age")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user.view_profile()

    elif choice == "2":
        user.change_password()

    elif choice == "3":
        user.change_age()

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid option, try again!")