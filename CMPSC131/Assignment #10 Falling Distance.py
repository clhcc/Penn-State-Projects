# This program is to calculate the distance an object would fall in an amount of time period.

# Author: Linhan Cai

# Set the initial values and display the beginning lines.
gravity = 9.8
print("This program tells you far an object will fall in a number of seconds.")
t = int(input("Enter the falling time in seconds: "))

# Write the distance function.
def falling_distance(time):
    distance = 1/2 * gravity * time ** 2
    print("The distance the object will fall in ", time," seconds, is: ", format(distance, '.1f')," meters.", end='\n\n')
    

# Use the written function to write a while loop.
while t >= 0:
    falling_distance(t)
    t = int(input("Enter the falling time in seconds: "))

