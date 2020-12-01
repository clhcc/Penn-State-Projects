# This program is to read numbers and calculate different values of the numbers.

# Author: Linhan Cai

# Import the file, remove the \n character.
with open('/Users/cailinhan/Downloads/Second Semester/CMPSC 131/Assignments/Assignment #6/random.txt', 'r') as file:
    num_list = file.read().splitlines()

# Convert the list to numbers instead of string, calculate the sum of the numbers and the average of the numbers.
real_nums = list(map(int, num_list))
total = sum(real_nums)
count = 0
for i in num_list:
    count += 1
average = total / count

# Print out the result.
file = open('/Users/cailinhan/Downloads/Second Semester/CMPSC 131/Assignments/Assignment #6/random.txt', 'r')
print('The following numbers were read from the random.txt file:' + '\n' + file.read(), end='')
file.close()
print('The lowest number in the list is:', min(real_nums))
print('The highest number in the list is:', max(real_nums))
print('The total of the numbers is:', total)
print('The average of the numbers in the list is:', format(average, '.1f' ))
