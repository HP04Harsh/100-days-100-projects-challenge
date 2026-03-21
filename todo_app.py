import json

task = input("Enter task: ")

try:
    with open("todo.json", "r") as f:
        data = json.load(f)
except:
    data = []

data.append(task)

with open("todo.json", "w") as f:
    json.dump(data, f)

print("Task added!")