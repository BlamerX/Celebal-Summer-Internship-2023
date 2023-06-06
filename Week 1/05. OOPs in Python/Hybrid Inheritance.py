# Hybrid inheritance: Hybrid inheritance is a combination of multiple inheritance and hierarchical inheritance. It allows for complex class hierarchies and can be difficult to manage.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def run(self):
        pass


class Dog(Mammal):
    def speak(self):
        return "Woof!"


class Cat(Mammal):
    def speak(self):
        return "Meow!"


class Bulldog(Dog):
    def speak(self):
        return "Bark!"


dog = Dog("Fido", 2)
cat = Cat("Whiskers", 3)
bulldog = Bulldog("Spike", 4)
print(dog.name)
print(dog.age)
print(dog.speak())
dog.run()
print(cat.name)
print(cat.age)
print(cat.speak())
cat.run()
print(bulldog.name)
print(bulldog.age)
print(bulldog.speak())
bulldog.run()
