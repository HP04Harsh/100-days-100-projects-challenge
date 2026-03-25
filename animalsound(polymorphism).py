# Base class (Parent class)
class Animal:
    def sound(self):
        # This method will be overridden by child classes
        print("Animal makes a sound")


# Child class 1
class Dog(Animal):
    def sound(self):
        # Overriding the parent method
        print("Dog barks 🐶")


# Child class 2
class Cat(Animal):
    def sound(self):
        # Overriding the parent method
        print("Cat meows 🐱")


# Child class 3
class Cow(Animal):
    def sound(self):
        # Overriding the parent method
        print("Cow moos 🐄")


# Function to demonstrate polymorphism
def make_sound(animal):
    # Same function works for different objects
    animal.sound()


# Creating objects
dog = Dog()
cat = Cat()
cow = Cow()

# Using polymorphism
make_sound(dog)
make_sound(cat)
make_sound(cow)