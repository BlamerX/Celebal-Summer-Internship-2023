# Single inheritance: In single inheritance, a derived class inherits from a single base class . This is the most common type of inheritance.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


dog = Dog("Fido")
print(dog.name)
print(dog.speak())
