#Lab #6
#Due Date: 10/04/2019, 11:59PM 
########################################
#                                      
# Name: Linhan Cai
# Collaboration Statement: Fei Liang      
#                          http://mathandmultimedia.com/2012/06/02/determining-primes-through-square-root/
#                          https://www.smartickmethod.com/blog/math/operations-and-algebraic- thinking/divisibility/prime-numbers-sieve-eratosthenes/
########################################


## ALL FUNCTIONS MUST BE RECURSIVE IN ORDER TO GET CREDIT FOR THEM


def mulBy(num):
    '''
        >>> mulBy(5)
        15
        >>> mulBy(8)
        384
        >>> mulBy(0)
        0
        >>> mulBy(1)
        1
    '''
    # --- Your code starts here

    # Base cases 
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    
    # Recursion
    else:
        return num * mulBy(num-2)




def flat(aList):
    '''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''
    # --- Your code starts here

    # Base case
    if aList == []:
        return aList

    # Recursion
    elif isinstance(aList[0], list):
        return flat(aList[0]) + flat(aList[1:])
    else:
        return aList[:1] + flat(aList[1:])



def isPrime(num, n=2):
    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(0)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
        >>> isPrime(2654)
        False
    '''
    # --- Your code starts here

    # Base cases
    if num < 2:
        return False
    if num == n:
        return True
    if num % n == 0:
        return False
    if n ** 2 == num:
        return False
    if n ** 2 > num:
        return True

    # Recursion
    return isPrime(num, n+1)





def countPrimes(num):
    '''
        >>> countPrimes(0)
        0
        >>> countPrimes(6)
        3
        >>> countPrimes(2)
        1
        >>> countPrimes(60)
        17
        >>> countPrimes(100)
        25
        >>> countPrimes(500)
        95
    '''
    # --- Your code starts here

    # Base cases
    if num == 0:
        return 0
    if num == 1:
        return 0

    # Recursion
    if isPrime(num):
        return countPrimes(num-1) + 1
    else:
        return countPrimes(num-1)

