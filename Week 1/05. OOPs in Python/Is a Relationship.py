'''
An "is-a" relationship is a type of relationship between classes that indicates inheritance. It is also known as a "subclass" relationship.

An "is-a" relationship means that a derived class is a type of its base class. For example, if we have a Dog class that inherits from an Animal class, we can say that "a dog is an animal". This means that a Dog object can be treated as an Animal object, and can be used in any context where an Animal object is expected.
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


animal = Animal("Bob")
print(animal.name)
animal = dog
print(animal.name)
print(animal.speak())
