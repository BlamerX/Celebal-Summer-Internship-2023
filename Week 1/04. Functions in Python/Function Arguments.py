'''
a function argument is a value that is passed to a function when it is called.
'''

# There are four types of function arguments in Python:

# 1. Positional Arguments: These are the most common type of arguments. They are passed to a function in the order they are defined in the function.


def greet(name, message):
    print(f"{message}, {name}!")


greet("Adarsh", "Hello")  # Output: Hello, Adarsh!

# 2. Keyword Arguments: These are arguments that are passed to a function with a keyword and a value. They are useful when you want to skip some arguments or pass them in a different order.


def greet(name, message):
    print(f"{message}, {name}!")


greet(message="Hello", name="Blamer")  # Output: Hello, Blamer!

# 3. Default Arguments: These are arguments that have a default value assigned to them. If the argument is not passed to the function, the default value is used.


def greet(name, message="Hello"):
    print(f"{message}, {name}!")


greet("X")  # Output: Hello, X!

# 4. Variable-length Arguments: These are arguments that allow you to pass any number of arguments to a function. There are two types of variable-length arguments: *args and **kwargs.


def greet(*names):
    for name in names:
        print(f"Hello, {name}!")


# Output: Hello, Adarsh! Hello, Jane! Hello, Blamerx!
greet("Adarsh", "X", "Blamerx")
