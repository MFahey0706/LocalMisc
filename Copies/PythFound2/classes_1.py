#Edit this file to complete the exercises in
#'Rolling Your Own Data Structures with Classes'

class CreditCard(object):
    '''
    This class provides a template for a
    personal credit card.
    '''
    

    #Add an __init__ method to this class that
    #meets the specifications laid out in this docstring:
    '''
    Initialize an instance of the class.
    
    Arguments:
    name: The name of the account holder
    card_number: The credit card number
    apr_percent: The APR, as a whole number percentage
        Input will be 20 for a 20% APR, it will **not** be 0.20.
        This is the annual rate.
    limit: The limit on the card.

    Returns:
    None

    Sets the following class attributes:
    name = name argument
    card_number = card_number argument
    apr_percent = apr_percent argument
    limit = limit argument
    balance = 0
    fees = 0

    For instance, the command to set the first attribute is:
    self.name = name
    '''
    def __init__(self, name, card_number, apr_percent, limit):
        self.name=name
        self.card_number=card_number
        self.apr_percent=apr_percent
        self.limit=limit
        self.balance=0
        self.fees=0
    
    #Add a make_purchase method to this class that
    #meets the specifications laid out in this docstring:
    '''
    Take in a purchase dollar amount, make sure it won't put the
    card over limit, and do one of the following:
    1. If under/at limit, add dollar amount to balance and return True
    2. If over limit, return False

    Arguments:
    purchase_price: The dollar amount to be charged to the card.

    Returns:
    purchase_approved: True if purchase_price + self.balance + self.fees <= self.limit,
        False otherwise.

    Examples:
    card_account = CreditCard('Lee Cardholder', 1234567891011121, 20, 1000)
    card_account.make_purchase(35) -> returns True, card_account.balance is now 35
    card_account.fees = 900
    card_account.make_purchase(65) -> returns True, card_account.balance is now 100
    card_account.make_purchase(1) -> returns False, card_account.balance is still 100
    '''
    def make_purchase(self,purch_amount):
        if (purch_amount + self.balance + self.fees) <= self.limit:
            self.balance += purch_amount
            return True
        else:
            return False

    
    #Add a pay_card method to this class that
    #meets the specifications laid out in this docstring:
    '''
    Take in the dollar amount of a potential payment to the card,
    verify that the payment is both greater than 0 and is less than or
    equal to the balance + fees, then apply that payment to first any fees
    and then the balance.

    Arguments:
    payment_amount: The dollar amount to be paid on the card.

    Returns:
    payment_approved: True if payment_amount > 0 and
        payment_amount <= self.balance + self.fees, False otherwise

    Examples:
    card_account = CreditCard('Lee Cardholder', 1234567891011121, 20, 1000)
    card_account.make_purchase(35) -> returns True, card_account.balance is now 35
    card_account.pay_card(20) -> returns True, card_account.balance is now 15
    card_account.fees = 50
    card_account.pay_card(-10) -> returns False, card_account.balance is still 15,
        card_account.fees is still 50
    card_account.pay_card(100) -> returns False, card_account.balance is still 15,
        card_account.fees is still 50
    card_account.pay_card(40) -> returns True, card_account.balance is still 15,
        card_account.fees is now 10
    card_account.pay_card(15) -> returns True, card_account.balance is now 10,
        card_account.fees is now 0
    '''
    def pay_card(self,payment):
        if payment <= 0 or payment > (self.balance + self.fees):
            return False
        else:
            if self.fees > payment:
                self.fees -= payment
                payment = 0
            else: 
                payment -= self.fees
                self.fees=0
                if self.balance > payment:
                    self.balance -= payment
                    payment = 0
                else:
                    payment -= self.balance
                    self.balance=0
            return True

    #Add a compute_interest method to this class that
    #meets the specifications laid out in this docstring:
    '''
    Compute the daily interest by dividing the apr_percent by 365,
    summing up the balance and fees, and then multiplying the daily
    percentage by this sum. If the daily interest is greater than zero,
    add it to the balance. Otherwise, do nothing.
    
    Arguments:
    None

    Returns:
    None

    Examples:
    card_account = CreditCard('Lee Cardholder', 1234567891011121, 20, 1000)
    card_account.make_purchase(365) -> returns True, card_account.balance is now 365
    card_account.compute_interest() -> card_account.balance is now 365.20
    card_account.apr_percent = -10
    card_account.compute_interest() -> card_account.balance is still 365.20
    card_account.apr_percent = 20
    card_account.balance = -10
    card_account.compute_interest() -> card_account.balance is still -10
    '''
    def compute_interest(self):
        self.balance += (self.apr_percent*.01/365)*(max(self.balance+self.fees,0))
