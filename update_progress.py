import datetime
import re

# 1. Configuration
START_DATE = datetime.date(2026, 5, 1) 
today = datetime.date.today()

# 2. Calculate Progress
day_count = (today - START_DATE).days + 1
if day_count > 100: day_count = 100
if day_count < 1: day_count = 1

# 3. Read README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 4. Update Placeholders
# This looks for CurrentValueand replaces only the CurrentValue
content = re.sub(r"().*?()", r"\1" + str(day_count) + r"\2", content)
content = re.sub(r"().*?()", r"\1" + str(day_count) + r"\2", content)
content = re.sub(r"().*?()", r"\1" + today.strftime('%B %d, %Y') + r"\2", content)

# 5. Update the Progress Bar Image URL
content = re.sub(r"progress/\d+", f"progress/{day_count}", content)

# 6. Save changes
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated README to Day {day_count}")
