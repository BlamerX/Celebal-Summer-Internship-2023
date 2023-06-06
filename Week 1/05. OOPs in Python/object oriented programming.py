'''
Object-oriented programming is a programming paradigm that uses objects to represent and manipulate data. In Python, everything is an object, and you can create your own objects by defining classes. A class is a blueprint for creating objects, and it defines the attributes and methods that the objects will have.
'''

# Example 1


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person = Person("Adarsh", 22)
person.say_hello()


# Example 2
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2

    @classmethod
    def set_pi(cls, pi):
        cls.pi = pi


print(Circle(5).area())
