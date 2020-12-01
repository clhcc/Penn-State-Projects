# This program calculates the BMI for a person and displays the weight situation.

# Author: Linhan Cai

# Collect the data from the user.
height = float(input('Please enter your height in inches: '))
weight = float(input('Please enter your weight in pounds: '))

# Calculate the BMI.
BMI = weight * 703 / height ** 2

# Display the result.
print('Your BMI is: ', format(BMI, '.1f'))
if BMI < 18.5:
    print('Your BMI indicates that you are underweight.')
elif BMI >= 18.5 and BMI <= 25:
    print('Your BMI indicates that you are optimal weight.')
else:
    print('Your BMI indicates that you are overweight.')

