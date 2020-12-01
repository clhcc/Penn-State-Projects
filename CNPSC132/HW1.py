#HW #1
#Due Date: 09/20/2019, 11:59PM 
########################################
#                                      
# Name: Linhan Cai
# Collaboration Statement: None      
#
########################################



def isPower(x, y):
    """
        >>> isPower(4, 64)
        3
        >>> isPower(5, 81)
        -1
        >>> isPower(7, 16807)
        5
    """
    # --- YOU CODE STARTS HERE
    
    # Set the initial value for power
    power = 0
    
    # y is not the power of x
    if y % x != 0:
        return -1
    # Count the power by dividing the y until it can't be divided.
    while y % x == 0:
        y = y / x
        power += 1

    return power



def translate(translation, txt):
    """
        >>> myDict = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1': 'one'} 
        >>> text = 'Up down left Right forward 1 time' 
        >>> translate(myDict, text) 
        'down up right left forward one time'
    """
    # --- YOU CODE STARTS HERE

    # Convert txt into all lowercase letters
    txt = txt.lower()

    # Split txt into list by whitespaces
    txtlist = txt.split(' ')

    # Loop through the dictionary
    for i in range(len(txtlist)):
        # For every element in the txtlist, replace it with the value and also keep the original value of the ones that were not mentioned
        if txtlist[i] in translation:
            txtlist[i] = translation[txtlist[i]]
            
        # Turn the list into a string
        txt = ' '.join(txtlist)

    return(txt)



def onlyTwo(x, y, z):
    """
        >>> onlyTwo(1, 2, 3)
        13
        >>> onlyTwo(3, 3, 2)
        18
        >>> onlyTwo(5, 5, 5)
        50
    """
    # --- YOU CODE STARTS HERE

    # Create an empty list to hold the three numbers
    List = []

    # Append all the numbers to the list.
    List.append(x)
    List.append(y)
    List.append(z)

    # Find the maximum number in the list
    big1 = max(List)

    # Remove the biggest number and find the second large number
    List.remove(big1)
    big2 = max(List)

    # Get the result
    res = big1 ** 2 + big2 ** 2
    return res



def largeFactor(num):
    """
        >>> largeFactor(15) 
        5
        >>> largeFactor(24)
        12
        >>> largeFactor(7)
        1
    """
    # --- YOU CODE STARTS HERE

    # Create an variable that would hold the maximum factor.
    factor = 0

    # Loop the number to find the factor
    for i in range(1, num):
        # when the number can divide the num
        if num % i == 0:
            factor = i
    return factor



def hailstone(num):
    """
        >>> hailstone(5)
        [5, 16, 8, 4, 2, 1]
        >>> hailstone(6)
        [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    # --- YOU CODE STARTS HERE

    # Create an empty list to hold the numbers
    List = []

    # While num is not 1
    while num != 1:
        List.append(num)
        # when the number is even
        if num % 2 == 0:
            num = num // 2
        # when the number is odd
        else:
            num = 3 * num + 1
            
    # Append all the numbers to the list
    List.append(num)
    
    return List
