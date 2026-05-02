# Map number to weekday name (1-7)
num = int(input("Enter weekday number (1-7): "))
days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
print(days.get(num, "Invalid weekday number"))
