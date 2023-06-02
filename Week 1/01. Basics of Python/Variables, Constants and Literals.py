'''
Variables, Constants, and Literals in Python

Variables are used to values that can change during the execution of a program.
In Python, you can create a variable by assigning a value to a name using the = operator.
The value of a variable can be changed by assigning a new value to the same name.
'''

# Example of creating and using a variable
x = 5
y = 3
z = x + y
print(z)  # Output: 8

'''
Constants are values that do not change during the execution of a program.
In Python, you can create a constant by using all capital letters for the name of the variable.
While Python does not have a built-in constant type, it is a convention to use all capital letters
to indicate that a variable should not be changed.
'''

# Example of creating and using a constant
TAX_RATE = 0.08
price = 10.0
tax = price * TAX_RATE
total = price + tax
print(total)  # Output: 10.8

'''
Literals are values that are directly written in the code.
In Python, literals can be numbers, strings, or boolean values.
'''

# Example of using literals
number = 42
string = "Hello, world!"
is_true = True
is_false = False
