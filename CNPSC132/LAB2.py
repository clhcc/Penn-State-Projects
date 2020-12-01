#Lab #2
#Due Date: 09/06/2019, 11:59PM 
########################################
#                                      
# Name: Linhan Cai
# Collaboration Statement: None             
#
########################################

def removePunctuation(txt):
    """
        >>> removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
        'I like chocolate cake      It s the best flavor      for real'
        >>> removePunctuation("Dots...................... many dots..X")
        'Dots                       many dots  X'
        >>> removePunctuation(55)
        >>> removePunctuation([3.5,6])
    """
    # --- YOU CODE STARTS HERE
    # Non-string input
    if type(txt) != str:
        return None
    # String input
    else:
        for i in range(len(txt)):
            # Check every character if it's an alphabet letter
            if txt[i].isalpha() != True:
                # If not, replace it with a space
                txt = txt.replace(txt[i], ' ')
        return txt


def studentGrades(gradeList):
    """
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3'],
        ...     ['John', 100, 90, 80],
        ...     ['McVay', 88, 99, 111],
        ...     ['Rita', 45, 56, 67],
        ...     ['Ketan', 59, 61, 67],
        ...     ['Saranya', 73, 79, 83],
        ...     ['Min', 89, 97, 101]]
        >>> studentGrades(grades)
        [90, 99, 56, 62, 78, 95]
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2'],
        ...     ['John', 100, 90],
        ...     ['McVay', 88, 99],
        ...     ['Min', 89, 97]]
        >>> studentGrades(grades)
        [95, 93, 93]
        >>> studentGrades(55)
        >>> studentGrades('32')
    """
    # --- YOU CODE STARTS HERE
    # Non-list input
    if type(gradeList) != list:
        return None
    # List input
    else:
        # Create an empty list
        avg_score = []
        for i in range(1, len(gradeList)):
            # Calculate the sum of scores
            sum_score = sum(gradeList[i][1:])
            # Get the amount of scores
            amount_score = len(gradeList[i][1:])
            # Calculate the average scores
            avg = round(sum_score / amount_score)
            # Fill in the empty list
            avg_score.append(avg)
        return avg_score
