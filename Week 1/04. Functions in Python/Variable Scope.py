'''
variable scope refers to the region of a program where a variable is accessible. There are three types of variable scopes in Python: local, global, nonlocal.
'''

# A local variable is a variable that is defined within a function. It can only be accessed within that function and is not accessible outside of it.


def my_function():
    x = 10
    print(x)


my_function()  # Output: 10
# print(x)  # Output: NameError: name 'x' is not defined


# A global variable, on the other hand, is a variable that is defined outside of any function. It can be accessed from anywhere within the program, including inside functions.
y = 10


def my_function():
    print(y)


my_function()  # Output: 10
print(y)  # Output: 10

# A nonlocal variable is a variable that is defined in the enclosing function of a nested function. It can be accessed from within the nested function but not from outside of it.


def outer_function():
    z = "outer"

    def inner_function():
        nonlocal z
        z = "inner"
        print(z)

    inner_function()
    print(z)


outer_function()  # Output: inner, inner
