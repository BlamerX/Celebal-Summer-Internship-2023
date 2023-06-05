'''
Recursion is a technique in programming where a function calls itself repeatedly until a certain condition is met. This can be a powerful for solving problems that can be broken down into smaller sub-problems.
'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
