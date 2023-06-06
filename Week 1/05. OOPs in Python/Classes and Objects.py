'''
A class is a blueprint for creating objects. It defines the attributes and methods that the objects will have. An object is an instance of a class. When you create an object, you are creating a specific instance of the class, with its own set of attributes and methods.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


'''
An object is an instance of a class. It is a self-contained entity that consists of both data and behavior.
'''

person = Person("Adarsh", 22)
person.say_hello()
