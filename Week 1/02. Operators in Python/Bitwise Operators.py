'''
Bitwise Operators: Bitwise operators are used to perform bitwise operations on binary numbers. Python supports the following bitwise operators:

* Bitwise AND (&): Returns 1 if both bits are 1.

* Bitwise OR (|): Returns 1 if at least one of the bits is 1.

* Bitwise XOR (^): Returns 1 if the bits are different.

* Bitwise NOT (~): Inverts all the bits.

* Left Shift (<<): Shifts the bits to the left by the specified number of positions.

* Right Shift (>>): Shifts the bits to the right by the specified number of positions.
'''

a = 60    # 0011 1100
b = 13    # 0000 1101

print(a & b)   # Output: 12 (0000 1100)
print(a | b)   # Output: 61 (1 1101)
print(a ^ b)   # Output: 49 (001 0001)
print(~a)      # Output: -61 (1100 0011)
print(a << 2)  # Output: 240 (1111 0000)
print(a >> 2)  # Output: 15 (0000 1111)
