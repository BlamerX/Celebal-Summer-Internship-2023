'''
Assignment Operators: Assignment operators are used to assign values to variables. Python supports the following assignment operators:

* Assignment (=): Assigns the value of the right-hand operand to the left-hand operand.

* Addition assignment (+=): Adds the value of the right-hand operand to the left-hand operand and assigns the result to the left-hand operand.

* Subtraction assignment (-=): Subtracts the value of the right-hand operand from the left-hand operand and assigns the result to the left-hand operand.

* Multiplication assignment (*=): Multiplies the left-hand operand by the value of the right-hand operand and assigns the result to the left-hand operand.

* Division assignment (/=): Divides the left-hand operand by the value of the right-hand operand and assigns the result to the left-hand operand.

* Modulus assignment (%=): Calculates the modulus of the left-hand operand and the right-hand operand and assigns the result to the left-hand operand.

* Exponentiation assignment (**=): Raises the left-hand operand to the power of the right-hand operand and assigns the result to the left-hand operand.

* Floor division assignment (//=): Calculates the floor division of the left-hand operand and the right-hand operand and assigns the result to the left-hand operand.
'''

a = 10

a += 5   # Equivalent to a = a + 5
print(a)  # Output: 15

a -= 3   # Equivalent to a = a - 3
print(a)  # Output: 12

a *= 2   # Equivalent to a = a * 2
print(a)  # Output: 24

a /= 3   # Equivalent to a = a / 3
print(a)  # Output: 8.0

a %= 5   # Equivalent to a = a % 5
print(a)  # Output: 3.0

a **= 2  # Equivalent to a = a ** 2
print(a)  # Output: 9.0

a //= 2  # Equivalent to a = a // 2
print(a)  # Output: 4.0
