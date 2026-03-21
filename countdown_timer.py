from datetime import datetime

date_str = input("Enter date (YYYY-MM-DD): ")
event_date = datetime.strptime(date_str, "%Y-%m-%d")

today = datetime.now()
days_left = (event_date - today).days

print(f"Days left: {days_left}")