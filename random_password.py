# Easy Random Password Generator

import random
import string

def generate_password(length=8):
    # All possible characters: letters + digits + symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Pick random characters for the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# ---------------- RUN ----------------
print("Random Password Generator")
length = int(input("Enter password length: "))
print("Your password is:", generate_password(length))
