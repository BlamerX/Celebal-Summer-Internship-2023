"""
Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }
"""

# Create a set of unique numbers
numbers = {1, 2, 3, 4, 5}

print(numbers)

# Add a new number to the set
numbers.add(6)

# Remove a number from the set
numbers.remove(3)

print(numbers)

# Check if a number is in the set
if 4 in numbers:
    print("4 is in the set")
else:
    print("4 is not in the set")

# Iterate over the set and print out each number
for number in numbers:
    print(number)

b = frozenset({4, 5})  # frozenset
print(type(b))  # Output: <class 'frozenset'>
