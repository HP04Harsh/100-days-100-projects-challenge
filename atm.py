class ATM:
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.__pin = pin  # private

    def check_pin(self, entered_pin):
        return entered_pin == self.__pin

    def check_balance(self):
        print(f"Balance: ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining: ₹{self.balance}")


# 🔹 Simple UI
user = ATM("Harsh", 10000, 1234)

pin = int(input("Enter PIN: "))

if user.check_pin(pin):
    while True:
        print("\n1. Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            user.check_balance()

        elif choice == "2":
            amt = int(input("Enter amount: "))
            user.deposit(amt)

        elif choice == "3":
            amt = int(input("Enter amount: "))
            user.withdraw(amt)

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice")
else:
    print("Wrong PIN!")