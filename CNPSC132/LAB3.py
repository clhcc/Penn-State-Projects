#Lab #3
#Due Date: 09/13/2019, 11:59PM
########################################
#                                      
# Name: Linhan Cai
# Collaboration Statement: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
#                          https://stackoverflow.com/questions/41430791/python-list-error-1-step-on-1-slice
#
########################################
# Import module string
import string

# Write the function
def isPalindrome(text):
    """
        >>> isPalindrome("alula")
        True
        >>> isPalindrome("love")
        False
        >>> isPalindrome("Madam")
        True
        >>> isPalindrome(12.5)
        False
        >>> isPalindrome(12.21)
        False
        >>> isPalindrome("Cigar? Toss it in a can.! It is so tragic.")
        True
        >>> isPalindrome("travel.. a town in Alaska")
        False
    """
    # --- YOU CODE STARTS HERE

    # Return False when input is not string
    if type(text) != str:
        return False

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Ignore capitalization by changing to all lowercase
    text = text.lower()

    # Ignore spaces
    text = text.replace(' ', '')

    # Create an empty variable to store the reversed text
    reverse = ''

    # Get the reversed text
    for i in text[::-1]:
        reverse += i

    # Check if a palindrome
    if reverse == text:
        return True
    else:
        return False
