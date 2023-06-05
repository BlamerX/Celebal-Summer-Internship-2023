'''
Special Operators: Python also supports some special operators, including:

* Identity Operators: is and is not are used to compare the memory locations of two objects.

* Membership Operators: in and not in are used to check if a value is present in a sequence.
'''

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)    # Output: True
print(a is not c)  # Output: True
print(2 in b)     # Output: True
print(4 not in a)  # Output: True
