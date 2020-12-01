#HW3
#Due Date: 11/03/2019, 11:59PM 
'''
Team members: Linhan Cai, Matthew Schaeffer

Collaboration Statement: Geeks For Geeks help gave us a good understanding of what Postfix was   

'''

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
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



#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.expr = None


    def isNumber(self, txt):
        # YOUR CODE STARTS HERE

        # Try to see if the txt could be converted into float. If so, it's a valid input.
        if isinstance(txt, str) and len(txt) != 0:
            try:
                float(txt)
                return True
            except ValueError:
                return False
        else:
            return 'Please enter a non-empty string'



    def postfix(self, txt):
        '''
            Required: postfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x.postfix(' 2 ^        4')
            '2.0 4.0 ^'
            >>> x.postfix('2')
            '2.0'
            >>> x.postfix('2.1*5+3^2+1+4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x.postfix('    2 *       5.34        +       3      ^ 2    + 1+4   ')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x.postfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x.postfix('(2.5)')
            '2.5'
            >>> x.postfix ('((2))')
            '2.0'
            >>> x.postfix ('     -2 *  ((  5   +   3)    ^ 2+(1  +4))    ')
            '-2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x.postfix ('  (   2 *  ((  5   +   3)    ^ 2+(1  +4)))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x.postfix ('  ((   2 *  ((  5   +   3)    ^ 2+(1  +4))))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x.postfix('   2 *  (  5   +   3)    ^ 2+(1  +4)    ')
            '2.0 5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
            >>> x.postfix('2 *    5   +   3    ^ -2       +1  +4')
            'error message'
            >>> x.postfix('2    5')
            'error message'
            >>> x.postfix('25 +')
            'error message'
            >>> x.postfix('   2 *  (  5   +   3)    ^ 2+(1  +4    ')
            'error message'
            >>> x.postfix('2*(5 +3)^ 2+)1  +4(    ')
            'error message'
        '''
        if not isinstance(txt,str) or len(txt)<=0:
            print("Argument error in postfix")
            return None

        postStack=Stack()
        # YOUR CODE STARTS HERE
        
        # Initialize the necessary condition. 
        
        # Create an empty list for the result
        self.output = []

        # Set the precedence for each operator
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

        # Set the list of operators for later-on condition checking
        opt_list = ['+', '-', '*', '/', '^', '(', ')']
        operator = ['+', '-', '*', '/', '^']
        
        # A while loop to scan through the txt and add spaces between numbers and operators
        start = 1
        while txt[start:]:
            if txt[start - 1] in opt_list and self.isNumber(txt[start]) or \
                self.isNumber(txt[start - 1]) and txt[start] in opt_list or \
                txt[start - 1] in opt_list and txt[start] in opt_list:
                txt = txt[:start] + ' ' + txt[start:]
            start += 1
        
        # Split the txt by spaces and make it into a list
        item = txt.split(' ')

        # Use filter and lambda function to get rid off the spaces 
        list_ = list(filter(lambda item1: item1 != '', item))
        
        # In case the first number is a negative number, make it a negative number.
        if list_[0] == '-' and self.isNumber(list_[1]):
            list_[0] = list_[0] + list_[1]
            list_.remove(list_[1])
        
        # Loop through the list, return an error message when two consecutive numbers or operators exist.
        for i in range(1, len(list_)):
            if (self.isNumber(list_[i-1]) and self.isNumber(list_[i])) or (list_[i-1] in operator and list_[i] in operator):
                return 'error message'
        
        # Loop through the list, return an error message when the number of starting and enclosing
        # parentheses do not match 
        # or the enclosing parenthesis is before the starting parenthesis.
        if '(' in list_ or ')' in list_:
            if list_.count('(') != list_.count(')') or list_.index(')') < list_.index('(') or list_[-1] == '(':
                return 'error message'
        
        # If the start or the end of the expression is an operator, return error message.
        if list_[0] in operator or list_[-1] in operator:
            return 'error message'

        # loop through the whole expression                
        for i in range(0, len(list_)): 
            # If the element is a float, add it to output and keep it that way
            if self.isNumber(list_[i]) and '.' in list_[i]: 
                self.output.append(str(list_[i]))

            # If the element is an integer, add it to output and give it one decimal place
            elif self.isNumber(list_[i]) and '.' not in list_[i]:
                self.output.append(str(round(float(list_[i]), 1))) 
              
            # If the element is an '(', push it to stack 
            elif list_[i]  == '(': 
                postStack.push(list_[i]) 
  
            # If the element is an ')' 
            elif list_[i] == ')': 
                # When there is an operator in the stack, pop it and add to the output
                while not postStack.isEmpty() and postStack.peek() != '(': 
                    a = postStack.pop() 
                    self.output.append(a) 
                # When the operator is '(', pop it.
                else: 
                    postStack.pop() 
  
            # If the element is an operator other than parenthesis
            else: 
                try:
                    # If the operator has lower or equal precedence than the operator on the top of the stack, 
                    # pop from the stack and append it to the output until this is not true. 
                    while not postStack.isEmpty() and self.precedence[list_[i]] <= self.precedence[postStack.peek()]:
                        self.output.append(postStack.pop()) 
                    # Then, push the incoming operator on the stack
                    else:
                        postStack.push(list_[i]) 
                # Raise a KeyError when the peek of the stack is parenthesis and push the operator to the stack.
                except KeyError:
                    postStack.push(list_[i]) 
  
        # pop all the operator from the stack and add them to the output in the postfix order
        while not postStack.isEmpty(): 
            self.output.append(postStack.pop()) 
        
        # return the result
        return " ".join(self.output) 


    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.expr='    4  +      3 -2'
            >>> x.calculate
            5.0
            >>> x.expr='  -2  +3.5'
            >>> x.calculate
            1.5
            >>> x.expr='4+3.65-2 /2'
            >>> x.calculate
            6.65
            >>> x.expr=' 23 / 12 - 223 +      5.25 * 4    *      3423'
            >>> x.calculate
            71661.91666666667
            >>> x.expr='   2   - 3         *4'
            >>> x.calculate
            -10.0
            >>> x.expr=' 3 *   (        ( (10 - 2*3)))'
            >>> x.calculate
            12.0
            >>> x.expr=' 8 / 4  * (3 - 2.45      * (  4- 2 ^   3)) + 3'
            >>> x.calculate
            28.6
            >>> x.expr=' 2   *  ( 4 + 2 *   (5-3^2)+1)+4'
            >>> x.calculate
            -2.0
            >>> x.expr='2.5 + 3 * ( 2 +(3.0) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2'
            >>> x.calculate
            1442.7777777777778
            >>> x.expr="4++ 3 +2"
            >>> x.calculate
            'error message'
            >>> x.expr="4    3 +2"
            >>> x.calculate
            'error message'
            >>> x.expr='(2)*10 - 3*(2 - 3*2)) '
            >>> x.calculate
            'error message'
            >>> x.expr='(2)*10 - 3*/(2 - 3*2) '
            >>> x.calculate
            'error message'
            >>> x.expr=')2(*10 - 3*(2 - 3*2) '
            >>> x.calculate
            'error message'
        '''

        if not isinstance(self.expr,str) or len(self.expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack=Stack()
        # YOUR CODE STARTS HERE
        
        # create lambda function to define what the operators' function are
        opt  = {'+': (lambda x,y: x+y), '-': (lambda x,y: x-y), '*': (lambda x,y: x*y), '/': (lambda x,y: x/y), '^': (lambda x,y: x ** y)}
       
        # calls postfix to turn the expression into a list
        expr = self.postfix(self.expr).split(' ') 
        
        # if the expression is invalid, return an error message
        if expr == ['error', 'message']: 
            return 'error message'
            
        # if the expression is valid, then
        else: 
            # loop through the expression
            for i in range(0, len(expr)):
                # checks if the element is a number in expression and pushes the numbers in until operator appears
                if self.isNumber(expr[i]):
                    calcStack.push(expr[i])
                    
                # pops the first two numbers and calculate the answer of them
                else: 
                    x = calcStack.pop()
                    y = calcStack.pop()
                    calcStack.push(str(opt[expr[i]] (float(y), float(x))))

        # returns the answer as a float
        return float(calcStack.pop())