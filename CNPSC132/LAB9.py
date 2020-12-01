#Lab #9
#Due Date: 11/08/2019, 11:59PM
########################################
#                                      
# Name: Linhan Cai
# Collaboration Statement: Prof. Lopez helped me a lot with the deleteMin() method.
#  
########################################



class MinHeap:
    '''
        >>> h = MinHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h.heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.parent(2)
        2
        >>> h.leftChild(1)
        5
        >>> h.rightChild(1)
        11
        >>> h.parent(8)
        10
        >>> h.leftChild(6)
        >>> h.rightChild(9)
        >>> h.deleteMin
        2
        >>> h.heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
    '''

    # -- YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR!
    def __init__(self):
        self.heap=[]

    def __str__(self):
    	return f'{self.heap}'

    __repr__=__str__


    def parent(self,index):
        # -- YOUR CODE STARTS HERE

        # Set the index for parent in the case of index starts at 0.
        parent = index // 2 - 1
        
        # Return the results based on the index given which starts at 1.
        if index <= 1:
            return None
        elif index > len(self.heap):
            return None
        else:
            return self.heap[parent]


    def leftChild(self,index):
        # -- YOUR CODE STARTS HERE

        # Set the index for left child in the case of index starts at 0.
        left = index * 2 -1
        
        # Return the results based on the index givien which starts at 1.
        if index < 1 or left + 1 > len(self.heap):
            return None
        else:
            return self.heap[left]



    def rightChild(self,index):
        # -- YOUR CODE STARTS HERE

        # Set the index for right child in the case of index starts at 0.
        right = index * 2

        # Return the results based on the index givien which starts at 1.
        if index < 1 or right + 1 > len(self.heap):
            return None
        else:
            return self.heap[right]



    def __len__(self):
        # -- YOUR CODE STARTS HERE
        return len(self.heap)
 
    # Create a swap method to make the methods of insert and deleteMin more convenient since it could just call this method when swapping.
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self,x):
        # -- YOUR CODE STARTS HERE

        # Append x to the heap list.
        self.heap.append(x)
        
        # Set a variable l to the length of the list.
        l = len(self.heap)
        
        # When parent exists which means the list is not empty
        while  l // 2 - 1 >= 0:
            # if the last element (newly inserted element) in the list is less than its parent
            if self.heap[l - 1] < self.parent(l):
                # Swap it with its parent
                self.swap(l // 2 - 1, l - 1)
            # if not, break the loop
            else:
                break
            # Update variable l to the current position of the element.
            l = l // 2
            
    @property
    def deleteMin(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            out=self.heap[0]
            self.heap=[]
            return out

        # -- YOUR CODE STARTS HERE

        # Give the minimum value a variable for latter return.
        minval = self.heap[0]

        # Move the last element to the first
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Set the index to 0 for the while loop to start with the root (the biggest value)
        index = 0

        # While there could be a left child exists
        while (index + 1) * 2 <= len(self.heap):
            # if the list only has a left child 
            if (index + 1) * 2 + 1 > len(self.heap):
                # the minimum element's index is the left child's index
                minIndex = (index + 1) * 2 -1
            # if the list has more than just a left child
            else:
                # if the right child is bigger
                if self.rightChild(index + 1) >= self.leftChild(index + 1):
                    # the minimum element's index is the left child's index
                    minIndex = (index + 1) * 2 - 1
                # if the left child is bigger, the minIndex is now the right child's
                else:
                    minIndex = (index + 1) * 2
            # Swap the biggest value with the smaller value of its children.
            if self.heap[index] > self.heap[minIndex]:
                self.swap(index, minIndex)
            # If it is in good position, break the loop
            else:
                break
            # Set the index to the current index of the value we are moving around.
            index = minIndex
        # return the minimum value that's been deleted.
        return minval