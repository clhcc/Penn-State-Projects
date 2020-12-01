# This program is to see if a name is popular for boys/girls.

# Author: Linhan Cai

# Read the files and set up the lists.
file1 = open('BoyNames.txt', 'r')
file2 = open('GirlNames.txt', 'r')
boy_list = file1.read().splitlines()
girl_list = file2.read().splitlines()
file1.close()
file2.close()

# Writhe the while loop.
print('Enter a name to see if it is a popular girls or boys name.', '\n')
name = input('Enter a name to check, or "stop" to stop: ')
while name != 'stop':
    if name in boy_list and name in girl_list:
        print(name, 'is a popular boys name and is ranked:', boy_list.index(name)+1)
        print(name, 'is a popular girls name and is ranked:', girl_list.index(name)+1, '\n')
        name = input('Enter a name to check, or "stop" to stop: ')
    elif name in boy_list:
        print(name, 'is a popular boys name and is ranked:', boy_list.index(name)+1)
        print(name, 'is not a popular girls name.', '\n')
        name = input('Enter a name to check, or "stop" to stop: ')
    elif name in girl_list:
        print(name, 'is a popular girls name and is ranked:', girl_list.index(name)+1)
        print(name, 'is not a popular boys name.', '\n')
        name = input('Enter a name to check, or "stop" to stop: ')
    else:
        print(name, 'is not a popular boys name.')
        print(name, 'is not a popular girls name.', '\n')
        name = input('Enter a name to check, or "stop" to stop: ')
