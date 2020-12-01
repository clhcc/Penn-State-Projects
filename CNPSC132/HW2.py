#Homework #2
#Due Date: 10/11/2019, 11:59PM
########################################
#
# Name: Linhan Cai
# Collaboration Statement: Fei Liang
#
########################################

from abc import *
import random

class Account(ABC):
    """
       Account class generates basic information for customers once they open their accounts
       It also provides methods to deposit money or withdraw money
    """
    def __init__(self, account_holder):
        """
           Initiate an instance.

           Parameters:
           -----------
           account_holder: str

           Returns:
           --------
           str: the name of the account holder
           int or float: the balance of the account
           int: the ID of the account
           list: the list contains the information of the account
        """
        self._name = account_holder
        self._balance = 0
        self.__id = self.__createID
        self.info = self.setInfo

    @property
    def __createID(self):
        """
           Initiate an ID

           Parameters:
           -----------
           None

           Returns:
           --------
           int: the ID of the account
        """
        return random.randint(100, 9000)
    
    @property
    def getID(self):
        """
           Display an ID

           Parameters:
           -----------
           None

           Returns:
           --------
           int: the ID of the account
        """
        return self.__id

    def setID(self, newid):
        """
           Modify an ID

           Parameters:
           -----------
           newid: int

           Returns:
           --------
           int: the new ID of the account
        """
        self.__id = newid
    
    @property
    def setInfo(self):
        """
           Put the information of an account into a list

           Parameters:
           -----------
           None

           Returns:
           --------
           list: a list containing the name and balance of an account
        """
        return ['Name:', self._name, 'Balance:', self._balance]


    def __repr__(self):
        """
           Represent an account object

           Parameters:
           -----------
           None

           Returns:
           --------
           str: the list of the name and balance of an account as string
        """
        return str(self.info)

    
    def deposit(self, amount):
        """
           Deposit the amount of money into an account

           Parameters:
           -----------
           amount: int or float

           Returns:
           --------
           int or float: the new balance of the account is returned
           str: error message when parameter is not int or float
        """
        if isinstance(amount, (int,float)):
            self._balance += amount
            self.info = self.setInfo
            return self._balance
        else:
            return 'Invalid operation'

    def withdraw(self, amount):
        """
           Withdraw the amount of money from an account

           Parameters:
           -----------
           amount: int or float

           Returns:
           --------
           int or float: the new balance of the account is returned
           str: error message when parameter is not int or float; error message when the balance is less than the amount
        """
        if isinstance(amount, (int,float)):
            if amount > self._balance:
                return 'Insufficient Funds'
            elif amount < self._balance:
                self._balance = self._balance - amount
                self.info = self.setInfo
                return self._balance
        else:
            return 'Invalid Operation'


class SavingsAccount(Account):
    """
       SavingsAccount class is the subclass of Account.
       It specify the savings account situation.
       It contains a deposit fee, a withdraw fee, and a minimum balance.
       The deposit and withdraw method are specified with this condition.
    """

    DEPOSIT_FEE = 1
    WITHDRAW_FEE = 2
    MIN_BALANCE =250

    def __init__(self, name):
        """
           Initiate an instance in the way of class Account does

           Parameters:
           -----------
           name: str

           Returns:
           --------
           str: the name of the account holder that's opening a savings account
        """
        super().__init__(name)

    def deposit(self, amount):
        """
           Deposit the amount of money into a savings account by using the superclass's method

           Parameters:
           -----------
           amount: int or float

           Returns:
           --------
           int or float: the new balance of the account is returned
           str: error message when parameter is not int or float
        """
        return Account.deposit(self, amount - SavingsAccount.DEPOSIT_FEE)

    def withdraw(self, amount):
        """
           Withdraw the amount of money from a savings account by using the superclass's method

           Parameters:
           -----------
           amount: int or float

           Returns:
           --------
           int or float: the new balance of the account is returned
           str: error message when parameter is not int or float; error message when the balance is less than the amount and the minimum balance
        """
        if self._balance - amount - SavingsAccount.WITHDRAW_FEE >= SavingsAccount.MIN_BALANCE:
            return Account.withdraw(self, amount + SavingsAccount.WITHDRAW_FEE)
        else:
            return 'Minimum balance error'


class CheckingAccount(Account):
    """
       CheckingAccount class is the subclass of Account.
       It specify the checking account situation.
       It contains a withdraw fee.
       The deposit and withdraw method are specified with this condition.
    """

    WITHDRAW_FEE = 1

    def __init__(self, name):
        """
           Initiate an instance in the way of class Account does

           Parameters:
           -----------
           name: str

           Returns:
           --------
           str: the name of the account holder that's opening a checking account
        """
        super().__init__(name)
    
    def deposit(self, amount):
        """
           Deposit the amount of money into a checking account by using the superclass's method

           Parameters:
           -----------
           amount: int or float

           Returns:
           --------
           int or float: the new balance of the account is returned
           str: error message when parameter is not int or float
        """
        return Account.deposit(self, amount)

    def withdraw(self, amount):
        """
           Withdraw the amount of money from a checking account by using the superclass's method

           Parameters:
           -----------
           amount: int or float

           Returns:
           --------
           int or float: the new balance of the account is returned
           str: error message when parameter is not int or float; error message when the balance is less than the amount with a withdraw fee
        """
        return Account.withdraw(self, amount + CheckingAccount.WITHDRAW_FEE)


class Bank:
    """
       Bank class stores the account information for customers and basic information for staffs
       It also provides methods to open a checking account or a savings account
    """
    def __init__(self, bankname):
        """
           Initiate an instance.

           Parameters:
           -----------
           bankname: str

           Returns:
           --------
           str: the name of the bank
           dictionary: dictionaries to store information of customer accounts and staffs
        """
        self._bank = bankname
        self._Manager = {}
        self._Assistant = {}
        self._Teller = {}
        self._Accounts = {}

    def openCheckingAccount(self, customer, amount, account_type=CheckingAccount):
        """
           Open a checking account for a customer and deposit some money for the customer
           This method create a key and a value in the _Accounts dictionary

           Parameters:
           -----------
           customer: a Customer object 
           amount: int or float

           Returns:
           --------
           str: a message informing the account is opened, with its information.
        """
        account=account_type(customer._name)
        account.deposit(amount)
        self._Accounts[account._Account__id]=account
        return 'Checking Account Opened, {}'.format(account)
    
    def openSavingsAccount(self, customer, amount, account_type=SavingsAccount):
        """
           Open a savings account for a customer and deposit some money for the customer
           This method create a key and a value in the _Accounts dictionary

           Parameters:
           -----------
           customer: a Customer object 
           amount: int or float

           Returns:
           --------
           str: a message informing the account is opened, with its information.
        """
        account=account_type(customer._name)
        account.deposit(amount)
        self._Accounts[account._Account__id]=account
        return 'Savings Account Opened, {}'.format(account)



class Person(ABC):
    """
       Person class generates the name for either customers or staffs
       It also provides an abstract method to let the person know his/her authority and what this person can do
    """
    def __init__(self, name):
        """
           Initiate an instance.

           Parameters:
           -----------
           name: str

           Returns:
           --------
           str: the name of the person
        """
        self._name = name

    @abstractmethod
    def whatyoucando(self):
        """
           Define an abstracmethod

           Parameters:
           -----------
           None

           Returns:
           --------
           NotImplementedError
        """
        raise NotImplementedError


class Customer(Person):
    """
       Customer class is the subclass of Person.
       It specify the customer as a type of person.
       It creates an instance of a customer.
       It has multiple methods that tell a customer what to do.
    """
    def __init__(self, name):
        """
           Initiate an instance.

           Parameters:
           -----------
           name: str

           Returns:
           --------
           str: the name of the customer
        """
        super().__init__(name)
    
    def whatyoucando(self):
        """
           Inherits the abstracmethod and implements the principle of Polymorphism

           Parameters:
           -----------
           None

           Returns:
           --------
           str: a message telling what a customer can do at this point
        """
        return 'Hi {}, start with us by opening an account first!'.format(self._name)

    def ask_loan(self):
        """
           A customer asking for a loan 

           Parameters:
           -----------
           None

           Returns:
           --------
           str: message that tells the customer to go to an Assistant for asking loan
        """
        return 'Please provide your account ID to the Assistant'

    def ask_creditcard(self):
        """
           A customer asking for a credit card 

           Parameters:
           -----------
           None

           Returns:
           --------
           str: message that tells the customer the card is issued and pay bill monthly
        """
        return 'Credit card is issued. Please pay your bill monthly'

    def send_money(self):
        """
           A customer requesting a money transfer 

           Parameters:
           -----------
           None

           Returns:
           --------
           str: message that tells the customer to go to an Assistant for transfering money
        """
        return 'Please ask the Assistant to transfer money for you'


class Staff(Person):
    """
       Staff class is the subclass of Person.
       It specify the staff as a type of person.
       It creates an instance of a staff.
    """
    def __init__(self, name, bank):
        """
           Initiate an instance.

           Parameters:
           -----------
           name: str
           bank: a Bank object

           Returns:
           --------
           str: the name of the staff
           object: the Bank object that this staff belongs to
        """
        super().__init__(name)
        self._bankemployed = bank
    
    def whatyoucando(self):
        """
           Inherits the abstracmethod and implements the principle of Polymorphism

           Parameters:
           -----------
           None

           Returns:
           --------
           str: a message telling what a staff can do at this point
        """
        return 'Hi {}, please specify your title'.format(self._name)


class Teller(Staff):
    """
       Teller class is the subclass of Staff.
       It specify the teller as a type of staff.
       It creates an instance of a teller.
    """
    def __init__(self, name, bank):
        """
           Initiate an instance.
           Append the information of this teller to the _Teller dictionary

           Parameters:
           -----------
           name: str
           bank: a Bank object

           Returns:
           --------
           str: the name of the teller
           object: the Bank object that this teller belongs to
        """
        super().__init__(name, bank)
        self._bankemployed._Teller['Teller'] = self._name

    def whatyoucando(self):
        """
           Inherits the abstracmethod and implements the principle of Polymorphism

           Parameters:
           -----------
           None

           Returns:
           --------
           str: a message telling the teller his/her authorities
        """
        return 'Hi {}, you can see the general information of customers'.format(self._name)
    
    def seeInfo(self, bank, customerID):
        """
           Get the general information of a customer

           Parameters:
           -----------
           bank: a Bank object
           customerID: int. It is the ID that was generated when a customer opened an account

           Returns:
           --------
           str: a message displaying the customer's name; or an error message when ID cannot be found in the _Accounts dictionary
        """
        if customerID in bank._Accounts:
            info = bank._Accounts[customerID]
            return 'Customer name: {}'.format(info._name)
        else:
            return 'Customer not found'


class Assistant(Teller):
    """
       Assistant class is the subclass of Teller.
       It specify the assistant as a type of staff.
       It creates an instance of an assistant.
    """
    def __init__(self, name, bank):
        """
           Initiate an instance.
           Append the information of this assistant to the _Assistant dictionary

           Parameters:
           -----------
           name: str
           bank: a Bank object

           Returns:
           --------
           str: the name of the assistant
           object: the Bank object that this assistant belongs to
        """
        super().__init__(name, bank)
        self._bankemployed._Assistant['Assistant'] = self._name
    
    def whatyoucando(self):
        """
           Inherits the abstracmethod and implements the principle of Polymorphism

           Parameters:
           -----------
           None

           Returns:
           --------
           str: a message telling the assistant his/her authorities
        """
        return 'Hi {}, you can approve loans and transfer money for customers. You also have the authority of a Teller'.format(self._name)

    def approve_loan(self, bank, customerID):
        """
           Approve a loan for a customer

           Parameters:
           -----------
           bank: a Bank object
           customerID: int. It is the ID that was generated when a customer opened an account

           Returns:
           --------
           str: a message telling the customer's loan is approved; or an error message when ID cannot be found in the _Accounts dictionary
        """
        if customerID in bank._Accounts:
            cus = bank._Accounts[customerID]
            return "{}'s loan is approved".format(cus._name)
        else:
            return 'Customer not found'
        
    def transfer_money(self, bank, out_account_id, in_account_id, amount):
        """
           Transfer money between accounts. 
           The account information (such as its balance) will be updated
           Money is transferred differently depending on the type of the accounts

           Parameters:
           -----------
           bank: a Bank object
           out_account_id: int
           in_account_id: int
           amount: int or float

           Returns:
           --------
           str: an error message suggests invalid operations
        """
        out_account = bank._Accounts[out_account_id]
        in_account = bank._Accounts[in_account_id]
        if isinstance(out_account, SavingsAccount) and out_account._balance - amount - SavingsAccount.WITHDRAW_FEE >= SavingsAccount.MIN_BALANCE:
            out_account.withdraw(amount)
            in_account.deposit(amount)
        elif isinstance(out_account, CheckingAccount) and amount < out_account._balance:
            out_account.withdraw(amount)
            in_account.deposit(amount)
        else:
            return 'Invalid Operation'


class Manager(Assistant):
    """
       Manager class is the subclass of Assistant.
       It specify the manager as a type of staff.
       It creates an instance of a manager.
    """
    def __init__(self, name, bank):
        """
           Initiate an instance.
           Append the information of this manager to the _Manager dictionary

           Parameters:
           -----------
           name: str
           bank: a Bank object

           Returns:
           --------
           str: the name of the manager
           object: the Bank object that this manager belongs to
        """
        super().__init__(name, bank)
        self._bankemployed._Manager['Manager'] = self._name

    def whatyoucando(self):
        """
           Inherits the abstracmethod and implements the principle of Polymorphism

           Parameters:
           -----------
           None

           Returns:
           --------
           str: a message telling the manager his/her authorities
        """
        return 'Hi {}, you can see the detail information of customers, delete accounts, and you have all the authorities other staffs have.'.format(self._name)

    def seeDetail(self, bank, customerID):
        """
           Get the detail information of a customer

           Parameters:
           -----------
           bank: a Bank object
           customerID: int. It is the ID that was generated when a customer opened an account

           Returns:
           --------
           str: a message displaying the customer's name and balance; or an error message when ID cannot be found in the _Accounts dictionary
        """
        if customerID in bank._Accounts:
            detail = bank._Accounts[customerID]
            return 'Customer name: {}, Customer balance: ${}'.format(detail._name, detail._balance)
        else:
            return 'Cstomer not found'

    def delete_account(self, bank, customerID):
        """
           Delete an account from the _Accounts dictionary

           Parameters:
           -----------
           bank: a Bank object
           customerID: int. It is the ID that was generated when a customer opened an account

           Returns:
           --------
           str: a message telling that the account is deleted; or an error message when ID cannot be found in the _Accounts dictionary
        """
        if customerID in bank._Accounts:
            del bank._Accounts[customerID]
            return 'Account deleted'
        else:
            return 'Customer not found'