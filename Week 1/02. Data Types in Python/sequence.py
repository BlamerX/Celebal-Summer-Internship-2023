"""
list and tuple fall under the Python Sequential DataType
these are data types that holds items

List - List is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ].

Tuple - Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.In Python, we use the parentheses () to store items of a tuple.
"""

# List Example
languages = ["Swift", "Java", "Python"]

# access element at index 2
print(languages[2])

# Tuiple Example
product = ('Microsoft', 'Xbox', 499.99)

# access element at index 1
print(product[1])   # Xbox


# example of how a list and tuple can be used together in Python.
students = [("John", 22), ("Jane", 21), ("Bob", 23)]

for name, age in students:
    print(name + " is " + str(age) + " years old.")
