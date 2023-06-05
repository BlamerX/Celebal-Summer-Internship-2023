"""
Dictionary

Python dictionary is an ordered collection of items. It stores elements in key/value pairs.

Here, keys are unique identifiers that are associated with each value.
"""


students = {
    'John': 'A',
    'Jane': 'B',
    'Bob': 'C'
}

# Display the dictionary
print(students)

# Write a Python program to calculate the total cost of a shopping cart using a dictionary of prices for different items and a dictionary of quantities for each item in the cart.

prices = {
    'apple': 0.5,
    'banana': 0.25,
    'orange': 0.75,
    'pear': 0.4
}

cart = {
    'apple': 3,
    'banana': 2,
    'orange': 1,
    'pear': 4
}


total_cost = 0
for item, quantity in cart.items():
    total_cost += prices[item] * quantity


print("Total cost: " + str(total_cost))
