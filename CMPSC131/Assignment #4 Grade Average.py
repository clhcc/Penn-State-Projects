# This program calculates the average of grades which the user entered.

# Author: Linhan Cai

# Set initial values.
grade = 0
count = 0
enter_grade = int(input('Enter a test score. To get the average enter "-1": '))

# Collect data from the user. Set the while loop.
while enter_grade != -1:
    if enter_grade < 0:
        enter_grade = int(input('Please enter a positive number: '))
    else:
        grade = grade + enter_grade
        count += 1
        enter_grade = int(input('Enter a test score. To get the average enter "-1": '))
else:
    average_grade = grade / count
    print('The average for all the grades is:', format(average_grade, '.1f'))
