# This program is to display a table of Celsius temperatures 0 through a numberentered by the user and their Fahrenheit equivalents.

# Author: Linhan Cai

# Collect data from the user.
numtemps = int(input('Enter the degree of celsius temperatures to display: '))


# Calculate the values and display them.
print('Celsius\tFahrenheit')
for celsius in range(0, numtemps + 1):
    fahrenheit  = 9 / 5 * celsius + 32
    print(celsius, '\t', format(fahrenheit, '.1f'))
