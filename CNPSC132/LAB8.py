#Lab #8
#Due Date: 10/25/2019, 11:59PM 
########################################
#                                      
# Name: Linhan Cai
# Collaboration Statement:             
#
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> x.reverse()
        >>> x
        Head:Node(3)
        Tail:Node(2)
        Queue:3 2
    '''
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        # --- Your code starts here

        # Return True when its empty, False otherwise.
        return self.head == None

    def enqueue(self, x):
        # --- Your code starts here
        new_node = Node(x)

        # When the queue is empty
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            self.count += 1
        # When the queue is not empty
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1


    def dequeue(self):
        # --- Your code starts here

        # When there are elements in the queue
        if not self.isEmpty():
            current = self.head

            # set the new head and remove the current head
            prev1 = current
            prev2 = self.head.value
            current = current.next

            self.head = current
            prev1 = None

            self.count -= 1
            # set the tail to None when the queue becomes empty
            if self.head == None:
                self.tail = None
            
            return prev2
            
        # When the queue is empty
        else:
            return 'Queue is empty'


    def __len__(self):
        # --- Your code starts here

        # return the length of the queue
        return self.count

    def reverse(self): 
        # --- Your code starts here
        prev = None
        current = self.head 
        reversed_tail = self.head
        # Traverse through and change the pointers' directions. 
        while current is not None: 
            current_next = current.next
            current.next = prev 
            prev = current 
            current = current_next
        # reset the head and tail 
        self.head = prev 
        self.tail = reversed_tail

        return