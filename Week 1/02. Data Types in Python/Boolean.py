"""
A boolean is a data type in programming that represents a logical value. It can only have one of two possible values: True or False. In some programming languages, True is represented by the integer value 1 and False is represented by the integer value 0.
"""

# Define two boolean variables
is_raining = True
is_sunny = False

# Use boolean operators to combine the variables
if is_raining and not is_sunny:
    print("It's raining but not sunny")
elif not is_raining and is_sunny:
    print("It's sunny but not raining")
elif is_raining and is_sunny:
    print("It's both raining and sunny")
else:
    print("It's neither raining nor sunny")
