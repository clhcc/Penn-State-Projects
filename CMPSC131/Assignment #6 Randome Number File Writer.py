# This program is to let usres put random numbers into the file 'random.txt'

# Author: Linhan Cai

# Import random.
import random

# Collect data from the user.
how_many_number = int(input('This program writes random numbers to the random.txt file. \nHow many numbers would you like to write: '))

# Write the for loop.
myfile = open('random.txt', 'w')
for i in range(how_many_number):
    random_number = random.randint(1, 500)
    myfile.write(str(random_number) + '\n')
myfile.close()
print(how_many_number, 'numbers were written to the random.txt file.')


