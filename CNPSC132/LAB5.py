#Lab #5
#Due Date: 09/27/2019, 11:59PM EST
########################################
#                                      
# Name: Linhan Cai
# Collaboration Statement: Jinhan Li             
#
########################################


class Complex:
    '''
        >>> a=Complex(5,-6)
        >>> b=Complex(2,14)
        >>> a+b
        (7, 8i)
        >>> a-b
        (3, -20i)
        >>> a*b
        (94, 58i)
        >>> b*5
        (10, 70i)
        >>> 5*b
        (10, 70i)
        >>> print(a)
        5-6i
        >>> print(b)
        2+14i
        >>> b
        (2, 14i)
        >>> isinstance(a+b, Complex)
        True
        >>> a.conjugate
        (5, 6i)
        >>> b==Complex(2,14)
        True
        >>> a==b
        False
    '''
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    # --- YOU CODE STARTS HERE

    # Define the add method
    def __add__(self, other):
        NewR = self.real + other.real
        NewI = self.imag + other.imag
        return Complex(NewR, NewI)

    # Define the sub method
    def __sub__(self, other):
        NewR = self.real - other.real
        NewI = self.imag - other.imag
        return Complex(NewR, NewI)

    # Define the mul method
    def __mul__(self, other):
        if isinstance(self, Complex):
            if isinstance(other, Complex):
                NewR = self.real * other.real - self.imag * other.imag
                NewI = self.real * other.imag + self.imag * other.real
            elif isinstance(other, (int, float)):
                NewR = self.real * other
                NewI = self.imag * other
        else:
            return 'TypeError: must be int or float'
        
        return Complex(NewR, NewI)

    #Define the rmul method to tell the computer what to do if the complex number and the int/float exchanges their locations.
    def __rmul__(self, other):
        return self.__mul__(other)

    # Define the eq method
    def __eq__(self, other):
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False

    # Define the str method
    def __str__(self):
        if self.imag <= 0:
            return str(self.real).strip() + str(self.imag).strip() + 'i'
        if self.imag > 0:
            return str(self.real).strip() + '+' + str(self.imag).strip() + 'i'

    # Define the repr method for a straight call of the name
    def __repr__(self):
        return '(' + str(self.real) + ', ' + str(self.imag) + 'i)'
            

    # Define the conjugate method
    @property
    def conjugate(self):
        return Complex(self.real, -self.imag)
