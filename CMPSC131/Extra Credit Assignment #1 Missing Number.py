# This program is to let the user enter a range of numbers and tell the user which number is missing.

# Author: Linhan Cai

# Set the initial values.
n = int(input('Enter n: '))
num = 0
total = 0

# Write the for loop.
for i in range(n-1):
    num += int(input('Please enter a unique number between 1 and ' + str(n) + ': '))
for j in range(1, n+1):
    total += j
m = total - num
print('The missing number is:', m)
