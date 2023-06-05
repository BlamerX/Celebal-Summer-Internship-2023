"""
Integers, floating-point numbers and complex numbers fall under Python numbers category. They are defined as int, float and complex classes in Python.

* int - holds signed integers of non-limited length.

* float - holds floating decimal points and it's accurate up to 15 decimal places.

* complex - holds complex numbers.
"""

# We can use the type() function to know which class a variable or a value belongs to.

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))


# Write a program to get the roots of a quadratic equation

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

d = (b**2) - (4*a*c)

if d >= 0:
    root1 = (-b + (d**0.5)) / (2*a)
    root2 = (-b - (d**0.5)) / (2*a)
else:
    real_part = -b / (2*a)
    imag_part = ((-d)**0.5) / (2*a)
    root1 = complex(real_part, imag_part)
    root2 = complex(real_part, -imag_part)

# Print the roots
print("Root 1:", root1)
print("Root 2: ", root2)
