# This program is to calculate the windchill.

# Author: Linhan Cai

# Print the headline.
print('This program calculates the windchill from the fahrenheit temperature and the wind speed.', '\n')

# Write the function to collect the user's input.
def get_input():
    temperature = int(input('Enter the fahrenheit temperature: '))
    speed = int(input('Enter the wind speed: '))
    return temperature, speed

temperature, speed = get_input()

# Write the function to calculate the windchill.
def calculate_windchill(temperature, wind_speed):
    windchill = 35.74 + 0.6215 * temperature - 35.75 * speed**0.16 + 0.4275 * temperature * speed**0.16
    print('The windchill is: ', format(windchill, '.1f'), '\n')
        
calculate_windchill(temperature, speed)

# Write the while loop.
while True:
    agree = str(input('Would you like to calculate another windchill? Enter "y" or "n": '))
    if agree == 'y':
        temperature, speed = get_input()
        calculate_windchill(temperature, speed)
    else:
        break


