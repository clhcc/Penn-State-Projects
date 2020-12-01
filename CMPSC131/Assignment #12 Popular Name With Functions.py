# This program is to rewrite the popular name function to make it simpler with functions.

# Author: Linhan Cai

# Define functions.
def get_names_list(filename):
    with open(filename, 'r') as file:
        name_list = file.read().splitlines()
    return name_list

def check_name(name, name_list):
    rank = 0
    for i in range(0, len(name_list)):
        if name_list[i] == name:
            rank = i + 1
            break
    return rank

# Set the lists.
boy_list = get_names_list('BoyNames.txt')
girl_list = get_names_list('GirlNames.txt')

# Write the loop.
print('Enter a name to see if it is a popular girls or boys name.', '\n')
name = input('Enter a name to check, or "stop" to stop: ')
while name != 'stop':
    boy_rank = check_name(name, boy_list)
    girl_rank = check_name(name, girl_list)
    if boy_rank != 0 and girl_rank != 0:
        print(name, 'is a popular boys name and is ranked:', boy_rank)
        print(name, 'is a popular girls name and is ranked:', girl_rank, '\n')
        name = input('Enter a name to check, or "stop" to stop: ')
    elif boy_rank != 0:
        print(name, 'is a popular boys name and is ranked:', boy_rank)
        print(name, 'is not a popular girls name.', '\n')
        name = input('Enter a name to check, or "stop" to stop: ')
    elif girl_rank != 0:
        print(name, 'is a popular girls name and is ranked:', girl_rank)
        print(name, 'is not a popular boys name.', '\n')
        name = input('Enter a name to check, or "stop" to stop: ')
    else:
        print(name, 'is not a popular boys name.')
        print(name, 'is not a popular girls name.', '\n')
        name = input('Enter a name to check, or "stop" to stop: ')



