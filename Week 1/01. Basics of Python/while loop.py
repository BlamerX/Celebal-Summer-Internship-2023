'''
While Loops in Python

While loops are used to repeatedly execute a block of code as long as a certain condition is true.
In Python, you can use a while loop to iterate over a sequence of values until a certain condition is met.
'''

# Example of using a while loop with a counter
count = 0
while count < 5:
    print(count)
    count += 1


# Example of using a while loop with a boolean condition
is_running = True
while is_running:
    user_input = input("Enter a command: ")
    if user_input == "quit":
        is_running = False
    else:
        print("Executing command:", user_input)
