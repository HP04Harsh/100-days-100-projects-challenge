# Calculate discounted bill amount
bill = float(input("Enter bill amount: "))
discount_percent = float(input("Enter discount percent (e.g., 10 for 10%): "))
if discount_percent < 0:
    print("Invalid discount")
else:
    discount = bill * (discount_percent / 100)
    final = bill - discount
    print(f"Discount: {discount}")
    print(f"Final bill after discount: {final}")
