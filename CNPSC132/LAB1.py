#Lab #1
#Due Date: 08/30/2019, 11:59PM
########################################
#                                      
# Name: Linhan Cai
# Collaboration Statement:  None           
#
########################################


def sumSquares(aList):
    """
        >>> sumSquares(5)
        'error'
        >>> sumSquares('5')
        'error'
        >>> sumSquares(6.15)
        'error'
        >>> sumSquares([1,5,-3,5,9,8,4])
        90
        >>> sumSquares(['3',5,-3,5,9.0,8,4,'Hello'])
        90.0
    """
    # --- YOU CODE STARTS HERE
    sum = 0
    
    if not isinstance(aList, list):
        return 'error'

    for num in aList:
        if type(num) in [int, float] and num % 3 == 0:
            sum += num ** 2
            
    return sum
