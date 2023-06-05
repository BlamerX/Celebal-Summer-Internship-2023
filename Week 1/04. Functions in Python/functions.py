'''
A function is a block of code that performs a specific task. It takes input, processes it, and produces output. Functions help break our program into smaller and modular chunks. As a result, the code becomes more organized, efficient, and reusable.

There are two types of functions in Python:

* Built-in functions: These functions are already defined in Python. Examples include print(), len(), range(), etc.

* User-defined functions: These functions are defined by the user to perform a specific task.
'''

# Method 1


def add_numbers(x, y):
    sum = x + y
    return sum


result = add_numbers(5, 7)
print(result)


# Method 2
def multiply(x, y): return x * y


result = multiply(3, 4)
print(result)
