'''
CMPSC132 - Quiz 2 Coding Exam
November 19th, 2019
'''

## QUESTION 1

def sumDigits(num):
    '''
        >>> sumDigits(34)
        7
        >>> sumDigits(23456)
        20
    '''
    # --YOUR CODE STARTS HERE
    if num < 10:
        return num
    elif num >= 10 and num < 100:
        sum = (num % 10) + (num // 10)
    else:
        sum = (num % 10) + sumDigits(num // 10)
    return sum



## QUESTION 2

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
 
class DoublyLinkedList:
    '''
        >>> x=DoublyLinkedList()
        >>> x.add(5)
        >>> x.add(9)
        >>> x.add(4)
        >>> x.add(3)
        >>> x.append(8)
        >>> x.append(12)
        >>> x.append(56)
        >>> x.add(45)
        >>> print(x)
        Head:Node(45)
        Head to End:45 3 4 9 5 8 12 56
        End to Head:56 12 8 5 9 4 3 45
    '''
 
    def __init__(self):
        self.head = None

    def __str__(self):
        temp=self.head
        last=None
        out_forward=[]
        out_backward=[]
        while temp:
            out_forward.append(str(temp.value))
            last=temp
            temp=temp.next
        out_forward=' '.join(out_forward) 

        while last:
            out_backward.append(str(last.value))
            last = last.prev 
        out_backward=' '.join(out_backward) 

        return ('Head:{}\nHead to End:{}\nEnd to Head:{}'.format(self.head,out_forward,out_backward))

    __repr__ = __str__


    def add(self, value):
        # Adds items at the beginning of the list
        new_node = Node(value)
        new_node.next = self.head
 
        if self.head is not None: #List is empty
            self.head.prev = new_node
 
        self.head = new_node
 

    def append(self, value):
        #  Rememeber that when the list is empty, then new node is the head
        new_node = Node(value)
        # --YOUR CODE STARTS HERE
        if self.head is None:
            self.head = new_node
        
        else:
            prev = self.head
            current = self.head.next

            while current is not None:
                prev = current
                current = current.next
            
            prev.next = new_node
            new_node.prev = prev

