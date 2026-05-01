import datetime
import re

# 1. Configuration: Set your start date here (Year, Month, Day)
START_DATE = datetime.date(2026, 5, 1) 
today = datetime.date.today()

# 2. Calculate Progress
day_count = (today - START_DATE).days + 1
if day_count > 100: day_count = 100
if day_count < 1: day_count = 1

# 3. Read README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 4. Update Placeholders using Regex
content = re.sub(r".*?", f"{day_count}", content)
content = re.sub(r".*?", f"{day_count}", content)
content = re.sub(r"progress/\d+", f"progress/{day_count}", content) # Updates the progress bar image
content = re.sub(r".*?", f"{today.strftime('%B %d, %Y')}", content)

# 5. Save changes
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ README updated to Day {day_count}")
