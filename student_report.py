import csv

students = [
    ["Name", "Marks"],
    ["Harsh", 85],
    ["Amit", 78]
]

with open("report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV created!")