#Lab #7
#Due Date: 10/11/2019, 11:59PM 
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
                        
                          
class OrderedLinkedList:
    '''
        >>> x=OrderedLinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.remDuplicates()
        >>> x.pop()
        8.76
        >>> x
        Head:Node(1)
        Tail:Node(5)
        List:1 3 5
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
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__

    def isEmpty(self):
        return self.head == None

    def __len__(self):
        return self.count


    def add(self, value):
        # --- Your code starts here
        new_node = Node(value)
        

        # When the linked list is empty
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node

        # When the new node is smaller than the head
        elif self.head.value >= new_node.value:
            new_node.next = self.head
            self.head = new_node
        
        # When the new node is larger than the head and the following nodes
        else:
            prev = self.head
            current = self.head.next
            
            # Traverse through the linked list and insert the new node 
            while current is not None and current.value < new_node.value:
                prev = current
                current = current.next

            new_node.next = current
            prev.next = new_node
            
            # Create a tail if the new node is bigger than all the number in the linked list
            if current is None:
                self.tail = new_node



    def pop(self):
        # --- Your code starts here

        # In case the linked list is empty
        if not self.isEmpty():
            current = self.head
        
            # Traverse through the linked list to the end, delete the tail, and update the tail
            while current.next is not None:
                prev = current
                current = current.next

            prev.next = None
            self.tail = prev

            return current.value

        else:
            return


    def remDuplicates(self):
        # --- Your code starts here
        current = self.head

        # In case the linked list is empty
        if self.isEmpty():
            return

        # Traverse through the list and remove all the duplicates
        while current.next is not None:
            if current.value == current.next.value:
                new_next = current.next.next
                current.next = None
                current.next = new_next
            else:
                current = current.next
        
        # set the new tail 
        self.tail = current
        return 