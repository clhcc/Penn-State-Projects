# This program is to o modify Programming Assignment 4 Grade Average to make it robust.

# Author: Linhan Cai

# Set the initial values.
sum = 0
count = 0

# Define the function.
def calculate_average(sum, count):
    try:
        if sum == 0 and count == 0:
            raise ZeroDivisionError
        else:
            avg = sum / count
            print('The sum of the numbers is', format(sum, '.1f' ))
            print('The average of the numbers is', format(avg, '.1f'))
    except ZeroDivisionError: 
        print('You did not enter any numbers to average.')

# Write the while loop.
n = int(input('Enter a positive number to total or a negative number to calculate average : '))
while n >= 0:
    try:
        sum = sum + n
        count += 1
        n = int(input('Enter a positive number to total or a negative number to calculate average : '))
    except ValueError:
        print('What you entered was not a valid number. Try again.')
        n = int(input('Enter a positive number to total or a negative number to calculate average : '))
else:
    calculate_average(sum, count)
