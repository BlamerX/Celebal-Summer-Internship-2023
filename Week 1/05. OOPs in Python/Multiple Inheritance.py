# Multiple inheritance: In multiple inheritance, a derived class inherits from multiple base classes. This allows the derived class to combine the functionality of multiple classes.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Mammal:
    def __init__(self, age):
        self.age = age

    def run(self):
        pass


class Dog(Animal, Mammal):
    def speak(self):
        return "Woof!"


dog = Dog("Fido", 2)
print(dog.name)
print(dog.age)
print(dog.speak())
dog.run()
