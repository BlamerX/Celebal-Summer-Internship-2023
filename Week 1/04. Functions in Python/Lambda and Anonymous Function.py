'''
A lambda function is a small anonymous function that can have any number of arguments, but can only have one expression. The expression is evaluated and returned as the result of the function. Lambda functions are often used as a shortcut for simple functions that are only used once.
'''

# Syntax of lambda Function
# lambda arguments: expression


# Example 1
def square(x): return x**2


print(square(5))  # Output: 25

# Example 2


def square(x): return x**2


print(square(5))  # Output: 25

# Example 3
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]
