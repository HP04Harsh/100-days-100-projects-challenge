# Simple gender check from input
g = input("Enter gender (M/F or male/female): ").strip().lower()
if g in ("m", "male"):
    print("Gender: Male")
elif g in ("f", "female"):
    print("Gender: Female")
else:
    print("Gender input not recognized")
