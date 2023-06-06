# Hierarchical inheritance: In hierarchical inheritance, multiple derived classes inherit from a single base class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog("Fido")
cat = Cat("Whiskers")
print(dog.name)
print(dog.speak())
print(cat.name)
print(cat.speak())
