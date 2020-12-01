# This program is to read the random numbers from the random.txt file created in Programming Assignment 6 and display several data.

# Author: Linhan Cai

# Set the initial values.
total_number = 0
count = 0
print('The following numbers were read from the random.txt file:')

# Write the loop.
myfile = open('/Users/cailinhan/Downloads/Second Semester/CMPSC 131/Assignments/Assignment #6/random.txt', 'r')

for line in myfile:
    print(line, end = '')
    total_number += int(line)
    count += 1
    
myfile.close

# Print the required data.
print('The total of the numbers is:', total_number)
print('The file contained', count, 'numbers.')
