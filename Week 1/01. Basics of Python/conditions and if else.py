"""
Python supports the usual logical conditions from mathematics:

* Equals: a == b

* Not Equals: a != b

* Less than: a < b

* Less than or equal to: a <= b

* Greater than: a > b

* Greater than or equal to: a >= b
"""

# Check weather a number is Greater, Equal or Smaller
num1 = 6
num2 = 56

if num1 > num2:
    print(f"{num1} is GREATER than {num2}")
elif num1 == num2:
    print("Both the Numbers are EQUAL")
else:
    print(f"{num1} is SMALLER than {num2}")


# Check if a nuumber is Present in a List
list1 = [15, 7, 3]
if 5 in list1:
    print("Yes")
else:
    print("No")
