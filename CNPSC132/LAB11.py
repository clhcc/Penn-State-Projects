#LAB 11
#Due Date: 11/22/2019, 11:59PM
########################################
#                                      
# Name: Linhan Cai
# Collaboration Statement:             
#
########################################


def selectionSort(numList):
    '''
        Takes a list and returns 2 values
        1st returned value: a dictionary with the state of the list after each complete pass of selection sort
        2nd returned value: the sorted list

        >>> selectionSort([9,3,5,4,1,78,67])
        ({1: [9, 3, 5, 4, 1, 78, 67], 2: [1, 3, 5, 4, 9, 78, 67], 3: [1, 3, 5, 4, 9, 78, 67], 4: [1, 3, 4, 5, 9, 78, 67], 5: [1, 3, 4, 5, 9, 78, 67], 6: [1, 3, 4, 5, 9, 78, 67], 7: [1, 3, 4, 5, 9, 67, 78]}, [1, 3, 4, 5, 9, 67, 78])
    '''
    # YOUR CODE STARTS HERE

    # Create a dictionary containing the original numList
    dict={1:numList[:]}

    # Traverse through the numList
    for i in range(len(numList) - 1):
        # Assume the minimum element's index is the current i
        min = i
        # Loop through the numList with the given i. 
        for j in range(i, len(numList)):
            # If a smaller element is found, set its index to the new minimum index.
            if numList[i] > numList[j]:
                min = j

        # Swap the new minimum element with the previous one
        numList[i], numList[min] = numList[min], numList[i]

        # Create new pairs in the dictionary.
        dict[i + 2] = numList[:]
        
    # Return the result
    return dict, numList