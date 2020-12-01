#HW 5
#Due Date: 12/13/2019, 11:59PM 
########################################
#
# Name: Linhan Cai
# Collaboration Statement:
#
########################################

# ---Copy your Queue code from lab 8 and your Stack code from HW3 here (you can remove their comments)  


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__



# ==========================Queue Code=================================================                       
                          
class Queue:
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

#============================Stack Code============================================

class Stack:
    def __init__(self):
        self.top = None
        self.count=0
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE

        # Return True when its empty, False otherwise.
        return self.top == None

    def __len__(self): 
        # YOUR CODE STARTS HERE

        # return the number of items on the stack
        return self.count

    def push(self,value):
        # YOUR CODE STARTS HERE
        
        # set a new node
        new_node =  Node(value)

        # if the stack is empty, push to the stack and make it the top
        if self.isEmpty():
            self.top = new_node
            self.count += 1
        
        # if the stack is not empty, push the new node in and make it the top
        else:
            new_node.next = self.top
            self.top = new_node
            self.count += 1


    def pop(self):
        # YOUR CODE STARTS HERE
        
        # If the stack is not empty, delete the top and make the next the top.
        if not self.isEmpty():
            current = self.top

            top = current
            top1 = self.top.value

            current = current.next
            self.top = current
            top = None
            self.count -= 1
            return top1
        else:
            return

    def peek(self):
        # YOUR CODE STARTS HERE

        # return the value of the top
        if not self.isEmpty():
            return self.top.value

        else:
            return






#----- HW5 Graph code     
class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr


    def bfs(self, start):
        '''
            >>> g1 = {'A': ['B','D','G'],
            ... 'B': ['A','E','F'],
            ... 'C': ['F'],
            ... 'D': ['A','F'],
            ... 'E': ['B','G'],
            ... 'F': ['B','C','D'],
            ... 'G': ['A','E']}
            >>> g=Graph(g1)
            >>> g.bfs('A')
            ['A', 'B', 'D', 'G', 'E', 'F', 'C']
        '''
        # YOUR CODE STARTS HERE

        # Set an empty queue
        Q = Queue()
        # Enqueue the start element
        Q.enqueue(start)


        # Create an empty list for the nodes visited
        visited = []
        # Add the start node to visited
        visited.append(start)


        # while the queue is not empty
        while not Q.isEmpty():
            # remove an element from the queue
            node = Q.dequeue()
            # visit its neighbors
            for x in sorted(self.vertList[node]):
                # if it's a tuple, ignore the cost
                if isinstance(x, tuple):
                    x=x[0]
                # add it to the que and mark as visited if it's not
                if x not in visited:
                    Q.enqueue(x)
                    visited.append(x)

        return visited



    def dfs(self, start):
        '''
            >>> g1 = {'A': ['B','D','G'],
            ... 'B': ['A','E','F'],
            ... 'C': ['F'],
            ... 'D': ['A','F'],
            ... 'E': ['B','G'],
            ... 'F': ['B','C','D'],
            ... 'G': ['A','E']}
            >>> g=Graph(g1)
            >>> g.dfs('A')
            ['A', 'B', 'E', 'G', 'F', 'C', 'D']
        '''
        # OUR CODE STARTS HERE

        # Set an empty stack
        S = Stack()
        # add the start element to the stack
        S.push(start)

        # set an empty list for visited nodes.
        visited = []

        # while the stack is not empty
        while not S.isEmpty():
            # pop a node
            node = S.pop()

            # if it is not visited already
            if node not in visited:
                # add it to visited list
                visited.append(node)
                
                # for its neighbors (in a reversed order)
                for x in reversed(sorted(self.vertList[node])):
                    # if it's a tuple, ignore its cost
                    if isinstance(x, tuple):
                        x=x[0]
                    # if it is not visited, push it to the stack
                    if x not in visited:
                        S.push(x)

        return visited