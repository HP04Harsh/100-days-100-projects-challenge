# Student Grade Manager using List Comprehensions

# Sample student data
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [60, 65, 58]},
    {"name": "Charlie", "grades": [95, 92, 88]},
    {"name": "Diana", "grades": [72, 70, 68]},
]

# 1. Calculate average grades for each student
averages = [sum(s["grades"]) / len(s["grades"]) for s in students]

# 2. Pair names with averages
student_averages = [(s["name"], sum(s["grades"]) / len(s["grades"])) for s in students]

# 3. Filter passing students (>= 70)
passing_students = [s["name"] for s in students if (sum(s["grades"]) / len(s["grades"])) >= 70]

# 4. Dictionary comprehension: map names to averages
average_dict = {s["name"]: sum(s["grades"]) / len(s["grades"]) for s in students}

# 5. Top performer
top_student = max(students, key=lambda s: sum(s["grades"]) / len(s["grades"]))
top_name = top_student["name"]
top_avg = sum(top_student["grades"]) / len(top_student["grades"])

# 6. Students with grade improvements (last grade > first grade)
improved_students = [s["name"] for s in students if s["grades"][-1] > s["grades"][0]]

# 7. Flatten all grades into one list
all_grades = [grade for s in students for grade in s["grades"]]

# 8. Overall class average
class_average = sum(all_grades) / len(all_grades)

# ---------------- OUTPUT ----------------
print("Individual Averages:", averages)
print("Student Averages:", student_averages)
print("Passing Students:", passing_students)
print("Average Dictionary:", average_dict)
print(f"Top Performer: {top_name} with {top_avg:.2f}")
print("Improved Students:", improved_students)
print("All Grades:", all_grades)
print(f"Class Average: {class_average:.2f}")
