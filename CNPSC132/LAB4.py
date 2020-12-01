#Lab #4
#Due Date: 09/20/2019, 11:59PM EST
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################


class BadSodaMachine:
    '''
        >>> m = BadSodaMachine('Coke', 10)
        >>> m.purchase()
        'Product out of stock'
        >>> m.purchase(2)
        'Product out of stock'
        >>> m.restock(3)
        'Current soda stock: 3'
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.purchase(2)
        'Please deposit $13'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Coke dispensed, take your $2'
        >>> m.deposit(20)
        'Balance: $20'
        >>> m.purchase(2)
        'Coke dispensed'
        >>> m.deposit(15)
        'Sorry, out of stock. Take your $15 back'
    '''
    def __init__(self, product, price):
    # --- YOU CODE STARTS HERE
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0
        self.pay = 0


    # --- YOU CODE STARTS HERE. Notes from Module 1 could be useful here!
    def purchase(self, demand = 1):
        self.pay = self.price * demand
        if self.stock == 0:
            return('Product out of stock')
        elif self.stock < demand:
            return('Current soda stock: {}'.format(stock))
        elif self.stock >= demand and self.balance < self.pay:
            return('Please deposit ${}'.format(self.pay - self.balance))
        elif self.stock >= demand and self.balance > self.pay:
            self.stock = self.stock - demand
            self.balance = 0
            return('{} dispensed, take your money'.format(self.product))

        else:
            self.balance = self.balance - self.pay
            self.stock = self.stock - self.demand
            return('{} dispensed'.format(product))


    def deposit(self, amount):
    # --- YOU CODE STARTS HERE
        self.balance += amount
        return('Balance: ${}'.format(self.balance))


    def restock(self, amount):
    # --- YOU CODE STARTS HERE
        self.stock += amount
        return('Current soda stok: {}'.format(self.stock))
        
    
