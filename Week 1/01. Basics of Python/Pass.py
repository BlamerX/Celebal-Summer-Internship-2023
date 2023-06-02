'''
Example code to demonstrate the use of pass statement

The pass statement is used as a placeholder when a statement is required syntactically but no code needs to be executed It is often used as a placeholder for code that has not been implemented yet
'''

# we define a function that does nothing using the pass statement


def do_nothing():
    pass


# The pass statement can also be used as a placeholder inside loops or conditional statements

# we use the pass statement to skip over an empty block of code
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)
