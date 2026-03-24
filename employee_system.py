# Employee Management System using Inheritance

# Parent Class
class Employee:
    def __init__(self, name, salary):
        # Constructor for base class
        self.name = name
        self.salary = salary

    def display_info(self):
        # Method to display employee details
        print(f"Name: {self.name}, Salary: {self.salary}")


# Child Class (inherits Employee)
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Calling parent constructor using super()
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        # Method overriding (polymorphism)
        print(f"Manager Name: {self.name}, Salary: {self.salary}, Department: {self.department}")


# Another Child Class
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print(f"Developer Name: {self.name}, Salary: {self.salary}, Language: {self.programming_language}")


# Creating objects
emp1 = Employee("Harsh", 30000)
mgr1 = Manager("Amit", 60000, "HR")
dev1 = Developer("Ravi", 50000, "Python")

# Calling methods
emp1.display_info()
mgr1.display_info()
dev1.display_info()