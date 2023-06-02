'''
break and continue in Python.

break and continue are two control flow statements in Python that allow you to alter the normal flow of a loop.

break is used to exit a loop prematurely. When break is encountered inside a loop, the loop is immediately terminated and the program continues executing from the next statement after the loop.

continue is used to skip over the current iteration of a loop and move on to the next iteration. When continue is encountered inside a loop, the current iteration is immediately terminated and the loop moves on to the next iteration.
'''

# Example of using break and continue in a loop
for i in range(1, 11):
    if i == 5:
        # Skip over the number 5
        continue
    elif i == 8:
        # Exit the loop when we reach 8
        break
    else:
        print(i)

# Write a program that prompts the user to enter a sequence of numbers. The program should print out the sum of all the even numbers in the sequence, but should stop adding numbers as soon as the sum exceeds 100.

numbers = input("Enter a sequence of numbers: ")

# Split the input string into a list of numbers
numbers_list = numbers.split()

# Initialize the sum and count variables
total = 0
count = 0

# Loop over the numbers in the list
for num in numbers_list:
    num = int(num)
    if num % 2 == 0:
        total += num
        if total > 100:
            break
        count += 1

# Print the sum and count
print("Sum of even numbers:", total)
print("Number of even numbers added:", count)
